import os
import json

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.path = f"{name}.json"
        if not os.path.exists(self.path):
            self._save([])

    def _load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f)

    def create(self, row):
        if len(row) != len(self.columns):
            raise ValueError("Invalid number of columns")
        data = self._load()
        data.append(dict(zip(self.columns, row)))
        self._save(data)

    def read(self, **kwargs):
        data = self._load()
        result = data
        for key, value in kwargs.items():
            result = [r for r in result if r[key] == value]
        return result

    def update(self, filter_kwargs, update_kwargs):
        data = self._load()
        for row in data:
            if all(row[key] == value for key, value in filter_kwargs.items()):
                for key, value in update_kwargs.items():
                    row[key] = value
        self._save(data)

    def delete(self, **kwargs):
        data = self._load()
        for row in data[:]:
            if all(row[key] == value for key, value in kwargs.items()):
                data.remove(row)
        self._save(data)


with open('C:/Users/user/source/repos/PythonCode/Projects/users.json', 'r') as f:
    data = json.load(f)

users = data['users']

# for user in users:
#     print(user)



# class Database:
#     def __init__(self, name):
#         self.name = name
#         self.tables = {}

#         if os.path.isfile(f"{name}.json"):
#             with open(f"{name}.json", "r") as f:
#                 data = json.load(f)
#                 for table_name, table_data in data.items():
#                     self.tables[table_name] = Table(table_name, table_data["columns"], table_data["rows"])
#         else:
#             with open(f"{name}.json", "w") as f:
#                 json.dump({}, f)
                
#     def table(self, name, columns=None):
#         if name in self.tables:
#             return self.tables[name]
#         else:
#             self.tables[name] = Table(name, columns)
#             return self.tables[name]
    
#     def save(self):
#         data = {}
#         for table_name, table in self.tables.items():
#             data[table_name] = {
#                 "columns": table.columns,
#                 "rows": table.rows
#             }

#         with open(f"{self.name}.json", "w") as f:
#             json.dump(data, f)



users_table = Table("users", ["id", "name", "age"])


users_table.delete(id=1)
