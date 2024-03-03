class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for db_start, db_end in self.double_bookings:
            if start < db_end and end > db_start:
                return False

        for event_start, event_end in self.events:
            if start < event_end and end > event_start:
                double_start = max(start, event_start)
                double_end = min(end, event_end)
                self.double_bookings.append((double_start, double_end))

        self.events.append((start, end))
        return True
