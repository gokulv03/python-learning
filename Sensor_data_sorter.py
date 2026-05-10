def sort_sensor_data(raw_readings):

    valid_readings = []  
    fault_log = []

    for number in raw_readings:
        if number >= 10 and number <= 60:
            valid_readings.append(number)
        else:
            fault_log.append(number)

    return valid_readings, fault_log

print("=== Testing the Sensor Sorting Function ===")
print()

numbers = [11, 25, 33, 888, 44, 50, 0, 30]

good_readings, bad_readings = sort_sensor_data(numbers)

print(f"Original Data: {numbers}")
print()
print(f"Valid Readings: {good_readings}")
print(f"Fault Log: {bad_readings}")
print()
print(f"Total Valid: {len(good_readings)}")
print(f"Total Faults: {len(bad_readings)}")