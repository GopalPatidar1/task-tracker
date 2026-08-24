import sys
from constant import COMMAND
from operation import op
from customException import CustomException


def guide():
    print(
        """
    Adding a new task
       add "Buy groceries"
       Output: Task added successfully (ID: 1)
     
    Updating and deleting tasks
      update 1 "Buy groceries and cook dinner"

    Updating and deleting tasks
      delete 1
      
    Marking a task as in progress or done
      mark-in-progress 1
      mark-done 1
      
    Listing all tasks
      list
      
    Listing tasks by status
      list done
      list todo
      list inprogress
    """
    )



def main():
    arguments = sys.argv[1:]  # remove the first because it contain file name

    if not arguments:
      guide()
      return

    command = arguments[0]
    if command ==COMMAND["ADD"]:
        if len(arguments) != 2:
           raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.")
           
    
        desc = arguments[1].strip()
    
        if not desc:
            raise CustomException("task desc can't be empty")
    
        getTaskId = op.getTaskId()
    
        op.addTask({"desc":desc, "id":getTaskId, "status": "todo"})
        return f"Task added successfully (ID: {getTaskId})"
    
    elif command == COMMAND["LIST"]:
         listOfTask = op.getListOfTask()
         status = arguments[1] if len(arguments) > 1 else None
         taskText = ""
         for item in listOfTask:
             if status and status !=item["status"]:
               continue
             taskText += "id: " + str(item["id"]) + " desc: " + item["desc"] + " status: " + item.get("status") + "\n"
         return taskText
    
    elif command == COMMAND["DELETE"]:
         if len(arguments) != 2:
                raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.")
     
         id = arguments[1]
     
         if not id:
             raise CustomException("task id can't be empty")
     
         op.deleteTask(id)

         return f"Task deleted successfully (ID: {id})"

    elif command == COMMAND['UPDATE']:
         if len(arguments) != 3:
             raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.")
     
         id = arguments[1]
         if not id:
             raise CustomException("task id can't be empty")
     
         desc = arguments[2].strip()
         if not desc:
             raise CustomException("task desc can't be empty")
     
         op.updateTask(id, desc)

         return f"Task updated successfully (ID: {id})"

    elif command == COMMAND["MARK_IN_PROGRESS"]:
         if len(arguments) != 2:
               raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.")
             
         id = arguments[1]
         if not id:
            raise CustomException("task id can't be empty")
   
         op.markInProgress(id)

         return f"Task updated successfully (ID: {id})"

    elif command == COMMAND["MARK_DONE"]:
         if len(arguments) != 2:
               raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.")
             
         id = arguments[1]
         if not id:
            raise CustomException("task id can't be empty")
         op.markDone(id)

         return f"Task updated successfully (ID: {id})"
    else:
       raise CustomException("Unknown command. Please refer to the user guide.")
      
try:
    print(main())
except CustomException as e:
    guide()
    print(e)
except Exception as e:
    print("Something went wrong:", e)