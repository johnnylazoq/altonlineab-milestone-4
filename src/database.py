import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

try:
    import mimerpy
    HAS_MIMER = True
except ImportError:
    HAS_MIMER = False
    logger.warning("MimerSQL client library not found. Using mock database connection.")

class MockCursor:
    def execute(self, query, params=None):
        self.last_query = query
        self.last_params = params
        print(f"[MOCK DB] Executing: {query} | Params: {params}")

    def fetchone(self):
        # Simple mock logic based on query content
        if "SELECT COUNT(*)" in self.last_query:
            # Mock: Department 1 is not leaf, others are leaf
            if self.last_params and self.last_params[0] == 1:
                return (1,) # Not leaf (count > 0)
            return (0,) # Leaf
        
        if "SELECT title, current_discount" in self.last_query:
            return ("Mock Product", 10.0)
            
        return None

    def fetchall(self):
        if "SELECT dept_id, title" in self.last_query:
            return [(2, "Electronics"), (3, "Books")]
        
        if "SELECT product_id, title" in self.last_query:
            return [(101, "Smartphone", 599.99), (102, "Laptop", 999.99)]
            
        return []

    def close(self):
        pass

class MockConnection:
    def cursor(self):
        return MockCursor()
    
    def commit(self):
        print("[MOCK DB] Commit")
        
    def close(self):
        print("[MOCK DB] Connection closed")

def connect(user=None, password=None, database=None):
    """
    Establishes a connection to the MimerSQL database.
    """
    if HAS_MIMER:
        return mimerpy.connect(
            user=user or os.getenv("DB_USER"),
            password=password or os.getenv("DB_PASSWORD"),
            database=database or os.getenv("DB_NAME")
        )
    else:
        return MockConnection()
