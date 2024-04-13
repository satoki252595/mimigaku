import os

def upload_audio(mega,fileName_pass:str) -> str:

    file = mega.upload(fileName_pass)
    
    return mega.get_upload_link(file)

if __name__ == "__main__":

    pwd = os.getcwd()
    fileName_pass = pwd + r"/20240406_上方演芸会　選　▽チキチキジョニー／浮世亭三吾・美ユル.mp3"
    url = upload_audio(fileName_pass)
    print(url)