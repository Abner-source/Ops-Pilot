from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(title="OpsPilot")
app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "OpsPilot is running"}
