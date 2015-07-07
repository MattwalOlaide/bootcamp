import time
import webbrowser
timez = [["google.com",10.0],["andela.co",20.0],["google.com",30.0]]

def open_url(tim):
	for addy in tim:
		lengthy = len(addy)
		last_item = addy[lengthy-1]
		for single_list in addy:
			url = single_list[0]
			delay_time = single_list[1]
			if single_list != last_item:
				webbrowser.open(url)
				time.sleep(delay_time)
			else:
				webbrowser.open(url)
open_url(timez)