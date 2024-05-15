import os
import sys



sys.path.insert(1, os.path.join(sys.path[0], '..')) # решение проблемы import

from fastapi import FastAPI
from app.users.router import router as router_users
from app.devices.router import router as router_device
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from app.database import engine
from app.admin.views import *
from app.admin.auth import authentication_backend

app = FastAPI()
admin = Admin(app, engine=engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)

admin.add_view(DeviceAdmin)
admin.add_view(ValueDeviceAdmin)
admin.add_view(ManagementLogAdmin)
admin.add_view(AccidentLogAdmin)

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




