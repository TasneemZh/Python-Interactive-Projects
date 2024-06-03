# Quotes and Time Project

Welcome to the Celebrity Quotes and ISS Notification Project! This project is divided into two parts: a GUI for displaying celebrity quotes and an email notification system for alerting users when the International Space Station (ISS) is overhead at night.

## Project Overview

### Part 1: Celebrity Quotes GUI

This part of the project provides a graphical user interface that displays celebrity quotes. When the user clicks on a celebrity's head, which acts as a clickable button, a new quote is fetched from a public API and displayed.

### Part 2: ISS Overhead Email Notification

This part of the project sends an email to the user when the ISS is above their location at night. It checks the ISS's current position against the user's location. If the ISS is overhead, and it is nighttime at the user's location, an email is sent.

## Key Features

- Interactive GUI: Displays quotes from a celebrity when their head is clicked.

- Real-time Data: Fetches real-time quotes and ISS position using public APIs.

- Email Notification: Notifies the user via email when the ISS is overhead at night.

- API Integration: Integrates multiple public APIs for quotes, ISS position, and sunrise/sunset times.

## How to Use

1. Clone this repository to your local machine.

2. Prepare your email credentials including an app password.

3. To run the Celebrity Quotes GUI:

    ```bash
    python celebrity_quotes.py
    ```

4. To run the ISS Overhead Email Notification:

    ```bash
    python night_moment.py
    ```

## *Enjoy the APIs!*