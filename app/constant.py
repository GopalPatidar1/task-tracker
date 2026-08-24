COMMAND={
    'ADD': 'add',
    'DELETE': 'delete',
    'LIST': 'list',
    'UPDATE': 'update',
    'MARK_IN_PROGRESS': 'mark-in-progress',
    'MARK_DONE': 'mark-done'
}

FILENAME ="task.json"


RESULT = {
    "NO_ARGUMENTS": lambda: "No arguments passed",
    "TASK_ADDED": lambda task_id: f"Task added successfully (ID: {task_id})",
    "TASK_DELETED": lambda task_id: f"Task deleted successfully (ID: {task_id})",
    "TASK_UPDATED": lambda task_id: f"Task updated successfully (ID: {task_id})",
}