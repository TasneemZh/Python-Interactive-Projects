from nutritionix import get_user_workouts
from sheety import create_workout_record

exercises = get_user_workouts()

for exercise in exercises:
    create_workout_record(exercise["name"], exercise["duration_min"], exercise["nf_calories"])
