import Command as Cmd
import JDns

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "dns"

        # Title of this command
        self.title       = "DNS Checker"

        # Description of this command
        self.description = "Finding and show DNS information"

        # Usage of this command
        self.usage = "dns <domain>"

    
    def call(self, func) :
        return self.functions[func]()

    def run(self, command=[]) :
        if len(command) == 0 :
            self.printUsage()
            return
        dns = JDns.JDns(command[0])
        dns.run()
        print(dns.pretty())
        