import os
import sys
from fastapi import FastAPI

app = FastAPI()

CONFIG_FILE = "/app/config/settings.json"

# Simula un error por falta de un archivo de configuración obligatorio
if not os.path.exists(CONFIG_FILE):
    print(f"[ERROR] Critical configuration file not found at {CONFIG_FILE}. Aborting startup.", file=sys.stderr)
    sys.exit(1)

@app.get("/")
def read_root():
    return {"status": "ok"}
