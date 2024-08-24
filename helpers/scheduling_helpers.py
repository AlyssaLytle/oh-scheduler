"""Functions to help match TAs to available shifts."""

def match(TA_dict: dict, shift: str) -> str:
    """Returns TA's response for a specific shift's availability."""
    if shift in TA_dict:
        return TA_dict[shift]
    else:
        return "None"

def find_perfect_match(TAs: list, shift: str, TA_dict: dict) -> str:
    """Finds a TA with 'YES: PERFECT' rating on a shift."""
    for TA in TAs:
        if TA in TA_dict:
            if match(TA_dict[TA], shift) == "YES: PERFECT":
                return TA
    return "None"

def find_good_match(TAs: list, shift: str, TA_dict: dict) -> str:
    """Finds a TA with 'YES' rating on a shift."""
    for TA in TAs:
        if TA in TA_dict:
            if match(TA_dict[TA], shift) == "YES":
                return TA
    return "None"

def find_ok_match(TAs: list, shift: str, TA_dict: dict) -> str:
    """Finds a TA with 'YES: NOT IDEAL' rating on a shift."""
    for TA in TAs:
        if TA in TA_dict:
            if match(TA_dict[TA], shift) == "YES: NOT IDEAL":
                return TA
    return "None"

def find_match(TAs: list, shift: str, TA_dict: dict, exclude: dict) -> str:
    searchable = []
    for person in TAs:
        if not person in exclude:
            searchable.append(person)
    ta = find_perfect_match(searchable, shift, TA_dict)
    if ta == "None":
        ta = find_good_match(searchable, shift, TA_dict)
        if ta == "None":
            ta = find_ok_match(searchable, shift, TA_dict)
    return ta

def report_open_slots(schedule_slots: dict):
    for shift in schedule_slots:
        if schedule_slots[shift] > 0:
            print(f"{schedule_slots[shift]} people missing from {shift}")
        
def print_schedule(schedule: dict[str, list]):
    for shift in schedule:
        print(f"\n{shift}:")
        for elem in schedule[shift]:
            print(elem)
        
def report_ta_under_schedules(ta_hours: dict):
    for ta in ta_hours:
        if ta_hours[ta] > 0:
            print(f"{ta_hours[ta]} hours not scheduled for {ta}")