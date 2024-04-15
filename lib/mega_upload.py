import os
import glob

def upload_audio(mega,file_name:str) -> list:

    fileURLList = []
    pwd = os.getcwd()
    
    fileName_pass = pwd +'/audio/'+ file_name

    if mega.find(file_name) == None:
        file = mega.upload(fileName_pass)
        fileURLList.append(mega.get_upload_link(file))
    
    return fileURLList
