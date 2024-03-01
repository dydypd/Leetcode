class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_satisfaction = 0
        current_satisfaction = 0

        for s in satisfaction:
            current_satisfaction += s
            max_satisfaction += current_satisfaction if current_satisfaction > 0 else 0

        return max_satisfaction