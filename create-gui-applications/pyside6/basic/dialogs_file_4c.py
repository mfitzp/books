import os

import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "All files (*.*)",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[3]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            dir=initial_dir,
            filter=filters,
            selectedFilter=initial_filter,
        )
        print("Result:", filename, selected_filter)

        # tag::get_filename[]
        if filename:
            with open(filename, "r") as f:
                file_contents = f.read()
            print(file_contents)
        # end::get_filename[]

    def get_filenames(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[1]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        (filenames, selected_filter,) = QFileDialog.getOpenFileNames(
            self,
            caption=caption,
            dir=initial_dir,
            filter=filters,
            selectedFilter=initial_filter,
        )
        print("Result:", filenames, selected_filter)

        # tag::get_filenames[]
        combined_contents = ""
        for filename in filenames:
            with open(filename, "r") as f:
                combined_contents += f.read()
        print(combined_contents)
        # end::get_filenames[]

    def get_save_filename(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        initial_filter = FILE_FILTERS[2]  # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            dir=initial_dir,
            filter=filters,
            selectedFilter=initial_filter,
        )
        print("Result:", filename, selected_filter)

        # tag::get_save_filename[]
        if filename:
            if os.path.exists(filename):
                # Existing file, ask the user for confirmation.
                write_confirmed = QMessageBox.question(
                    self,
                    "Overwrite file?",
                    f"The file {filename} exists. Are you sure you want to overwrite it?",
                )
            else:
                # File does not exist, always-confirmed.
                write_confirmed = True

            if write_confirmed:
                with open(filename, "w") as f:
                    file_content = "YOUR FILE CONTENT"
                    f.write(file_content)
        # end::get_save_filename[]

    def get_folder(self):
        caption = ""  # Empty uses default caption.
        initial_dir = ""  # Empty uses current folder.
        folder_path = QFileDialog.getExistingDirectory(
            self,
            caption=caption,
            dir=initial_dir,
            options=QFileDialog.DontUseNativeDialog,
        )
        print("Result:", folder_path)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
