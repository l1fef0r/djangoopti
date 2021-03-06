from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile
from geekshop import settings


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = f'https://api.vk.com/method/users.get/?fields=bdate,sex,photo_max_orig,about&access_token={response["access_token"]}&v=5.92'

    response = requests.get(api_url)

    if response.status_code != 200:
        return

    data = response.json()['response'][0]
    if 'sex' in data:
        if data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        elif data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE

    if 'photo_max_orig' in data:
        photo = requests.get(data['photo_max_orig'])
        with open(f'{settings.MEDIA_ROOT}/users_avatars/{user.id}.jpg', 'wb') as photo_wb:
            photo_wb.write(photo.content)
            user.avatar = f'users_avatars/{user.pk}.jpg'

    if 'about' in data:
        if data['about']:
            user.shopuserprofile.about_me = data['about']

    if 'bdate' in data:
        if data['bdate']:
            bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

            age = timezone.now().date().year - bdate.year
            if age < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.save()