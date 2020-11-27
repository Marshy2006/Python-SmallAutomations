import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") #gets datetime in y:m:h h:m

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

credspath = "/path/to/creds/file"
sheetname = "sheetname"

creds = ServiceAccountCredentials.from_json_keyfile_name(credspath, scope)
client = gspread.authorize(creds)
sheet = client.open(sheetname).sheet1  # Open the spreadsheet

def next_available_row(sheet):
    str_list = list(filter(None, sheet.col_values(1)))
    return str(len(str_list)+1)
next_row = int(next_available_row(sheet))
print("Next availiable row: " + str(next_row))

sheet.update_cell(next_row,1, date_time) #add date and to google sheet

result = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp']) # gets temp
result = int(result)
divide = int("1000")
FINAL_TEMP = result/divide
#print(FINAL_TEMP)
sheet.update_cell(next_row,2, FINAL_TEMP) # updates sheet with temp

freqresult = subprocess.check_output(["vcgencmd", "measure_clock", "arm"]) # gets cpu frequency
freqresult = int(freqresult[14:])
divide = int("100000000")
final_freq = freqresult/divide
print(final_freq)
sheet.update_cell(next_row,3, final_freq) # updates sheet with frequency
