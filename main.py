# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def find_mismatch(text):
    #opening_brackets_stack = []
    #opening_brackets_position = {}
    for i, next in enumerate(text):
        if next in '([{':
            # Process opening bracket, write your code here)
            opening_brackets_stack.append(Bracket(next, i+1)) #pievieno vienu vērtību
            #opening_brackets_stack.append(next)
            opening_brackets_position[next]=i+1
            pass

       
            # Process closing bracket, write your code here
        #elif next in ')]}':
            #if len(openiing_brackets_stack)==0:
                #return i+1
            #opening_brackets=opening_brackets_stack.pop()
            #if (next==')'and opening_brackets != '(') or \
               #(next==']'and opening_brackets != '[') or \
               #(next=='}'and opening_brackets != '{'):
                        #return i + 1, opening_brackets_position[opening_brackets]
    #if len(opening_brackets_stack)==0:
        #return opening_brackets_stack[0].position
        #return "Success"
    #else:
        #return opening_brackets_position[opening_brackets_stack.pop()]
            if not opening_brackets_stack or not are_mismatching(opening_brackets_stack.pop().char,next):
            #if opening_brackets_stack==0 or are_matching==0(opening_brackets_stack.pop().char,next):
                return i+1
            if opening_brackets_stack:
                return opening_brackets_stack[0].position
            return "Success"
            pass


def main():
    text = input()
    if text[0]=="I":
        text=input()
        mismatch = find_mismatch(text)
    # Printing answer, write your code here
#if (opening_brackets_stack:
   #print(opening_brackets_stack[-1].position)
#else:
    print(mismatch)

if __name__ == "__main__":
    main()
