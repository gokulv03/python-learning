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
    print(f"Sensor ID {sensor['id']} is reading {sensor['reading']} {sensor['unit']}.")

