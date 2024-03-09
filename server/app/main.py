from fastapi import FastAPI



from app.users.router import router as router_users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)

origins = [
    "https://localhost",
    "https://localhost:5173",
    "http://localhost",
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                    "Access-Control-Allow-Origin", "Authorization", "Access-Control-Allow-Credentials",
                    ],
)



app.include_router(router_users)




