"""
    This file contains all the Database configurations
"""
from sqlmodel import SQLModel, select, create_engine, Session, Field
from models import Link
from typing import List

class Database:
    def __init__(self) -> None:
        self.uri = "sqlite:///backend/data/data.db"
        self.engine = create_engine(self.uri)

    @property
    def session(self) -> Session:
        return Session(self.engine)
    
    def add_link(self, link: Link):
        with self.session as session:
            session.add(link)
            session.commit()
            session.refresh(link)
            return link.id
        
    def fetch_links(self, course=None) -> List[Link]:
        with self.session as session:
            if course:
                return session.exec(select(Link).where(Link.course == course)).all()
            return session.exec(select(Link)).all()
        
    def fetch_courses(self) -> List[str]:
        with self.session as session:
            courses = []
            links = session.exec(select(Link)).all()
            for link in links:
                if link.course not in courses:
                    courses.append(link.course)
            return courses
            

if __name__ == "__main__":
    SQLModel.metadata.create_all(Database().engine)
