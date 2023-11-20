import psutil
import platform
import json

computer = {
    "Name": platform.system(),
    "CPU": platform.machine(),
    "RAM total": psutil.virtual_memory().total,
    "RAM busy": psutil.virtual_memory().used,
    "RAM free": psutil.virtual_memory().available,
    "RAM occupancy rate": psutil.virtual_memory().percent,
}

print(json.dumps(computer, indent=4))