# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in '([{':
            # Process opening bracket, write your code here)
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

       
            # Process closing bracket, write your code here
        if next in ')]}':
            opening_brackets_stack.pop():
            if (next==')'and opening_brackets != '(') or \
               (next==']'and opening_brackets != '[') or \
               (next=='}'and opening_brackets != '{'):
                        return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"
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
    print("Success")

if __name__ == "__main__":
    main()
