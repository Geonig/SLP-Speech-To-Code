import re #used for searching tags
from pyautogui import typewrite, press #used to write on any program
import tagger as t

def format_stmt(stmt):
    result = t.tag(stmt)
    
    return result
def format_brakets(stmt):
    pass
    
    
def main():
    pass

if __name__ == '__main__':
    main()
