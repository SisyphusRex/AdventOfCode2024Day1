"""program module"""


def main(*args):
    """method to run program"""
    list1, list2 = read_data("input_data.txt")
    list1.sort()
    list2.sort()
    distance_list = []

    for index1, value1 in enumerate(list1):
        count = 0
        for index2, value2 in enumerate(list2):
            if value1 == value2:
                count += 1
        distance_list.append(value1 * count)

    my_sum = 0

    for i in range(len(distance_list)):
        my_sum += distance_list[i]

    print(my_sum)


def read_data(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    list1 = []
    list2 = []
    with open(filename, "r") as f:
        for line in f:
            stripped = line.strip()
            split_list = stripped.split("   ")
            list1.append(int(split_list[0]))
            list2.append(int(split_list[1]))

    return list1, list2
