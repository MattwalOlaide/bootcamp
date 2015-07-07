import time
import webbrowser
timez = [[url1,time1],[url1,time1],[url1,time1]]

def open_url(tim):
	for addy in tim:
		lengthy = len(addy)
		last_item = addy[lengthy-1]
		url = addy[0]
		delay_time = addy[1]
		if addy != last_item:
			webbrowser.open(url)
			time.sleep(delay_time)
		else:
			webbrowser.open(url)
open_url(timez)