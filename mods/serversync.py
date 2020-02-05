from github import Github
from github import InputGitTreeElement
import requests
import os
import zipfile
print("ServerSync By Samuel")
print("Coded entirely in python")
user = 'Sasdallas'
password = 'Samrocks1!'
from subprocess import call
g = Github(user,password)
repo = g.get_user().get_repo('ServerSync')
sendorreceive = input("Is this system receiving or sending? Type R or S: ")
if sendorreceive == "R" or sendorreceive == "r":
    print("Receiving files selected")
    minecraftinstalleddiff = input("Is the minecraft path normal? If unknown, type n. Type N or Y: ")
    if minecraftinstalleddiff == "N" or minecraftinstalleddiff == "n":
        print("Minecraft Install Path Normal")
        path = os.getlogin() + "\AppData\Roaming\.minecraft\mods"
        if os.path.exists(path) == "True":
            print("Path check complete. Minecraft Forge is installed.")
            wirelessorgithub = input("Do you want to use wireless transfer or GITHUB transfer(always works)? Type G or W: ")
            if wirelessorgithub == "G" or wirelessorgithub == "g":
                print("Downloading files...")
                modsdownloaded = 0
                gotallmods = False
                while not gotallmods:
                    fileurl = "https://raw.githubusercontent.com/sasdallas/ServerSync/mod" + modsdownloaded
                    print("Downloading File:", fileurl)
                    try:
                        r = requests.get(fileurl)
                    except:
                        print("All Mods Downloaded")
                        gotallmods = True
                        break

                    try:
                        modname = path + "\mod" + modsdownloaded + ".jar"
                        mod = open(modname,"w+")
                        mod.write(r.data)
                        mod.close()
                    except:
                        gotallmods = True
                        break
                    modsdownloaded = modsdownloaded + 1
                print("All Mods Successfully downloaded!")
                print("Total Mods:", modsdownloaded)
elif sendorreceive == "S" or sendorreceive == "s":
    print("Send files selected.")
    sendall = input("Send all files in mods folder? [y/n] ")
    if sendall == "y" or sendall == "Y":
        user = os.getlogin()
        minecraftpath =  os.getenv('APPDATA') + "\.minecraft"
        minecraftpath = os.path.abspath(minecraftpath + "/mods/")
        print(minecraftpath)
        if os.path.exists(minecraftpath) == True:
            print("Sending files...")
            files = os.listdir(minecraftpath)
            if "desktop.ini" in files:
                files.remove("desktop.ini")
            for file in files:
                print(os.path.isdir(file))
                
                if os.path.isdir(file) == True:
                    files.remove(file)

        
                
            modnum = 0
            
            
            batchfile = open("upload.bat", "w+")
            batchfile.write("git clone https://github.com/sasdallas/ServerSync.git\n")
            batchfile.write("cd ServerSync\n")
            
            print(minecraftpath)
            for file in files:
                print(files)
                print("Sending file:", file)
                print(os.path.abspath(file))
                
                
                file_names = []
                file_list = []
                
                
                
                batchfile.write("git add " + file + "\n")
                batchfile.write("git commit -m 'Added Mod'\n")
                
                commit_message = 'Mod uploaded'
                master_ref = repo.get_git_ref('heads/master')
                master_sha = master_ref.object.sha
                base_tree = repo.get_git_tree(master_sha)
                element_list = list()
                for i, entry in enumerate(file_list):
                    with open(entry, 'rb') as input_file:
                        data = input_file.read()
                    
                        
                    try:
                        batchfile = open("upload.bat", "w")
                        batchfile.write("git push\n")
                        batchfile.close()
                        call([os.path.abspath("upload.bat")])
                    except:
                        print("except")
                        element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                        element_list.append(element)
                        tree = repo.create_git_tree(element_list, base_tree)
                        parent = repo.get_git_commit(master_sha)
                        commit = repo.create_git_commit(commit_message, tree, [parent])
                        master_ref.edit(commit.sha)
                
                modnum = modnum + 1
        else:
            print("invalid path")

        print("Sent successfully")
