from typing import Optional
from sqlmodel import SQLModel, Field

class Link(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    course: str = Field(nullable=False)
    url: str = Field(nullable=False)
