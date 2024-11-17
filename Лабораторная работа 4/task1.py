# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r") as file:
        json_data = json.load(file)
    return round(sum(val["score"] * val["weight"] for val in json_data), 3)


print(task())
