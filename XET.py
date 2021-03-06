#!/usr/bin/python3
import os
import sys
import time
import urllib.request
import hashlib

try:
    from colorama import Fore, Back, Style, init
except ModuleNotFoundError:
    print ("You have no colorama installed, i will install it for you")
    print
    path = sys.executable
    #path = path[:-11]
    path = path.replace("python.exe","")
    os.system(path+"/Scripts/pip install colorama")
    print
    print ("Ok, now you can restart script :)")
    from colorama import Fore, Back, Style, init

from twrp import twrpInstaller
    

init()

# here i'm checking wchich os you are using and setting command to clear cmd/terminal window
if sys.platform == "linux" or sys.platform == "linux2":
    clear = lambda: os.system('clear')
    s = "l"
elif sys.platform == "win32":
    clear = lambda: os.system('cls')
    s = "w"

# some global variables
dashed_line = (Fore.MAGENTA + "--------------------------------------------------------------------" + Fore.RESET)

killsystem = os.system("adb kill-server")

# this is path to /res/ folder and to .py file

resPath = os.path.abspath(os.path.dirname(__file__)) + os.sep + "res" + os.sep

filePath = os.path.abspath(os.path.dirname(__file__)) + os.sep

# resPath = os.path.dirname(sys.executable)+os.sep+"res"+os.sep

# filePath = os.path.dirname(sys.executable)+os.sep


# this is list of devices with official twrp support

devices = ["cancro", "libra", "ferrari", "aqua", "gemini", "virgo", "leo", "scorpio", "jason", "tiffany", "song",
           "meri", "tisson", "capricorn", "natrium", "lithium", "chiron", "sagit", "hydrogen", "oxygen", "helium",
           "HM2013023", "armani", "HM2014811", "HM2014813", "omega", "lcsh92_wet_jb9", "gucci", "dior", "hermes", "ido",
           "land", "hennessy", "kate", "kenzo", "nikel", "prada", "markw", "ugg", "mido", "rolex", "santoni", "mocha",
           "latte", "cappu","ugglite" ]

devicesDict = {'aries': "Mi 2", 'pisces': "Mi 3 TD", 'cancro': "Mi 3 W/Mi 4", 'libra': "Mi 4c",
               'ferrari': "Mi 4i", 'aqua': "Mi 4s", 'gemini': "Mi 5", 'virgo': "Mi Note",
               'leo': "Mi Note Pro", 'scorpio': "Mi Note 2", 'jason': "Mi Note 3", 'tiffany': "Mi 5x",
               'song': "Mi 5c", 'meri': "Mi 5c", 'tissot': "Mi A1", 'capricorn': "Mi 5s", 'natrium': "Mi 5s+",
               'lithium': "Mi MIX", 'chiron': "Mi MIX 2",'polaris':'Mi MIX 2s', 'sagit': "Mi 6", 'hydrogen': "Mi MAX",
               'oxygen': "Mi MAX 2", 'helium': "Mi MAX PRO",
                'HM2013023': "Redmi 1 - WCDMA",
               'armani': "Redmi 1s - WCDMA", 'HM2014811': "Redmi 2 - WCDMA", 'HM2014813': "Redmi 2 - TD",
               'omega': "Redmi PRO", 'lcsh92_wet_jb9': "Redmi note 1 - 3g-mtk", 'gucci': "Redmi note 1s",
               'dior': "Redmi Note 1 - 4g", 'hermes': "Redmi Note 2", 'ido': "Redmi 3", 'land': "Redmi 3 S/X",
               'hennessy': "Redmi Note 3 (MTK)", 'kate': "Redmi Note 3 Global",
               'kenzo': "Redmi Note 3 Chinese", 'nikel': "Redmi Note 4", 'prada': "Redmi 4",
               'markw': "Redmi 4 pro", 'ugg': "Redmi Note 5A", 'mido': "Redmi Note 4/4x", 'rolex': "Redmi 4a",
               'santoni': "Redmi 4x", 'ugglite':'Redmi Note 5A','vince':'Redmi Note 5/5+','whyred':'Redmi Note 5 Pro',
                'mocha': "Mi PAD", 'latte': "Mi PAD 2", 'cappu': "Mi PAD 3"}

