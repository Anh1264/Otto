import requests

def create_robot():
    endpoint = 'http://127.0.0.1:8000/robot/create/'
    data = {
    # 'robot': Robot.objects.get(id=1),
    # 'session_seconds': "5",
    'name': "Test6",
    'type': "Prototype",
    'location': 'B1F6',
    }
    get_response = requests.post(endpoint,json=data)
    print(get_response.json())

def get_robot_list():
    endpoint = 'http://127.0.0.1:8000/robot/'
    get_response = requests.get(endpoint)
    print(get_response.json())

def get_robot_detail():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/robot/{pk}/'
    get_response = requests.get(endpoint)
    print(get_response.json())

def update_robot():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/robot/{pk}/update/'
    data = {
        'status': True,
    }

    get_response = requests.put(endpoint, json=data)
    print(get_response.json())

def destroy_robot():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/robot/{pk}/destroy/'
    get_response = requests.delete(endpoint)
    print(get_response)

create_robot()
# get_robot_list()
# get_robot_detail()
# update_robot()
# destroy_robot()