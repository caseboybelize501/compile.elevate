import asyncio
from fastapi import FastAPI
from src.bootstrap.system_scanner import SystemScanner
from src.agents.ir_agent import IRAgent
from src.agents.pass_agent import PassAgent
from src.agents.build_agent import BuildAgent
from src.agents.benchmark_agent import BenchmarkAgent
from src.agents.perf_agent import PerfAgent
from src.agents.learn_agent import LearnAgent

app = FastAPI(title="Autonomous Compiler Engineering Jarvis")

@app.on_event("startup")
async def startup_event():
    scanner = SystemScanner()
    await scanner.scan()
    print("System scan complete.")

@app.get("/")
def read_root():
    return {"message": "Autonomous Compiler Engineering Jarvis is running."}
