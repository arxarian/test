import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Nastavení kořene pro QML moduly
    qml_base_dir = Path(__file__).parent / "qml"
    engine.addImportPath(str(qml_base_dir))
    engine.addImportPath(str(qml_base_dir) + "/items")
    engine.addImportPath(str(qml_base_dir) + "/views")
    print(engine.importPathList())

    # Načtení hlavního souboru
    engine.load(str(qml_base_dir / "Main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    
    print("Running...")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
