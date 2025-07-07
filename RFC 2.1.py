import sys
#from PyQt6.QtCore import QTimer #wird zum automatischen Vergleich in einem bestimmten Zeitintervall benötigt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit

class Mainframe():
    
    def __init__(self):
        super().__init__()
        
        self.window = QWidget()

        self.window.resize(320, 163)
        self.window.setWindowTitle("RFC (Rather Fast Comparison)")
        self.layout1 = QVBoxLayout()
        self.window.setLayout(self.layout1) 

        #Feld mit der Anleitung hinzufügen
        self.anleitung = QLabel(f"Insert your strings in the boxes to compare them.")
        self.layout1.addWidget(self.anleitung)

        #Die beiden Textboxen zum Eintragen der Zeichenfolgen hinzufügen
        self.textfeld1 = QLineEdit()
        self.textfeld2 = QLineEdit()
        self.layout1.addWidget(self.textfeld1)
        self.layout1.addWidget(self.textfeld2)

        #Das Feld/Label hinzufügen, in dem nachher das Ergebnis angezeigt wird
        self.label = QLabel()
        self.layout1.addWidget(self.label)

        #Ein zweites Label zur Anzeige von Zusatzinformationen/möglichen Komplikationen
        self.labelZusatz = QLabel()
        self.layout1.addWidget(self.labelZusatz)

        #Automatischer Vergleich alle 150ms
        #self.timer = QTimer(self, interval=150, timeout=self.vergleich)
        #self.timer.start()

        #Automatischer Vergleich, sobald sich etwas in einem der Textfelder ändert
        self.textfeld1.textChanged.connect(self.vergleich)
        self.textfeld2.textChanged.connect(self.vergleich)

    #Vergleicht die beiden Zeichenfolgen in den Textfeldern
    def vergleich(self):
        self.zeichenfolge1 = str(self.textfeld1.text())
        self.zeichenfolge2 = str(self.textfeld2.text())

        if self.zeichenfolge1 == self.zeichenfolge2:
            mainframe.label.setStyleSheet("color: green")
            mainframe.label.setText(f"Both strings are the SAME!")
        else:
            mainframe.label.setStyleSheet("color: red")
            mainframe.label.setText(f"Both strings are DIFFERENT!")

        #Fügt einen Hinweis hinzu, wenn vor oder hinter einer Zeichenfolge Leerzeichen vorhanden sind
        mainframe.labelZusatz.setStyleSheet("color: red") #alle Meldungen im Zusatzlabel sollen in roter Farbe erscheinen
    
        if self.zeichenfolge1.startswith(" "):
            mainframe.labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe first box!)")
        elif self.zeichenfolge1.endswith(" "):
            mainframe.labelZusatz.setText(f"(Caution: There is a space at the end of \nthe first box!)")
        elif self.zeichenfolge2.startswith(" "):
            mainframe.labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe second box!)")
        elif self.zeichenfolge2.endswith(" "):
            mainframe.labelZusatz.setText(f"(Caution: There is a space at the end of \nthe second box!)")
        else:
            mainframe.labelZusatz.setText(f"")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainframe = Mainframe()
    mainframe.window.show()
    sys.exit(application.exec())