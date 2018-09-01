# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:55:32 2018

@author: KELS
"""

#Import Regular Expression
import re

#Stack Implementation Class
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    #Function for program that can check an HTML document for proper opening and closing tags.
    def check_balance(self,text):

        # To tell the file 'text' where to split
        L = re.split('(<[^>]*>)', text)[1:2]

        # To iterate the file after the splitting
        for word in L:
            if ('/' not in word):
                s.push(word)
            elif not s.is_empty() and (word.replace('/', '') == s.peek()):
                s.pop()
            return s.is_empty()


s = Stack()
print(s.check_balance(text='''</html>
    <head>
        <title>
            Example
        </title>
    </head>

    <body>
        <h1>  Hello, world </h1>
    </body>
</html>'''))