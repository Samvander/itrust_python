from datetime import datetime


class Event:
    event_count = 0
    def __init__(self, timestamp=None):
        self.__class__.event_count += 1
        if timestamp is None:
            self.timestamp = datetime.now().timestamp()
        self.id = self.event_count

class DatetimeEventStore:
    def __init__(self):
        self.events = []

    def store_event(self):
        event = Event()
        self.events.append(event)
        # print(event.timestamp)
        # print(event.id)

    def get_events(self, start, end):
        returned_events = []
        for event in self.events:
            if event.timestamp > start and event.timestamp < end:
                returned_events.append(event)
        print(returned_events)
        return returned_events