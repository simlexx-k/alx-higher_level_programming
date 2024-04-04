#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists."""
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                result = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
