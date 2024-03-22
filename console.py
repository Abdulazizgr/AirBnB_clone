#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        The class inheriting the cmd module
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """ overrides an empty command """
        return

    def do_quit(self, line):
        """ Quit command to exit the pogram """
        exit()

    def do_EOF(self, line):
        """ End of File, Ctrl+C && Ctrl+D """
        return True

    def postloop(self):
        """ Overrides the end of the loop """
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
