import time

from urllib.request import Request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import countries
from starlette.status import HTTP_408_REQUEST_TIMEOUT

REQUEST_TIMEOUT_ERROR = 3  # Threshold

app = FastAPI(
    version="0.3",
    title="CodeTask",
    description="data collector"
)


@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        start_time = time.time()
        return await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT_ERROR)

    except asyncio.TimeoutError:
        process_time = time.time() - start_time
        return JSONResponse({'detail': 'Request processing time excedeed limit',
                             'processing_time': process_time},
                            status_code=HTTP_408_REQUEST_TIMEOUT)


app.include_router(countries.router)

if __name__ == "__main__":
    import asyncio
    import uvicorn

    HOST = "127.0.0.1"
    PORT = 8000

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(uvicorn.run(app, host=HOST, port=PORT))
