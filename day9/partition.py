def partition_array(my_list):
    pivot = my_list[0]
    for i in range(1, len(my_list)):
        if pivot < my_list[i]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j += 1
    my_list[0], my_list[j] = my_list[j], my_list[0]
l1=[]