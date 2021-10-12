import os
import sys
import traceback
from colorama import Fore


if sys.platform != "linux" and sys.platform != "linux":
    print(Fore.RED + "Helena can only be installed on Linux!")
    print(Fore.RED + "Quitting...")
    quit()


# check if run in 'Helena' directory
files = os.listdir()
if "src" not in files:
    print(Fore.RED + "You have run this file incorrectly!")
    print(Fore.RED + "Please follow installation instructions on the github!")
    print(Fore.RED + "Quitting...")
    quit()


# check if admin
is_admin = (os.getuid() == 0)
if not is_admin:
    print(Fore.RED + "Admin privileges are needed to install Helena.")
    print(Fore.RED + "Try running the command with 'sudo'!")
    print(Fore.RED + "Quitting")
    quit()


try:
    os.system("mkdir /opt/helena")
    os.system("cp -r src /opt/helena/src")
    os.system("chmod +x installer/helena")
    os.system("cp -r installer/helena /usr/local/bin/helena")

    print(Fore.GREEN + "Helena was installed successfully!")
    print(Fore.GREEN + "Try running helena with the command 'helena' in the terminal!")
except SystemExit:
    # Excepted Error
    pass
except BaseException:
    print(Fore.RED + "An unexpected Error occured: Please open an issue on github!")
    print(Fore.WHITE)
    traceback.print_exc()
