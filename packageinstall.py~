import os
import sys
import json
data = open('package.json').read()
full_data = json.loads(data)
actual_data = full_data['Dependencies']
for i in range (len(actual_data)):
	cmd = "pip install "+actual_data[i]['Name'] +"=="+ actual_data[i]['version']
	os.system(cmd)
for i in range (len(actual_data)):
	if  actual_data[i]['Name'] in sys.modules:
		print("sucess")
	else :
		if i == 0:
			print("-------Failed to install below packages or modules-------")
		print(actual_data[i]['Name'])

	

