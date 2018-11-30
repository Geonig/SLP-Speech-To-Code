import sys
import re
#sys.path.append('../output')
import formatter


class translator:
    '''Class would translate the meta java code into formal java code.'''
    def __init__(self,text):
        self.text = text

#        formatter.__init__(result)  #send it to the next stage.
        
    def translate2java(self):
        counter = 100 #not solution found verification
        output = []
        text =[token for token in self.text.split(" ") if not token  == '']
        while(not text == []):
            #print statements
            #print (text)
            if (text[0] == 'print'):
                output.append('System.out.println();')
                text.pop(0) #move to next item
                output.append('\"{}\"'.format(text[0])) #string to be printed
                text.pop(0)
            #newly created variables
            elif (self.is_java_type(text[0])):
                output.append(self.trans_assig(text))
            #conditional structures
            elif(self.is_conditional(text[0])):
                output.append(self.trans_conditional(text))
                #classes and methods
            elif (self.visibility_type(text[0])):
                if (text[1] == 'class'):
                    output.append(self.trans_class(text))
                elif(text[1 == 'method']):
                    output.append(self.trans_method(text))
            #for loops
            elif(self.is_for_loop(text[0])):
                output.append(self.trans_forloop(text))

            counter -= 1
            if counter == 0:
                return 'translator error'

        return output

    #checkers
    is_java_type = lambda self, token :re.search(r'int|integer|boolean|string|double|float',token,re.I)
    is_conditional = lambda self,token:re.search(r'while|if|else',token,re.I)
    is_for_loop  = lambda self, token: re.search(r'for',token,re.I)
    is_new_inst = lambda self,text: any( re.search(r'new',item,re.I)for item in text)

    #helpers
    visibility_type = lambda self, token: re.search(r'public|private',token,re.I)
        
    def trans_assig(self,text):
        #<type> <name> <new> <value>
        var_type = text.pop(0)
        name = text.pop(0)
        if self.is_new_inst(text):
            value = text.pop(1)
            value = text.remove('new')
            return'{} {} = {};'.format(var_type,name,value)
        value = text.pop(0)
        return '{} = {};'.format(name,value)
    
    def trans_conditional(self,text):
        #<if|else|while|> <name> <symb> <name>
        conditional = text.pop(0)
        return '%s (){}, '% (conditional)

    def trans_forloop(self,text):
        #<for> <> <> <>
        pass


    def trans_class(self,text):
        #(public|private) class new <name>
        visibility = text.pop(0)
        name = text.pop(2)
        text.pop(0)
        text.pop(0)
        return '%s class %s{} ' %(visibility,name)
    

    def trans_method(self,text):
        #<public|private> method  new <name>
        visibility = text.pop(0)
        name = text.pop(2)
        text.pop(0)
        text.pop(0)
        return '%s static void  %s(){} '% (visibility,name)
"""
x = translator('print hello')
x = translator('int x new 3 ')
x = translator('int x 3')
x = translator('public class new blue')
x = translator('private method new Thing')
"""

