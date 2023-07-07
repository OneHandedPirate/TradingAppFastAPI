from fastapi import Request, status
from fastapi.exceptions import HTTPException


class Guard:
    def __init__(self, name: str, requested_cookie):
        self.name = name
        self.requested_cookie = requested_cookie

    def __call__(self, request: Request):
        if self.requested_cookie not in request.cookies:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return True


operations_guard = Guard("operations", requested_cookie="operations_cookie")




