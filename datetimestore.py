from datetime import datetime


class Event:
    event_count = 0
    def __init__(self, time_stamp):
        self.__class__.event_count += 1
        self.time_stamp = time_stamp
        self.id = self.event_count

class DatetimeEventStore:
    def __init__(self):
        self.events = []

    def store_event(self, time_stamp):
        event = Event(time_stamp)
        self.events.append(event)

    def get_events(self, start, end):
        returned_events = []
        for event in self.events:
            if event.time_stamp > start and event.time_stamp < end:
                returned_events.append(event)
        return returned_events