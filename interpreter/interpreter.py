import warnings
warnings.filterwarnings("ignore")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

import sys
import re
import nltk
from nltk.corpus import stopwords


##-GlobalExpressions-------------------------------------

commandRe = re.compile('[mM]ake|[Cc]reate|[Gg]ive')
actionRe = re.compile('')
stateRe = re.compile('(if)|(while)|(else)|(else \s+ if)|(for)|(class)|(method)')
dataRe = re.compile('(?P<int>int(eger))|(?P<array>array)|(?P<String>string)|(?P<object>object)')
symbolsRe = re.compile('((greater|less)\s*than)|(equal|set)|(not)|(add)|(subtract)|(minus)|(plus)|(times)|(divided)')
symbolsList = [ 'greater than', '> ', 'less than', '<' , 'equal', '=' , 'set', '=' , 'not', '!', 'add', '+', 'subtract', '-' , 'minus' , '-', 'plus', '+', 'times', '*', 'divided', '/']
stopWords = re.compile( 'a|it|its|too|to|greater|less|named|called|private|public'  )

#def reCommands(vinput):
    

#def reActios(vinput):
    

def reStatements(vinput):

    token = ' '.join(vinput)
    
    m = stateRe.search(token)

    output = ''

    if m is not None:
        output = m.group()

    if 'private' in token:
        if re.match('(class)|(method)', output):
            output = 'private ' + output
            return output

    if re.match('(class)|(method)', output):
        output = 'public ' + output
    
    return output
    


def reSymbols(vinput):

    token = ' '.join(vinput)
    
    m = symbolsRe.search(token)

    output = ''

    if m is not None: 
        if m.group() in symbolsList:
            output = symbolsList[symbolsList.index(m.group())+1]

    #print(output)
    return output

    
def reDatatypes(vinput):

    m = re.match(' '," ")

    output = ' '

    token = ' '.join(vinput)

    if dataRe.search(token):
        m = dataRe.search(token)
        output = m.lastgroup
    

    if re.match('array', output):
        output = "[]"

    #print(output)
    return output



def reNumbers(vinput):


    output = []

    for strings in vinput:
        if re.match('\d+', strings):
            output.append(strings)

    #print(output)

    return output



def reNames(vinput):

    nameslist = []

    numbers = re.compile('\d+')

    reglist = [stateRe,commandRe,dataRe,symbolsRe,stopWords, numbers]

    for strings in vinput:
        if all(re.match(options, strings) is None for options in reglist):
            if not strings in nameslist:
                nameslist.append(strings)

    en_stops = set(stopwords.words('english'))

    
    for word in nameslist:
        if word in en_stops:
            nameslist.remove(word)
            
                    
    #print (nameslist)
    return nameslist
    
    

##-Main----------------------------------------------------

voiceinput =  []

for args in sys.argv[1:]:
    voiceinput.append(args)

#print(voiceinput) 
    
#commands = reCommands(voiceinput)
#actions = reActions() 
statements = reStatements(voiceinput)
datatypes = reDatatypes(voiceinput)
symbols = reSymbols(voiceinput)
names = reNames(voiceinput)
values = reNumbers(voiceinput)

interpretedString = statements + datatypes + symbols + ' '.join(names) + ' '.join(values)

print(interpretedString)
