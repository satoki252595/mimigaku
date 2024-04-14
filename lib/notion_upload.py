import configparser

from notion_database.database import Database
import pprint


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

def upload_notion_database(notion_token:str,database_id:str):
    
    D = Database(integrations_token=NOTION_TOKEN)
    D.retrieve_database(database_id, get_properties=True)
    properties_list = D.properties_list
    #print(properties_list)
    #PROPERTY = ...

    pprint.pprint(D.result)

    #D.update_database(database_id=database_id, title="DB", add_properties=PROPERTY)
    

if __name__ == '__main__':
    

    #設定ファイルの読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    #notionへアクセスするためのインスタンスを作成する
    NOTION_TOKEN = config_ini['notion']['api_key']
    database_id = config_ini['notion']['database_id']
    
    upload_notion_database(NOTION_TOKEN,database_id)

