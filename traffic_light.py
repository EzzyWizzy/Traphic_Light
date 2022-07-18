import time

import os, sys
from uuid import getnode



CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

#from utils.utils import get_logger

#logger = get_logger(name=__name__)

is_raspberry = False
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    is_raspberry = True

except Exception as e:
    #logger.error(f"Not running on Raspberry Pi {e}")
    is_raspberry = False

#east west (EW)
RED_PIN = 14 
GREEN_PIN = 15
YELLOW_PIN = 18

#east west (WE)
RED_WE = 2
GREEN_WE = 3
YELLOW_WE = 4

#north south (NS)
RED_NS = 25
GREEN_NS = 8
YELLOW_NS = 7

#north south (SN)
RED_SN = 13
GREEN_SN = 19
YELLOW_SN = 26


GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(RED_SN, GPIO.OUT)
GPIO.setup(GREEN_SN, GPIO.OUT)
GPIO.setup(YELLOW_SN, GPIO.OUT)
GPIO.setup(RED_NS, GPIO.OUT)
GPIO.setup(GREEN_NS, GPIO.OUT)
GPIO.setup(YELLOW_NS, GPIO.OUT)
GPIO.setup(RED_WE, GPIO.OUT)
GPIO.setup(GREEN_WE, GPIO.OUT)
GPIO.setup(YELLOW_WE, GPIO.OUT)
def off_all(red, yellow, green):
    GPIO.output(RED_PIN, red)
    GPIO.output(YELLOW_PIN, yellow)
    GPIO.output(GREEN_PIN, green)
    GPIO.output(RED_SN, red)
    GPIO.output(GREEN_SN, yellow)
    GPIO.output(YELLOW_SN, green)
    GPIO.output(RED_NS, red)
    GPIO.output(GREEN_NS, yellow)
    GPIO.output(YELLOW_NS, green)
    GPIO.output(RED_WE, red)
    GPIO.output(GREEN_WE, yellow)
    GPIO.output(YELLOW_WE, green)

off_all(0, 0, 0)

    
def traffic_state(red, yellow, green) -> None:   
    GPIO.output(RED_PIN, red)
    GPIO.output(YELLOW_PIN, yellow)
    GPIO.output(GREEN_PIN, green)
    
def traffic_state2(red, yellow, green) -> None:   
    GPIO.output(RED_SN, red)
    GPIO.output(GREEN_SN, green)
    GPIO.output(YELLOW_SN, yellow)

def traffic_state3(red, yellow, green) -> None:   
    GPIO.output(RED_NS, red)
    GPIO.output(GREEN_NS, green)
    GPIO.output(YELLOW_NS, yellow)

def traffic_state4(red, yellow, green) -> None:   
    GPIO.output(RED_WE, red)
    GPIO.output(GREEN_WE, green)
    GPIO.output(YELLOW_WE,yellow)



def traffic_light():
    #logger.info("RED Lights")
    #car from east and from west must go while ns must stop
    print('EAST WEST ROAD')
    traffic_state(0, 1, 0)
    traffic_state4(0, 1, 0)
    
    traffic_state2(1, 0, 0)
    traffic_state3(1, 0, 0)
    time.sleep(20)
    off_all(0, 0, 0)
    traffic_state(0, 0, 1)
    traffic_state4(0, 0, 1)
    
    traffic_state2(1, 0, 0)
    traffic_state3(1, 0, 0)
    time.sleep(5)
    
    off_all(0, 0, 0)
    traffic_state(1, 0, 0)
    traffic_state4(1, 0, 0)
    traffic_state2(0, 1, 0)
    traffic_state3(0, 1, 0)
    time.sleep(20)
    traffic_state(1, 0, 0)
    traffic_state4(1, 0, 0)
    traffic_state2(0, 0, 1)
    traffic_state3(0, 0, 1)
    time.sleep(5)
    off_all(0, 0, 0)
    
    
    
    #logger.info("YELLOW Lights")
    # print('SOUTH NORTH ROAD')
    # traffic_state2(1, 1, 1)
    # time.sleep(10)
    # off_all(0, 0, 0)
    #logger.info("GREEN Lights")
    # print('NORTH SOUTH ROAD')
    # traffic_state3(1, 1, 1)
    # time.sleep(10)
    # off_all(0, 0, 0)

    

    
while True:
    traffic_light()

