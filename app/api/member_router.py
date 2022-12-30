from http import HTTPStatus
from typing import List, Union

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.dtos.member_dto import CreateUpdateMemberDTO, MemberDTO
from app.fixtures.member_dto_fixtures import members

member_router = APIRouter()


def find_member_by_id(id: int) -> Union[MemberDTO, None]:
    for member in members:
        if member.id == id:
            return member
    return None


@member_router.get("/", response_model=List[MemberDTO])
async def get_members():
    return members


@member_router.get("/{id}", response_model=MemberDTO)
async def get_member_by_id(id: int):
    target_member = find_member_by_id(id)
    if target_member is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return target_member


@member_router.post("/", response_model=MemberDTO)
async def create_member(member: CreateUpdateMemberDTO):
    new_member = MemberDTO(
        id=3,
        name=member.name,
        nick_name=member.nick_name,
        age=member.age,
        gender=member.gender,
        attendance_count_current_month=member.attendance_count_current_month,
        attendance_count_total=member.attendance_count_total,
        role=member.role,
        state=member.state,
    )

    return JSONResponse(status_code=HTTPStatus.CREATED, content=new_member)


@member_router.patch("/{id}", response_model=MemberDTO)
async def update_member(id: int, member: CreateUpdateMemberDTO):
    target_member = find_member_by_id(id)
    if target_member is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return MemberDTO(
        id=target_member.id,
        name=member.name,
        nick_name=member.nick_name,
        age=member.age,
        gender=member.gender,
        attendance_count_current_month=member.attendance_count_current_month,
        attendance_count_total=member.attendance_count_total,
        role=member.role,
        state=member.state,
    )


@member_router.delete("/{id}", response_model=MemberDTO)
async def remove_member(id: int):
    target_member = find_member_by_id(id)
    if target_member is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return target_member
