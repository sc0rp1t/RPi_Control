#!/usr/bin/python3

# Sunrise / Sunset times from ephem module 
# by TJK @ 28/10/2018
# for time adjustment add """+datetime.timedelta(hours=1.5)""" as below 
#  eg. +/- hours if required for light control after sunrise and before sunset 

import datetime
import time
import ephem


# home Location latitude and longtitude
home_lat  = '51.82'
home_long = '-0.82'

sleepT = 60

# check for sunrise and sunset times 
def sun_check():
    obs = ephem.Observer()
    obs.lat = home_lat
    obs.lon = home_long
    next_sr = ephem.localtime(obs.next_rising(ephem.Sun())) #+datetime.timedelta(hours=1.5)
    next_ss = ephem.localtime(obs.next_setting(ephem.Sun())) #+datetime.timedelta(hours=-1.5)
    print ('next sunrise - ', next_sr)
    print ('next sunset  - ', next_ss)

    if next_sr > next_ss:
        return 1
    else:
        return 0

if __name__ == '__main__':
    try:
        while True:
            x = sun_check()
            if x == 1:
                print ('daytime')
            else:
                print ('nighttime')
            time.sleep(sleepT)

    except KeyboardInterrupt:
        print ("\n CTRL-C \n --- QUIT --- \n")
