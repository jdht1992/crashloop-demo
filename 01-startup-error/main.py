import sys
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    app_env: str = "production"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Intento de carga de configuración al iniciar la app
try:
    settings = Settings()
except Exception as e:
    print(f"[FATAL] Configuration validation failed: {e}", file=sys.stderr)
    # En producción esto genera un código de salida distinto a 0, 
    # lo que le indica a Kubernetes que el contenedor falló.
    sys.exit(1)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "environment": settings.app_env}
