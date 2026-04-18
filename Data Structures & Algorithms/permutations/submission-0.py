class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: if the nums is empty, return an empty list
        if len(nums) == 0:
            return []

        # Base case: if the nums has only one element, return that element as the only permutation
        if len(nums) == 1:
            return [nums]

        # Recursive case: generate permutations
        permutations = []
        for i in range(len(nums)):
            # Extract the current element
            current_element = nums[i]
            # Remaining elements
            remaining_elements = nums[:i] + nums[i+1:]

            # Generate all permutations for the remaining elements
            for p in self.permute(remaining_elements):
                # Add the current element to the front of each permutation of the remaining elements
                permutations.append([current_element] + p)

        return permutations