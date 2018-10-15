#!/usr/bin/python3

#  Temperature controlled Fan
#  by Sc0rp1t @ 18/11/2017

from gpiozero import OutputDevice
from w1thermsensor import W1ThermSensor
import datetime, time, os.path

sensor = W1ThermSensor()                    # 1 Wire Temperature Sensor
K1 = OutputDevice(17, active_high=False)    # Relay1 FAN
sleepT = 60                                 # sleep.time()
tempH = 28                                  # temperature treshold
log = "/home/thomas/scripts/fan_control.log"

def log_off():
  tempC = sensor.get_temperature()
  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
  log_f = open(log,'a')
  log_f.write('on ' + timestamp + ' - temp: ' + str(tempC) + '\t' + ' -- FAN OFF --' + '\n')
  log_f.close()

def log_on():
  tempC = sensor.get_temperature()
  timestamp = time.strftime("%d/%m/%Y @ %H:%M:%S")
  log_f = open(log, 'a')
  log_f.write('on ' + timestamp + ' - temp: ' + str(tempC) + '\t' + ' -- FAN ON --' + '\n')
  log_f.close()

def main():
  while True:
    tempC = sensor.get_temperature()
    if tempC <= 28:
      K1.off()
#      log_off()
    elif tempC > 28:
      K1.on()
#      log_on()
    else:
      K1.off()
      print ("Possible problems")
    time.sleep(sleepT)

#MAIN LOOP

if __name__ == '__main__':
  try:
    main()

  except KeyboardInterrupt:
    print ("\n CTRL-C \n --- QUIT --- \n")
