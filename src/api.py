from fastapi.routing import APIRouter

from src.democratic import STRATAGEM_LIST

api = APIRouter()


@api.get("/stratagems")
def _():
    return {
        "status": "ok",
        "data": STRATAGEM_LIST,
    }


@api.get("/call/{_id}")
def _(_id: str):
    for stratagem in STRATAGEM_LIST:
        if stratagem.id == _id:
            stratagem.call()
            return {"status": "ok"}
    return {"status": "error", "msg": "stratagem not found"}


@api.get("/check")
def _():
    return {"status": "ok"}
