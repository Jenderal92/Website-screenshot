import requests
from colorama import Fore

def banner():
	print(Fore.YELLOW+'\nWEBSITE SCREENSHOT' +Fore.WHITE)
banner()

WEBSITESS = raw_input("\nEnter URL  : ")

def sw():
	try:
		KEY = requests.get('https://pastebin.com/raw/Y8pHhCwa').text
		urls = 'https://api.screenshotmachine.com/?key='+KEY+'&url='+WEBSITESS+'&dimension=1024xfull&delay=3000'
		response = requests.get(urls)
		if response.status_code == 200 :
			file_name = str(WEBSITESS) + ".jpg"
			print(Fore.GREEN + '\nfile download successful !\nSaved to current folder !' + Fore.WHITE + file_name)
			open(file_name, 'wb').write(response.content)
	except:
		pass
sw()