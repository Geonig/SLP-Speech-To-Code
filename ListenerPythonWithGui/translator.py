import sys
import re
#sys.path.append('../output')
import formatter


class translator:
    '''Class would translate the meta java code into formal java code.'''
    def __init__(self,text):
        self.text = text
        
    def translate2java(self):
        output = []
        text =[token for token in self.text.split(" ") if not token  == '']
        #print (text)
        if (text[0] == 'print'):
           output.append(self.trans_print(text))
        #newly created variables
        elif (self.is_java_type(text[0])):
            output.append(self.trans_assig(text))
        #modify existing variables
        elif(text[0] == '='):
            output.append(self.trans_mod(text))
        #conditional structures
        elif(self.is_cond(text[0])):
            output.append(self.trans_cond(text))
            #classes and methods
        elif (self.visibility_type(text[0])):
            if (text[1] == 'class'):
                output.append(self.trans_class(text))
            elif(text[1] == 'method'):
                output.append(self.trans_method(text))
        #for loops
        elif(self.is_for_loop(text[0])):
            output.append(self.trans_forloop(text))

        else:
            return 'translator error'

        return output

    #checkers
    is_java_type = lambda self, token : re.search(r'int|boolean|string|double|float',token,re.I)
    is_cond = lambda self,token : re.search(r'while|if|else',token,re.I)
    is_for_loop  = lambda self, token: re.search(r'for',token,re.I)
    is_new_inst  = lambda self,text: any( re.search(r'new',item,re.I)for item in text)
    visibility_type = lambda self, token: re.search(r'public|private',token,re.I)

    def trans_print(self,text):
        '''' print <value>+'''
        text.pop(0) #remove print from the list
        value = text.pop(0) #get the first word of the print statment
        while(text):
            value += " %s" % (text.pop(0)) #join all the words
          
            return 'System.out.println(\"%s\");' % (value)
                              
    def trans_assig(self,text):
        '''Takes care of newly created strings and ints'''
        array = False  # used for created arrays
        if (text[0] == '[]'):
            array = True
            text.pop(0) # remove the "[]"symbol
        #<type> "=" <value> <name>
        var_type = text.pop(0)
        text.pop(0) #remove the '=' symbol
        if (var_type == 'String'):
            name = text.pop(0)
            value = text.pop(0)
        else:
            name = text.pop(0)
            value = text.pop(0)
            while(text):
                value += " %s" % (text.pop(0))
        if array:
            #<type>[]  name = new <type>[<value>] 
            return'{1}[] {2} = {1}[{3}];'.format(var_type,name,value)
        # <type> <name> = <value>
        return'{} {} = {};'.format(var_type,name,value)

    
    def trans_mod(self,text):
        '''rasigns new values to created variables'''
        # = <name> <value>
        text.pop(0) # remove "="
        value = text.pop() #remove the value before accesing the name
        name  =  text.pop(0)
        while(text):
            name += text.pop(0).title() #join the variable names
        
        return'{} = {};'.format(name,value)

    
    def trans_cond(self,text):
        #<if|else|while|> <symb> <name1> <name2>
        cond = text.pop(0)
        symb = text.pop(0)
        vall = text.pop(0)
        val2 = text.pop(0)
        return '%s(%s %s %s){}'% (cond,vall,symb,val2)

    def trans_forloop(self,text):
        #<for> <> <> <>
        pass


    def trans_class(self,text):
        #(public|private) class new <name>
        visibility = text.pop(0)
        name = text.pop(2)
        text.pop(0)
        text.pop(0)
        
        return '%s class %s{}' %(visibility,name)
    

    def trans_method(self,text):
        #<public|private> method  new <name>
        visibility = text.pop(0)
        text.pop(0) # "method" word
        text.pop(0) # "new" word
        name = text.pop(0) #name of the method        if" text == []"
        if (text):
            if (text[0] == 'with'):
                text.pop(0) # remove the "with"
                par_type = text.pop(0) # get the type of the class
                par_name = text.pop(0) # get the name of the class
                return '%s static void  %s(%s %s){}' % (visibility, name, par_type, par_name)
        return '%s static void  %s(){}'% (visibility,name)


def main():   
    x = translator('print hello this is a really long String of text')
    print(x.translate2java())
    y = translator('int = x blue ')
    print(y.translate2java())
    z = translator('if x < 30')
    print(z.translate2java())
    a = translator('public class new blue')
    print(a.translate2java())
    b = translator('private method new Thing')
    print(b.translate2java())
    e = translator('private method new more words in here')
    print(e.translate2java())
    c = translator('String = word Hello world!')
    print(c.translate2java())
    d = translator('= x 500')
    print(d.translate2java())
    f = translator('private method new Thing with int x')
    print(f.translate2java())

if __name__ == "__main__":
    main()
