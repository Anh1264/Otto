import requests

def create_activity():
    endpoint = 'http://127.0.0.1:8000/activity/create/'
    data = {
    'robot_id': 1,
    'session_seconds': "5",
    'off_time': "2023-11-01_05-55-11",
    # 'off_time': "2023-11-01_05-59-11",
    'scans': 2,
    'wifi': 4,
    'cam': 5,
    }
    get_response = requests.post(endpoint,json=data)
    print(get_response.json())

def get_activity_list():
    endpoint = 'http://127.0.0.1:8000/activity/'
    get_response = requests.get(endpoint)
    print(get_response.json())

def get_activity_detail():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/activity/{pk}/'
    get_response = requests.get(endpoint)
    print(get_response.json())

def get_robot_activities():
    robot_id = int(input("Enter lookup robot_id: "))
    endpoint = f'http://127.0.0.1:8000/activity/robot_activities/{robot_id}/'
    get_response = requests.get(endpoint)
    print(get_response.json())

def update_activity():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/activity/{pk}/update/'
    data = {
        'camera': "11",
    }

    get_response = requests.put(endpoint, json=data)
    print(get_response.json())

def destroy_activity():
    pk = int(input("Enter lookup id: "))
    endpoint = f'http://127.0.0.1:8000/activity/{pk}/destroy/'
    get_response = requests.delete(endpoint)
    print(get_response)

create_activity()
# get_activity_list()
# get_activity_detail()
# update_activity()
# destroy_activity()
# get_robot_activities()