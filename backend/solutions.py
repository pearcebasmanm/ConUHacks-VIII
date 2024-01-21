from typing import TypeAlias
import copy

Entry: TypeAlias = (str, str, str)
Schedule: TypeAlias = list[(int, int, Entry)]

def optimized(requests, bays, rejected) -> None:
    # sort by time
    requests.sort(key=lambda request: request[1])

    # convert to smaller data types
    minified_requests = []
    for request in requests:
        (_, requested, vehicle) = request
        [_, time] = requested.split()
        (start, end) = request_start_end(time, vehicle)
        vehicle = VEHICLE_NAMES.index(vehicle)
        minified_requests.append((start, end, vehicle))

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

    current_request = requests[index]
    (start, end, vehicle) = current_request
    
    general = next((idx + 5 for bay in enumerate(bays[5:]) if all(other_start not in range(start, end) and other_end not in range(start, end) for (start, end, _) in bay)), None)

    dedicated = bays[vehicle] if all(other_start not in range(start, end) and other_end not in range(start, end) for (start, end, _) in bays[vehicle]) else None

    maximum = 0
    best_bays
    best_rejected
    
    for bay in [general, dedicated]:
        if bay is None:
            continue


        potential_request_indexes = [index]

        # run the simulation for each vehicle that would otherwise take its place
        colliders_index = index + 1
        while requests[colliders_index][0] > end:
            collider = requests[colliders_index]
            if bay >= 5 or bay == collider[2]:
                potential_requests.append(colliders_index)
                        
        for potential_request_index in potential_request_indexes
        # run the recursive simulation for the current vehicle
        sub_bays = copy.deepcopy(bays)
        sub_rejected = copy.deepcopy(rejected)
        sub_bay[bay].append((start, collider[1], collider_index))
        sub_bay
        parameter = optimized_recursive(colliders_index + 1, requests, sub_bays, sub_rejected)
        if parameter > maximum:
            best_bays = sub_bays
            best_rejected = sub_rejected
            maximum = parameter
            
    

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
