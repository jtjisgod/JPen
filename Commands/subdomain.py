import Command as Cmd
import JDns

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "subdomain"

        # Title of this command
        self.title       = "Subdomain Finder"

        # Description of this command
        self.description = "Finding sub domains of input domain with DNS"

    
    def call(self, func) :
        return self.functions[func]()

    def run(self, command=[]) :
        print("ASDASDSAD")
        