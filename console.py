#!usr/bin/python3

"""Defines the HBnb console"""

import cmd
import models

"""entry point for hbnb console"""

class HBNBCommand(cmd.Cmd):
    """creates a custom command line"""
    prompt = '(hbnb) '

    def emptyline(self):
        """does nothing when an empythline is entered"""
        pass

    def do_create(self, clsname=None):
        """Creates an new instance of the BaseModel
        saves the instance and print the id of the instance"""
        if not clsname:
            print('**class name missing **')
        elif not self.clslist.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[clsname]()
            models.storage.save()
            print(obj.id)

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program when user presses Ctrl-D"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
