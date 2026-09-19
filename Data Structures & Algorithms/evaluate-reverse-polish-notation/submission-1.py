class Solution:
    # ["1","2","+","3","*","4","-"]
    # ["3","3","*","4","-"]
    # ["9","4","-"]
    # ["5"]
    # ((1 + 2) * 3) - 4 = 5

    # ["1","2","+","3","*","4","-"]
    # 1 + 2 * 3 - 4 = 3

    # utilize stack keep number in the stack
    # when found operator, do operation on the two number inside the stack
    # put the result
    # continue iterate the input
    
    def evalRPN(self, tokens: List[str]) -> int:
        #          lp
        # ["1","2","+","3","*","4","-"]
        # stack = []
        # ops_num = [1, 2]
        # ops_result = 3

        #                  lp
        # ["1","2","+","3","*","4","-"]
        # stack = [9]
        # ops_num = [3, 3]
        # ops_result = 9

        #                           lp
        # ["1","2","+","3","*","4","-"]
        # stack = [5]
        # ops_num = [9, 4]
        # ops_result = 5

        # ["2","1","+","3","*"]
        # stack = [9]
        # ops_num = [3, 3]
        # ops_result = 9

        stack = []
        for t in tokens:
            num, is_num = self.convertStrToInt(t)
            if is_num:
                stack.append(num)
            else:
                # if not is_num then it's is_operator no need checking because there's contraints   
                right = stack.pop()
                left = stack.pop()

                ops_result = 0
                match t:
                    case "+":
                        ops_result = left + right
                    case "-":
                        ops_result = left - right
                    case "*":
                        ops_result = left * right
                    case "/":
                        ops_result = int(left / right)
                
                # put the ops result back to the stack as input for next ops if any, or if reach end of input will be the final result
                stack.append(ops_result)

        return stack[0]


                    

    def convertStrToInt(self, s: str) -> tuple[Optional[int], bool]:
        try:
            result = int(s)
            return result, True
        except ValueError:
            return None, False
        