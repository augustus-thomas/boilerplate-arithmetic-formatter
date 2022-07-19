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
    operators = []
    operands = []
    for x in problems: 
        new_operator = re.findall('\s(\S+)\s', x)
        new_operand = re.findall('(*)\s\S\s(*)', x)
        operators.append(new_operator)
        operands.append(new_operand)

    ## Note: Operands becomes a list of lists (tuple?) we need to handle this
    decompressed_operands = []
    i = 0
    while i < len(operands):
        j = 0
        while j < len(operands[i]):
            decompressed_operands.append(operands[i][j])



    ## Transfering problems string to a workable operations dictionary
    ## Note: this step could be combined with trimming for computational efficieny, but
    ## is done seperately for readability.



    # Checking and passing  provisioned errors
    if n > 5:
        raise Exception("Error: Too many problems.")
    
    for x in range(operators):
        if (x != "-") and (x != "+"):
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