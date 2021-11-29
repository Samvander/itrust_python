from datetimestore import DatetimeEventStore
import datetime
import random

start_ts = datetime.datetime(2000, 1, 1).timestamp()
end_ts = datetime.datetime(2022, 1, 1).timestamp()


store = DatetimeEventStore()

for i in range(10000):
    dt = datetime.datetime.fromtimestamp(
    random.randint(start_ts, end_ts))
    store.store_event(time_stamp=dt)
    for event in store.get_events(
        start=datetime.datetime(year=2018, month=1, day=1),
        end=datetime.datetime(year=2018, month=2, day=1)):
            print(event)

