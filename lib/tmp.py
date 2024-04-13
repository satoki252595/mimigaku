from mega import Mega 
import os

import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

email = config_ini['mega_account']['mail']
password = config_ini['mega_account']['pw']

mega = Mega()
m = mega.login(email,password)

#files = m.get_files()

file = m.find('20240406_上方演芸会　選　▽チキチキジョニー／浮世亭三吾・美ユル.mp3')
print(file)