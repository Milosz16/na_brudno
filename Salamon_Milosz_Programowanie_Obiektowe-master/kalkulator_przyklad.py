# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:01:54 2020

@author: misalamon
"""

from PyQt5.QtWidgets import QApplication, QWidget


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())