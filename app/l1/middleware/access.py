# middleware/access.py

# lib
from typing import Callable, Awaitable
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

# l2

# definition
class AccessMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        # 요청 전


        resp:Response = await call_next(req)
        # 요청 후

        return resp