import configparser
import pprint
import datetime

from notion_database.database import Database
from notion_database.properties import Properties



## database properties
# PROPERTY = Properties()
# PROPERTY.set_title("title")
# PROPERTY.set_rich_text("description")
# PROPERTY.set_number("number")
# PROPERTY.set_select("select")
# PROPERTY.set_multi_select("multi_select")
# PROPERTY.set_checkbox("checkbox")
# PROPERTY.set_url("url")
# PROPERTY.set_email("email")
# PROPERTY.set_phone_number("phone")
# PROPERTY.set_date("date")
# PROPERTY.set_files("file")

def set_property_radio(radio_name,download_url,radio_date,radio_name_select):
    
    PROPERTY = Properties()
    PROPERTY.set_title('radio_name',radio_name)
    PROPERTY.set_url('download_url',download_url)
    PROPERTY.set_date('radio_date',radio_date)
    PROPERTY.set_select('radio_name_select',radio_name_select)
    
    return PROPERTY


def upload_notion_database(NOTION_TOKEN:str,database_id:str,PROPERTY):
    
    D = Database(integrations_token=NOTION_TOKEN)
    D.update_database(database_id=database_id, title="aaaaaaa", add_properties=PROPERTY)
    pprint.pprint(D.result)
    

    
def select_notion_database(notion_token:str,database_id:str):

    D = Database(integrations_token=notion_token)
    D.find_all_page(database_id=database_id)
    pprint.pprint(D.result)

####################################### 

def upload_notion_database_test(NOTION_TOKEN:str,database_id:str,PROPERTY):
    
    D = Database(integrations_token=NOTION_TOKEN)
    D.update_database(database_id=database_id, title="aaaaaaa", add_properties=PROPERTY)
    pprint.pprint(D.result)
     
def set_property_test(radio_name):
    
    PROPERTY = Properties()
    PROPERTY.set_title('radio_name',radio_name)
    
    return PROPERTY
    

if __name__ == '__main__':
    

    #設定ファイルの読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    #notionへアクセスするためのインスタンスを作成する
    NOTION_TOKEN = config_ini['notion']['api_key']
    database_id = config_ini['notion']['database_id']
    
    #PROPERTYへ値をセットする。
    radio_name = 'ラジオ英会話'
    download_url = 'https://notion-database.readthedocs.io/'
    radio_date = str(datetime.datetime.today())
    radio_name_select = 'ラジオ英会話'
    PROPERTY = set_property_radio(radio_name,download_url,radio_date,radio_name_select)
    
    new_record_data = {
        "radio-name": {
            "title": [
                {
                    "text": {"content": "レコードタイトル"}
                }
            ]
        },
        "download-url": {
            "url": "https://example.com/download.zip"
        },
        "radio-date": {
            "date": {
                "start": "2024-04-16"
            }
        },
        "radio-name-select": {
            "name": "選択肢A"
        }
    }
    
    client = notion_database.Client(auth=token)

