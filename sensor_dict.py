from datetime import datetime

pressure_sensor = {
    "id": "P-201",
    "reading": 120,
    "unit": "psi"
}

flow_sensor = { 
    "id": "F-305",
    "reading": 45,
    "unit": "GPM"
}

factory_sensors = [pressure_sensor, flow_sensor]

for sensor in factory_sensors:
    timestamp = datetime.now()
    clean_time = timestamp.strftime("%H:%M:%S")
    print(f" {clean_time} - Sensor ID {sensor['id']} is reading {sensor['reading']} {sensor['unit']}.")
    with open("sensor_log.txt", "a") as log_file:
        log_file.write(f"{clean_time} - Sensor ID {sensor['id']} is reading {sensor['reading']} {sensor['unit']}.\n")



