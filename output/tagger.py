from enum import Enum, unique
@unique
class tags(Enum):
    '''list of the tags used to communicate to the formatter'''
    ENT = '#ENT#'
    SPC = '#SPC#'
    MVU = '#MVU#'
    MVD = '#MVD#'
    MVF = '#MVF#'
    MVB = '#MVB#'
    MVE = '#MVE#'
    MVS = '#MVS#'
    P = '#P#'
    JU = '#JU#'
    JD = '#JD#'
    EXT = '#EXT'

def fix_brakets(stmt):
   '''adds an new line tag for all the parts that have brackets '''
   front, back  = stmt.split('{')
   return '%s{%s%s' % (front,tags.ENT.value,back)

def fix_param(stmt):
   'add the postional tag for if, else, single param methods ,do ,while loops'
   front,back = stmt.split("(")
   value = tags.P.value
   value = list(value)
   value = value[:2]+[str(1)]+value[2:]
   value = ''.join(value)
   return '%s(%s%s'% (front,value,back)

def fix_params(stmt):
    '''add the positional tag from multiple argument method and conditional
    structures'''
    front, back = stmt.split('(')
    #get the number of params
    values =back.split(',')
    if len(values) == 1 :
        return fix_param(stmt)
    else:
        for val, i in enumerate(values):
             val = tags.P.value
             val = list(val)
             val = val[:2]+[str(i)]+val[2:]
             val = ''.join(val)
        values = ''.join(values)
        return '%s(%s%s'% (front,values,back)
    
def tag(stmt):
    '''automatic tag the given statement'''
    stmt = fix_brakets(stmt)
    stmt = fix_param(stmt)
    return stmt


def main():
    pass
if __name__ == '__main__':
    main()
