#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        # self.us = UltrasonicSensor(Port.S4)
        self.us = UltrasonicSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def akku(self):
        # akkumulátor töltése
        # konzol ablakba kiírás
        print("akkumulátor töltöttségi szintje: "+str(self.ev3.battery.voltage())/1000)+" V"
        # robot képernyőre
        akuErtek = "akkumulátor töltöttségi \n szintje: "+str(self.ev3.battery.voltage()/1000)+"V"
        self.ev3.screen.print(akuErtek)
        wait(1000)

    def csipog(self):
        self.ev3.speaker.beep()

    def feladat1():
        #Haladjon az asztal széle felé a robot majd álljon meg a szélén
        while(self.cs.reflection()>40)
            self.robot.drive(100,0)
            #print ("Szín:"+str(self.cs.reflection()))
        self.robot.stop(Stop.BRAKE)