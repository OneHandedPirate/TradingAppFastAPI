from httpx import AsyncClient


async def test_add_operation(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "quantity": "quantity",
        "figi": "figi",
        "instrument_type": "instrument",
        "type": "type"
    })
    assert response.status_code == 200
