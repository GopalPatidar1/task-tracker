# task-tracker
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

## Run the application

From the project root:

    python -m app.task_cli list

## Examples

Add a task:

    python -m app.task_cli add "Buy groceries"

List tasks:

    python -m app.task_cli list

Update a task:

    python -m app.task_cli update 1 "Buy groceries and cook dinner"

Delete a task:

    python -m app.task_cli delete 1

Mark task as in progress:

    python -m app.task_cli mark-in-progress 1

Mark task as done:

    python -m app.task_cli mark-done 1

## Run tests

    python -m pytest