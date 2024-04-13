from lib.mega_upload import upload_audio
from lib.nhk_radio_download import nhk_audo_download

from mega import Mega

import os
import shutil
import glob
import configparser

#megaへアクセスするオブジェクトの作成
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

email = config_ini['mega_account']['mail']
password = config_ini['mega_account']['pw']

mega = Mega()
m = mega.login(email,password)

#NHK番組をダウンロードする。
#この中でmegaに無いaudioファイルをダウンロードする仕組みとしている。
nhk_audo_download(m,"nhk_downloader.txt")

#audioフォルダ配下のaudioファイルを全件リスト取得する。
files = glob.glob("./audio/*.mp3")

#megaへuploadする
for file in files:
    upload_audio(m,file)

#最後にaudio配下の全てのファイルを削除する。
target_dir = './audio/'
shutil.rmtree(target_dir)
os.mkdir(target_dir)
    

