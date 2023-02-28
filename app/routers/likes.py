from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session




router = APIRouter(
    prefix="/like",
    tags=["Like"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.Like, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.POS_ID == like.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID: {like.post_id} does not exist")

    like_query = db.query(models.Likes).filter(models.Likes.LIK_POS_ID == like.post_id, models.Likes.LIK_USU_ID == current_user.USU_ID)
    found_like = like_query.first()

    if (like.dir == 1):
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.USU_ID} has already liked the post {like.post_id}")
        
        new_like = models.Likes(LIK_POS_ID = like.post_id, LIK_USU_ID=current_user.USU_ID)
        db.add(new_like)
        db.commit()
        return {"message": "Like added!"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Like doesnt exist")

        like_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Like deleted!"}