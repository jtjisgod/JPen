import os
from terminaltables import AsciiTable

class JCommand:

    def __init__(self):
        self.commands = {
            "help" : {
                "title" : "Shows helps",
                "description" : "Shows manuals",
                "run" : self.help
            },
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
        asciiTable.title = "DAOGI HELP"
        print(asciiTable.table)
    
    def control(self, command) :
        if not command.strip() :
            return False

        command = command.split(" ") if " " in command else [command, ]

        if command[0] not in self.commands.keys() :
            print("Invalid Command [ %s ]"%(command[0]))
            return False
 
        commandObject = self.commands[command[0]]
        if type(commandObject) == dict : commandObject['run'](command[1:])
        else : commandObject.run(command[1:])
