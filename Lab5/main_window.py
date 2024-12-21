from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QLabel, QPushButton, QFileDialog, QWidget, QMessageBox
)
from PyQt5.QtCore import Qt
from iterator import ClassIterator


class MainWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Dataset Viewer")
        self.setGeometry(200, 200, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(600, 400)

        self.select_annotation_button = QPushButton("Выбрать файл аннотации")
        self.select_annotation_button.clicked.connect(self.select_annotation)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.select_annotation_button)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.iterator = None
        self.dataset_path = None

    def select_annotation(self):
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотации", filter="*.txt *.csv")
        if file:
            try:
                self.iterator = ClassIterator(file)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить аннотации: {str(e)}")
