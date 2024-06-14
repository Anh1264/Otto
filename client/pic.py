import requests
import sys
sys.path.append('..')
from picture.service import save_base64_image, image_to_base64

image_path = 'image/headphones.jpg'
base64_string = image_to_base64(image_path)

def create_picture():
    endpoint = 'http://127.0.0.1:8000/picture/create/'
    data = {
    # 'robot': Robot.objects.get(id=1),
    # 'session_seconds': "5",
    'robot_id': 1,
    'file_name': "230000x4000x2020-12-11_10-45-30xON.jpg",
    'file_data': base64_string,
    }
    get_response = requests.post(endpoint,json=data)
    print(get_response.json())

# def get_robot_list():
#     endpoint = 'http://127.0.0.1:8000/robot/'
#     get_response = requests.get(endpoint)
#     print(get_response.json())

# def get_robot_detail():
#     pk = int(input("Enter lookup id: "))
#     endpoint = f'http://127.0.0.1:8000/robot/{pk}/'
#     get_response = requests.get(endpoint)
#     print(get_response.json())

# def update_robot():
#     pk = int(input("Enter lookup id: "))
#     endpoint = f'http://127.0.0.1:8000/robot/{pk}/update/'
#     data = {
#         'status': True,
#     }

#     get_response = requests.put(endpoint, json=data)
#     print(get_response.json())

# def destroy_robot():
#     pk = int(input("Enter lookup id: "))
#     endpoint = f'http://127.0.0.1:8000/robot/{pk}/destroy/'
#     get_response = requests.delete(endpoint)
#     print(get_response)

create_picture()
# get_robot_list()
# get_robot_detail()
# update_robot()
# destroy_robot()