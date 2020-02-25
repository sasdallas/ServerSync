from subprocess import call

import tkinter
import zipfile
import os
import requests
import urllib.request
import ctypes
def Mbox(title, text, style):
  return ctypes.windll.user32.MessageBoxW(0, text, title, style)
print("Installing BEE2")
def beeinstall():
    button.configure(bg = '#ff9900', text="Downloading(this may lag window)...")
    
    button.update()
    main.update_idletasks()
    print("Downloading ")
    print("File Name: BEE2.zip")
    url = 'https://github.com/BEEmod/BEE2.4/releases/download/2.4.36.1_/BEE2_4.36.1_win.zip'
    try:
        urllib.request.urlretrieve(url, os.path.abspath("BEE2.zip"))
    except:
        Mbox("Error", "Download failed. Remove the old BEE2.zip and try again.", 1)
    os.mkdir("BEE2")
    zip_ref = zipfile.ZipFile(os.path.abspath("BEE2.zip"), 'r')
    zip_ref.extractall("BEE2")
    zip_ref.close()
    print("Downloading packages...")
    url = 'https://github.com/BEEmod/BEE2-items/releases/download/v4.36.0/BEE2_v4.36.0_packages.zip'
    urllib.request.urlretrieve(url,os.path.abspath("PACKAGES.zip"))
    zip_ref = zipfile.ZipFile(os.path.abspath("PACKAGES.zip"), 'r')
    zip_ref.extractall("BEE2")
    zip_ref.close()
    print("Launching BEE2...")
    call(["BEE2/bee2.exe"])
    button.configure(bg = '#ff3300')
    button.update()
    main.update_idletasks()
main = tkinter.Tk()
main.title("Install BEE2")
button = tkinter.Button(main, text="Install BEE2", command=beeinstall)
button.pack()


