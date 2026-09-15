import psutil
import time
from winotify import Notification



notified = False
full_notified = False


while True:
    battery = psutil.sensors_battery()

    percent = battery.percent
    plugged = battery.power_plugged
    percent = 100
    plugged = True

    print(f"Battery: {percent}% | Charger: {plugged}")

    if percent <= 30 and not plugged:
        if not notified:
            notification = Notification(
                app_id="Battery Monitor",
                title="Battery Low",
                msg=f"{percent}% Battery remaining!"
            )
            notification.show()
            notified = True
    else:
        notified = False

    if percent == 100 and plugged:
        if not full_notified:
            notification = Notification(
                app_id="Battery Monitor",
                title="Battery Full",
                msg=f"{percent}% Batteryfull!"
            )
            notification.show()
            full_notified = True
    else:
        full_notified = False

    time.sleep(60)