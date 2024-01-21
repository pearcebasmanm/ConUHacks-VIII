# imports
from solutions import *
import pandas as pd

def main() -> None:
    # reading requests from csv
    df = pd.read_csv("ScheduleInfo.csv")
    requests = []
    for index, row in df.iterrows():
        [issued, requested, vehicle] = row.iloc
        requests.append((issued, requested, vehicle))

    # sort by day the request was issued
    requests.sort(key=lambda request: request[1])

    # chunk the requests by day
    days = []
    current_day = ""
    for request in requests:
        request_day = request[1].split()[0]
    
        if request_day > current_day:
            current_day = request_day
            days.append([request])
        else:
            days[-1].append(request)

    # find the optimal outcome for each day
    for day in days:
        result = solve_day(day)
        # print(result)


def solve_day(requests: list[Request]) -> (dict[str, Schedule], list[Request]):
    bays = {
        "compact": [],
        "medium": [],
        "full-size": [],
        "class 1 truck": [],
        "class 2 truck": [],
        "general 1": [],
        "general 2": [],
        "general 3": [],
        "general 4": [],
        "general 5": []
    }
    
    rejected: list[Request] = []

    validated_requests = []

    for request in requests:
        if valid(request):
            validated_requests.append(request)
        else:
            rejected.append(request)

    reserved_time_chronological(validated_requests, bays, rejected)
    # issued_time_chronological(validated_requests, bays, rejected)
    # optimized(validated_requests, bays, rejected)

    return (bays, rejected)


def valid(request: Request) -> bool:
    (issued, requested, vehicle) = request
    [issued_date, _] = issued.split()
    [requested_date, requested_time] = requested.split()
    (start, end) = request_start_end(requested_time, vehicle)

    appropriately_issued = "2022-09-01" <= issued_date <= requested_date
    within_active_months = "2022-10-01" <= requested_date <= "2022-11-30"
    within_active_hours = 7 * 60 <= start and end <= 19 * 60
    valid_vehicle = vehicle in ["compact", "medium", "full-size", "class 1 truck", "class 2 truck"]

    return appropriately_issued and within_active_months and within_active_hours and valid_vehicle


if __name__ == "__main__":
    main()
