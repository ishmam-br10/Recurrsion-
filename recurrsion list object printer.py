def list_objects(list, a=0):
    list1 = list.copy()
    print(list1[a])
    if a < len(list)-1:
        return list_objects(list1, a+1)


list_objects([1,2,3,4,5],0)