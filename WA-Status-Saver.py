# WHATSAPP STATUS SAVER FOR ANDROID ONLY!
# PLEASE INSTALL COLORAMA MODULE BY USING ''pip install colorama'' BEFORE RUNNING THE SCRIPT.
# IT IS RECOMMENDED THAT YOU RUN THIS SCRIPT IN TERMUX APP.


# IMPORTING NECESSARY MODULES

import time
import os
import shutil
import sys
import platform

# CHECKING A COLORAMA MODULE IS ALREADY INSTALLED OR NOT BEFORE IMPORTING COLORAMA MODULE TO PREVENT MODULE NOT FOUND ERROR
try:
	from colorama import Fore, Back, Style, init
	init(autoreset=True)
except ModuleNotFoundError:
	print( '\nERROR: Colorama Module Not Installed. Please Install it by running "pip install colorama" in the terminal.')
	sys.exit(1)
	



# VARIABLES

# source of WhatsApp statuses
source = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses"

# destination where WhatsApp statuses will be saved
destination = "/storage/emulated/0/Download/Status Saver"

# path for .nomedia file that prevents statuses from showing in gallery 
nomedia_path = ( "/storage/emulated/0/Download/Status Saver/.nomedia")

# CHECK ANDROID OS AVALIABILITY
android = 'android' in platform.uname().release.lower()

# MAIN MENU
choices = Fore.CYAN + Style.BRIGHT + """1. Manual Status Saving\n2. Automated Status Saving\n3. Help"""

# HELP MENU
help = """\n—————————————————————————————————————————————————————\nHELP:\n• Exit: Ctrl + C\n• Manual Saving: You have to run the script every time you need to save statuses.\n• Automated Saving: The Script will keep saving statuses on specified time intervals as long as the script is running\n• Automated Saving may use some battery. Use Manual mode for better battery life.\n—————————————————————————————————————————————————————"""

print(Fore.YELLOW + Style.BRIGHT + Back.RED + 'WhatsApp Status Saver '.center(52))


# FUNCTIONS

# CHECKING IF RUNNING ON ANDROID OS OR NOT
def check_android_os():
	pass


# DETECT AND PARSE ANDROID VERSION
def android_v():
	global android_version
	android_version = (os.popen('getprop ro.build.version.release').read().strip()[0:3])
	if float(android_version) < 9:
		android_version = android_version[0:2]
	elif float(android_version) > 10:
		android_version = android_version[0:3]
	else:
		print(Fore.RED + Style.BRIGHT + 'Non-Android OS Detected, This Script Will Only Work on Android OS')
		sys.exit(1)



# CHECK ANDROID VERSION
def check_android_version():
    if float(android_version) <= 9:
        global source
        source = "/storage/emulated/0/WhatsApp/Media/.Statuses"
    else:
        pass 



# COPY STATUSES TO PATH		
def copy_statuses():
	try:
		shutil.copytree(source, destination, dirs_exist_ok = True ) #create a new folder if it doesn't exists and pass if it already exists
	except TypeError:
		print(Fore.LIGHTRED_EX + 'ERROR: OUTDATED PYTHON VERSION. Please Update Python to 3.8 or newer.')
		sys.exit(1)



# DELETE .NOMEDIA FILE TO SHOW STATUSES IN GALLERY
def delete_nomedia():
	if os.path.exists(nomedia_path):
		os.remove(nomedia_path)
		time.sleep(0.5)


# CHECK ANDROID OS
check_android_os()


# SUB-MAIN FUNCTION
def sub_main():
	android_v()
	check_android_version()
	copy_statuses()
	delete_nomedia()



# AUTOMATION ZONE
def automated_sub_main():
	sleep_time = float(input('Enter Number of Seconds for Every Automated Status Saving Interval: '))
	print(Fore.YELLOW+ Style.BRIGHT + f"\nAuto-Saving Statuses every {sleep_time:.1f} seconds...\nEnter Ctrl+C to exit the loop...")
	while True:
		sub_main()
		time.sleep(sleep_time)
		print(Fore.GREEN+ Style.BRIGHT + f"Saved Statuses At: {time.strftime('%H:%M:%S')}")



# SHOW MENU AND ASK FOR CHOICE 
def ask_method():
	inp = int(input(Style.BRIGHT +Fore.YELLOW+ f'\nCHOOSE AN OPTION:\n{choices}\n'))
	if inp == 1:
		sub_main()
		print(Fore.GREEN + Style.BRIGHT + 'Statuses Saved In Downloads Folder.')
	elif inp == 2:
		automated_sub_main()
	elif inp == 3:
		print(Style.BRIGHT + Fore.CYAN + help)
	else:
		print(Fore.RED + Style.BRIGHT + '\nERROR: INVALID CHOICE')



#MAIN FUNCTION
def main():
	while True:
		try:	
			ask_method()
		except KeyboardInterrupt:
			print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '\n\n👋 Exiting... Goodbye!')
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + f'\nERROR: Invalid Input')
		except FileNotFoundError:
			print(Fore.RED + Style.BRIGHT + '\nERROR: WhatsApp is not Installed in Your Phone. Please Install it Or Try again. If the Problem persists, please make Sure Download Folder Exists on your Device.')
			sys.exit(1)
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f'\nERROR: {e}')
			sys.exit(1)

# MAIN
main()


# END
# Uzair_902 — 20 June 2025 9:31 AM PST
# Thanks For Using!
# Enjoy!