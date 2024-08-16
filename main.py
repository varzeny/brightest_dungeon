# main.py

"""
uvicorn main:app --host 0.0.0.0 --port 9100
"""

# lib
from fastapi import FastAPI, staticfiles

# core
import app.core.util as UTIL

# l1
from app.l1.middleware.access import AccessMiddleware
from app.l1.endpoint.common import router as common_router

# definition
async def startup():
    # Database

    # Authorization
    
    print()

async def shutdown():
    print() 


# app
app = FastAPI(
    on_startup=[startup],
    on_shutdown=[shutdown]
)

# mount
app.mount(
    path="/static",
    app=staticfiles.StaticFiles(directory="app/static")
)

# middleware
app.add_middleware( AccessMiddleware )

# router
app.include_router( common_router )

# config
app.state.config = UTIL.read_file_from_ini()
