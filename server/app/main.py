# from fastapi import FastAPI
# from users.router import router as router_users
# from fastapi.middleware.cors import CORSMiddleware

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..')) # решение проблемы import

from fastapi import FastAPI
from app.users.router import router as router_users
from fastapi.middleware.cors import CORSMiddleware



# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)

# origins = [
#     "https://localhost",
#     "http://localhost",
#     "https://localhost:5173",
#     "http://localhost:5173",
#     "https://localhost:7777",
#     "http://localhost:7777"
#     "https://localhost:5173",
#     "http://localhost:5173",
#     "https://localhost:9000",
#     "http://localhost:9000"
#     "https://127.0.0.1",
#     "http://127.0.0.1",
#     "https://127.0.0.1:5173",
#     "http://127.0.0.1:5173",
#     "https://127.0.0.1:7777",
#     "http://127.0.0.1:7777"
#     "https://127.0.0.1:5173",
#     "http://127.0.0.1:5173",
#     "https://127.0.0.1:9000",
#     "http://127.0.0.1:9000",
# ]

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
#                     "Access-Control-Allow-Origin", "Authorization", "Access-Control-Allow-Credentials",
#                     ],
# )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
#                     "Access-Control-Allow-Origin", "Authorization", "Access-Control-Allow-Credentials"],
# )




app.include_router(router_users)




