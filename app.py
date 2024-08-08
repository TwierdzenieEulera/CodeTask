from fastapi import FastAPI

from routers import countries

app = FastAPI(
    version="0.2",
    title="CodeTask",
    description="data collector"
)

app.include_router(countries.router)

if __name__ == "__main__":
    import asyncio
    import uvicorn

    HOST = "127.0.0.1"
    PORT = 8000

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(uvicorn.run(app, host=HOST, port=PORT))
