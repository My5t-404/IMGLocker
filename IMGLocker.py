#This is a simple Gallery Lock Script
#Coded By MY5T404 || Arif Elahi Redoy
#Personal Use Only

import os
import subprocess
import getpass
import msvcrt
import base64
import shutil

def clear():
    subprocess.run("cls",shell=True)

def intro():
    print("\n\n")
    print("Welcome To Gallery Lock")
    print("============================")
    print("coded By MY5T404\n")

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
def copy_files():
    source_folder = 'Encrypt_Pic'
    target_folder = 'Extra_Copy'
    file_list = os.listdir(source_folder)
    for file_name in file_list:
        source_file_path = os.path.join(source_folder, file_name)
        target_file_path = os.path.join(target_folder, file_name)
        shutil.copy2(source_file_path, target_file_path)

def lock_extension():
    copy_files()
    folder_path="Encrypt_Pic"
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.avaif'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.fi'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.gif'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.fig'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.jpeg'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.ge'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.jpg'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.gp'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.jfif'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.fiff'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.pjpeg'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.gep'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.png'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.np'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.webp'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.bp'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.ico'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.oc'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.mp4'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.pm'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.mov'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.vom'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.wmv'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.vmw'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.avi'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.iv'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.mkv'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64encode(os.path.splitext(file_name)[0].encode()).decode() + '.vk'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        else:
            print("\n\nSorry, Error Occurs.\n\n")
    print("\n\nFiles are Successfully Locked.\n")
    input("Press 'Enter' to continue.........")
    clear()


def unlock_extention():
    folder_path="Decrypt_Pic"
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.fi'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.avaif'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.fig'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.gif'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.ge'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.jpeg'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.gp'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.jpg'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.fiff'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.jfif'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.gep'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.pjpeg'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.np'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.png'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.bp'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.webp'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.oc'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.ico'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.pm'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.mp4'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.vom'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.mov'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.vmw'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.wmv'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.iv'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.avi'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        elif file_name.endswith('.vk'):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = base64.b64decode(os.path.splitext(file_name)[0].encode()).decode() + '.mkv'
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        else:
            print("\n\nSorry, Error Occurs.\n\n")
    print("\n\nFiles are Successfully Unlocked.\n")
    input("Press 'Enter' to continue.........")
    clear()

def smenu():
    intro()
    print("Press '1' to Login. OR '0' to exit")
    ask=int(msvcrt.getch().decode())
    if ask==1:
        print("\n\n")
        mainF()
    elif ask==0:
        clear()
        exit()
    else:
        print("\n\nSorry Wrong Input")
        smenu()

def instruction():
    clear()
    print("\n")
    intro()
    print("____________")
    print("Instructions")
    print("____________")
    print("""
    1. To Lock Your Pictures, At fist you need to keep the pictures in 'Encrypt_Pic' Folder.
    2. After the Executing the process, you need to copy the encrypted File in a secure folder, Otherwise those files might be lost.
    3. To Unlock the encrypted files, you need to copy the encrypted files to the 'Decrypt_Pic' folder.
    4. After processing the program. You need to copy the decrypt files into a secure folder. Otherwise those files maybe lost from this folder.
    5. For safety, When You run the encryption process, there will generate a copy of the real files in the 'Extra_Copy' folder.


    ***Note: Please noted that, the encrypted files can only be decrypted by this Decryption script.


    Thanks.
    MY5T404
    """)
    print("\n\n")

    input("Press 'Enter' to return Menu....")
    clear()
    intro()
    mainF()

def mainF():
    passwd=getpass.getpass("Enter The Password- ")
    if passwd == "MySt404":
        clear()
        intro()
        print("Menu-")
        print(" 0.Exit")
        print(" 1.Lock Pictures")
        print(" 2.Unlock Pictures")
        print(" 3.Instructions")
        print("\nEnter Your Choice(0-3)=> ",end="")
        ask=int(msvcrt.getch().decode())
        if ask==0:
            exit()
        elif ask==1:
            lock_extension()
            smenu()
        elif ask==2:
            unlock_extention()
            smenu()
        elif ask==3:
            instruction()
        else:
            print("\n\nWrong Input.You are Automatically Logout. Try Again Later....")
            input("\n\nPress 'ENTER' to continue....")
            clear()
            intro()
            mainF()       
    else:
        print("\n")
        print("Sorry. You are not allowed.\n")
        print("Press 'Q' for Exit or Press any key to continue.\n")
        quit=msvcrt.getch().decode()
        if quit=="Q" or quit=="q":
            exit()
        else:
            clear()
            intro()
            mainF()


create_folder("Encrypt_Pic")
create_folder("Extra_Copy")
create_folder("Decrypt_Pic")
clear()
smenu()
mainF()