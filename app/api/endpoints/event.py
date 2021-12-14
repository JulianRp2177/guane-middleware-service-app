from typing import List, Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.event import CreateEvent, UpdateEvent, PayloadEvent
from app.services.service_db import service_db


router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def create_event(*, event: CreateEvent):
    event_transform = event.dict()
    route = "/api/event/"
    response = await service_db.create(obj_in=event_transform, route=route)
    if response:
        return response
    else:
        response = {"message": "Error in create event"}
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
async def counter(*, payload: PayloadEvent = None):
    payload_transform = payload.dict(exclude_none=True)
    route = "/api/event/counter"
    counter = await service_db.counter(obj_in = payload_transform, route=route)
    return counter

@router.get(
    "/{id_event}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_by_id(*, id_event: int):
    route = "/api/event/"
    response = await service_db.get_by_id(_id=id_event, route=route)
    if response:
        return response
    else:
        response = {"message": "event not found"}
        return response

# @router.get(
#     "/",
#     response_class=JSONResponse,
#     response_model=dict,
#     status_code=200,
#     responses={
#         200: {"description": "event found"},
#         401: {"description": "event unauthorized"},
#         404: {"description": "event not found"},
#     },
# )
# async def get_all(skip: int = 0, limit: int = 20):
#     route = "/api/event/"
#     response = await service_db.get_with_payload(payload = {}, skip=skip, limit=limit, route=route)
#     if response:
#         return response
#     else:
#         response = {"message": "events not found"}
#         return response

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[dict],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadEvent],
        skip_interval: int = 0,
        limit_interval: int = 10):
    route = "/api/event/payload"
    payload_transform = payload.dict(exclude_none=True)
    events = await service_db.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events 

@router.put(
    "/{id_event}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def update( *,id_event: int, in_event: UpdateEvent):
    route = "/api/event/"
    event_transform = in_event.dict(exclude_none=True)
    event = await service_db.update(_id = id_event, obj_in = event_transform, route=route )
    if not event:
        return JSONResponse(status_code=404)
    else:
        return event

@router.delete(
    "/{id_event}",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def delete_by_id( *,id_event : int):
    route = "/api/event/"
    event = await service_db.delete(_id= id_event, route=route)
    if not event:
        return JSONResponse(status_code=404)
    else:
        return "register deleted"

