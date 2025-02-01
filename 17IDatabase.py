#Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod
list=[]
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self,data):
        pass
    
    def update(self,query,data):
        pass

class Nosqldatabase(IDatabaseOperations):
    def __init__(self):
        self.list=[]
    def insert(self, data):
        self.list.append(data)
        print(f"Nossql data inserted {data}")
    def update(self, dataid, newdata):
        for data in self.list:
            if data.get('id')==dataid:
                data.update(newdata)
                print(f"Nosqldata updated {data}")
                return
        print(f"Nosql data eroor no data found with id ={dataid}")
    def delete(self,dataid):
        for data in self.list:
            if data.get('id')==dataid:
                self.list.remove(data)
                print(f"NoSQLDatabase Deleted: {data}")
                return
        print(f"NoSQLDatabase Error: No record found with id = {dataid}")
class SQLDatabase(IDatabaseOperations):
    def __init__(self):
        self.dict = {}

    def insert(self, data):
        dataid = data.get("id")
        if dataid in self.dict:
            print(f"SQLDatabase Error: Record with id {dataid} already exists.")
        else:
            self.dict[dataid] = data
            print(f"SQLDatabase Inserted: {data}")

    def update(self, dataid, new_data):
        if dataid in self.dict:
            self.dict[dataid].update(new_data)
            print(f"SQLDatabase Updated: {self.dict[dataid]}")
        else:
            print(f"SQLDatabase Error: No record found with id = {dataid}")

    def delete(self, dataid):
        if dataid in self.dict:
            deleted_record = self.dict.pop(dataid)
            print(f"SQLDatabase Deleted: {deleted_record}")
        else:
            print(f"SQLDatabase Error: No record found with id = {dataid}")

sql_db = SQLDatabase()
nosql_db = Nosqldatabase()

record1 = {"id": 1, "name": "Alice", "age": 30}
record2 = {"id": 2, "name": "Bob", "age": 25}

# SQL Database Operations
sql_db.insert(record1)
sql_db.insert(record2)
sql_db.update(1, {"age": 31})
sql_db.delete(2)
print()
# NoSQL Database Operations
nosql_db.insert(record1)
nosql_db.insert(record2)
nosql_db.update(1, {"age": 32})
nosql_db.delete(2)