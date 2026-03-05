import re
from typing import Dict, List

class PerfParser:
    def __init__(self):
        pass

    def parse_perf_output(self, output: str) -> Dict:
        # Parse perf stat output
        data = {}
        lines = output.split('\n')
        for line in lines:
            if 'cycles' in line:
                match = re.search(r'(\d+\.?\d*)\s+cycles', line)
                if match:
                    data['cycles'] = float(match.group(1))
            elif 'instructions' in line:
                match = re.search(r'(\d+\.?\d*)\s+instructions', line)
                if match:
                    data['instructions'] = float(match.group(1))
        return data
