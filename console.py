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
        """ Prints the string representation of an instance
            based on the class name and id
        """

        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name in HBNBCommand.class_maps:
            instance_val = '{}.{}'.format(class_name, instance_id)
            objects_all = models.storage.all()

            if instance_val in objects_all.keys():
                obj = objects_all[instance_val]
                print(obj)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """ Documentation for show command """
        print("\n".join([
            "Usage: show [class_name][id]",
            "Prints the string representation of an instance",
            "Based on the class name and id"]))

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.class_maps:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if class_name in HBNBCommand.class_maps:
            instance_val = '{}.{}'.format(class_name, instance_id)
            objects_all = models.storage.all()

            if instance_val in objects_all.keys():
                del models.storage.all()[instance_val]
                models.storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """ Documentation for destroy command """
        print("\n".join([
            "Usage: destroy [class_name] [id]",
            "Deletes an instance based on the class name and id",
            "Save the change into the JSON file"]))

    def do_all(self, line):
        """ Prints all string representation of all instances """
        args = shlex.split(line)

        all_objects = models.storage.all()
        all_obj_list = []

        if not line:
            for object in all_objects.values():
                all_obj_list.append(str(object))
            print(all_obj_list)
            return

        class_name = args[0]
        if class_name not in HBNBCommand.class_maps:
            print("** class doesn't exist **")
            return

        obj_list = []
        for object in all_objects.values():
            if type(object).__name__ == class_name:
                obj_list.append(str(object))
            print(obj_list)

    def help_all(self):
        """ Documentation of all command """
        print("\n".join([
            "Usage: all [class_name] or all",
            "Prints all string representation of all instances",
            "Based or not on the class name."]))

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in HBNBCommand.class_maps:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        instance_val = '{}.{}'.format(class_name, instance_id)
        objects_all = models.storage.all()

        if instance_val not in objects_all.keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_val = args[3]

        attr_type = type(eval(attr_val))
        if attr_type not in (str, float, int):
            return

        setattr(objects_all[instance_val], attr_name, eval(attr_val))
        models.storage.save()

    def help_update(self):
        """ Documentation for the update command """
        print("\n".join([
            "Usage: update [class_name] [id] [attr_name] [attr_value]",
            "Updates an instance based on the class name and id"
            "by adding or updating attribute",
            "Then save the change into the JSON file"]))

    def do_quit(self, line):
        """ Quit command to exit the pogram """
        exit()

    def help_quit(self):
        """ Documentation for the quit command"""
        print("Exit the program cleanly when quit is entered")

    def do_EOF(self, line):
        """ End of File, Ctrl+C && Ctrl+D """
        print()
        return True

    def help_EOF(self):
        """ Documentation for EOF command """
        print("\n".join(["Ctrl+C: KeyboardInterrupt that exit program",
                         "Ctrl+D: End the program"]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
