# imports
from solutions import *
from dataclasses import dataclass
import pandas as pd
from pymongo import MongoClient

allow_rescheduling = False

def main() -> None:
    # reading entries from csv
    df = pd.read_csv("ScheduleInfo.csv")
    entries = []
    for index, row in df.iterrows():
        [issued, requested, vehicle] = row.iloc
        entries.append(Entry(issued, requested, vehicle))

    # sort by day by priorities:, 1) date requested, 2) datetime issued
    # sorting by issued first as it gets superceeded by the requested sort
    entries.sort(key=lambda entry: entry.issued)
    entries.sort(key=lambda entry: entry.date_requested())

    # chunk the entries by day
    days = []
    current_date = ""
    for entry in entries:
        if entry.date_requested() > current_date:
            current_date = entry.date_requested()
            days.append([entry])
        else:
            days[-1].append(entry)

    # call the simulation algoritm for each day, storing the result
    outputs_by_day = []
    for day in days:
        outputs_by_day.append(solve_day(day))


    total_revenue = 0
    total_revenue_loss = 0
    serviced_customers = {
        "compact": 0,
        "medium": 0,
        "full-size": 0,
        "class 1 truck": 0,
        "class 2 truck": 0,
    }
    potential_customers = {
        "compact": 0,
        "medium": 0,
        "full-size": 0,
        "class 1 truck": 0,
        "class 2 truck": 0,
    }

    # sum = 0

    for (walk_in_bays, booking_bays, turned_away) in outputs_by_day:
        for bay in walk_in_bays.values():
            print(len(bay))
            for (_, _, walk_in) in bay:
                total_revenue += servicing_charge[walk_in.vehicle]
                serviced_customers[walk_in.vehicle] += 1;
                     

        for bay in booking_bays:
            print(len(bay))
            for (_, _, booking) in bay:
                total_revenue += servicing_charge[booking.vehicle]
                serviced_customers[booking.vehicle] += 1;

        print(len(turned_away))
        for entry in turned_away:
            total_revenue_loss += servicing_charge[entry.vehicle]
            potential_customers[entry.vehicle] += 1;


    # print(sum)
    print(total_revenue)
    print(total_revenue_loss)
    print(serviced_customers)
    print(potential_customers)

    # # calculate serviced customers 
    # for (walk_in_bays, booking_bays, _) in outputs_by_day:
    #     for (_, _, vehicle) in walk_in_bays:

    CONNECTION_STRING = "mongodb+srv://max:5678@cluster0.uspsoud.mongodb.net/"
    def get_database():
       client = MongoClient(CONNECTION_STRING)
       return client['Schedule_Optimization']

    db = get_database()

    for (walk_in_bays, booking_bays, turned_away) in outputs_by_day:
        for bay in walk_in_bays.values():
            for (start, end, walk_in) in bay:
                db[walk_in.vehicle].insert_one({
                    "start_minute": start,
                    "end_minute": end,
                    "issued_datetime": walk_in.issued,
                    "requested_date": walk_in.date_requested(),
                    "vehicle_type": walk_in.vehicle
                })
                     

        for idx, bay in enumerate(booking_bays):
            for (start, end, booking) in bay:
                db[f"general {idx + 1}"].insert_one({
                    "start_minute": start,
                    "end_minute": end,
                    "issued_datetime": booking.issued,
                    "requested_date": booking.date_requested(),
                    "vehicle_type": booking.vehicle
                })

        for entry in turned_away:
            db["turned away"].insert_one({
                "issued_datetime": entry.issued,
                "requested_datetime": entry.requested,
                "vehicle_type": entry.vehicle
            })

           

# with MongoClient("mongodb+srv://max:5678@cluster0.uspsoud.mongodb.net/", connect=False) as client:
#     db = client.Schedule_Optimization
    # tools = db.ScheduleCollectionName
    # result = tools.insert_many(data)
    
    


