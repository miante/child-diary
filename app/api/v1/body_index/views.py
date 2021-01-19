from fastapi import APIRouter, Depends, Request, HTTPException, Response
from starlette import status

from app.api.auth.shortcuts import is_authenticated
from app.api.v1.body_index.serializers import (
    BodyIndexInput,
    BodyIndexUpdateInput,
    BodyIndexOutput,
    ChildBodyIndexesSerializer,
)
from app.db.engine import Session, get_session
from app.db.models import BodyIndex, Child

router = APIRouter()


@router.get(
    '/body-index/{child_id}/list',
    dependencies=[Depends(is_authenticated)],
    response_model=ChildBodyIndexesSerializer,
)
def get_body_indexes(
    child_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Returns the list of children body indexes created by a session user
    """

    query = session.query(BodyIndex) \
        .join(Child) \
        .filter(
            Child.id == child_id,
            Child.user_id == request.user.id,
        )
    response = ChildBodyIndexesSerializer(body_indexes=query.all())

    return response


@router.post(
    '/body-index/create',
    dependencies=[Depends(is_authenticated)],
    response_model=BodyIndexOutput,
    status_code=status.HTTP_201_CREATED,
)
def create_body_index(
    body_index: BodyIndexInput,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Create a child body index status
    """

    child = session.query(Child) \
        .filter(
            Child.id == body_index.child_id,
            Child.user_id == request.user.id,
        ) \
        .scalar()
    if not child:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    model = BodyIndex(**body_index.dict())

    session.add(model)
    session.commit()
    session.refresh(model)

    response = BodyIndexOutput(**model.__dict__)

    return response


@router.put(
    '/body-index/{body_index_id}/update',
    dependencies=[Depends(is_authenticated)],
    response_model=BodyIndexOutput,
)
def update_body_index(
    body_index: BodyIndexUpdateInput,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Updates the body index of known child
    """

    model = session.query(BodyIndex) \
        .join(Child) \
        .filter(
            BodyIndex.id == body_index.id,
            Child.user_id == request.user.id,
        ) \
        .scalar()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for k, v in body_index.dict().items():
        setattr(model, k, v)

    response = BodyIndexOutput(**model.__dict__)
    session.commit()

    return response


@router.delete(
    '/body-index/{body_index_id}/child/{child_id}/delete',
    dependencies=[Depends(is_authenticated)],
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_body_index(
    body_index_id: int,
    child_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Deletes a body index from child
    """

    is_deleted = session.query(BodyIndex) \
        .filter(
            BodyIndex.id == body_index_id,
            Child.id == child_id,
            Child.user_id == request.user.id,
        ) \
        .delete(synchronize_session=False)
    session.commit()

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
