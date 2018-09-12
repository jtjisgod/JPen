import Command as Cmd
import JTarget
import JFIO
import JEnum
import JDto

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "dto"

        # Title of this command
        self.title       = "Domain takeover Checker"

        # Description of this command
        self.description = "Finding hijacking available domains."

        # Usage of this command
        self.usage = "dto <domain>"

    
    def call(self, func) :
        return self.functions[func]()

    def run(self, command=[]) :
        if len(command) == 0 :
            self.printUsage()
            return
        mJTarget = JTarget.JTarget(command[0])
        mJDto = JDto.JDto(mJTarget.element("domain"))
        if mJDto.run() == False :
            print("Please run 'subdomain' firstly.")
            return
        