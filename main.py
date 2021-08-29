import datetime
import shutil
import zipfile
import os
import time

begin_time = datetime.datetime.now()

print("Welcome to AlphaCloud's Pack Script")
print("---------------------------------")

print("Where is the .jar of the Minecraft version located?")
jarLocation = input()

print("Where is the destination folder?")
destination = input()

print("---------------------------------")
print(f".jar location: {jarLocation}")
print(f"Destination folder: {destination}")
print("---------------------------------")

print("Do you want to create texture pack source? 1 = Yes, 2 = No")
answer = int(input())

if answer == 1:
    # Extracting .jar file
    with zipfile.ZipFile(rf'{jarLocation}') as jar:
        for files in jar.namelist():
            print(f"Files In Jar: {files}")

        print("Extracting Files ", end='')
        jar.extractall(path=destination)
        print(" [DONE]")

    # Cleaning Source
    print("Cleaning Extra Files")

    print("Removing META-INF Folder", end='')
    shutil.rmtree(rf"{destination}\META-INF")
    print(" [DONE]")

    print("Removing net Folder", end='')
    shutil.rmtree(rf"{destination}\net")
    print(" [DONE]")

    print("Removing Class Files", end='')
    files = os.listdir(destination)

    for file in files:
        if file.endswith(".class") or file.endswith(".xml"):
            print(f"Removing {file}")
            os.remove(os.path.join(destination, file))

    print("Completed")

    print("What Do You Want Your McMeta File Description To Be?")
    description = input()

    print("Writing McMeta File", end='')
    with open(rf"{destination}\pack.mcmeta", "w") as f:
        f.write("{")
        f.write("\"pack\": {")
        f.write("\"pack_format\": 1,")
        f.write(f"\"description\": \"{description}\"")
        f.write("}")
        f.write("}")
        f.close()

    print("[DONE]")

print("Do you want to replace the Alex And Steve Skin? 1 = Yes, 2 = No")
answer = int(input())

if answer == 1:
    print("Skins from these websites work:")
    print("https://minecraftskinstealer.com/")
    print("https://minecraft.tools/en/skin.php")

    print("What is the file path of the skin?")
    skinPath = input()

    print("---------------------------------")
    print(f"Skin Path: {skinPath}")
    print("---------------------------------")

    print("Overriding Skins", end='')
    shutil.copy(skinPath, rf"{destination}\assets\minecraft\textures\entity\alex.png")
    shutil.copy(skinPath, rf"{destination}\assets\minecraft\textures\entity\steve.png")
    print(" [DONE]")

print("What is your pack name?")
name = input()

print("Zipping Pack", end='')


# Stolen from here: https://stackoverflow.com/a/10480441
def zipfolder(foldername, target_dir):

    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])


zipfolder(name, destination)  # insert your variables here

print(" [DONE]")

print(f"Completed in {datetime.datetime.now() - begin_time}")

print("Auto Closing in 5 seconds")
time.sleep(5)