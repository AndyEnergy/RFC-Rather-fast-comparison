import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit

#Definiert die Funktion "vergleich", die 2 Strings miteinander vergleicht
def vergleich(x, y):
    if x == y:
        label.setStyleSheet("color: green")
        return str(f"Both strings are the SAME!")
    else:
        label.setStyleSheet("color: red")
        return str(f"Both strings are DIFFERENT!")

class Komplikationen():
    
    def __init__(self):
        super().__init__()
    
    def komplikationenSchleife(self):
        try:   #verhindert ein Abstürzen, solange ein oder beide Textfelder noch leer sind (fängt den Fehler ab)
            self.zeichenfolge1 = str(textfeld1.text())
            self.zeichenfolge2 = str(textfeld2.text())
            self.laengezeichenfolge1 = len(self.zeichenfolge1)
            self.laengezeichenfolge2 = len(self.zeichenfolge2)
            if  self.zeichenfolge1[0] == " ":
                labelZusatz.setStyleSheet("color: red")
                labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe first box!)")
            elif self.zeichenfolge1[self.laengezeichenfolge1-1] == " ":
                labelZusatz.setStyleSheet("color: red")
                labelZusatz.setText(f"(Caution: There is a space at the end of \nthe first box!)")
            elif self.zeichenfolge2[0] == " ":
                labelZusatz.setStyleSheet("color: red")
                labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe second box!)")
            elif self.zeichenfolge2[self.laengezeichenfolge2-1] == " ":
                labelZusatz.setStyleSheet("color: red")
                labelZusatz.setText(f"(Caution: There is a space at the end of \nthe second box!)")
            else:
                labelZusatz.setStyleSheet("color: red")
                labelZusatz.setText(f"")
        except: 
            labelZusatz.setText(f"")


application = QApplication(sys.argv)

window = QWidget()
window.resize(320, 180)
window.setWindowTitle("RFC (Rather Fast Comparison)")
layout = QVBoxLayout()
window.setLayout(layout)

#Feld mit der Anleitung hinzufügen
anleitung = QLabel(f"Insert your strings in the boxes and press \n\"Compare\" to compare them.")
layout.addWidget(anleitung)

#Die beiden Textboxen zum Eintragen der Zeichenfolgen hinzufügen
textfeld1 = QLineEdit()
textfeld2 = QLineEdit()
layout.addWidget(textfeld1)
layout.addWidget(textfeld2)

#Den Button hinzufügen, der den Vergleich startet
button = QPushButton("Compare")
button.setFixedSize(120, 30)
layout.addWidget(button)

#Das Feld/Label hinzufügen, in dem nachher das Ergebnis angezeigt wird
label = QLabel()
layout.addWidget(label)

#Ein zusätzliches Label, das anzeigt, ob Leerzeichen vor oder hinter den kopierten Strings vorhanden sind 
labelZusatz = QLabel()
layout.addWidget(labelZusatz)

#Zuweisung einer aufrufbaren variablen für die Klasse "Komplikationen"
komplikationen = Komplikationen()

#Definiert die Funktion, die beim Klicken des Buttons oder der Enter Taste ausgeführt wird (Werte der Textfelder einlesen und vergleichen,
#auf unbeabsichtigte Leerzeichen prüfen und dann das Ergebnis in dem dafür vorgesehenen Label ausgeben.)
def vergleich_starten():
    komplikationen.komplikationenSchleife() 
    zeichenfolge1 = str(textfeld1.text())
    zeichenfolge2 = str(textfeld2.text())
    vergleich_ergebnis = (vergleich(zeichenfolge1, zeichenfolge2))
    label.setText(vergleich_ergebnis)
button.clicked.connect(vergleich_starten)
textfeld1.returnPressed.connect(vergleich_starten)
textfeld2.returnPressed.connect(vergleich_starten)

#Macht das Fenster sichtbar
window.show()

sys.exit(application.exec())