from enum import Enum, unique

@unique
class tags(Enum):
    '''list of the tags used to communicate to the formatter'''
    ENT = '#ENT#'
    SPC = '#SPC#'
    TAB = '#TAB#'
    MVU = '#MVU#'
    MVD = '#MVD#'
    MVF = '#MVF#'
    MVB = '#MVB#'
    MVE = '#MVE#'
    MVS = '#MVS#'
    P = '#P_#'
    JU = '#JU#'
    JD = '#JD#'
    EXT = '#EXT'

def fix_brakets(stmt):
   '''adds an new line tag for all the parts that have brackets '''
   front, back  = stmt.split('{')
   return '%s{%s%s' % (front,tags.ENT.value,back)

def fix_param(stmt):
   '''add the postional tag for conditional structures and methods with only one stament'''
   front,back = stmt.split("(") # [ 'if', '){}']
   value = tags.P.value         # '#P_#'
   value = list(value)          # [#,P,_,#]
   value = value[:2]+[str(0)]+value[3:]
   value = ''.join(value)
   return '%s(%s%s'% (front,value,back)

def fix_params(stmt):
    '''add the positional tag from multiple argument method and conditional
    structures'''
    front, back = stmt.split('(') #public static my method(,,,){}
    #get the number of params
    arg_num = back.split(',')     # we care about last and first values
    if len(arg_num) == 1 :
        return fix_param(stmt)
    else:
        values = ''
        for  i in range(len(arg_num)):
             value = tags.P.value
             values += value.replace('_', str(i)) + ","
        values = values[:-1]
        return '%s(%s%s'% (front,values,arg_num[-1])

def comma_separator(stmt):
    return stmt.replace(',',','+ tags.SPC.value)

def tag(stmt):
    '''automatic tag the given statement'''
    stmt = fix_brakets(stmt)
    stmt = fix_params(stmt)
    stmt = comma_separator(stmt)
    return stmt


def main():
    pass
if __name__ == '__main__':
    main()
