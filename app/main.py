from fastapi import FastAPI

app = FastAPI(
    title="Sentinel app",
    description='Website and API monitoring service',
    version='0.1.0'
)

@app.get('/health')
def health_check():
    return {'status': 'ok'}