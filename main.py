from lib.mega_upload import upload_audio
from lib.nhk_radio_download import nhk_audo_download

from mega import Mega

import os
import shutil
import glob
import configparser

#設定ファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

#megaへアクセスするインスタンスを作成する
email = config_ini['mega_account']['mail']
password = config_ini['mega_account']['pw']

mega = Mega()
m = mega.login(email,password)

#notionへアクセスするためのインスタンスを作成する
NOTION_TOKEN = config_ini['notion']['api_key']
database_id = config_ini['notion']['database_id']


#NHK番組をダウンロードする。
#megaに無いaudioファイルをダウンロードする仕組みとしている。

# with open("nhk_downloader.txt") as f:

#     #自分の聴きたいラジオデータのjson URLを取得
#     urls = f.readlines()    
#     for audio_url in urls:
        
#         #該当番組のダウンロードを実施。戻り値は１週間分のラジオ番組名リスト
#         file_name_list = nhk_audo_download(m,audio_url)
#         if len(file_name_list) > 0:
#             for file_name in file_name_list:
#                 download_url = upload_audio(m,file_name)
                
#                 #notionへアップロードする処理を入れる。

# #最後にaudio配下の全てのファイルを削除する。
# target_dir = './audio/'
# shutil.rmtree(target_dir)
# os.mkdir(target_dir)
    

