import psutil
import time

psutil.sensors_battery()
# sbattery(percent=0.0, secsleft=-1, power_plugged=None)
power_status = psutil.sensors_battery().power_plugged
# None

print(power_status)
