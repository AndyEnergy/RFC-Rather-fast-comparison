import sys
import time
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit

application = QApplication(sys.argv)

#definiert die Schleife, die die beiden Strings vergleicht
class Vergleich(QObject):
    
    def __init__(self):
        super().__init__()
    
    def vergleichSchleife(self):
        self.laeuft = True

        while self.laeuft:
            time.sleep(0.25)
            self.zeichenfolge1 = str(mainframe.textfeld1.text())
            self.zeichenfolge2 = str(mainframe.textfeld2.text())
            if self.zeichenfolge1 == self.zeichenfolge2:
                mainframe.label.setStyleSheet("color: green")
                mainframe.label.setText(f"Both strings are the SAME!")
            else:
                mainframe.label.setStyleSheet("color: red")
                mainframe.label.setText(f"Both strings are DIFFERENT!")

#Testet, ob am Anfang oder Ende eines Strings Leerzeichen vorhanden sind
class Komplikationen(QObject):
    
    def __init__(self):
        super().__init__()
    
    def komplikationenSchleife(self):
        self.laeuft = True
       
        while self.laeuft:
            try:      #verhindert ein Abstürzen, solange ein oder beide Textfelder noch leer sind (fängt den Fehler ab)
                time.sleep(0.25)
                self.zeichenfolge1 = str(mainframe.textfeld1.text())
                self.zeichenfolge2 = str(mainframe.textfeld2.text())
                self.laengezeichenfolge1 = len(self.zeichenfolge1)
                self.laengezeichenfolge2 = len(self.zeichenfolge2)
                if  self.zeichenfolge1[0] == " ":
                    mainframe.labelZusatz.setStyleSheet("color: red")
                    mainframe.labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe first box!)")
                elif self.zeichenfolge1[self.laengezeichenfolge1-1] == " ":
                    mainframe.labelZusatz.setStyleSheet("color: red")
                    mainframe.labelZusatz.setText(f"(Caution: There is a space at the end of \nthe first box!)")
                elif self.zeichenfolge2[0] == " ":
                    mainframe.labelZusatz.setStyleSheet("color: red")
                    mainframe.labelZusatz.setText(f"(Caution: There is a space at the beginning of \nthe second box!)")
                elif self.zeichenfolge2[self.laengezeichenfolge2-1] == " ":
                    mainframe.labelZusatz.setStyleSheet("color: red")
                    mainframe.labelZusatz.setText(f"(Caution: There is a space at the end of \nthe second box!)")
                else:
                    mainframe.labelZusatz.setStyleSheet("color: red")
                    mainframe.labelZusatz.setText(f"")
            except: 
                mainframe.labelZusatz.setText(f"")

#legt das Hauptanzeigefenster mit seinen Inhalten fest
class Mainframe():
    
    def __init__(self):
        super().__init__()
        
        self.window = QWidget()

        self.window.resize(320, 163)
        self.window.setWindowTitle("RFC (Rather Fast Comparison)")
        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout) 

        #Feld mit der Anleitung hinzufügen
        self.anleitung = QLabel(f"Insert your strings in the boxes to compare them.")
        self.layout.addWidget(self.anleitung)

        #Die beiden Textboxen zum Eintragen der Zeichenfolgen hinzufügen
        self.textfeld1 = QLineEdit()
        self.textfeld2 = QLineEdit()
        self.layout.addWidget(self.textfeld1)
        self.layout.addWidget(self.textfeld2)

        #Das Feld/Label hinzufügen, in dem nachher das Ergebnis angezeigt wird
        self.label = QLabel()
        self.layout.addWidget(self.label)

        #Ein zweites Label zur Anzeige von Zusatzinformationen/möglichen Komplikationen
        self.labelZusatz = QLabel()
        self.layout.addWidget(self.labelZusatz)



#erstellt zusätzliche Threads und weist jeweils die Schleife zum Vergleichen der Strings
#und die Prüfung möglicher Fehlerquellen diesen zu
thread1 = QThread()
vergleich = Vergleich()
vergleich.moveToThread(thread1)

thread2 = QThread()
komplikationen = Komplikationen()
komplikationen.moveToThread(thread2)

#verbindet "vergleichSchleife" der "Schleife" Klasse mit dem separaten Thread
#und startet den Thread
thread1.started.connect(vergleich.vergleichSchleife)
thread1.start()

#weist den zweiten Thread zu und starten diesen
thread2.started.connect(komplikationen.komplikationenSchleife)
thread2.start()

#Macht das QWidget sichtbar
mainframe = Mainframe()
mainframe.window.show()

sys.exit(application.exec())

