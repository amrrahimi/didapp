import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

from didban.ui import QSS, MainWindow


def res(*p):
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base.joinpath(*p)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Didban")
    app.setLayoutDirection(Qt.RightToLeft)
    fonts = res("didban", "assets")
    for f in fonts.glob("*.ttf") if fonts.exists() else []:
        QFontDatabase.addApplicationFont(str(f))
    icon = res("didban", "assets", "icon.png")
    if icon.exists():
        app.setWindowIcon(QIcon(str(icon)))
    app.setStyleSheet(QSS)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
