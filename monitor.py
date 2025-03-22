import psutil
import subprocess
import time

threshold = 75  # CPU usage threshold in percent

def check_cpu():
    cpu = psutil.cpu_percent(interval=5)
    if cpu > threshold:
        print(f"High CPU: {cpu}% → Launching EC2 at {time.ctime()}")
        subprocess.run(["bash", "scale_up.sh"])

while True:
    check_cpu()
