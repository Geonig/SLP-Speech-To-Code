import re #used for searching tags
from pyautogui import typewrite, press #used to write on any program
import tagger as t


def format_statements(statements):    
    '''compresses the list of statments by putting parameters in the corresponding places'''
    b_s = [stmt for stmt in statements if '(' in list(stmt)]
    # get all the staments that require parameters
    var_nums = [len(stmt.split(',')) for stmt in b_s]
    # check for number of parameters
    for stmt, args in zip(b_s, var_nums):
        pos = statements.index(stmt)
        statements[pos] = format_params(statements[pos:(pos + args + 1)])
        # get all the corresponding args and put it union  on the old place.
        statements = statements[:pos+1]+statements[pos+1+args:]
        #return the statements without the arguemnts
    return statements
    # return the formated staments plus the rest


    
def format_params(statements):
    '''arrange original statements and store all the variables in their corresponding places'''
    base = t.fix_params(statements[0])
    param_num = len(statements[0].split(',')) #how many statements are parameters
    pos = re.compile(r'#P[\d]+#')
    for arg in statements[1: param_num+1]:
        base = re.sub(pos, arg, base, count = 1)
    base = format_spaces(t.comma_separator(base))       
    return base
    
    
        
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
