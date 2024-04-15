import os
import configparser
import datetime

from notion_client import Client


def add_record(notion,database_id,radio_name, download_url, radio_date, radio_name_select):
    
    data = {
        "parent": { "database_id": database_id },
        "properties": {
            "radio-name": {
                "title": [
                    {
                        "text": {
                            "content": radio_name
                        }
                    }
                ]
            },
            "download-url": {
                "url": download_url
            },
            "radio-date": {
                "date": {
                    "start": radio_date,
                    "end": None
                }
            },
            "radio-name-select": {
                "select": { "name": radio_name_select }
            }
        }
    }
    

    # レコードを追加
    notion.pages.create(**data)



if __name__ == '__main__':
    
    #設定ファイルの読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    #notionへアクセスするためのインスタンスを作成する
    NOTION_TOKEN = config_ini['notion']['api_key']
    database_id = config_ini['notion']['database_id']

    notion = Client(auth=NOTION_TOKEN)


    download_url = 'https://vod-stream.nhk.jp/radioondemand/r/632/s/stream_632_6e552d498373ad900abfdfedde221e34/index.m3u8'
    radio_date = '20240413'
    radio_name_select = '真打ち競演'
    radio_name = radio_date +r'-'+ radio_name_select

    add_record(notion,database_id,radio_name,download_url,radio_date,radio_name_select)
