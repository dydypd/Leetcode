class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for event_start, event_end in self.events:
            if start < event_end and end > event_start:
                return False
        self.events.append((start, end))
        return True
