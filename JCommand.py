import os
from terminaltables import AsciiTable

class JCommand:

    def __init__(self):
        self.shell = (
            "clear",
            "ls",
            "cat",
            "curl",
            
        )
        self.history = []
        self.commands = {
            "help" : {
                "title" : "Shows helps",
                "description" : "Shows manuals",
                "run" : self.help
            },
            "history" : {
                "title" : "Shows command history",
                "description" : "Shows history",
                "run" : self.showHistory
            }
        }
        for d in os.scandir("./Commands/") :
            if ".py" not in d.name :
                continue
            command = vars(__import__("Commands.%s"%(d.name.split(".py")[0])))[d.name.split(".py")[0]].Command()
            self.commands[command.command] = command

    def help(self, args=[]) :
        # os.system("clear")
        table = [["COMMAND", "TITLE", "DESCRIPTION"]]
        for command in self.commands.keys() :
            tr = []
            if type(self.commands[command]) == dict :
                title = self.commands[command]['title']
                description = self.commands[command]['description']
            else :
                title = self.commands[command].__dict__['title']
                description = self.commands[command].__dict__['description']
            tr.append(command)
            tr.append(title)
            tr.append(description)
            table.append(tr)

        asciiTable = AsciiTable(table)
        asciiTable.title = "JPEN COMMAND HELP"
        print(asciiTable.table)
    
    def showHistory(self, args=[]) :
        if len(args) == 1 :
            try :
                i = int(args[0])
            except :
                print("Insert only number.")
                return
            try :
                self.control(self.history[i])
            except :
                print("Out of index.. Please check history index.")
            return
        for i in range(0, len(self.history)) :
            print("\t#%04d %s"%(i, self.history[i]))

    def control(self, command) :

        command = command.strip()

        if command == "q" :
            return False
        
        if not command.strip() :
            return True

        self.history.append(command)

        command = command.split(" ") if " " in command else [command, ]

        if command[0] in self.shell :
            os.system(" ".join(command))
            return True

        if command[0] not in self.commands.keys() :
            print("Invalid Command [ %s ]"%(command[0]))
            return True
 
        commandObject = self.commands[command[0]]
        if type(commandObject) == dict : commandObject['run'](command[1:])
        else : commandObject.run(command[1:])
        return True
