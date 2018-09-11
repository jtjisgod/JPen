#!/bin/sh

# Python Utils
import JThread      # Simple Thread Module
import JCommand     # For TUI Mode
import JGui         # For Web Mode

# Service Analysis
import JDns         # DNS Digging tool

# Setting
from JEnum import JEnum

def main() :
    mJCommand = JCommand.JCommand()
    while mJCommand.control(input("JPen >> ")) :
        pass

if __name__ == "__main__" :
    main()