print("SENSOR READING ANALYZER")
print()

valid_readings = []
fault_log = []

numbers = [11, 25, 33, 888, 44, 50, 0, 30]

for number in numbers:
    if number >= 10 and number <= 60:
        valid_readings.append(number)
    else:
        fault_log.append(number)

print(f"Valid Readings: {valid_readings}")
print(f"Fault Log: {fault_log}")