# Полянскова Юлия, 40-я когорта - Финальный проект. Инженер по тестированию
import sender_stand_request
import data

# Функция проверки статус кода заказа
def status_assert(order_track, code):
    track_response=sender_stand_request.get_order(order_track)
    assert track_response.status_code == code, f"Ожидался статус код {code}, получен {track_response.status_code}\n"

# Тест на проверку статус кода 200
def test_code_200_in_respons():
    order_response=sender_stand_request.post_new_order(data.order_body)
    order_track=order_response.json().get('track')

    status_assert(order_track, 200)