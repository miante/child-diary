from fastapi import APIRouter, Depends, Request, HTTPException, Response
from starlette import status

from app.api.auth.shortcuts import is_authenticated
from app.api.v1.child.serializers import (
    ChildInput,
    ChildOutput,
    ChildrenSerializer,
)
from app.db.engine import Session, get_session
from app.db.models import Child

router = APIRouter()


@router.get(
    '/child/list',
    dependencies=[Depends(is_authenticated)],
    response_model=ChildrenSerializer,
)
def get_user_children(
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Returns the list of children created by a session user
    """

    query = session.query(Child).filter(Child.user_id == request.user.id)
    response = ChildrenSerializer(children=query.all())

    return response


@router.post(
    '/child/create',
    dependencies=[Depends(is_authenticated)],
    status_code=status.HTTP_201_CREATED,
)
def create_user_child(
    child: ChildInput,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Create a child for the user in session
    """

    model = Child(**child.dict())
    model.user_id = request.user.id

    session.add(model)
    session.commit()
    session.refresh(model)

    response = ChildOutput(**model.__dict__)

    return response


@router.delete(
    '/child/{child_id}/delete',
    dependencies=[Depends(is_authenticated)],
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_child(
    child_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Deletes a child from database
    """

    is_deleted = session.query(Child) \
        .filter(Child.id == child_id, Child.user_id == request.user.id) \
        .delete()
    session.commit()

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
