

from app.api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()


def test_add_new_pet_with_negative_name(name='00000', animal_type='Котя',
                                        age='5', pet_photo='images/Caty.jpg'):
    """Проверяем что можно добавить питомца с некорректным именем"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 400
    assert result['name'] == name


def test_add_new_pet_with_negative_animal_type(name='Теюша', animal_type='22222',
                                               age='5', pet_photo='images/Caty.jpg'):
    """Проверяем что можно добавить питомца с некорректным animal_type"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 400
    assert result['animal_type'] == animal_type


def test_add_new_pet_with_negative_age(name='Теюша', animal_type='Котя',
                                       age='-10', pet_photo='images/Caty.jpg'):
    """Проверяем что можно добавить питомца с отрицательным возрастом"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 400
    assert result['age'] == age
