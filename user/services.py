from typing import Dict, Any
from django.contrib.auth.models import User


def create_user(data: Dict[str, Any]):
    password = data.pop('password')
    user = User(**data)
    user.set_password(password)
    user.save()

    return user


def update_user(obj, data):
    user = User.objects.get(data['id'])
    if 'password' in data:
        password = data.pop('password')
        user.set_password(password)

    User.objects.filter(id=user.id).update(**data)
    obj.user = user.id

    return obj
