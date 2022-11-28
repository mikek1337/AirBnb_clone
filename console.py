#!/usr/bin/python3
"Console module."

import cmd
from models import BaseModel
import models 


class HBNBCommand(cmd.Cmd):
    """Command entry."""
    prompt = ("(hbnb) ")

    def do_EOF(self, line):
        """Quit command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self) -> bool:
        """Check's if """
        return False

    def do_create(self, line):
        """Create's and saves new class instance."""
        if len(line) == 0:
            print("** class name missing **")
            return

        try:
            args = line.split(" ")

            new_instance = eval("models."+args[0])()
            print(line)
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows object string based on the model name and id."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if (len(args) == 1):
                print("** instance id missing **")
                return
            try:
                objs = models.storage.all()
                eval("models."+args[0])
                key = args[0] + "." + args[1]
                try:
                    value = objs[key]
                    print(value)
                except KeyError:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy's object based on model name and id"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(" ")
            try:
                eval("models."+args[0])
                objs = models.storage.all()
                key = args[0] + "." + args[1]
                try:
                    objs.pop(key)
                    models.storage.save()
                except KeyError:
                    print("** instance not found. **")
            except NameError:
                print("** class doesn't extst **")

    def do_all(self, line):
        """Show's all stored objects"""
        if len(line) == 0:
            objs = models.storage.all()
            print(objs)
        else:
            try:
                eval(line)
                objs = models.storage.all()
                found = 0
                for key, value in objs.items():
                    key_split = key.split(".")
                    if key_split[0] == line:
                        print(value)
                        found = 1
                if (found == 0):
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
            Update an instance based on the class name and id
            sent as args.
        """
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = models.storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
