import sys

from paths import Paths

from PySide6.QtCore import QSize, Qt, QUrl
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QToolBar,
    QVBoxLayout,
)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozzarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(Paths.icon("ma-icon-128.png")))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozzarella Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        # tag::navigationSignals[]
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        # end::navigationSignals[]

        # tag::navigation1[]
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(
            QIcon(Paths.icon("arrow-180.png")), "Back", self
        )
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
        # end::navigation1[]

        # tag::navigation2[]
        next_btn = QAction(
            QIcon(Paths.icon("arrow-000.png")), "Forward", self
        )
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(Paths.icon("arrow-circle-315.png")),
            "Reload",
            self,
        )
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(Paths.icon("home.png")), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        # end::navigation2[]

        navtb.addSeparator()

        # tag::navigation3[]
        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(Paths.icon("lock-nossl.png")))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(
            QIcon(Paths.icon("cross-circle.png")), "Stop", self
        )
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        # end::navigation3[]

        self.menuBar().setNativeMenuBar(False)
        self.statusBar()

        # tag::menuFile[]
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(
            QIcon(Paths.icon("disk--arrow.png")),
            "Open file...",
            self,
        )
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(Paths.icon("disk--pencil.png")),
            "Save Page As...",
            self,
        )
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)
        # end::menuFile[]

        # tag::menuPrint[]
        print_action = QAction(
            QIcon(Paths.icon("printer.png")), "Print...", self
        )
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        # Create our system printer instance.
        self.printer = QPrinter()
        # end::menuPrint[]

        # tag::menuHelp[]
        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(
            QIcon(Paths.icon("question.png")),
            "About Mozzarella Ashbadger",
            self,
        )
        about_action.setStatusTip(
            "Find out more about Mozzarella Ashbadger"
        )  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozzarella_action = QAction(
            QIcon(Paths.icon("lifebuoy.png")),
            "Mozzarella Ashbadger Homepage",
            self,
        )
        navigate_mozzarella_action.setStatusTip(
            "Go to Mozzarella Ashbadger Homepage"
        )
        navigate_mozzarella_action.triggered.connect(
            self.navigate_mozzarella
        )
        help_menu.addAction(navigate_mozzarella_action)
        # end::menuHelp[]

        self.setWindowIcon(QIcon(Paths.icon("ma-icon-64.png")))

    # tag::navigationTitle[]
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Mozzarella Ashbadger" % title)

    # end::navigationTitle[]

    # tag::menuHelpfn[]
    def navigate_mozzarella(self):
        self.browser.setUrl(QUrl("https://www.pythonguis.com/"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec()

    # end::menuHelpfn[]

    # tag::menuFilefnOpen[]
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Hypertext Markup Language (*.htm *.html);;"
            "All files (*.*)",
        )

        if filename:
            with open(filename, "r") as f:
                html = f.read()

            self.browser.setHtml(html)
            self.urlbar.setText(filename)

    # end::menuFilefnOpen[]

    # tag::menuFilefnSave[]
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Page As",
            "",
            "Hypertext Markup Language (*.htm *html);;"
            "All files (*.*)",
        )

        if filename:
            # Define callback method to handle the write.
            def writer(html):
                with open(filename, "w") as f:
                    f.write(html)

            self.browser.page().toHtml(writer)

    # end::menuFilefnSave[]

    # tag::menuPrintfn[]
    def print_page(self):
        page = self.browser.page()

        def callback(*args):
            pass

        dlg = QPrintDialog(self.printer)
        dlg.accepted.connect(callback)
        if dlg.exec() == QDialog.Accepted:
            page.print(self.printer, callback)

    # end::menuPrintfn[]

    # tag::navigationHome[]
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    # end::navigationHome[]

    # tag::navigationURL[]
    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    # end::navigationURL[]

    # tag::navigationURLBar[]
    def update_urlbar(self, q):

        if q.scheme() == "https":
            # Secure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(Paths.icon("lock-ssl.png"))
            )

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(Paths.icon("lock-nossl.png"))
            )

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    # end::navigationURLBar[]


app = QApplication(sys.argv)
app.setApplicationName("Mozzarella Ashbadger")
app.setOrganizationName("Mozzarella")
app.setOrganizationDomain("mozzarella.org")

window = MainWindow()
window.show()
app.exec()