googleApps = {
    "youtube": "com.google.android.youtube",
    "drive": "com.google.android.apps.docs",
    "music": "com.google.android.music",
    "maps": ":com.google.android.apps.maps",
    "videos": "com.google.android.videos",
    "photos": "com.google.android.apps.photos",
    "chrome": "com.android.chrome",
    "gmail": "com.google.android.gm",
    "translate": "com.google.android.apps.translate",
    "duo": "com.google.android.apps.tachyon"

}

miuiApps = {
    "bugreport": "com.miui.bugreport",
    "compass": "com.miui.compass",
    "video": "com.miui.videoplayer",
    "mail": "com.android.email",
    "music": "com.miui.player",
    "scanner": "com.xiaomi.scanner",
    "browser": "com.android.browser",
    "screenrecorder": "com.miui.screenrecorder",
    "gallery": "com.miui.gallery",
    "updater": "com.android.updater",
    "midrop": "com.xiaomi.midrop",
    "calendar": "com.android.calendar",
    "miui assistant": "com.mi.android.globalpersonalassistant",
    "notes": "com.miui.notes",

}

localmd5s = [
    "f337d1707478d63315820a45030f547d",  # 0.camera
    "537e17e2585e731a1c26fbd81eb2affa",  # 1.home
]

def getInt():
    
    try:
        case = int(input(Back.BLUE + "choose: " + Back.RESET))
        return case
    except ValueError:
        print()
        print(Fore.RED+"Wrong, choose right option!"+Fore.RESET)
        case = int(getInt())
    return case
    
        




def mydevice():
    os.system("adb start-server")
    os.system("adb shell mount /system")
    glob_device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
    glob_device = open('tmp', 'r').read()
    open('tmp', "r").close()
    os.remove("tmp")
    os.system("adb shell umount /system")
    glob_device = glob_device.lstrip('ro.product.device')[1:]
    codename = ''.join(glob_device.split())
    devicename = codename
    clear()
    for key, values in devicesDict.items():
        if key == codename:
            codename = values
            return codename
        elif key != codename:
            continue
    codename = "none"
    return codename

# Thanks to stackoverflow!
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def dpiChanger():
    print(dashed_line)
    os.system("adb shell mount /system")
    print("Make sure that you made a build.prop backup! just in case")
    dpi = input("Tell me what is your desired dpi: ")
    print("Ok, i'll change dpi to this value!")
    os.system('adb shell "grep -v "ro.sf.lcd_density" /system/build.prop > /system/build.prop.2"')
    os.system('adb shell "cp /system/build.prop.2 /system/build.prop"')
    os.system('adb shell "echo "ro.sf.lcd_density = ' + dpi + '" >> /system/build.prop"')
    os.system('adb shell "chmod 644 /system/build.prop"')
    print("Dpi has been changed!" + Fore.RESET)
    os.system("adb shell umount /system")
    input("push enter to continue")
    print(dashed_line)
    sTweaksMenu()

def mix2Cam():
    print(dashed_line)
    path = resPath + os.sep + "cam.apk"
    os.system("adb shell mount /system")
    isf = os.path.isfile(os.path.dirname(resPath) + os.sep + "cam.apk")
    if not isf:
        print(Fore.WHITE + "I need to download camera file first, be patient please" + Fore.RESET)
        urllib.request.urlretrieve('http://www1.zippyshare.com/d/T0XrorQl/9267/cam.apk', resPath + 'cam.apk')
    elif isf:
        print(Fore.WHITE + "Ok, you have camera file already!" + Fore.RESET)
    md5sum = md5(path)
    if md5sum == localmd5s[0]:
        os.system("adb push " + resPath + "cam.apk /system/priv-app/MiuiCamera/MiuiCamera.apk")
        os.system("adb shell chmod 644 /system/priv-app/MiuiCamera/MiuiCamera.apk")
        print(Back.BLUE + "Your old camera is still here, backed up, just in case" + Back.RESET)
        os.system("adb shell umount /system")
        input(Fore.GREEN + "push enter to continue" + Fore.RESET)
        print(dashed_line)
        sTweaksMenu()
    else:
        print("But it's looks like it's broken, let me re-download it!")
        os.remove(path)
        mix2Cam()

