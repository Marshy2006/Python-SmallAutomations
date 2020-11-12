import os
import datetime
import time

longyear = datetime.datetime.now().strftime("%Y")
shortyear = longyear[-2:]
datemd = datetime.datetime.now().strftime("%m%d")
date = shortyear + datemd

def backup():
    cp = "sudo cp -r ~/Py ~/usb/Py/" + date + "_Py"
    os.system(cp)

backup()
