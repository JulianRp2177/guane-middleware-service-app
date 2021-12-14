from typing import Any, Dict, Optional, TypeVar
from app.config import settings
from pydantic.main import BaseModel
from app.infra.httpx.client import HTTPClient

class ServiceDB():
    def __init__(
        self,
        client: HTTPClient = HTTPClient(),
    ):
        self._client = client

    async def create(
        self, *, obj_in: dict, route: Optional[str] = ""
    ) -> Any:
        url = f"{settings.SERVICE_DATABASE}{route}"
        body = obj_in
        response = await self._client.post(url_service=url, body=body)
        if response:
            response = response.json()
            return response
        else:
            return None
    
    async def counter(
        self, *, obj_in: dict, route: Optional[str] = ""
    ) -> Any:
        url = f"{settings.SERVICE_DATABASE}{route}"
        body = obj_in
        response = await self._client.post(url_service=url, body=body)
        if response:
            response = response.json()
            return response
        else:
            return None

    async def update(
        self, *, _id: int, obj_in: dict, route: Optional[str] = ""
    ) -> Any:
        url = f"{settings.SERVICE_DATABASE}{route}{_id}"
        body = obj_in
        response = await self._client.put(url_service=url, body=body)
        if response:
            response = response.json()
            return response
        else:
            return None

    async def delete(self, *, _id: int, route: Optional[str] = "") -> Any:
        url = f"{settings.SERVICE_DATABASE}{route}{_id}"
        response = await self._client.delete(url_service=url)
        if response:
            response = response.json()
            return response
        else:
            return None

    async def get_by_id(self, *, _id: int, route: Optional[str] = "") -> Any:
        url = f"{settings.SERVICE_DATABASE}{route}{_id}"
        response = await self._client.get(url_service=url)
        if response:
            response = response.json()
            return response
        else:
            return None

    async def get_all(
        self,
        payload: Optional[Dict[str, Any]],
        skip: int = 0,
        limit: int = 99999,
        route: Optional[str] = "",
    ) -> Any:
        if payload:
            payload.update({"skip": skip, "limit": limit})
        else:
            payload = {"skip": skip, "limit": limit}
        url = f"{settings.SERVICE_DATABASE}{route}"
        response = await self._client.get(url_service=url, params=payload)
        if response:
            response = response.json()
            return response
        else:
            return None

    async def get_with_payload(
        self,
        payload: Optional[Dict[str, Any]],
        skip: int = 0,
        limit: int = 99999,
        route: Optional[str] = "",
    ) -> Any:
        params = {}
        if payload:
            params["skip"] = skip
            params["limit"] = limit
        else:
            params = {}
            params["skip"] = skip
            params["limit"] = limit
        url = f"{settings.SERVICE_DATABASE}{route}"
        response = await self._client.post(url_service=url, params=params, body=payload)
        if response:
            response = response.json()
            return response
        else:
            return None



service_db = ServiceDB()