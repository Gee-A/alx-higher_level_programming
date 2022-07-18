#!/usr/bin/Python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
        res.append(div)
    return res
