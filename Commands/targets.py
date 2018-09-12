import Command as Cmd
from terminaltables import AsciiTable

import JFIO

import JEnum

import JTarget

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "targets"

        # Title of this command
        self.title       = "Show attack targets"

        # Description of this command
        self.description = "Show attack targets in assets directory."

        # Usage of this command
        self.usage = "targets # list of targets.\n\ttargets create <domain> # Create Target on target list \n\ttargets remove <domain> # Remove Target"

    
    def call(self, func) :
        return self.functions[func]()

    def run(self, command=[]) :
        if len(command) == 0 :
            files = JFIO.getFileList(JEnum.targets, lambda x: x.endswith(".bin"))
            tableKeys = []
            table = []
            targets = []
            for file in files :
                mJTarget = JTarget.JTarget(file, initType=1)
                tableKeys.extend(mJTarget.target.keys())
                targets.append(mJTarget.target)
            tableKeys = list(set(tableKeys))
            for target in targets :
                row = []
                for tableKey in tableKeys :
                    row.append(target.get(tableKey, "-"))
                table.append(row)
            tableKeys = [tableKeys,]
            asciiTable = AsciiTable(tableKeys + table)
            asciiTable.title = "Target List"
            print(asciiTable.table)
            return
        elif len(command) == 2 :
            if command[0] == "create" :
                mJTarget = JTarget.JTarget(command[0])
                mJTarget.element("domain", command[0])
                return
            elif command[0] == "remove" :
                filename = JEnum.targets + command[1] + ".bin"
                mJTarget = JTarget.JTarget(filename, initType=1)
                mJTarget.remove()
                return
        self.printUsage()
        return
        