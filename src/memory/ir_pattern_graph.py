from neo4j import GraphDatabase
from typing import Dict, List

class IRPatternGraph:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    async def add_pattern(self, pattern_type: str, pattern_data: Dict) -> bool:
        try:
            with self.driver.session() as session:
                session.write_transaction(
                    self._create_pattern_node,
                    pattern_type,
                    pattern_data
                )
            return True
        except Exception as e:
            print(f"Error adding pattern: {e}")
            return False

    @staticmethod
    def _create_pattern_node(tx, pattern_type: str, pattern_data: Dict):
        query = (
            "CREATE (p:Pattern {type: $type, data: $data})"
            "RETURN p"
        )
        tx.run(query, type=pattern_type, data=pattern_data)
