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
        elif next in ')]}':
            if len(stack)==0:
                return i+1
            opening_brackets_stack.pop():
            if (next==')'and opening_brackets != '(') or \
               (next==']'and opening_brackets != '[') or \
               (next=='}'and opening_brackets != '{'):
                        return i + 1, opening_bracket_position[opening_bracket]
    if len(stack)==0:
        return "Success"
    else:
    return opening_bracket_position[stack.pop()]
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
