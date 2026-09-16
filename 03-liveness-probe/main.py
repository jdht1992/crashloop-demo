from fastapi import FastAPI, Response


app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "running"}


# Ruta de Liveness Probe que simula un fallo interno de la app
@app.get("/healthz")
def health_check(response: Response):
    # Forzamos un error 500 para que Kubernetes mate el contenedor
    response.status_code = 500
    return {"status": "unhealthy"}
