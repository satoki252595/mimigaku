import requests
import os


def nhk_audo_download(mega,nhk_downloader_txt:str):

    # ダウンロード対象リスト読み込み
    with open(nhk_downloader_txt) as f:
        urls = f.readlines()
        
    for url in urls:
        url = url.strip()
        if url == '':
            continue
        resp = requests.get(url)
        js = resp.json()
        program_title = js['main']['program_name']
            
        # 音声ファイルダウンロード
        for d1 in js['main']['detail_list']:
            for d2 in d1['file_list']:

                try:
                    title = d2['file_title']
                    date = d2['aa_vinfo3'][0:8]
                    file_name = date +"_" +title + r'.mp3'
                    file = d2['file_name']

                    #megaの中にファイルがなければダウンロードする
                    if mega.find(file_name) == None:
                        cmd = f'ffmpeg -y -vn -v verbose -http_seekable 0 -i "{file}" -id3v2_version 3 -metadata artist="NHK" -metadata title="{date}" -metadata album="{program_title}" -metadata date="2022" -metadata track="236" -ab 48k -ar 24000 -ac 1 "./audio/{file_name}"'
                        os.system(cmd)
                except:
                    print('titleなどが取得できない可能性があります。')
                