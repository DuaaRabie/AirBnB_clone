#!/usr/bin/python3
""" This Module For Interpreter (console) """
import cmd
import uuid
import sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage


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
        """ create a model instance """
        if not line:
            print("** class name missing **")
            return
        if line not in globals():
            print("** class doesn't exist **")
            return
        instance = class_name()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """ show the instance """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, line):
        """ deletes an instance """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals(): 
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """ prints all string representations for all instances"""
        if line and line not in globals():
            print("** class doesn't exist **")
            return
        stored = storage.all().items()
        instances = [str(v) for k, v in stored if line in k or not line]
        print([instance for instance in instances])

    def do_update(self, line):
        """ Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        if not instance_id:
            print("** instance id missing **")
            return
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        attr = args[2]
        if not attr:
            print("** attribute name missing **")
            return
        value = args[3]
        if not value:
            print("** value missing **")
            return
        setattr(instance, attr, value)
        instance.save()

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
