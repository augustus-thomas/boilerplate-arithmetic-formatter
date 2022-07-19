from ast import boolop
from curses.ascii import isdigit
import re
import sys
from xmlrpc.client import boolean

def arithmetic_arranger(problems, *isSolved):
    # Initializing variables
    n = len(problems)
    answer=""
    fail_message=""
    operations = {}
    
    operators = []
    operands = []
    for x in problems: 
        new_operator = re.findall(r'\d+\s(\W)\s\d+', x)
        new_operand = re.findall(r'\d+', x)
        operators.append(new_operator)
        operands.append(new_operand)
    print("operands and operators", operands, operators)
    # Extracting operands lists into one list
    decompressed_operands = []
    i = 0
    while i < len(operands):
        j = 0
        while j < len(operands[i]):
            decompressed_operands.append(operands[i][j])
            j += 1
        i += 1
    # print(decompressed_operands)

    ## Transfering problems string to a workable operations dictionary
    ## Note: this step could be combined with trimming for computational efficieny, but
    ## is done seperately for readability.


    # Checking and passing  provisioned errors
    if (n > 5):
        return ("Error: Too many problems.")
    
    for x in operators:
        if ((x != "-") and (x != "+")):
            return ("Error: Operator must be '+' or '-'.")

    
    for y in decompressed_operands:
        if (not isdigit(y)):
            return ("Error: Numbers must only contain digits.")

    for y in decompressed_operands:
        if abs(int(y)) >= 10000:
            return ("Error: Numbers cannot be more than four digits.")


    
    
    # Computing intermediary values


    # Arranging Regex


    # Outputing Regex and error message
    return answer