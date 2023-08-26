from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    # if the title is sent from the frontend, create a slug out of it
    def generate_slug(cls, values):
        if 'title' in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
