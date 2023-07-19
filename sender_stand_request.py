import requests
import configuration
import data

# Силакова Елена. 6 когорта - финальный проект. инженер по тестированию плюс
def post_new_order(body): # POST запрос на создание нового заказа
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_info_orders(track): # GET запрос на заказ по треку
    return requests.get(configuration.URL + configuration.CREATE_ORDER_PATH + "/track?t="+track,
                         headers=data.headers)

response = post_new_order(data.user_body)

assert response.status_code == 201

order_track = response.text.split(":")[1].split("}")[0]
response_track = get_info_orders(order_track)

assert response_track.status_code == 200

print('code: 200')
print(response_track.text)
