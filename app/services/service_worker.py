from typing import Any, Dict, Optional, TypeVar
from app.config import settings
from pydantic.main import BaseModel
from app.infra.httpx.client import HTTPClient

class ServiceWorker():
    def __init__(
        self,
        client: HTTPClient = HTTPClient(),
    ):
        self._client = client

    async def create(
        self, *, obj_in: dict, route: Optional[str] = ""
    ) -> Any:
        obj_in = obj_in.dict()
        url = f"{settings.WORKER_API}{route}"
        body = obj_in
        response = await self._client.post(url_service=url, body=body)
        if response:
            response = response.json()
            return response
        else:
            return None
    


service_worker = ServiceWorker()