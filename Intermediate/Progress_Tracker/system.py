import sys


def exit_if_error(response):
    print(f"➡️ {response.json()["message"]}")
    if not response.json()["isSuccess"]:
        sys.exit(1)
