import requests
import os
import configparser

from mega import Mega

def nhk_audo_download(mega,audio_url) -> list:
    
    '''
    ■INPUT
    ・mega     :megaへアクセスするためのインスタンス。
    ・audio_url:NHKの聞き逃しラジオ情報データを保持するJsonデータ。NHKより提供されている。
    
    ■OUTPUT
    ・file_info_list(list型)
        ・'date':ラジオ放送日,
        ・'program_title':ラジオ番組名,
        ・'file_name':audioファイル名
    で構成されているリスト。１週間分のラジオ番組情報を格納。
    '''

    #URL両端の不要な改行コードなどを削除
    audio_url = audio_url.strip()
    
    #returnの初期値
    file_name = ''
    file_info_list =[]

    #audio_urlが存在しなければ、ダウンロードはできないのでif文で分岐を行う。
    if audio_url == '':
        print("URLなし")
        

    else:
        resp = requests.get(audio_url)
        js = resp.json()
        program_title = js['main']['program_name']
            
        # 音声ファイルダウンロード。audio_url上に定義されている情報を変数として保持。return文で辞書型リスト形式で返す。
        for d1 in js['main']['detail_list']:
            for d2 in d1['file_list']:

                try:
                    title = d2['file_title']
                    date = d2['aa_vinfo3'][0:8]
                    file_name = date +"_" +title + r'.mp3'
                    file_url = d2['file_name']

                    #megaの中にファイルがなければダウンロードする
                    if mega.find(file_name) == None:
                        cmd = f'ffmpeg -y -vn -v verbose -http_seekable 0 -i "{file_url}" -id3v2_version 3 -metadata artist="NHK" -metadata title="{date}" -metadata album="{program_title}" -metadata date="2022" -metadata track="236" -ab 48k -ar 24000 -ac 1 "./audio/{file_name}"'
                        os.system(cmd)
                        
                        file_info_list.append(
                            {
                                'date':date,
                                'program_title':program_title,
                                'file_name':file_name
                                
                                }
                            )
                        
                except:
                    print('titleなどが取得できない可能性があります。')

                
    return file_info_list

if __name__ == '__main__':
    
    #設定ファイルの読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    #megaへアクセスするインスタンスを作成する
    email = config_ini['mega_account']['mail']
    password = config_ini['mega_account']['pw']

    mega = Mega()
    m = mega.login(email,password)

    audio_url = 'https://www.nhk.or.jp/radioondemand/json/0045/bangumi_0045_01.json'
    nhk_audo_download(m,audio_url)
            