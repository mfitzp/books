from PySide2.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout
)

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QWidget window;
    QLineEdit *lineEdit = new QLineEdit();
    QPushButton *button = new QPushButton("Clear");
    QHBoxLayout *layout = new QHBoxLayout();
    layout->addWidget(lineEdit);
    layout->addWidget(button);
    
    QObject::connect(&button,   &QPushButton::pressed,
                     &lineEdit, &QLineEdit::clear);
    
    window.setLayout(layout);
    window.setWindowTitle("Why?");
    window.show();
    return app.exec();
}