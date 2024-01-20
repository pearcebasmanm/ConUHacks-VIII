Request: TypeAlias = (str, Integer, str)
Schedule: TypeAlias = List[(Integer, Integer)]

def solve_day(requests: List[Request]) -> (Dict[String, Schedule], List[Request]):
    bays = {
        "compact": Schedule,
        "medium": Schedule,
        "full-size": Schedule,
        "class 1 truck": Schedule,
        "class 2 truck": Schedule,
        "any": [Schedule] * 5
    }

    rejected: List[Request] = []

    requests.sort(key=issued_time)
    for request in requests:
        (issued, requested, vehicle) = request
        start = requested
        end = requested + servicing_time[vehicle]


        for schedule in [bays[vehicle], bays["any"][0], bays["any"][1], bays["any"][2], bays["any"][3], bays["any"][4]]:
            conflicting = false
            for time in schedule:
                if time[0] in range(start, end) or time[1] in range(start, end):
                    conflicting = true
                    break
            
            if not conflicting:
                bays[vehicle].add((start, end))
                break
        else:
            rejected.add(request);

        

servicing_time = {
    "compact": 30,
    "medium": 30,
    "full-size": 30,
    "class 1 truck": 60,
    "class 2 truck": 120
}

def issued_time(request: Request) -> String:
    return request[0]
