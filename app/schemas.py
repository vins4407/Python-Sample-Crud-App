from datetime import datetime
from typing import List
from pydantic import BaseModel
from bson.objectid import ObjectId


class NoteBaseSchema(BaseModel):
    id: str | None = None
    title: str
    note: str
    category: str = ""
    description: str = ""
    published: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateNoteSchema(BaseModel):
    title: str | None = None
    note: str | None = None
    category: str | None = None
    description: str  | None = None
    published: bool | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class NoteResponse(BaseModel):
    status: str
    note: NoteBaseSchema


class ListNoteResponse(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]
