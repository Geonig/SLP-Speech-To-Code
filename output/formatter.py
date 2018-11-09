import re #used for searching tags
from pyautogui import typewrite, press #used to write on any program
import tagger as t


def format_statements(statements):    
    '''arrange original statements and store all the variables in their corresponding places'''
    base = t.fix_params(statements[0])
    param_num = len(statements[0].split(',')) #how many statements are parameters
    pos = re.compile(r'#P[\d]+#')
    for arg in statements[1: param_num+1]:
       base = re.sub(pos, arg, base, count = 1)
    base = format_spaces(t.comma_separator(base))       
    return base[:param_num+1]

def format_params(statements):    
    '''arrange original statements and store all the variables in their corresponding places'''
    base = t.fix_params(statements[0])
    param_num = len(statements[0].split(',')) #how many statements are parameters
    pos = re.compile(r'#P[\d]+#')
    for arg in statements[1: param_num+1]:
       base = re.sub(pos, arg, base, count = 1)
    base = format_spaces(t.comma_separator(base))       
    return [base, statements[param_num+2:] ]

        
def format_brackets(stmt):
    '''expects a stament which has the tag already added to it.'''
    return re.sub(r'#ENT#', '\n', t.fix_brakets(stmt), count = 1)

def format_spaces(stmt):
    '''set up spaces given by the tags'''
    return stmt.replace(t.tags.SPC.value, ' ')



def main():
    pass

if __name__ == '__main__':
    main()
