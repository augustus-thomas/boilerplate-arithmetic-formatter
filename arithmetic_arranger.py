from ast import boolop
from curses.ascii import isdigit
import re
import sys
from xmlrpc.client import boolean




def arithmetic_arranger(problems, isSolved):
    # Initializing variables
    n = len(problems)
    answer=""
    fail_message=""
    operations = {}
    
    # Trimming input data


    ## Transfering problems string to a workable operations dictionary
    ## Note: this step could be combined with trimming for computational efficieny, but
    ## is done seperately for readability.



    # Checking and passing  provisioned errors
    if n > 5:
        raise Exception("Error: Too many problems.")
    
    for x in range(operators):
        if x is not "-" and x is not "+":
            raise Exception("Error: Operator must be '+' or '-'.")
            break
    
    for y in range(operands):
        if not isdigit(y):
            raise Exception("Error: Numbers must only contain digits.")
            break
        
    for y in range(operands):
        if abs(int(y)) >= 10000:
            raise Exception("Error: Numbers cannot be more than four digits.")
            break

    
    
    # Computing intermediary values


    # Arranging Regex


    # Outputing Regex and error message
    return answer, fail_message