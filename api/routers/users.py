from fastapi import APIRouter


router = APIRouter()

dict_user = {
    "1":"user 1",
    "2":"user 2"
}


@router.get("/users/",tags=["users"])
async def get_user():
    return dict_user


