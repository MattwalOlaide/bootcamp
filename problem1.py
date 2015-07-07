import time
import webbrowser

url = 'www.google.com'
kount = 0
while kount < 3:
	webbrowser.open(url)
	time.sleep(5)
	kount +=1