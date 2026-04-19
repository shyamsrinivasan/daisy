from typing import Generic, Optional, TypeVar, List
from pydantic import BaseModel, Field, AnyHttpUrl


M = TypeVar('M')

class PaginatedResponse(BaseModel, Generic[M]):
    count: int = Field(description='Total number of items returned in response')
    items: List[M] = Field(description='List of items in response mapped to parameter of Type M')
    next_page: Optional[AnyHttpUrl] = Field(None, description='next page url, if available')
    previous_page: Optional[AnyHttpUrl] = Field(None, description='previous pgae url, if availabel')


    
