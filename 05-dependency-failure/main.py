import sys
import socket
from fastapi import FastAPI

app = FastAPI()

def check_database_connection():
    # Simulamos intentar conectar a una base de datos que no existe en el cluster
    db_host = "db-service.default.svc.cluster.local"
    db_port = 5432
    
    try:
        s = socket.create_connection((db_host, db_port), timeout=2)
        s.close()
    except (socket.timeout, socket.error):
        print(f"[ERROR] Could not connect to database at {db_host}:{db_port}. Dependency failure!", file=sys.stderr)
        sys.exit(1) # Rompe el arranque si la dependencia no responde

# Se ejecuta al arrancar FastAPI
check_database_connection()

@app.get("/")
def read_root():
    return {"status": "connected"}
