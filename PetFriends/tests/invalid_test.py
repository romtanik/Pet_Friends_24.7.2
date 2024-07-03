

from app.api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password


pf = PetFriends()


def test_get_api_key_for_invalid_email_user(email=invalid_email, password=valid_password):
    """Проверяем что при невалидном значении email запрос api ключа возвращает статус 403"""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_password_user(email=valid_email, password=invalid_password):
    """Проверяем что при невалидном значении password запрос api ключа возвращает статус 403"""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_full_invalid_setting(email=invalid_email, password=invalid_password):
    """Проверяем что при невалидных значениях и email и password запрос api ключа возвращает статус 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
