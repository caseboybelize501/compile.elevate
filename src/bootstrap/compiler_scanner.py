import subprocess
import json

class CompilerScanner:
    def __init__(self):
        self.tools = ["clang", "gcc", "rustc"]

    async def scan(self):
        results = []
        for tool in self.tools:
            try:
                version_output = subprocess.check_output([tool, "--version"], stderr=subprocess.STDOUT, text=True)
                path = subprocess.check_output(["which", tool], text=True).strip()
                
                result = {
                    "tool": tool,
                    "version": version_output.split('\n')[0],
                    "path": path,
                    "features": self._extract_features(tool, version_output)
                }
                results.append(result)
            except Exception as e:
                print(f"Error scanning {tool}: {e}")
        return results

    def _extract_features(self, tool, version):
        features = []
        if "clang" in tool:
            features.extend(["LLVM", "C/C++", "Optimization"])
        elif "gcc" in tool:
            features.extend(["GNU", "C/C++", "Optimization"])
        elif "rustc" in tool:
            features.extend(["Rust", "Safe", "LLVM Backend"])
        return features
