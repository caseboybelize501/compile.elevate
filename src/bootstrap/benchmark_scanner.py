import os
import subprocess

class BenchmarkScanner:
    def __init__(self):
        self.benchmarks = [
            "/opt/spec-cpu",
            "/opt/coremark",
            "/opt/microbench"
        ]

    async def scan(self):
        results = []
        for benchmark_path in self.benchmarks:
            if os.path.exists(benchmark_path):
                try:
                    # Try to run a simple check
                    subprocess.check_output([benchmark_path, "--version"], stderr=subprocess.STDOUT)
                    results.append({
                        "name": os.path.basename(benchmark_path),
                        "path": benchmark_path,
                        "detected": True
                    })
                except Exception:
                    pass
        return results
