import os
from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QLabel, QPushButton, QFileDialog, QWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from iterator import ClassIterator


class MainWindow(QMainWindow):
    """
    Инициализация и настройка окна

    """
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Dataset Viewer")
        self.setGeometry(200, 200, 900, 700)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(800, 500)

        self.next_button = QPushButton("Next image")
        self.next_button.clicked.connect(self.show_next_image)

        self.select_annotation_button = QPushButton("Annotation file")
        self.select_annotation_button.clicked.connect(self.select_annotation)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.select_annotation_button)

        img = QWidget()
        img.setLayout(self.layout)
        self.setCentralWidget(img)

        self.iterator = None

    def select_annotation(self) -> None:
        file, _ = QFileDialog.getOpenFileName(self, "Choose annotation file", filter="*.txt *.csv")
        if file:
            try:
                self.iterator = ClassIterator(file)
                self.show_next_image()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def show_next_image(self) -> None:
        if self.iterator is None:
            QMessageBox.warning(self, "Error", "Choose annotation file")
            return

        try:
            image_path = next(self.iterator)
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            else:
                QMessageBox.critical(self, "Error", f"Image {image_path} not found.")
        except StopIteration:
            QMessageBox.information(self, "Error", "This is end of list")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")
