from typing import TypeAlias
import copy

Entry: TypeAlias = (str, str, str)
Schedule: TypeAlias = list[(int, int, Entry)]


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
