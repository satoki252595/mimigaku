import os

def upload_audio(mega,file_name:str) -> list:

    #audioデータアップロードが完了後にmega上の参照URLを格納するリスト。
    fileURLList = []
    pwd = os.getcwd()
    
    #ダウンロードしたラジオデータのファイル相対パスを定義
    fileName_pass = pwd +'/audio/'+ file_name

    #mega上に同一ファイル名称がなければ、ファイルをアップロード。
    if mega.find(file_name) == None:
        file = mega.upload(fileName_pass)
        #mega上にアップロードしたaudioファイルのURLをgetし、fileURLListへ格納する。
        fileURLList.append(mega.get_upload_link(file))
    
    return fileURLList
