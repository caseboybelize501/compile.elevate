import psycopg2
from typing import Dict, List

class PerfStore:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="compiler_jarvis",
            user="postgres",
            password="password"
        )

    async def store_regression(self, ir_pattern: str, cpu_arch: str, performance_delta: float) -> bool:
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO performance_registrations (ir_pattern, cpu_arch, performance_delta) VALUES (%s, %s, %s)",
                (ir_pattern, cpu_arch, performance_delta)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error storing regression: {e}")
            return False
