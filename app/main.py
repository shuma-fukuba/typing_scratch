from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI
import env
from middlewares import http_log

if env.APP_ENV == 'development':
    app = FastAPI()
else:
    app = FastAPI(docs_url=None,
                  redoc_url=None,
                  openapi_url=None)


app.add_middleware(BaseHTTPMiddleware, dispatch=http_log)
