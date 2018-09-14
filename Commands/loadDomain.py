import Command as Cmd
from terminaltables import AsciiTable

import JFIO

import JEnum

import JTarget

import os

class Command(Cmd.Command) :

    def __init__(self) :

        super().__init__()

        # Instruction of this command
        self.command     = "loadDomain"

        # Title of this command
        self.title       = "Loading domain from text file"

        # Description of this command
        self.description = "Load and make targets from domain text file"

        # Usage of this command
        self.usage = "loadDomain domains.txt"

    def run(self, command=[]) :
        if len(command) != 1 :        
            self.printUsage()
        if not os.path.exists(command[1]) :
            print("Error.. No such file or directory")
            return
        for domain in JFIO.readFile2Line(command[1]) :
            print(domain)
        return
        