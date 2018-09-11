import Command as Cmd
import JSubdomainFinder
from terminaltables import AsciiTable
import os

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "subdomain"

        # Title of this command
        self.title       = "Subdomain Finder"

        # Description of this command
        self.description = "Finding sub domains of input domain with DNS"

        self.usage = "subdomain *.bughunting.net"

    def run(self, command=[]) :

        if len(command) == 0 :
            self.printUsage()
            return
        
        dictionary = "./assets/subdomains/"
        
        dicts = []
        cnt = 1
        for file in os.scandir("./assets/subdomains/") :
            if file.name[-4::] == ".txt" :
                dicts.append([cnt, file.name])
                cnt += 1

        table = [["#", "Subdomain Seed File Name"]]
        table.extend(dicts)
        asciiTable = AsciiTable(table)

        while True :
            asciiTable.title = "<< Select a txt file >>"
            print(asciiTable.table)
            try :
                idx = int(input(">>> ")) - 1
                dictionary += dicts[idx][1]
                break
            except :
                continue

        mJSubdomainFinder = JSubdomainFinder.JSubdomainFinder(command[0], dictionary=dictionary)
        res = mJSubdomainFinder.run()

        cnt = 1
        table = [["#", "DOMAIN"]]
        for k, v in res.items() :
            if v :
                table.append([cnt, k])
                cnt += 1

        asciiTable = AsciiTable(table)
        asciiTable.title = "Subdomain List"
        print("\n\n")
        print(asciiTable.table)
        
        # for k, v in res.items() :
        #     if v :
        #         print("\t[ %s ] %s"%(v, k))
        