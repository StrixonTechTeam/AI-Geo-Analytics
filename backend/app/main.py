from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI-Geo-Analytics API") # creates API server application to handle the request

# This allows Frontend React app (on a different port) to call the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], #allows frontend URL
    allow_methods=["*"],# allows all http methods (PUT, GET, etc)
    allow_headers=["*"], #allows any request header
)

@app.get("/health") #creating an API endpoint/route for health
def health_check():
    return {"status": "ok"}