#!/bin/sh

# Python Utils
import JThread      # Simple Thread Module
import JTest        # Time Test Module
import JDomain      # Domain Object
import JFIO         # File I/O Helper
import JCommand     # For TUI Mode
import JGui         # For Web Mode

# Service Analysis
import JDns         # DNS Digging tool

# Setting
from JEnum import JEnum

def main() :
    interactiveMode()
    domains = JFIO.readFile2Line(JEnum.domainFile)
    mJDomain = JDomain.JDomain(domains)
    mJCommand = JCommand.JCommand()
    while mJCommand.control(input("JPen >> ")) :
        pass
    

def interactiveMode() :
    domain = input("domain file? [default=domains.txt] >> ")
    JEnum.domainFile = domain if domain else JEnum.domainFile

if __name__ == "__main__" :
    main()