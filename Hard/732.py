class MyCalendarThree:
    def __init__(self):
        self.timeline = {}

    def book(self, start: int, end: int) -> int:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1

        max_k = 0
        ongoing = 0
        for timestamp in sorted(self.timeline.keys()):
            ongoing += self.timeline[timestamp]
            max_k = max(max_k, ongoing)

        return max_k



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)