def collect_user_progress():
    if input("Have you completed the progress for today? [yes/no] \n").lower() == "yes":
        data = "1"
    else:
        data = "0"
    return data
