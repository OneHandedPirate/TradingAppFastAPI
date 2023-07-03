from fastapi import FastAPI, Request, status
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title='Trading App'
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    """Validation handler to show user internal server errors"""

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )
