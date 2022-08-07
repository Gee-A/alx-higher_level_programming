# 0x0C. Python - Almost a circle

# Background Context
This project is a fore preparation towards the AirBnB project of the Higher level curriculum.

## Review made in Preparation
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* **Unittest**
* Read/Write
* args and kwargs
* Serialization/Deserialization
* **JSON**
***
execute tests using: ``python -m unittest discover tests``
***

## Table of Content
| Files | Description |
|:-----:|:------------|
[tests/test_models/*.py](./tests/test_models/) | contains all ``unittest`` test file '.py' for this project. Files are organized in same way as the project in the models directory.
[models](./models) | Folder containing all the modules of this project
[models/__init__.py](./models/__init__.py) | Empty file that makes the project a package
[models/base.py](./models/base.py) | Class Base is the 'base' class of all other classes in these project
[models/rectangle.py](./models/rectangle.py) | a class Rectangle that inherits from Base
[models/square.py](./models/square.py) | a class Square that inherits from Rectangle
