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
#megaに無いaudioファイルをダウンロードする仕組みとしている。

with open("nhk_downloader.txt") as f:
    urls = f.readlines()
    for audio_url in urls:
        file_name = nhk_audo_download(m,audio_url)
        if len(file_name) > 0:
            download_url = upload_audio(m,file_name)

#最後にaudio配下の全てのファイルを削除する。
target_dir = './audio/'
shutil.rmtree(target_dir)
os.mkdir(target_dir)
    

