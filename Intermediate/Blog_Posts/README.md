# Blog Posts

## Overview

This project is a Flask-based web application that uses a Bootstrap template to create a blog website.

## Features

### Homepage
- Route: /
- Description: This route fetches and displays a list of blog posts. The homepage uses the index.html template and presents the blog posts in a visually appealing layout.

### Blog Post Details
- Route: /posts/<int:post_id>
- Description: This route displays the details of a specific blog post identified by its post_id. The blog-details.html template is used to show the content of the selected blog post.

### Contact Information
- Route: /contacts
- Description: This route displays the contact information page. The contact.html template is used to present the contact details.

### About Us Page
- Route: /about_us 
- Description: This route displays the about us page. The about.html template provides random information about the website.

## Setup

1. Install Flask using pip if it is not already installed:
    ```bash
    pip install Flask
    ```
2. Clone this repository to your local machine.

3. Use the command line to navigate to the project directory.

4. Execute the following command to start the Flask application:
    ```bash
    python server.py
    ```
5. Open your web browser and navigate to http://127.0.0.1:5000/ to view the homepage. You can navigate to different pages using the URLs provided for each route.

## License

This project is licensed under the MIT License.

## *Enjoy The Blogs* 📖 *!*