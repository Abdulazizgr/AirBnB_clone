#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""
import cmd
import models
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        The class inheriting the cmd module
    """
    prompt = "(hbnb) "

    class_maps = {'BaseModel': BaseModel}

    def emptyline(self):
        """ overrides an empty command """
        pass

    def help_emptyline(self):
        """ Documentation for the emptyline """
        print("\n".join(["This prints an empty line",
                         "It ensures nothing is executed \
when empty line + ENTER is pressed", ]))

    def do_create(self, line):
        """ Creates a new instance of the BaseModel and save it """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name in HBNBCommand.class_maps:
            create_instance = HBNBCommand.class_maps[class_name]()
            create_instance.save()
            print('{}'.format(create_instance.id))
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """ Documentation for the create command """
        print("It creates a instance of the BaseModel, save it \
and use it print the id of the Basemodel")

    def do_show(self, line):
        """ Prints the string representation of an instance \
based on the class name and id """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name in HBNBCommand.class_mapping:
            instance_val = '{}.{}'.format(class_name, instance_id)
            objects_all = models.storage.all()

            if instance_val in objects_all.keys():
                obj = objects_all[instance_all]
                print(obj)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """ Quit command to exit the pogram """
        exit()

    def help_quit(self):
        """ Documentation for the quit command"""
        print("Exit the program cleanly when quit is entered")

    def do_EOF(self, line):
        """ End of File, Ctrl+C && Ctrl+D """
        return True

    def help_EOF(self):
        """ Documentation for EOF command """
        print("\n".join(["Ctrl+C: KeyboardInterrupt that exit program",
                         "Ctrl+D: End the program"]))

    def postloop(self):
        """ Overrides the end of the loop """
        print()

    def help_postloop(self):
        """ Documentation for postloop command """
        print(""" Ensures a newline after the program is exited """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
