import requests
from system import exit_if_error


def handle_graph_setup(user_data, headers):
    user_answer = input("Do you have a graph? [yes/no] \n").lower()
    graph_id = input("Enter your graph ID: ")
    name = input("Enter your graph name: ")
    graph_data = {
        "id": graph_id,
        "name": name,
        "unit": "commit",
        "type": "int",
        "color": "shibafu"
    }
    if user_answer == "no":
        new_graph_endpoint = f"https://pixe.la/v1/users/{user_data["username"]}/graphs"
        new_graph_response = requests.post(url=new_graph_endpoint, json=graph_data, headers=headers)
        exit_if_error(new_graph_response)

    return graph_data
