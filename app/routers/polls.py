from fastapi import APIRouter

router = APIRouter(
    prefix="/polls",
    tags=["polls"]
)

#temporary db
polls = []

@router.get("/")
def get_polls():
    return {"polls": polls,
            "polls": ["poll 1", "poll 2"]
            }

@router.post("/")
def create_polls(poll: dict):
    polls.append(poll)
    return {"message": "poll created successfully", "poll": poll}