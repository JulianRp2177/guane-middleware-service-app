from typing import List, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.schemas.trainer import CreateTrainer, UpdateTrainer, TrainerInDB, PayloadTrainer
from app.services.service_db import service_db


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
async def create_user(*, trainer: CreateTrainer):
    trainer_transform = trainer.dict()
    route = "/api/trainer/"
    response = await service_db.create(obj_in=trainer_transform, route=route)
    if response:
        return response
    else:
        response = {"message": "Error in create trainer"}
        return response

@router.post(
    "/counter",
    response_class=JSONResponse,
    response_model=int,
    status_code=200,
    responses={
        200: {"description": "trainer found"},
        401: {"description": "trainer unauthorized"},
        404: {"description": "trainer not found"},
    },
)
async def counter(*, payload: PayloadTrainer = None):
    payload_transform = payload.dict(exclude_none=True)
    route = "/api/trainer/counter"
    counter = await service_db.counter(obj_in = payload_transform, route=route)
    return counter

@router.get(
    "/{id_trainer}",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "trainer found"},
        401: {"description": "trainer unauthorized"},
        404: {"description": "trainer not found"},
    },
)
async def get_by_id(*, id_trainer: int):
    route = "/api/trainer/"
    response = await service_db.get_by_id(_id=id_trainer, route=route)
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
#         200: {"description": "trainer found"},
#         401: {"description": "trainer unauthorized"},
#         404: {"description": "trainer not found"},
#     },
# )
# async def get_all(skip: int = 0, limit: int = 20):
#     route = "/api/trainer/"
#     response = await service_db.get_with_payload(payload = {}, skip=skip, limit=limit, route=route)
#     if response:
#         return response
#     else:
#         response = {"message": "trainers not found"}
#         return response

@router.get(
    "/my_events/{id_trainer}",
    response_class=JSONResponse,
    response_model=list,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_my_events(*, id_trainer: int, skip_interval: int, limit_interval: int):

    route = "/api/event/payload"
    payload_transform = {}
    payload_transform["trainer_id"] = id_trainer
    events = await service_db.get_with_payload(payload = payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events

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
        payload: Optional[PayloadTrainer],
        skip_interval: int = 0,
        limit_interval: int = 10):
    route = "/api/trainer/payload"
    payload_transform = payload.dict(exclude_none=True)
    trainers = await service_db.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval , route = route)
    if not trainers:
        return JSONResponse(status_code=404)
    else:
        return trainers 

@router.put(
    "/{id_trainer}",
    response_class=JSONResponse,
    response_model=TrainerInDB,
    status_code=200,
    responses={
        200: {"description": "trainer found"},
        401: {"description": "trainer unauthorized"},
        404: {"description": "trainer not found"},
    },
)
async def update( *,id_trainer: int, in_trainer: UpdateTrainer):
    route = "/api/trainer/"
    trainer_transform = in_trainer.dict(exclude_none=True)
    trainer = await service_db.update(_id = id_trainer, obj_in = trainer_transform, route=route )
    if not trainer:
        return JSONResponse(status_code=404)
    else:
        return trainer

@router.delete(
    "/{id_trainer}",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "trainer found"},
        401: {"description": "trainer unauthorized"},
        404: {"description": "trainer not found"},
    },
)
async def delete_by_id( *,id_trainer : int):
    route = "/api/trainer/"
    trainer = await service_db.delete(_id= id_trainer, route=route)
    if not trainer:
        return JSONResponse(status_code=404)
    else:
        return "register deleted"

