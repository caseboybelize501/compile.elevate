import subprocess
from src.bootstrap.compiler_scanner import CompilerScanner
from src.bootstrap.cpu_scanner import CPUScanner
from src.bootstrap.benchmark_scanner import BenchmarkScanner
from src.bootstrap.profile_writer import ProfileWriter

class SystemScanner:
    def __init__(self):
        self.compiler_scanner = CompilerScanner()
        self.cpu_scanner = CPUScanner()
        self.benchmark_scanner = BenchmarkScanner()
        self.profile_writer = ProfileWriter()

    async def scan(self):
        print("Starting system scan...")
        compilers = await self.compiler_scanner.scan()
        cpu_info = await self.cpu_scanner.scan()
        benchmarks = await self.benchmark_scanner.scan()
        
        profile = {
            "compilers": compilers,
            "cpu": cpu_info,
            "benchmarks": benchmarks
        }
        
        await self.profile_writer.write(profile)
        print("System scan complete.")
