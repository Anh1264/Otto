from django.shortcuts import render
import requests
# Create your views here.
def homePage(request):
    return render(request, 'main/home.html')

def ottosPage(request):
    endpoint = 'http://127.0.0.1:8000/robot/'
    get_response = requests.get(endpoint)
    robots = get_response.json()


    context = {'robots': robots}
    return render(request, 'main/ottos.html', context)

def activityListPage(request,robot_id):
    # get robot's activities
    endpoint = f'http://127.0.0.1:8000/activity/robot_activities/{robot_id}/'
    get_response = requests.get(endpoint)
    robot_activities = get_response.json()
    # get robot

    endpoint = f'http://127.0.0.1:8000/robot/{robot_id}/'
    get_response = requests.get(endpoint)
    robot = get_response.json()
    print(robot)

    context = {'robot_activities': robot_activities, 'robot': robot}
    return render(request, 'main/activityList.html', context)