def solve_day(entries: list[Entry]) -> (dict[str, Schedule], list[Schedule], list[Entry]):
    # set up the containers for the outputs
    walk_in_bays = {
        "compact": [],
        "medium": [],
        "full-size": [],
        "class 1 truck": [],
        "class 2 truck": [],
    }
    booking_bays = [[]] * 5
    turned_away: list[Entry] = []
    
    # split the entries into bookings and walk-ins
    bookings = []
    walk_ins = []
    for entry in entries:
        if entry.is_walk_in():
            walk_ins.append(entry)
        else:
            bookings.append(entry)

    # break up the problem into two parts
    solve_bookings(bookings, booking_bays, turned_away)
    simulate_walk_ins(walk_ins, walk_in_bays, turned_away)

    return (walk_in_bays, booking_bays, turned_away)


def solve_bookings(bookings: list[Entry], bays: list[Schedule], turned_away: list[Entry]) -> None:
    # validate bookings in advance, since we have the information in advance of the day
    validated_bookings = []
    for booking in bookings:
        if booking.is_valid():
            validated_bookings.append(booking)
        else:
            turned_away.append(booking)

    # secondary datetime-issued-centric ordering still preserved from main
    # as such the goal of this shop is that the first to book a time is the one who gets it
    for booking in validated_bookings:
        (start, end) = booking.range_requested()
        this_range = range(start, end)
        # find an available bay, or none if there isn't any
        available_bay = next((bay for bay in bays if all(other_start not in this_range and other_end not in this_range for (other_start, other_end, _) in bay)), None)

        if available_bay == None:
            if allow_rescheduling:
                # this is where you would reschedule if that was a design decision you madeo
                print("unimplemented by choice")
            else:
                turned_away.append(booking)
                continue

        available_bay.append((start, end, booking))

        

def simulate_walk_ins(walk_ins: list[Entry], bays: dict[str, Schedule], turned_away: list[Entry]) -> None:
    for walk_in in walk_ins:
        # validate walk-ins here because it wouldn't be done ahead of time in real life
        if not walk_in.is_valid():
            turned_away.append(walk_in)
            continue

        # put in the appropriate bay if available. otherwise reject
        (start, end) = walk_in.range_requested()
        bay = bays[walk_in.vehicle]
        if not bay or bay[-1][1] <= start:
            bay.append((start, end, walk_in))
        else:
            turned_away.append(walk_in)        


@dataclass
class Entry:
    issued: str
    requested: str
    vehicle: str

    def overlaps_with_bay(self, bay: Schedule) -> bool:
        # for (start, end)
        (this_start, this_end) = self.range_requested()
        this_range = range(this_start, this_end)
        (other_start, other_end) = other.range_requested()
        
                

    def is_valid(self) -> bool:
        (start, end) = self.range_requested()

        appropriately_issued = "2022-09-01" <= self.date_issued() <= self.date_requested()
        within_active_months = "2022-10-01" <= self.date_requested() <= "2022-11-30"
        within_active_hours = 7 * 60 <= start and end <= 19 * 60
        valid_vehicle = self.vehicle in ["compact", "medium", "full-size", "class 1 truck", "class 2 truck"]

        return appropriately_issued and within_active_months and within_active_hours and valid_vehicle

    def range_requested(self) -> (int, int):
        [hours, minutes] = self.time_requested().split(":")
        start = int(hours) * 60 + int(minutes)
        end = start + servicing_time[self.vehicle]
        return (start, end)

    def is_walk_in(self) -> bool:
        return self.date_issued() == self.date_requested()
        
    def date_requested(self) -> str:
        return self.requested.split()[0]

    def time_requested(self) -> str:
        return self.requested.split()[1]

    def date_issued(self) -> str:
        return self.issued.split()[0]

    def time_issued(self) -> str:
        return self.issued.split()[1]


if __name__ == "__main__":
    main()