def comMiuiHome():
    print(dashed_line)
    path = resPath + os.sep + "com.miui.home"
    os.system("adb shell mount /system")
    os.system("adb shell mv /system/media/theme/default/com.miui.home /system/media/theme/default/com.miui.home.old")
    isf = os.path.isfile(os.path.dirname(resPath) + os.sep + "com.miui.home")
    if not isf:
        print(Fore.WHITE + "I need to download custom home file first, be patient please" + Fore.RESET)
        urllib.request.urlretrieve('http://www9.zippyshare.com/d/dRMuSMgW/9585/com.miui.home', resPath + 'com.miui.home')
    elif isf:
        print(Fore.WHITE + "Ok, you have custom home file already!" + Fore.RESET)
    md5sum = md5(path)
    if md5sum == localmd5s[1]:
        os.system("adb push " + resPath + "com.miui.home /system/media/theme/default/com.miui.home")
        os.system("adb shell chmod 644 /system/media/theme/default/com.miui.home")
        print(Back.BLUE + "Your old com.miui.home is still here, backed up, just in case" + Back.RESET)
        os.system("adb shell umount /system")
        input(Fore.GREEN +"push enter to continue" + Fore.RESET)
        print(dashed_line)
        sTweaksMenu()
    else:
        os.remove(path)
        print("But it's looks like it's broken, let me re-download it!")
        comMiuiHome()

def bl():
    os.system("adb reboot bootloader")
    clear()
    print(dashed_line)
    print("Your bootloader status is: ")
    os.system('fastboot oem device-info > results.txt 2>&1')
    bl = open('results.txt', 'r').read()
    os.remove('results.txt')
    # bl = bl[72]+bl[73]+bl[74]+bl[75]+bl[76]
    if bl[72] == "t":
        bl = "Unlocked"
        print(Fore.GREEN + bl + Fore.RESET)
    elif bl[72] == "f":
        bl = "Locked"
        print(Fore.RED + bl + Fore.RESET)
    print()
    input(Back.BLUE + "Push enter to exit" + Back.RESET)
    menu()

def sideloader():
    while (True):
        print(dashed_line)
        print(
            Fore.WHITE + "Due to problems with adb sideload implementation, you have to start sideload on your phone manually!" + Fore.RESET)
        sideloadFile = input(Back.BLUE + "Drag and drop your file here: " + Back.RESET)
        os.system("adb sideload " + sideloadFile)
        ifContinue = input("Do you want to sideload next file? (y/n)")
        ifContinue = str(ifContinue).lower()
        if ifContinue == 'n':
            print(Fore.WHITE + "Ok, we'll go back now" + Fore.RESET)
            input("Push enter to continue")
            print(dashed_line)
            menu()
        elif ifContinue == "y":
            print(Fore.WHITE + "Ok! so here we go again" + Fore.RESET)
        else:
            print(
                Fore.RED + "Wrong option, so we will stop now, if u want to continue sideloading, just re launch this option from menu" + Fore.RESET)
            print(dashed_line)
            time.sleep(5)
            menu()

