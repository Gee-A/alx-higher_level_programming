#!/usr/bin/python3
# run code in Python3.8.x (since hidden_4.pyc was compiled with this version)

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
