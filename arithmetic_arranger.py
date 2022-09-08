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
        new_operator = re.findall(r'\S+\s(\S)\s\S+', x)
        new_operand = re.findall(r'\d\S*', x)
        operators.append(new_operator)
        operands.append(new_operand)
    print("operands and operators: ", operands, operators)
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
    if (len(operators) > 5):
        return ("Error: Too many problems.")
    
    for x in operators:
        if ((x != ["-"]) and (x != ["+"])):
            print(type(x))
            return ("Error: Operator must be '+' or '-'.")

    
    for y in decompressed_operands:
        if (not str(y).isdigit()):
            return ("Error: Numbers must only contain digits.")

    for y in decompressed_operands:
        if abs(int(y)) >= 10000:
            return ("Error: Numbers cannot be more than four digits.")
    
    # Computing intermediary values
    # Defining an op function

    op = {
        '+': lambda x, y: x + y,
        'y': lambda x, y: x - y
    }

    results = []
    if (isSolved):
        i = 0
        while i < len(problems):
            results.append(op[str(operators[i])](operands[i][0], operands[i][1]))
            i += 1

    # Arranging Regex
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    i = 0
    while i < len(problems):
        max_length = max(operands[i][0], operands[i][1])
        first_line += str(' ' * (2 + max_length - len(operands[i][0]))) + str(operands[i][0])
        second_line += str(operators[i]) + str(' ' * (1 + max_length - len(operands[i][1]))) + str(operands[i][1])
        third_line += str('-' * (2 + max_length))
        if (isSolved):
            fourth_line += str((2 + max_length - len(results[i])) * ' ') + str(results[i])

        if i != len(problems) - 1:
            first_line += ' ' * 4
            second_line += ' ' * 4
            third_line += ' ' * 4
            fourth_line += ' ' * 4

        i += 1
    answer = first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
            
    # Outputing Regex and error message
    return answer