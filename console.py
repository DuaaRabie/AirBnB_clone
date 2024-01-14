#!/usr/bin/python3
""" This Module For Interpreter (console) """
import cmd


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

    def help_EOF(self):
        print("Exit the console")

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_emptyline(self):
        print("Do nothing")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
