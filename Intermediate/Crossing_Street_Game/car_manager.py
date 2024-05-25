from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
HEIGHT = 20
WIDTH = 60


class CarManager:
    def __init__(self):
        self.cars = []
        self.current_speed = 0

    def create_random_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(1, 3)
        car.color(random.choice(COLORS))
        starting_pos = random.choice(range(-240, 260, 30))
        car.goto(300, starting_pos)
        car.setheading(180)
        self.cars.append(car)
        if 0 < self.current_speed <= 10:
            car.speed(self.current_speed)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
        if len(self.cars) and self.cars[0].xcor() < (-300 - WIDTH):
            self.cars = self.cars[1:]

    def check_collision(self, player):
        for car in self.cars:
            if player.distance(car) <= 30:
                return False
        return True

    def speed_up(self):
        self.current_speed += 3
        print(f"current_speed: {self.current_speed}")
        for car in self.cars:
            car.speed(self.current_speed)
