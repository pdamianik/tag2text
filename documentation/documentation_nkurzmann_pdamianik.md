# [GK] 10.2 Robotik

## Raspberrypi und RFID Chips

### Ziel

Ziel ist es einen Raspberrypi mit einem RFID Kartenleser zu verbinden und dann die Daten, in unseren Falle Buchstaben auszulesen von den RFID Chips auszulesen. 


### Vorraussetzungen

Für diese Übung werden ein Raspberrypi und ein RFID Kartenleser, sowie RFID Karten benötigt. Der RFID Kartenleser ist von der Firma SparkFun und hat die Modellnummer Qwiic RFID-IDXXLA [2]. 


### Arbeitsschritte

Als Grundlage wurde die Anleitung von Sparkfun verwendet [3].

Zuerst haben wir auf eine MikroSD Karte das Raspberrypi OS mittels Raspberrypi Imager installiert. Danach mussten wir auf diesen Raspberrypi Python installieren. Danach wollten wir den RFID Kartenleser mit dem Raspberrypi mittels I2C verbinden. Dabei haben wir 3 Jumper Kabel und ein Steckbrett benötigt. Die Jumper Kabel haben wir dann bei dem Raspberrypi auf den Pin 3 (SDA) und Pin 5 (SCL) angesteckt und bei den RFID Kartenleser auch bei den SDA und SCL Pins. Das dritte Kabel verbindet den Pin 1 (3.3V) beim Raspberrypi mit dem Pin für die Stromversorgung bei dem Kartenleser. Danach haben wir den Python Code für die Auslesung von den Daten der RFID Karten geschrieben. Den Code zum Verbinden mit dem RFID Kartenleser kann man von dem Github Repository [1] nehmen. Dann haben wir eine Klasse geschrieben, welche überprüft, welche Karte am Kartenleser eingescannt wurde und dann den Buchstaben zurückgegeben.
```
from RFID_Reader import RFID_Reader

class RFID_Method:
    def __init__(self):
        self.rfid_reader = RFID_Reader()
        self.rfid_reader.begin()
    
    #Check which tag is scanned
    def check_tag(self, tag) -> Str:
        if tag == "10301489265238":
            return("H")
        elif tag == "10401442523026":
            return("I")
        elif tag == "1030148216166141":
            return("T")
        else:
            return "Unknown Tag"
```

### Probleme

Zuerst konnte der Raspberrypi keine Verbindung zum WLAN aufbauen. Nach längerem debuggen hat sich herausgestellt, dass der speziefische Pi einer vom Model 3B ist, allerdings kein WIFI integiert hat. Anschließend trat das nächste Problem auf, mit dem einige Zeit verloren ging. Wir haben nämlich initial Raspberry Pi OS der Lite Version installiert. Allerdings hat diese Version viele Packages nicht in ihren repos, unter anderem ein Python Package, welches wir für den RFID Reader gebraucht haben. Nach einem reflashen konnten wir dieses installieren und mit der Implementierung fortsetzen. Danach ist ein weiteres Problem mit dem RFID Kartenleser aufgetreten. Auf der Produktbeschreibung des RFID Kartenleser steht zwar, dass dieser I2C-fähig ist, allerdings konnten wir das Gerät nicht über den Raspberrypi finden. Letztenendlich haben wir es geschaft das der Kartenleser den benötigten Strom erhält, aber nicht das er mit dem Raspberrypi kommunizieren kann. 

### Quellen

[1] https://github.com/sparkfun/Qwiic_RFID_Py
[2] https://www.sparkfun.com/products/15191
[3] https://learn.sparkfun.com/tutorials/sparkfun-qwiic-rfid-idxxla-hookup-guide

