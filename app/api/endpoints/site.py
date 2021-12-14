from typing import List, Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.site import CreateSite, UpdateSite, PayloadSite
from app.services.service_db import service_db


router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def create_site(*, site: CreateSite):
    site_transform = site.dict()
    route = "/api/site/"
    response = await service_db.create(obj_in=site_transform, route=route)
    if response:
        return response
    else:
        response = {"message": "Error in create site"}
        return response

@router.post(
    "/counter",
    response_class=JSONResponse,
    response_model=int,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def counter(*, payload: PayloadSite = None):
    payload_transform = payload.dict(exclude_none=True)
    route = "/api/site/counter"
    counter = await service_db.counter(obj_in = payload_transform, route=route)
    return counter

@router.get(
    "/{id_site}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def get_by_id(*, id_site: int):
    route = "/api/site/"
    response = await service_db.get_by_id(_id=id_site, route=route)
    if response:
        return response
    else:
        response = {"message": "site not found"}
        return response

# @router.get(
#     "/",
#     response_class=JSONResponse,
#     response_model=dict,
#     status_code=200,
#     responses={
#         200: {"description": "site found"},
#         401: {"description": "site unauthorized"},
#         404: {"description": "site not found"},
#     },
# )
# async def get_all(skip: int = 0, limit: int = 20):
#     route = "/api/site/"
#     response = await service_db.get_with_payload(payload = {}, skip=skip, limit=limit, route=route)
#     if response:
#         return response
#     else:
#         response = {"message": "sites not found"}
#         return response

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[dict],
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadSite],
        skip_interval: int = 0,
        limit_interval: int = 10):
    route = "/api/site/payload"
    payload_transform = payload.dict(exclude_none=True)
    sites = await service_db.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    if not sites:
        return JSONResponse(status_code=404)
    else:
        return sites 

@router.put(
    "/{id_site}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def update( *,id_site: int, in_site: UpdateSite):
    route = "/api/site/"
    site_transform = in_site.dict(exclude_none=True)
    site = await service_db.update(_id = id_site, obj_in = site_transform, route=route )
    if not site:
        return JSONResponse(status_code=404)
    else:
        return site

@router.delete(
    "/{id_site}",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def delete_by_id( *,id_site : int):
    route = "/api/site/"
    site = await service_db.delete(_id= id_site, route=route)
    if not site:
        return JSONResponse(status_code=404)
    else:
        return "register deleted"

