def parse(feet_inches):
    # Using the split method based on the Empty Space:
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
