from fastapi import Query
from sqlalchemy import Select
from sqlmodel import Session
from sqlmodel import select, func
from typing import Dict, Optional

from .middleware import request_object


class PaginatedParams:
    def __init__(self, page: int = Query(1, ge=1), 
                per_page: int = Query(100, ge=0)):
        self.limit = per_page * page
        self.offset = (page - 1) * per_page



async def paginate(query: Select, limit: int, offset: int, db: Session) -> Dict:
    return {
        'count': db.scalar(select(func.count()).select_from(query.subquery())),
        'items': db.scalars(query.limit(limit).offset(offset))
    }


class Paginator:
    def __init__(self, db: Session, query: Select, page: int, per_page: int):
        self.db = db
        self.query = query
        self.page = page
        self.per_page = per_page
        self.request = request_object
        self.number_of_pages = 0
        self.next_page = None
        self.previous_page = None

    def _get_next_page(self) -> Optional[str]:
        if self.page >= self.number_of_pages:
            return
        url = self.request.url.include_query_params(page=self.page + 1)
        return str(url)
    
    def _get_previous_page(self) -> Optional[str]:
        if self.page == 1 or self.page > self.number_of_pages + 1:
            return
        url = self.request.url.include_query_params(page=self.page - 1)
        return str(url)
    
    async def get_response(self) -> dict:
        return {
            'count': await self._get_total_count(),
            'next_page': self._get_next_page(),
            'previous_page': self._get_previous_page(),
            'items': [todo for todo in await self.db.scalars(self.query.limit(self.limit).offset(self.offset))]
        }
    
    def _get_number_of_pages(self, count: int) -> int:
        rest = count % self.per_page
        quotient = count // self.per_page
        return quotient if not rest else quotient + 1

    async def _get_total_count(self) -> int:
        count = await self.db.scalar(select(func.count()).select_from(self.query.subquery()))
        self.number_of_pages = self._get_number_of_pages(count)
        return count

    