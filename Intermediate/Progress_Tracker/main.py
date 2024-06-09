import requests
from datetime import datetime
from progress import collect_user_progress
from user import handle_user_access
from graph import handle_graph_setup
from system import exit_if_error

user_data = handle_user_access()

headers = {
    "X-USER-TOKEN": user_data["token"]
}

graph_data = handle_graph_setup(user_data, headers)

current_date = datetime.now()
formatted_date = current_date.strftime('%Y%m%d')

data = collect_user_progress()

new_pixel_endpoint = f"https://pixe.la/v1/users/{user_data["username"]}/graphs/{graph_data["id"]}"
new_pixel = {
    "date": formatted_date,
    "quantity": data
}
new_pixel_response = requests.post(url=new_pixel_endpoint, json=new_pixel, headers=headers)
exit_if_error(new_pixel_response)

end_loop = False
while not end_loop:
    confirmation = input("Are you sure of your today's progress? [yes/no] \n").lower()
    if confirmation == "yes":
        end_loop = True
    else:
        end_loop = False
        data = collect_user_progress()
        edited_pixel_endpoint = f"https://pixe.la/v1/users/{user_data["username"]}/graphs/{graph_data["id"]}/{formatted_date}"
        edited_pixel = {
            "quantity": data
        }
        edited_pixel_response = requests.put(url=edited_pixel_endpoint, json=edited_pixel, headers=headers)
        exit_if_error(edited_pixel_response)

if input("Do you want to delete today's progress? [yes/no] \n").lower() == "yes":
    deleted_pixel_endpoint = f"https://pixe.la/v1/users/{user_data["username"]}/graphs/{graph_data["id"]}/{
        formatted_date
    }"
    deleted_pixel_response = requests.delete(url=deleted_pixel_endpoint, headers=headers)
    exit_if_error(deleted_pixel_response)
