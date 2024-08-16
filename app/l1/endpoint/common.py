# endpoint/common.py

# lib
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response, RedirectResponse, FileResponse

# l2

# definition
router = APIRouter()
template = Jinja2Templates(directory="app/template/common")

# endpoint
@router.get("/")
async def get_root(req:Request):
    resp = template.TemplateResponse(
        name="index.html",
        context={"request":req},
        status_code=200
    )
    return resp



# @router.get("/logout") # logout #############################################
# async def get_logout(req:Request):
#     req.state.access_token = AUTH.AccessToken( account_role_="guest" )
#     return RedirectResponse(url="/")


@router.get("/favicon.ico") # icon #############################################
async def get_favicon():
    return FileResponse( path="app/static/image/icon/brightest_dungeon.ico" )