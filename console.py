#!/usr/bin/python3
""" This Module For Interpreter (console) """
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ Custom command interpreter/console for AirBnB """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Exit the console """
        return True

    def do_EOF(self, line):
        """ Handle EOF (ctrl+D) Exit the console """
        return True

    def emptyline(self):
        """ When emptyline do nothing """
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line == "BaseModel":
            instance = BaseModel()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                ins_id = args[1]
                all_ins = models.storage.all()
                for key, value in all_ins.items():
                    ins_key = key.split(".")
                    instance = ins_key[1]
                    if instance == ins_id:
                        print(value)
                        return
                print("** no instance found **")
                return

    """ Help and Documentation Section """

    def help_EOF(self):
        """ EOF Doc """
        print("Exit the program")

    def help_quit(self):
        """ Quit Doc """
        print("Quit command to exit the program\n")

    def help_emptyline(self):
        """ Emptyline Doc """
        print("Do nothing")

    def help_create(self):
        """ Create Doc """
        print("This create new BaseModel instance\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
