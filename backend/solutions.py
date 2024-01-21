from typing import TypeAlias

Request: TypeAlias = (str, str, str)
Schedule: TypeAlias = list[(int, int, Request)]

def optimized(requests, bays, rejected) -> None:
    # sort by time
    requests.sort(key=lambda request: request[1])

    # convert to smaller data types
    minified_requests = []
    for request in requests:
        (_, requested, vehicle) = request
        [_, time] = requested.split()
        (start, end) = request_start_end(time, vehicle)
        cost = servicing_charge[vehicle]
        minified_requests.append((start, end, cost))

    # create compacter versions of the destination structures
    minified_bays = [[]] * 10
    minified_rejected = []
    
    # optimized on those smaller data types
    optimized_recursive(0, minified_requests, minified_bays, minified_rejected)

    # convert the results back to actual choices
    for idx, bay_name in enunmerate(BAY_NAMES):
        bays[bay_name] = [(start, end, requests[i]) for (start, end, i) in minified_bays[idx]]
    rejected.entend(requests[i] for i in minified_rejected)


def optimized_recursive(index: int, requests: list[(int, int, int)], bays: list[list[(int, int, int)]], rejected: list[int]) -> int:   
    index = 0

    while True:
        (start, end, vehicle) = requests[index]

        bays = [BAY_NAMES[idx] for idx, bay in enumerate(bays) if all(other_start not in range(start, end) and other_end not in range(start, end) for (start, end, _) in bay)]

        colliders

        place_found: bool = False
        for schedule in [bays[vehicle], bays["general 1"], bays["general 2"], bays["general 3"], bays["general 4"], bays["general 5"]]:
            conflicting: bool = False
            for time in schedule:
                if time[0] in range(start, end) or time[1] in range(start, end):
                    conflicting = True
                    break
            
            if not conflicting:
                bays[vehicle].append((start, end, request))
                place_found = True
                break

        if not place_found:
            print(request, bays)
            rejected.append(request);
    

def reserved_time_chronological(requests, bays, rejected) -> None:
    requests.sort(key=lambda request: request[1])
    prioritize_order(requests, bays, rejected)

    
def issued_time_chronological(requests, bays, rejected) -> None:
    requests.sort(key=lambda request: request[0])
    prioritize_order(requests, bays, rejected)

    
def prioritize_order(requests, bays, rejected) -> None:
    for request in requests:
        (_, requested, vehicle) = request
        [_, time] = requested.split()
        (start, end) = request_start_end(time, vehicle)

        place_found: bool = False
        for schedule in [bays[vehicle], bays["general 1"], bays["general 2"], bays["general 3"], bays["general 4"], bays["general 5"]]:
            conflicting: bool = False
            for time in schedule:
                if time[0] in range(start, end) or time[1] in range(start, end):
                    conflicting = True
                    break
            
            if not conflicting:
                bays[vehicle].append((start, end, request))
                place_found = True
                break

        if not place_found:
            print(request, bays)
            rejected.append(request);


def request_start_end(time: str, vehicle: str) -> (int, int):
    [hours, minutes] = time.split(":")
    start = int(hours) * 60 + int(minutes)
    end = start + servicing_time[vehicle]
    return (start, end)

VEHICLE_NAMES = ["compact", "medium", "full-size", "class 1 truck", "class 2 truck"]

BAY_NAMES = VEHICLE_NAMES + [f"general {i}" for i in range(1, 6)]

servicing_time = {
    "compact": 30,
    "medium": 30,
    "full-size": 30,
    "class 1 truck": 60,
    "class 2 truck": 120
}

servicing_charge = {
    "compact": 150,
    "medium": 150,
    "full-size": 150,
    "class 1 truck": 250,
    "class 2 truck": 700
}
