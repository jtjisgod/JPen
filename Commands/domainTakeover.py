import Command as Cmd
import JTarget
import JFIO
import JEnum
import JDto
import pickle
import os
from terminaltables import AsciiTable

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

        search = True
        if os.path.exists(JEnum.takeover + mJTarget.element('domain') + ".bin") :
            search = False
            if input("Already checked takeover available. Do you want to recheck? (y/N) : ").upper() == "Y" :
                search = True
        
        tablesKey = [["IDX", "DOMAIN"]]
        if search :
            res = mJDto.run()
            if res == False :
                print("Please run 'subdomain' firstly.")
                return
            idx = 0
            tables = []
            for k, v in res.items() :
                if v :
                    idx += 1
                    tables.append([idx, k])
            with open(JEnum.takeover + mJTarget.element('domain') + ".bin", "wb") as f :
                pickle.dump(tables, f)
            mJTarget.element("takeover", idx)
        else :
            with open(JEnum.takeover + mJTarget.element('domain') + ".bin", "rb") as f :
                tables = pickle.load(f)

        asciiTable = AsciiTable(tablesKey + tables, "Exploitable Subdomain List")
        print(asciiTable.table)
        