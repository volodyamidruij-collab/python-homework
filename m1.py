import colorama:
from colorama import Fore, Back, Style

colorama.init()


print(dir(colorama))

print(colorama.__doc__)

print(dir(Fore))

print(dir(Back))

print(dir(Style))

print(Fore.RED + "Червоний текст" + Style.RESET_ALL)
print(Fore.GREEN + "Зелений текст" + Style.RESET_ALL)

print(Back.YELLOW + "Жовтий фон" + Style.RESET_ALL)

print(Style.BRIGHT + "Яскравий текст" + Style.RESET_ALL)
print(Style.DIM + "Тьмяний текст" + Style.RESET_ALL)