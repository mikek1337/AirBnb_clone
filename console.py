"Console module."

import cmd


class HBNBCommand(cmd.Cmd):

    def preloop(self):
        self.prompt = "(hbnb) "

    def do_EOF(self, line):
        """Close program"""
        return True

    def do_quit(self, line):
        """Close progam"""
        return True
    def emptyline(self) -> bool:
        return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()
