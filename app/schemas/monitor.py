from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

class MonitorCreate(BaseModel):
    name: str = Field(min_lenght=1, max_lenght=100)
    url: HttpUrl
    interval_seconds: int = Field(default=60, ge=10, le=86400)
    is_active: bool=True


class MonitorResponse(BaseModel):
    id: int
    name: str
    url: str
    interval_seconds: int
    is_active: bool
    created_at: datetime

    model_config =ConfigDict(from_attributes=True)
    