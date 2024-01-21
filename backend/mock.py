# imports
from solutions import *
import pandas as pd

def main() -> None:
    # reading entries from csv
    df = pd.read_csv("ScheduleInfo.csv")
    entries = []
    for index, row in df.iterrows():
        [issued, requested, vehicle] = row.iloc
        entries.append((issued, requested, vehicle))

    # sort by day the entry requests
    entries.sort(key=lambda entry: entry[1])

    # chunk the requests by day
    days = []
    current_date = ""
    for entry in entries:
        if requested_date(entry) > current_date:
            current_date = requested_date(entry)
            days.append([entry])
        else:
            days[-1].append(entry)

    for day in days:
        solve_day(day)


def solve_day(entries: list[Entry]) -> (dict[str, Schedule], list[Entry]) -> None:
    # set up the containers for the outputs
    walk_in_bays = {
        "compact": [],
        "medium": [],
        "full-size": [],
        "class 1 truck": [],
        "class 2 truck": [],
    }
    booking_bays = [[]] * 5
    rejected: list[Entry] = []
    
    # split the entries into bookings and walk-ins
    bookings = []
    walk_ins = []
    for entry in day:
        if issued_date(entry) == requested_date(entry):
            walk_ins.append(entry)
        else:
            bookings.append(entry)

    solve_bookings(bookings, booking_bays, rejected)
    simulate_walk_ins(walk_ins, walk_in_bays, rejected)



    return (bays, rejected)


def solve_bookings(bookings: list[Entry], bays: dict[str, Schedule], rejected: list[Entry]) -> None:
    # validate bookings
    validated_bookings = []
    for booking in bookings:
        if valid(booking):
            validated_bookings.append(booking)
        else:
            rejected.append(booking)
    bookings = validated_bookings

    

def simulate_walk_ins(walk_ins: list[Entry], bays: dict[str, Schedule], rejected: list[Entry]) -> None:
    for walk_in in walk_ins:
        (start, end) = 
        




def valid(request: Entry) -> bool:
    (issued, requested, vehicle) = request
    [issued_date, _] = issued.split()
    [requested_date, requested_time] = requested.split()
    (start, end) = request_start_end(requested_time, vehicle)

    appropriately_issued = "2022-09-01" <= issued_date <= requested_date
    within_active_months = "2022-10-01" <= requested_date <= "2022-11-30"
    within_active_hours = 7 * 60 <= start and end <= 19 * 60
    valid_vehicle = vehicle in ["compact", "medium", "full-size", "class 1 truck", "class 2 truck"]

    return appropriately_issued and within_active_months and within_active_hours and valid_vehicle

def requested_range(entry: Entry) -> (int, int):
    [hours, minutes] = time_requested(entry).split(":")
    start = int(hours) * 60 + int(minutes)
    end = start + servicing_time[entry[2]]
    return (start, end)

def date_requested(request: Entry) -> str:
    return request[1].split()[0]

def time_requested(request: Entry) -> str:
    return request[1].split()[0]

def date_issued(request: Entry) -> str:
    return request[0].split()[0]

def time_issued(request: Entry) -> str:
    return request[0].split()[0]

def date(datetime: str) -> str:
    return datetime.split()[0]

def time(datetime: str) -> str:
    return datetime.split()[1]


if __name__ == "__main__":
    main()
