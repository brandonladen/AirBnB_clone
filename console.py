#!usr/bin/python3

"""Defines the HBnb console"""

import cmd
import models
from models.base_model import BaseModel

"""entry point for hbnb console"""

class HBNBCommand(cmd.Cmd):
    """creates a custom command line"""
    prompt = '(hbnb) '
    classlist = {'BaseModel': BaseModel}

    def emptyline(self):
        """does nothing when an empythline is entered"""
        pass

    def do_create(self, classname=None):
        """Creates an new instance of the BaseModel
        saves the instance and print the id of the instance"""
        if not classname:
            print('**class name missing **')
        elif not self.classlist.get(classname):
            print('** class doesn\'t exist **')
        else:
            obj = self.classlist[classname]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """displays the string rep of the instance based on the class name and id"""
        classname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not classname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.classlist.get(classname):
            print('** class doesn\'t exist')
        else:
            i = classname + "." + objid
            obj = models.storage.all().get(i)
            if not obj:
                print('** no istance found **')
            else:
                print(obj)
            
    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program when user presses Ctrl-D"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
