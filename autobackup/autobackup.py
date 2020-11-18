import os
import datetime
import time

longyear = datetime.datetime.now().strftime("%Y")
shortyear = longyear[-2:]
datemd = datetime.datetime.now().strftime("%m%d")
date = shortyear + datemd
backup = "Path to file you want to backup"
path = "Path to destination"

def backup():
    cp = "sudo cp -r" + backup + path + date
    os.system(cp)

backup()
