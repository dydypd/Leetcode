class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        current = 0

        for num in target:
            if num > current:
                operations += num - current
                current = num
            else:
                current = num

        return operations