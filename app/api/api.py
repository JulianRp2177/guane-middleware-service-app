from fastapi import APIRouter

from app.api.endpoints import (
    root,
    user,
    trainer,
    site,
    event
)

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(trainer.router, prefix="/trainer", tags=["Trainer"])
api_router.include_router(site.router, prefix="/site", tags=["Site"])
api_router.include_router(event.router, prefix="/event", tags=["Event"])