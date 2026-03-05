import subprocess
import asyncio
from typing import Dict, List

class BenchmarkRunner:
    def __init__(self):
        pass

    async def run_all_benchmarks(self) -> List[Dict]:
        benchmarks = [
            "spec_cpu",
            "coremark",
            "geekbench"
        ]
        results = []
        for bench in benchmarks:
            try:
                result = subprocess.run([
                    f"run_{bench}.sh"
                ], capture_output=True, text=True, check=True)
                results.append({
                    "benchmark": bench,
                    "status": "success",
                    "output": result.stdout
                })
            except Exception as e:
                results.append({
                    "benchmark": bench,
                    "status": "failed",
                    "error": str(e)
                })
        return results
