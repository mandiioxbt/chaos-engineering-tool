import subprocess, time

class NetworkPartition:
    def __init__(self, target, dur=60): self.target, self.dur = target, dur
    def execute(self):
        subprocess.run(f"sudo iptables -A OUTPUT -d {self.target} -j DROP".split())
        time.sleep(self.dur)
        subprocess.run(f"sudo iptables -D OUTPUT -d {self.target} -j DROP".split())

class CPUStress:
    def __init__(self, dur=30, workers=4): self.dur, self.workers = dur, workers
    def execute(self): subprocess.run(f"stress-ng --cpu {self.workers} --timeout {self.dur}s".split())
