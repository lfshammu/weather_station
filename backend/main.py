import uvicorn
from fastapi import FastAPI
from msgpack_asgi import MessagePackMiddleware

from endpoints.v1 import weather_consumer, base

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)
app.add_middleware(MessagePackMiddleware)
app.router.include_router(base.router, prefix='/api/v1')
app.router.include_router(weather_consumer.router, prefix='/api/v1')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
