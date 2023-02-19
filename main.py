# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
            # Process opening bracket, write your code here
def _init_(self,char,position):
    self.char=char
    self.position=position
            if next == '(' or next == '[' or next '{':
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

       
            # Process closing bracket, write your code here
            def if_statement (next, opening_brackets_stack):
                if (next == ')' or next == ']' or next '}'):
                    if (opening_brackets_stack.empty() or
                          opening_brackets_stack.top().Matchc(next)):
                        return i + 1
                    opening_brackets_stack.pop():
                return opening_brackets_stack[0].position
            return 'Success'
            pass


def main():
    text = input()
    if text[0]=="i";
        text=input()
        mismatch = find_mismatch(text)
    # Printing answer, write your code here
if (opening_brackets_stack:
   print(opening_brackets_stack[-1].position)
else:
    print('Success')

if __name__ == "__main__":
    main()
