# Task Manager System

This program is a task manager system for a small business to help manage tasks assigned to members of the team. It uses two text files, `user.txt` and `tasks.txt`, to store user credentials and task details, respectively.

## Features

- User Registration (Admin User only): Allows the Admin user to register a new account by providing a username and password. The credentials are stored in the `user.txt` file.

- Display Statistics (Admin User only): Allows the Admin user to display the number of registered users and tasks recorded in the text files.

- Add Task: Enables users to add a new task and assign it to a specific team member by selecting their username. The task details are stored in the `tasks.txt` file.

- View All Tasks: Displays all the tasks recorded in the `tasks.txt` file, including the username of the assignee and the task description.

- View My Tasks: Shows only the tasks assigned to the currently logged-in user.

## File Structure

- `task_manager.py`: The main Python script that implements the task manager system.
- `user.txt`: A text file to store user credentials (username and password).
- `tasks.txt`: A text file to store task details (assigned username and task description).
