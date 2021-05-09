import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import playsound
import os


# DEFINITIONS #
time_now = time.strftime('%Y-%m-%d_%H-%M', time.localtime())
racun = "racun" + time_now + ".txt"
duration = 0.1  # beep seconds
freq = 672  # beep Hz


##########################
#    PRODUCTS CATALOG    #
##########################
catalog = {
    "pivo - Lasko": 120.0,
    "pivo - Union": 115.0,
    "energijska pijaca - FlyingPower": 67.0,
    "avto - Ferrari": 450.0,
    "sladko - smetana": 231.0,
    "zvecilni - Orbit": 88.5
}

##########################
#        SCANNER         #
##########################
class Scanner():
    'Scanner class. Defines how scanner is working and writing data.'

    def __init__(self):
        self.seznam = ["Artikli:"]
        self.cas1 = time.time()
        self.cas2 = time.time()
        self.counter = 0

    def decoder(self,image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)
        # Barcode decoder
        for obj in barcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)

            # Data writing
            self.cas1 = time.time()
            artikel = str(barcodeData)
            if self.seznam[-1] != artikel:
                self.seznam.append(artikel)
                #print(self.seznam)
                print("You added a new item: " + artikel)
                os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                self.counter += catalog[artikel]
                self.cas2 = time.time()
            if int(self.cas1-self.cas2) > 1.5:
                self.seznam.append(artikel)
                #print(self.seznam)
                print("You added a new item: " + artikel)
                os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                self.counter += catalog[artikel]
                self.cas2 = time.time()

            cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
            #print("Barcode: "+barcodeData +" | Type: "+barcodeType)


    def scan(self):
        cap = cv2.VideoCapture(-1)
        while True:
            ret, frame = cap.read()
            self.decoder(frame)
            cv2.imshow('Image', frame)
            code = cv2.waitKey(10)
            if code == ord('q'):
                return self.counter
                break