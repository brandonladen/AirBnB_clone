#!usr/bin/python3

"""Defines the HBnb console"""

import cmd
"""entry point for hbnb console"""

class HBNBCommand(cmd.Cmd):
    """creates a custom command line"""
    prompt = '(hbnb) '

    def emptyline(self):
        """does nothing when an empythline is entered"""
        pass

    def do_quit(sef, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program when user presses Ctrl-D"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
