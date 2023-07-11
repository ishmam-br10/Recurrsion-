def TowerOfHanoi(disks, main, destiny, helper, count):
    # main is the pole where disks are stacked
    # helper is which pole remains idle
    # destiny is the pole where disk will go
    if disks == 1:
        print(f"Move disk {disks} from pole {main} to destination pole {destiny}")
        count[0] = count[0] + 1
        return

    TowerOfHanoi(disks-1, main, helper, destiny, count)
    print(f"Move disk {disks} from pole {main} to destination pole {destiny}")
    count[0] = count[0] + 1
    TowerOfHanoi(disks-1, helper, destiny, main, count)
    # return count
count = [0]
number_of_disks = int(input("Number dao: "))
print("## Printing the simulation for poles A , B , C ##")
TowerOfHanoi(number_of_disks, 'A', 'B', 'C', count)
# print(f"Steps needed to complete the sorting: {TowerOfHanoi(number_of_disks)}")
print(f"Number of steps needed to complete: {count[0]}")