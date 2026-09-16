from fastapi import FastAPI

app = FastAPI(title="AI Data Intelligence Platform")


@app.get("/")
def root():
    return {"message": "AI Data Intelligence Platform API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}