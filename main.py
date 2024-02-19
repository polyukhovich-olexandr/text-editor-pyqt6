from PyQt6.QtWidgets import *
from PyQt6.QtGui import QKeySequence, QAction


class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window,
            None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
        )
        if answer & QMessageBox.Save:
            save()
            if text.document().isModified():
                # This happens when the user closes the Save As... dialog.
                # We do not want to close the window in this case because it
                # would throw away unsaved changes.
                e.ignore()
        elif answer & QMessageBox.Cancel:
            e.ignore()


app = QApplication([])
app.setApplicationName("Text Editor")
text = QPlainTextEdit()
window = MainWindow()