def remover(appList):
    print(dashed_line + Fore.LIGHTCYAN_EX)
    i = 1
    for key, values in appList.items():
        print("%i. %s" % (i, key.capitalize()))
        i = i + 1
    print()
    print("0. Exit")
    case = getInt()
    i = 0
    if case == 0:
        clear()
        sTweaksMenu()
    else:
        for key, values in appList.items():
            pckg = values
            if case == i + 1:
                clear()
                print(dashed_line + Fore.GREEN)
                os.system("adb shell \"pm uninstall -k --user 0 %s\"" % pckg)
                print (pckg)
                if appList==miuiApps:
                    removermiui()
                elif appList==googleApps:
                    removergoogle()
            else:
                i = i + 1
                continue


def appremover():
    print(dashed_line)
    print(Fore.YELLOW + "| X.E.T                                                            |")
    print("| App remover menu                                                  |")
    print(dashed_line)
    print(Fore.CYAN + "| 1. Miui Apps")
    print(dashed_line)
    print(Fore.CYAN +"| 2. Google Apps")
    print(dashed_line)
    print(Fore.CYAN +"| 3. Full")
    print(Fore.RED + "| ^This one will remove all possible google and miui apps"+Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "| 0. Exit")
    print(dashed_line)
    case = getInt()
    if case == 1:
        clear()
        remover(miuiApps)
    elif case == 2:
        clear()
        remover(googleApps)
    elif case == 3:
        apps = list("")
        pckg = list("")
        i = 0
        for key, values in googleApps.items():
            apps.append(key)
            pckg.append(values)
            i = i + 1
            continue
        for key, values in miuiApps.items():
            apps.append(key)
            pckg.append(values)
            i = i + 1
            continue
        print(Fore.RED + "Are you sure you want to remove: %s?" % ', '.join(apps))
        case = input(Back.BLUE + "Y/N: " + Back.RESET)
        if case.lower() == "y":
            for x in pckg:
                os.system("adb shell \" pm uninstall -k --user 0 %s\"" % x)
            clear()
            print(dashed_line)
            print("Everything seems to be removed")
            input("Press enter to go back")
            sTweaksMenu()
        elif case.lower() == "n":
            sTweaksMenu()
    elif case==0:
        sTweaksMenu()

def rbMenu():
    clear()
    print(mydevice())
    print(dashed_line)
    print(Fore.YELLOW + "| X.E.T                                                            |")
    print("| REBOOT MENU                                                      |")
    print("| Some devices, like RN3P might have problems with reboots         |")
    print("| from system, but reboots should work from adb/fastboot           |")
    print(dashed_line + Fore.RESET)
    print(Fore.CYAN + "|1. Reboot to recovery                                             |")
    print(Fore.WHITE + "|Reboot to recovery using ADB (so make sure to turn on debugging)  |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|2. Reboot to fastboot                                             |")
    print(Fore.WHITE + "|Reboot to fastboot using ADB (so make sure to turn on debugging)  |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|3. Reboot to system                                               |")
    print(Fore.WHITE + "|Reboot to system using ADB (so make sure to turn on debugging)    |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|4. Reboot to system                                               |")
    print(Fore.WHITE + "|Reboot to system using Fastboot mode!                             |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|5. Reboot to adb-sideload                                         |")
    print(Fore.WHITE + "|Reboot to sideload using ADB-root (so use it when in recovery)    |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|6. Boot twrp from file                                            |")
    print(Fore.WHITE + "|You can use it when you dont want to install it                   |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|0. Back to main menu                                              |")
    print(dashed_line + Fore.RESET)
    case = getInt()
    if case == 1:
        clear()
        os.system('adb reboot recovery')
        os.system('adb kill-server')
        rbMenu()
    elif case == 2:
        clear()
        os.system('adb reboot bootloader')
        os.system('adb kill-server')
        rbMenu()
    elif case == 3:
        clear()
        os.system('adb reboot')
        os.system('adb kill-server')
        rbMenu()
    elif case == 4:
        clear()
        os.system('fastboot reboot')
        menu()
    elif case == 5:
        clear()
        os.system('adb reboot sideload')
        menu()
    elif case == 6:
        clear()
        twrp = input("Put twrp file here: ")
        os.system('fastboot boot '+twrp)
        menu()
    elif case == 0:
        killsystem
        clear()
        menu()
    else:
        clear()
        print(Fore.RED + "Error you should choose right option!" + Fore.RESET)
        input("push enter to continue")
        rbMenu()

