fileName ="task.json"
import json
from customException import CustomException

class Operation:
    def __init__(self):
        pass

    def getTaskId(self):
        with open(fileName, 'r') as file:
           tasks =  json.load(file)
           return (tasks[-1]["id"] + 1) if tasks else 1; 

    def writeTask(self, obj):
        with open(fileName, "w") as file:
         json.dump(obj, file, indent=4)

    def getListOfTask(self):
        with open(fileName, 'r') as file:
           return json.load(file)

    def addTask(self, task):
        tasks = self.getListOfTask()
        tasks.append(task)

        self.writeTask(tasks)

    def updateTask(self, id, desc):
        tasks= self.getListOfTask()

        task = next((item for item in tasks if item["id"] == int(id)), None)

        if task is None:
            raise CustomException("Task does not exist")
        
        update = [ { **item, "desc": desc } 
                              if item["id"] == int(id) else item
                              for item in tasks
                        ]
        
        self.writeTask(update)

    def markInProgress(self, id):
        tasks= self.getListOfTask()

        update = [ {**item, "status": "inprogress"} 
                      if item["id"] == int(id) else item
                      for item in tasks
                ]

        self.writeTask(update)

    def markDone(self, id):
        tasks= self.getListOfTask()

        update = [  { **item, "status": "done" } 
                      if item["id"] == int(id) else item
                      for item in tasks
                ]
        self.writeTask(update)

    def deleteTask(self, id):
        listOfTask = self.getListOfTask()
        filterTask = [item for item in listOfTask if item["id"] != int(id)]

        with open(fileName, "w") as file:
             json.dump(filterTask, file, indent=4)

op = Operation()




