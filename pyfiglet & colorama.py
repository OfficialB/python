# colorama & pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pyfiglet import figlet_format,Figlet
# ascii with color
f = Figlet(font='doom')
print(Fore.BLUE + f.renderText('pyfiglet is cool!'))
print(Fore.BLACK + f.renderText('colorama is cool!'))