import sys
from app.core.constant import COMMAND, RESULT
from app.service.operation import Operation
from app.core.constant import FILENAME
from app.customException.customException import CustomException


def guide():
    print(
        """
    Adding a new task
       python -m app.task_cli add "Buy groceries"
       Output: Task added successfully (ID: 1)
     
    Updating and deleting tasks
      python -m app.task_cli update 1 "Buy groceries and cook dinner"

    Updating and deleting tasks
      python -m app.task_cli delete 1
      
    Marking a task as in progress or done
      python -m app.task_cli mark-in-progress 1
      python -m app.task_cli mark-done 1
      
    Listing all tasks
      python -m app.task_cli list
      
    Listing tasks by status
      python -m app.task_cli list done
      python -m app.task_cli list todo
      python -m app.task_cli list inprogress
    """
    )



def main(fileName = None):
    op = Operation(fileName or FILENAME)

    arguments = sys.argv[1:]  # remove the first because it contain file name

    if not arguments:
      guide()
      return RESULT["NO_ARGUMENTS"]()

    command = arguments[0]
    if command ==COMMAND["ADD"]:
        if len(arguments) != 2:
           raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.", show_guide=True)
           
    
        desc = arguments[1].strip()
    
        if not desc:
            raise CustomException("task desc can't be empty")
    
        getTaskId = op.getTaskId()
    
        op.addTask({"desc":desc, "id":getTaskId, "status": "todo"})
        return RESULT["TASK_ADDED"](getTaskId)
    
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
                raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.", show_guide=True)
     
         id = arguments[1]
     
         if not id:
             raise CustomException("task id can't be empty")
     
         op.deleteTask(id)

         return RESULT["TASK_DELETED"](id)

    elif command == COMMAND['UPDATE']:
         if len(arguments) != 3:
             raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.", show_guide=True)
     
         id = arguments[1]
         if not id:
             raise CustomException("task id can't be empty")
     
         desc = arguments[2].strip()
         if not desc:
             raise CustomException("task desc can't be empty")
     
         op.updateTask(id, desc)

         return RESULT["TASK_UPDATED"](id)

    elif command == COMMAND["MARK_IN_PROGRESS"]:
         if len(arguments) != 2:
               raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.", show_guide=True)
             
         id = arguments[1]
         if not id:
            raise CustomException("task id can't be empty")
   
         op.markInProgress(id)

         return RESULT["TASK_UPDATED"](id)

    elif command == COMMAND["MARK_DONE"]:
         if len(arguments) != 2:
               raise CustomException("Incorrect syntax. Please refer to the user guide for correct usage.", show_guide=True)
             
         id = arguments[1]
         if not id:
            raise CustomException("task id can't be empty")
         op.markDone(id)

         return RESULT["TASK_UPDATED"](id)
    else:
       raise CustomException("Unknown command. Please refer to the user guide.", show_guide=True)

if __name__ == "__main__":   
     try:
         print(main())
     except CustomException as e:
         if e.show_guide:
          guide()
         print(e)
     except Exception as e:
         print("Something went wrong:", e)