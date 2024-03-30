import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..')) # решение проблемы import

from fastapi import FastAPI
from app.users.router import router as router_users
from app.devices.router import router as router_device
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router_users)
app.include_router(router_device)




