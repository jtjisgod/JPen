class Command :

    def __init__(self) :
        self.command     = ""    # Instruction of this command
        self.title       = ""    # Title of this command
        self.description = ""    # Description of this command
        self.usage       = ""    # Usage of this command
        self.functions = {"run": self.run,}

    def run(self, command=[]) :
        pass
    
    def printUsage(self) :
        print("\tUsage of this command < %s > : "%(self.title))
        print("\t" + self.usage)
        