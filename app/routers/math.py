from fastapi import APIRouter
from pydantic import BaseModel

from ..utils.numbers import average, sum

router = APIRouter(
    prefix="/math",
    tags=["math"],
    responses={404: {"description": "Not found"}},
)


class SumResponseModel(BaseModel):
    sum: int


class AverageResponseModel(BaseModel):
    average: float


@router.post(
    "/sum",
    response_model=SumResponseModel,
)
async def sum_numbers(numbers: list[int]):
    return {"sum": sum(numbers)}


@router.post(
    "/average",
    response_model=AverageResponseModel,
)
async def average_numbers(numbers: list[int]):
    return {"average": average(numbers)}
