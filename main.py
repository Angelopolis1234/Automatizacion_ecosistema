from GUI import window as wd
import os

def auto_conf():
    with open("configs/config.txt","r") as file: line=file.readline()
    if line=="None":
        with open("configs/config.txt","w") as file:
            file.write(f"[OUTPUT]={os.path.expanduser('~')}\\Documents")

auto_conf()
wd.main_window()