# Tweaks
def sTweaksMenu():
    clear()
    print(mydevice())
    print(dashed_line)
    print(Fore.YELLOW + "| X.E.T                                                            |")
    print("| SYSTEM TWEEKS MENU                                               |")
    print(dashed_line)
    print(Fore.CYAN + "|1. Build.prop backup                                              |")
    print(Fore.WHITE + "|Use it to backup your build.prop file!                            |")
    print(dashed_line)
    print(Fore.CYAN + "|2. Build.prop restore                                             |")
    print(Fore.WHITE + "|Use it to restore your build.prop file!                           |")
    print(dashed_line)
    print(Fore.CYAN + "|3. Change DPI                                                     |")
    print(Fore.WHITE + "|For changing dpi more than once, you have to restore build.prop!  |")
    print(dashed_line)
    print(Fore.CYAN + "|4. Install mix 2 camera                                           |")
    print(Fore.WHITE + "|Mix 2 camera ported for all Xiaomi devices;Tested only on miui9   |")
    print(dashed_line)
    print(Fore.CYAN + "|5. Install modified com.miui.home (desktop grid up to 10x10)      |")
    print(Fore.WHITE + "|Miui 9 exclusive                                                  |")
    print(dashed_line)
    print(Fore.CYAN + "|6. Activate Camera 2 API                                          |")
    print(Fore.WHITE + "|Use it to activate cam2api in your build.prop                     |")
    print(dashed_line)
    print(Fore.CYAN + "|7. System apps remover                                            |")
    print(Fore.WHITE + "|Remove google/miui apss without root, from system                 |")
    print(dashed_line)
    print(Fore.CYAN + "|0. Back to main menu                                              |")
    print(dashed_line)
    case = getInt()
    if case == 1:
        clear()
        print(dashed_line)
        os.system("adb shell mount /system")
        os.system("adb pull /system/build.prop " + resPath + "build.prop")
        print(Fore.WHITE + "Backup complete! Your build.prop is now in res folder!" + Fore.RESET)
        os.system("adb shell umount /system")
        input("push enter to continue")
        print(dashed_line)
        sTweaksMenu()
    elif case == 2:
        clear()
        print(dashed_line)
        os.system("adb shell mount /system")
        os.system("adb push " + resPath + "build.prop /system/build.prop")
        os.system('adb shell "chmod 644 /system/build.prop"')
        print(Fore.WHITE + "Restore complete!" + Fore.RESET)
        os.system("adb shell umount /system")
        input("push enter to continue")
        print(dashed_line)
        sTweaksMenu()
    elif case == 3:
        clear()
        dpiChanger()
    elif case == 4:
        clear()
        mix2Cam()
    elif case == 5:
        clear()
        comMiuiHome()
    elif case == 6:
        clear()
        os.system("adb shell mount /system")
        os.system('adb shell "echo persist.camera.HAL3.enabled=1 >> /system/build.prop"')
        print("You have enabled Camera 2 API YAY!")
        os.system("adb shell umount /system")
        input("push enter to continue")
        sTweaksMenu()
    elif case == 7:
        clear()
        appremover()
    elif case == 8:
        clear()
        autoroot()
    elif case == 0:
        killsystem
        clear()
        menu()
    else:
        clear()
        print(Fore.RED + "Error you should choose right option!" + Fore.RESET)
        input("push enter to continue")
        sTweaksMenu()

