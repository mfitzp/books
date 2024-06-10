import sys

from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QColor, QPainter, QBrush
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QApplication, QDial



class _Bar(QWidget):
    def __init__(self, steps):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding,
        )

        if isinstance(steps, list):
            # list of colors.
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps, int):
            # int number of bars, defaults to red.
            self.n_steps = steps
            self.steps = ["red"] * steps

        else:
            raise TypeError("steps must be a list or int")

        self._bar_solid_percent = 0.8
        self._background_color = QColor("black")
        self._padding = 4  # n-pixel gap around edge.

    # end::Barinit[]

    def sizeHint(self):
        return QSize(40, 120)

    # tag::paintEvent[]
    def paintEvent(self, e):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(
            0,
            0,
            painter.device().width(),
            painter.device().height(),
        )
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        # Define our canvas.
        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        # Draw the bars.
        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent

        # Calculate the y-stop position, from the value in range.
        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * self.n_steps)

        for n in range(n_steps_to_draw):
            brush.setColor(QColor(self.steps[n]))
            ypos = (1 + n) * step_size
            rect = QRect(
                self._padding,
                self._padding + d_height - int(ypos),
                d_width,
                int(bar_height),
            )
            painter.fillRect(rect, brush)

        painter.end()

    # end::paintEvent[]

    def _trigger_refresh(self):
        self.update()



class PowerBar(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, parent=None, steps=5):
        super().__init__(parent)

        layout = QVBoxLayout()
        self._bar = _Bar(steps)

        layout.addWidget(self._bar)

        self._dial = QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)



app = QApplication(sys.argv)
window = PowerBar(
    steps=[
        "#5e4fa2",
        "#3288bd",
        "#66c2a5",
        "#abdda4",
        "#e6f598",
        "#ffffbf",
        "#fee08b",
        "#fdae61",
        "#f46d43",
        "#d53e4f",
        "#9e0142",
    ]
)
window.show()
app.exec()
