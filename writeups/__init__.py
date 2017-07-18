import overflow1, overflow2, overflow3, overflow4, overflow5
from binaryninja import get_choice_input, PluginCommand

choices = ['Overflow 1', 'Overflow 2', 'Overflow 3', 'Overflow 4', 'Overflow 5']

def choose_writeup(bv):
    choice = get_choice_input("Writeup:", "Open Writeup", choices) + 1

    if choice == 1:
        overflow1.render(bv)
    elif choice == 2:
        overflow2.render(bv)
    elif choice == 3:
        overflow3.render(bv)
    elif choice == 4:
        overflow4.render(bv)
    elif choice == 5:
        overflow5.render(bv)

PluginCommand.register("Open Writeup", "Opens one of the PicoCTF Overflow Writeups", choose_writeup)
