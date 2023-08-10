#!usr/bin/python3

"""Defines the HBnb console"""

import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
from shlex import shlex
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

"""entry point for hbnb console"""

class HBNBCommand(cmd.Cmd):
    """creates a custom command line"""
    prompt = '(hbnb) '
    classlist = {'BaseModel': BaseModel, 'User': User, 'State': State,
                 'City': City, 'Amenity': Amenity, 'Place': Place,
                 'Review': Review,}

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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and instance id"""
        classname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            objid =args[1]
        if not classname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.classlist.get(classname):
            print('** class doesn\'t exist **')
        else:
            i = classname + "." + objid
            obj = models.storage.all().get(i)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[i]
                models.storage.save()

    def do_all(self, arg):
        """prints the string rep of all instances,
        either based on the provided class name or for all classes"""
        if not arg:
            print([str(s) for i, s in models.storage.all().items])
        else:
            if not self.classlist.get(arg):
                print("** class doesn\'t exist **")
                return False
            print([str(s) for i, s in models.storage.all().items()
                   if type(s) is self.classlist.get(arg)])
            
    def do_update(self, arg):
        """Updates an instance bsed on the classname and id"""
        classname, objid, attrname, attrval = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            objid = args[1]
        if len(args) > 2:
            attrname = args[2]
        if len(args) > 3:
            attrval = list(shlex(arg[3]))[0].strip('"')
        if not classname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not attrname:
             print('** attribute name missing **')
        elif not attrval:
            print('** value missing **')
        elif not self.classlist.get(classname):
            print('**class doen\'t exist')
        else:
            i = classname + "." + objid
            obj = models.storage.all().get(i)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attrname):
                    if type(getattr(obj, attrname)) == int:
                        attrval = int(attrval)
                    elif type(getattr(obj, attrval)) == float:
                        attrval = float(attrval)
                    setattr(obj, attrname, attrval)
                    obj.updated_at = updatetime
                    models.storage.save()

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program when user presses Ctrl-D"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
