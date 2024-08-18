from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging

# from core.config import CoreConfig

from endpoints.user import router as user_router


logging.basicConfig(filename='daisyAPI.log', level=logging.INFO)

app = FastAPI()

origins = [
    "http://locahost",
    "http://locahost:8080", 
]

app.include_router(user_router, prefix='/user')

app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )



