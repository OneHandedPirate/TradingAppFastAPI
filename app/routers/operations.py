from typing import Any
from time import sleep

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.schemas import OperationResponse, OperationCreate
from fastapi_cache.decorator import cache

from app.database import models
from app.dependencies import operations_guard

router = APIRouter(
    prefix='/operations',
    tags=['operations'],
    dependencies=[Depends(operations_guard)]
)


@router.get("/long_operation")
@cache(expire=60)
def get_long_operation():
    sleep(5)
    return "Много данных"


@router.get('')
async def get_specific_operations(operation_type: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(models.operation).filter(models.operation.c.type == operation_type)
        result = await db.execute(query)
        print(result)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except ZeroDivisionError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail={
                                "status": "error",
                                "data": None,
                                "detail": "Zero Division is unacceptable!"
                            })
    except Exception:
        return {
            "status": "error",
            "data": None,
            "detail": None
        }


@router.post('')
async def create_operations(new_operation: OperationCreate, db: AsyncSession = Depends(get_db)):
    stmt = insert(models.operation).values(**new_operation.dict())
    await db.execute(stmt)
    await db.commit()
    return {"status": "success"}

