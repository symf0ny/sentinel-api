from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.monitor import MonitorCreate, MonitorResponse
from app.services.monitor import create_monitor


router = APIRouter(
    prefix='/monitors',
    tags=['Monitors'],
)


@router.post(
    '',
    response_model=MonitorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_monitor_endpoint(
    data: MonitorCreate,
    db: Session = Depends(get_db),
):
    return create_monitor(db, data)