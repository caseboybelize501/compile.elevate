from pydantic import BaseModel
from typing import List, Dict, Optional

class CompilerInfo(BaseModel):
    tool: str
    version: str
    path: str
    features: List[str]

class CPUInfo(BaseModel):
    architecture: str
    cores: int
    cache_sizes: Dict[str, str]
    simd_support: List[str]

class BenchmarkInfo(BaseModel):
    name: str
    path: str
    detected: bool

class CompilerSystemProfile(BaseModel):
    compilers: List[CompilerInfo]
    cpu: CPUInfo
    benchmarks: List[BenchmarkInfo]
