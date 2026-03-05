import subprocess
import json

class CPUScanner:
    def __init__(self):
        pass

    async def scan(self):
        try:
            lscpu_output = subprocess.check_output(["lscpu"], text=True)
            cpu_info = self._parse_lscpu(lscpu_output)
            return cpu_info
        except Exception as e:
            print(f"Error scanning CPU: {e}")
            return {}

    def _parse_lscpu(self, output):
        info = {}
        lines = output.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()
        return info
