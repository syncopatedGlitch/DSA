from typing import Self

'''
Singletons vs. Idiomatic Python
Singletons are an Anti-pattern: In many object-oriented
languages like Java, singletons are used to ensure only
one instance of a class exists. In Python, this is often
considered an anti-pattern and can lead to code
maintenance issues, make testing difficult, and introduce
hidden global state.
Modules are "Natural" Singletons: Python's module system
automatically enforces the singleton concept. When you
import a module for the first time in a program, the
Python interpreter executes its code and creates a single
module object, which is then cached in sys.modules.
Any subsequent imports of the same module in any other
part of the program will simply return the already-loaded,
single module object, not a new one.
Simplicity over Complexity: The elaborate class-based
implementation you provided using __new__ adds unnecessary
complexity to achieve something Python handles automatically
and more simply at the module level.
The Idiomatic Alternative: Module-level Instance
For shared resources like a DatabaseConnection, the
idiomatic Python way is to define the resource
(e.g., the class) in a module and then create a single,
module-level instance of that class.
Here's how you would refactor your example to be idiomatic:
1. Create a module (e.g., database.py):
python
# database.py module
class DatabaseConnection:
    def query(self, sql: str) -> None:
        # Database operations
        print(f"Executing query: {sql}")
        pass

# Create the single instance at the module level
db = DatabaseConnection()


2. Import and use the instance directly in other files:
python
# main_app.py
from database import db  # Imports the *single* instance
created in database.py

def main():
    db.query("SELECT * FROM users")
    # All parts of the application import 'db' and share
    # the same connection instance.

'''


class DatabaseSingleton:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def query(self, sql: str):
        pass


db = DatabaseSingleton()
db.query("Select * from users")
