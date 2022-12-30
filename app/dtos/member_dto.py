from enum import Enum

from app.dtos.base import BaseDTO


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Role(Enum):
    MEMBER = "MEMBER"
    ADMIN = "ADMIN"


class State(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    BANNED = "BANNED"


class CreateUpdateMemberDTO(BaseDTO):
    name: str
    nick_name: str
    age: int
    gender: Gender
    attendance_count_current_month: int = 0
    attendance_count_total: int = 0
    role: Role = "MEMBER"
    state: State = "ACTIVE"


class MemberDTO(CreateUpdateMemberDTO):
    id: int
