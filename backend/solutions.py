from typing import TypeAlias

Request: TypeAlias = (str, int, str)
Schedule: TypeAlias = list[(int, int)]

def solve_day(requests: list[Request]) -> (dict[str, Schedule], list[Request]):
    test: (int, int) = (1, 2)
    print(test[1])

    
    bays = {
        "compact": Schedule,
        "medium": Schedule,
        "full-size": Schedule,
        "class 1 truck": Schedule,
        "class 2 truck": Schedule,
        "any": [Schedule] * 5
    }

    rejected: list[Request] = []

    requests.sort(key=issued_time)

    
    for request in requests:
        (issued, requested, vehicle) = request
        start = requested
        end = requested + servicing_time[vehicle]
        
        for schedule in [bays[vehicle], bays["any"][0], bays["any"][1], bays["any"][2], bays["any"][3], bays["any"][4]]:
            conflicting: bool = False
            for time in schedule:
                if time[0] in range(start, end) or time[1] in range(start, end):
                    conflicting = true
                    break
            
            if not conflicting:
                bays[vehicle].add((start, end))
                break
        else:
            rejected.add(request);

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

def main() -> None:
    returned = solve_day([("15:00", 120, "compact"), ("08:00", 90, "class 2 truck")])
    print(returned)
    
main()
