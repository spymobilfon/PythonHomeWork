def number_to_string(number):
    return str(number)

int_list = [3, 4, 90, -2]

string_list = list(map(number_to_string, int_list))
print(string_list)