import requests
from system import exit_if_error


def handle_user_access():
    user_answer = input("Do you have a user? [yes/no] \n").lower()
    username = input("Enter your username: ")
    token = input("Enter your token: ")
    user_data = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    if user_answer == "no":
        new_user_endpoint = "https://pixe.la/v1/users"
        new_user_response = requests.post(url=new_user_endpoint, json=user_data)
        exit_if_error(new_user_response)

    return user_data
