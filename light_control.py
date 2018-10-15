#!/usr/bin/python3

# OUTSIDE LIGHT CONTROL with LDR and PIR
# by TJK @ 18/11/2017

from gpiozero import LightSensor, MotionSensor, OutputDevice
import datetime, time

LDR = LightSensor(25)
PIR = MotionSensor(24)
K2 = OutputDevice(27, active_high=False)    # LDR relay
K3 = OutputDevice(22, active_high=False)    # PIR relay

sleepT = 60

log = "/home/user/light_control.log"        # log location 

def motion_day():
  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
  log_f = open(log,'a')
  log_f.write('on ' + timestamp + '\t' + "-:  daytime MOTION !!" + '\n')
  log_f.close()

def motion_night():
  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
  log_f = open(log,'a')
  log_f.write('on ' + timestamp + '\t' + "-:  nighttime MOTION !!" + '\n')
  log_f.close()
  K3.on()
  time.sleep(5)

def daytime():
# logging disabled 
#  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
#  log_f = open(log,'a')
#  log_f.write('on ' + timestamp + '\t' + "-:  daytime" + '\n')
#  log_f.close()
  K2.off()
  PIR.when_motion = motion_day
  PIR.when_no_motion = None
  K3.off()

def nighttime():
# logging disabled 
#  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
#  log_f = open(log,'a')
#  log_f.write('on ' + timestamp + '\t' + "-:  nighttime" + '\n')
#  log_f.close()
  K2.on()
  PIR.when_motion = motion_night
  PIR.when_no_motion = K3.off

if __name__ == '__main__':
  try:
    while True:
      if LDR.light_detected:
        daytime()
      else:
        nighttime()
      time.sleep(sleepT)

  except KeyboardInterrupt:
    print ("\n CTRL-C \n --- QUIT --- \n")
