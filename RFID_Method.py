from RFID_Reader import RFID_Reader

class RFID_Method:
    def __init__(self):
        self.rfid_reader = RFID_Reader()
        self.rfid_reader.begin()
    
    #Check which tag is scanned
    def check_tag(self, tag):
        if tag == "10301489265238":
            print("H")
        elif tag == "10401442523026":
            print("I")
        elif tag == "1030148216166141":
            print("T")
        else:
            return "Unknown Tag"