import termcolor
import pyfiglet
from pyfiglet import FigletString
from pyfiglet import Figlet
from pyfiglet import figlet_format

f = Figlet(font='isometric1')

word_to_prnt = "hi"
word_converted = ""

for letter in word_to_prnt:
    if word_to_prnt.index(letter) % 2 == 0 :
        word_converted += termcolor.colored(figlet_format(letter), "green")
    else:
        word_converted += termcolor.colored(figlet_format(letter), "blue")

print(word_converted)