# about
def aboutMenu():
    clear()
    print(mydevice())
    print(dashed_line)
    print(Fore.YELLOW + "| X.E.T                                                            |")
    print("| About                                                            |")
    print(dashed_line)
    print(Fore.CYAN + "|1. About script                                                   |")
    print(dashed_line)
    print(Fore.CYAN + "|2. Contact                                                        |")
    print(dashed_line)
    print(Fore.CYAN + "|3. Donations                                                      |")
    print(dashed_line)
    print(Fore.CYAN + "|4. Credits                                                        |")
    print(dashed_line)
    print(Fore.CYAN + "|0. Back                                                           |")
    print(dashed_line)
    case = getInt()
    if case == 1:
        print(dashed_line)
        print("Simply script, created by student, to make some tweaks easier to apply")
        print("First script purpose was to only automatize twrp installing (that's why repo is called twrp-installer)")
        print("Script is aiming to support Xiaomi devices(Some features are universal) on both Windows and Linux")
        print("When more test will be made, there will be stable executable version avalible for Windows")
        print(dashed_line)
        input()
        aboutMenu()
    elif case == 2:
        print(dashed_line)
        print("U can contact me on various sites, mostly under nickname Mezutelni")
        print("- github.com/mezutelni/")
        print("- miuipolska.pl/forum/profile/7082-mezutelni/")
        print("- forum.xda-developers.com/member.php?u=6270598")
        print(dashed_line)
        input()
        aboutMenu()
    elif case == 3:
        print(dashed_line)
        print(
            "If you want to buy me a beer, or keep my servers online, or simply say Thank You, please consider Donation for me")
        print("You can do it by PayPal on PayPal.me/Mezutelni or by contacting with me directly (see contact)")
        print(dashed_line)
        input()
        aboutMenu()
    elif case == 4:
        print(dashed_line)
        print("Thanks to: ")
        print("- Facebook group \" Złomowisko Rudej\" for inspiration and help with testing")
        print("- MiuiPolska forum society for help with testing and trusting me")
        print("- Orjon from MiuiPolska for idea and alpha code for google's app remover")
        print(dashed_line)
        input()
        aboutMenu()
    elif case == 0:
        menu()
    else:
        aboutMenu()

# main
def menu():
    clear()
    print(mydevice())
    print(dashed_line)
    print(Fore.YELLOW + "| X.E.T                                                            |")
    print("| Xiaomi Essential Tools                                           |")
    print(dashed_line + Fore.RESET)
    print(Fore.CYAN + "|1. Reboot menu                                                    |")
    print(Fore.WHITE + "|Simple reboot menu, to make your life more comfortable!           |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|2. System tweaks                                                  |")
    print(Fore.WHITE + "|Here you can find system tweaks, they are all applied in recovery!|" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|3. Install Recovery                                               |")
    print(Fore.WHITE + "|Use it to install recovery | Due to server problems, auto installer is off for now|" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|4. Check bootloader status (locked/unlocked)                      |")
    print(Fore.WHITE + "|You have to be in fastboot mode to make it work                   |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|5. ADB sideloader                                                 |")
    print(Fore.WHITE + "|Start in recovery, then use it to flash all zips you want!        |" + Fore.RESET)
    print(dashed_line)
    print(Fore.CYAN + "|9. About                                                          |")
    print(dashed_line)
    print(Fore.CYAN + "|0. Exit                                                           |")
    print(dashed_line + Fore.RESET)
    case = getInt()
    
    if case == 1:
        killsystem
        rbMenu()
    elif case == 2:
        killsystem
        sTweaksMenu()
    elif case == 3:
        killsystem
        twrpInstaller(mydevice(), s)
        menu()
    elif case == 4:
        clear()
        bl()
        input("push enter to continue")
        menu()
    elif case == 5:
        killsystem
        clear()
        sideloader()
    elif case == 9:
        clear()
        aboutMenu()
    elif case == 0:
        killsystem
        print(Fore.GREEN + "Consider a donation for me to keep my servers up!")
        print("www.paypal.me/Mezutelni")
        sys.exit()
    else:
        clear()
        print("Error choose right option\n" + Fore.RESET)
        input("push enter to continue")
        menu()

menu()
