from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.user import CreateUser, UpdateUser, UserInDB, PayloadUser, Reservation
from app.services.service_db import service_db
from app.services.service_worker import service_worker

router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_user(*, user: CreateUser):
    user_transform = user.dict()
    route = "/api/user/"
    response = await service_db.create(obj_in=user_transform, route=route)
    if response:
        return response
    else:
        response = {"message": "Error in create User"}
        return response

@router.post(
    "/registration",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_regristration(*, reservation: Reservation):
    reservation_transform = reservation.dict()
    route = "/api/event_x_user/"

    route_event = "/api/event/"
    response_event = await service_db.get_by_id(_id=reservation_transform["event_id"], route=route_event)
    if response_event:
        if response_event["reservation"] == True:
            #message = {"message": "the event needs reservation"}
            reservation_route = "/api/reservation/"
            reservation = await service_worker.create(obj_in=reservation, route=reservation_route)

            return reservation
        
        else:
            response = await service_db.create(obj_in=reservation_transform, route=route)
            if response:
                return response
            else:
                response = {"message": "Error in create reservation"}
                return response
    else:
        response = {"message": "Event not found"}
        return response

@router.post(
    "/registration",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_reservation(*, reservation: Reservation):
    reservation_transform = reservation.dict()
    route = "/api/event_x_user/"

    route_event = "/api/event/"
    response_event = await service_db.get_by_id(_id=reservation["event_id"], route=route_event)
    if response_event:
        if response_event["reservation"] == False:
            message = {"message": "the event not needs reservation"}
            return message
    else:
        response = await service_db.create(obj_in=reservation_transform, route=route)
        if response:
            return response
        else:
            response = {"message": "Error in create reservation"}
            return response        

@router.get(
    "/registration",
    response_class=JSONResponse,
    response_model=list,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_reservation(*, id_user: int, skip_interval: int, limit_interval: int):
    response_events = []
    route = "/api/event_x_user/payload"
    payload_transform = {}
    payload_transform["user_id"] = id_user
    events = await service_db.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    
    if events:
        for event in events:
            route_event = "/api/event/"
            response = await service_db.get_by_id(_id=event["event_id"], route=route_event)
            response_events.append(response)
    else:
        return []

    if not response_events:
        return JSONResponse(status_code=404)
    else:
        return response_events


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
async def counter(*, payload: PayloadUser = None):
    payload_transform = payload.dict(exclude_none=True)
    route = "/api/user/counter"
    counter = await service_db.counter(obj_in = payload_transform, route=route)
    return counter

@router.get(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_by_id(*, id_user: int):
    route = "/api/user/"
    response = await service_db.get_by_id(_id=id_user, route=route)
    if response:
        return response
    else:
        response = {"message": "User not found"}
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
#     route = "/api/user/"
#     response = await service_db.get_with_payload(payload = {}, skip=skip, limit=limit, route=route)
#     if response:
#         return response
#     else:
#         response = {"message": "Users not found"}
#         return response

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[dict],
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_with_payload( *,
        payload: PayloadUser,
        skip_interval: int = 0,
        limit_interval: int = 10):
    route = "/api/user/payload"
    payload_transform = payload.dict(exclude_none=True)
    users = await service_db.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    if not users:
        return JSONResponse(status_code=404)
    else:
        return users 

@router.put(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,id_user: int, in_user: UpdateUser):
    route = "/api/user/"
    user_transform = in_user.dict(exclude_none=True)
    user = await service_db.update(_id = id_user, obj_in = user_transform, route=route )
    if not user:
        return JSONResponse(status_code=404)
    else:
        return user

@router.delete(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_user : int):
    route = "/api/user/"
    user = await service_db.delete(_id= id_user, route=route)
    if not user:
        return JSONResponse(status_code=404)
    else:
        return "register deleted"

