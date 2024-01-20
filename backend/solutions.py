from typing import TypeAlias

Request: TypeAlias = (str, str, str)
Schedule: TypeAlias = list[(int, int, Request)]

def solve_day(requests: list[Request]) -> (dict[str, Schedule], list[Request]):
    bays: dict[str, Schedule]= {
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

    requests.sort(key=issued_time)

    
    for request in requests:
        (issued, requested, vehicle) = request
        (start, end) = request_start_end(request)
        
        for schedule in [bays[vehicle], bays["general 1"], bays["general 2"], bays["general 3"], bays["general 4"], bays["general 5"]]:
            conflicting: bool = False
            for time in schedule:
                if time[0] in range(start, end) or time[1] in range(start, end):
                    conflicting = true
                    break
            
            if not conflicting:
                bays[vehicle].append((start, end, request))
                break
        else:
            rejected.append(request);

    return (bays, rejected)



servicing_time = {
    "compact": 30,
    "medium": 30,
    "full-size": 30,
    "class 1 truck": 60,
    "class 2 truck": 120
}

def issued_time(request: Request) -> str:
    return request[0]

def request_start_end(request: Request) -> (int, int):
    (_, requested_datetime, vehicle) = request
    requested_time = requested_datetime.split()[1]
    [hours, minutes] = requested_time.split(":")
    start = int(hours) * 60 + int(minutes)
    end = start + servicing_time[vehicle]
    return (start, end)

def main() -> None:
    returned = solve_day([("15:00", "2023-01-01 12:40", "compact"), ("08:00", "2023-01-01 12:50", "class 2 truck")])
    print(returned)
    
main()
