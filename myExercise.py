import sys

list1 = []
list_of_names = []
names = sys.argv[2].split(",")
d = {}
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        line = line.split(":")
        list1.append(line)

    for i in list1:
        d[i[0]] = i[1]
        list_of_names.append(i[0])
    for k in names:
        try:
            print("Name:{}, University: {}".format(k, d[k]))
        except KeyError:
            print("No record of '{}' was found!".format(k))
