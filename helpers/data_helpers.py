"""Functions to pull data from .csv files."""

import csv

def get_hours(fname: str) -> dict:
    """Get weekly hours as dict from TA-Hours.csv."""
    hours_dict: dict[str, int] = {}
    seniority_dict: dict[str, int] = {}
    with open(fname) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            name = row[0].lower()
            hours = int(row[2])
            hours_dict[name] = hours
            seniority = int(row[3])
            seniority_dict[name] = seniority
    return [hours_dict, seniority_dict]

def get_availability(fname: str) -> dict:
    """Get availability as dict from WhenIsGood data. 
    (oh.csv and tutoring.csv)"""
    avail_dict: dict[str, dict] = {}
    time_slot_scores: dict = {}
    with open(fname) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        names = next(reader)[3:]
        # set blank dict to store each team member's availability
        for name in names:
            avail_dict[name.lower()] = {}
        for row in reader:
            time_slot = row[0]
            score = row[2]
            time_slot_scores[time_slot] = int(score)
            availabilites = row[3:]
            # for each shift, populate each team member's availability in their dict
            for idx in range(len(availabilites)):
                avail_dict[names[idx].lower()][time_slot] = availabilites[idx] 
    return [time_slot_scores, avail_dict]
    