from helena import Helena
import colorama
import sys


helena = None


def check_python_version():
    return sys.version_info[0] == 3


def main():
    global helena
    # enable color on windows
    colorama.init()
    helena = Helena()
    helena.cmd_loop()


def get_helena():
    return helena


if __name__ == "__main__":
    if check_python_version():
        main()
    else:
        print("Helena only works with Python 3!")
