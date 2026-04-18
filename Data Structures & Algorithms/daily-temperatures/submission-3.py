class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        monotonic_stack=[]

        for index,element in enumerate(temperatures):
            while monotonic_stack and monotonic_stack[-1][1] < element:
                previous_element = monotonic_stack.pop()
                res[previous_element[0]]= index - previous_element[0]
            monotonic_stack.append([index,element])
        return res