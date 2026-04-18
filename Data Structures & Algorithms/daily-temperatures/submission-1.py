class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[]
        for i in range(len(temperatures)):
            j=i+1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    output.append(j-i)
                    break
                j+=1
            if j >= len(temperatures):
                output.append(0)    
        return output


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0 for i in range(len(temperatures))]
        stack = [[0,temperatures[0]]]

        for index in range(1,len(temperatures)):
            print(stack)
            print(res)
            while stack and stack[-1][1] < temperatures[index]:
                res[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index,temperatures[index]])
        
        print(stack,res)
        return res