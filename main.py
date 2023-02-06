#!/usr/bin/env python3

class Solution:

    def isValid(self, input_string: str) -> bool:
        stack = []
        # dict to map open to close
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }

        for char in input_string:
            if char in close_to_open:
                # if the stack is not empty, and the last value[-1] against our dict
                if stack and stack[-1] == close_to_open[char]:
                    print(stack[-1])
                    print(close_to_open[char])
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False

def main():

    input_string = "()[]{}"
    solve = Solution()
    print(solve.isValid(input_string))

if __name__ == "__main__":
    main()