import configuration
import requests
import data 

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREAT_ORDERS_PATH, json=body, headers=data.headers)

# Функция получения сведений о заказе
def get_order(order_track):
    params = {"t": str(order_track)}  # Формируем параметры запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH, 
                        params=params)