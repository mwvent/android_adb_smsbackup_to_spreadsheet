import json
import time
import datetime
import csv
import sys
import string
inputArgs = sys.argv
from datetime import datetime

def remove_prefix(text, prefix, repl):
    if text.startswith(prefix):
        return repl+ text[len(prefix):]
    return str(text)


f = open('messages.csv', 'w')
csvwriter = csv.DictWriter(f,{'address' : 0, 'type' : 0, 'date' : 0, 'time' : 0, 'message': 0})

for i in inputArgs[1:]:
	fl = i.encode('utf-8', 'ignore').strip().decode("utf-8") 
	print(fl)
	with open(fl) as json_file:
		data = json.load(json_file)
		for row in data:
			try:
				rowTxt = ""
				newRow = {}
				rowTxt += remove_prefix(row["address"], "+44", "0") + "," 
				newRow["address"] = str(remove_prefix(row["address"], "+44", "0"))
				rowTxt += datetime.utcfromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d') + ","
				rowTxt += datetime.utcfromtimestamp(int(row["date"])/1000).strftime('%H:%M:%S') + ","
				newRow["date"] = datetime.utcfromtimestamp(int(row["date"])/1000).strftime('%Y-%m-%d')
				newRow["time"] = datetime.utcfromtimestamp(int(row["date"])/1000).strftime('%H:%M:%S')
				typeTxt = "Received" if row["type"] == "1" else "Sent"
				newRow["type"] = typeTxt
				rowTxt += typeTxt + ","
				rowTxt += row["body"] 
				newRow["message"] = row["body"]
				#print(rowTxt)
				csvwriter.writerow(newRow)
			except:
				nop = 1
f.close()
	
