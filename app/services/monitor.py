from sqlalchemy.orm import Session

from app.models.monitor import Monitor
from app.schemas.monitor import MonitorCreate


def create_monitor(db: Session, data: MonitorCreate) -> Monitor:
    monitor = Monitor(
        name=data.name,
        url=str(data.url),
        interval_seconds=data.interval_seconds,
        is_active=data.is_active,
    )

    db.add(monitor)
    db.commit()
    db.refresh(monitor)

    return monitor