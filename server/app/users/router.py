from fastapi import APIRouter, Depends, Response
import json
from app.users.dependencies import get_current_user, is_admin_user
from app.users.models import Users
from app.exceptions import *
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dao import UsersDAO
from app.users.schemas import SUser, SUserAuth, SUserBase, SUserBaseId, SUserDB, SUserLogin


# from fastapi import APIRouter, Depends, Response
# import json
# from users.dependencies import get_current_user, is_admin_user
# from users.models import Users
# from exceptions import *
# from users.auth import authenticate_user, create_access_token, get_password_hash
# from users.dao import UsersDAO
# from users.schemas import SUserAuth, SUserBase, SUserDB, SUserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],    
)

@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    existing_user = SUserDB(**user_data.model_dump(), hashed_password=hashed_password).model_dump()
    existing_user = await UsersDAO.add(**existing_user)
    return {'status': 200, 'detail': 'Пользователь успешно зарегистрирован'}

@router.post('/login')
async def login_user(user_data: SUserLogin, response: Response):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({'sub': str(user.id)})
    # response.set_cookie("app_access_token", access_token, httponly=True, max_age=3600, samesite=None, secure=True)
    response.set_cookie("app_access_token", access_token)
    return {'access_token': access_token}

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie("app_access_token")
    return {'status': 200, 'detail': 'ОК'}


@router.get('/me', response_model=SUserBase)
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

@router.get('/all_users', response_model=list[SUserBaseId], dependencies=[Depends(is_admin_user)])
async def get_all_users():
    # filter = {'role': 'admin'}
    # users = await UsersDAO.find_all(**filter)
    users = await UsersDAO.find_all()
    return users

@router.delete('/delete_user/{user_id}', dependencies=[Depends(is_admin_user)])
async def delete_user(user_id: int):
    return await UsersDAO.delete_by_id(user_id)


@router.patch('/change_user/{user_id}', dependencies=[Depends(is_admin_user)])
async def change_user(user_id: int, corrected_user: SUser):
    await UsersDAO.change_by_id(user_id, **corrected_user.model_dump())
    return {'status': 200, 'detail': 'Данные пользователя изменены'}