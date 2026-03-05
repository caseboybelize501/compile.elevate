import chromadb
from typing import Dict, List

class MetaLearner:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("meta_learning")

    async def store_cycle_data(self, cycle_number: int, performance_metrics: Dict) -> bool:
        try:
            self.collection.add(
                documents=[f"Cycle {cycle_number} performance"],
                metadatas=[{
                    "cycle": cycle_number,
                    "metrics": performance_metrics
                }],
                ids=[f"cycle_{cycle_number}"]
            )
            return True
        except Exception as e:
            print(f"Error storing cycle data: {e}")
            return False
