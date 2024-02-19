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
window.setCentralWidget(text)


def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path


def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)


def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()


def show_about_dialog():
    text = (
        "<center>"
        "<h1>Text Editor</h1>"
        "&#8291;"
        "<img src=icon.svg>"
        "</center>"
        "<p>Version 31.4.159.265358<br/>"
        "Copyright &copy; Company Inc.</p>"
    )
    QMessageBox.about(window, "About Text Editor", text)
