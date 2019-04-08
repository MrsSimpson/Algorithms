from rod_cutting import *
from greedy_algorithm import *



def main():
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_activity = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_activity = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print("The possible rod lengths are:  " + str(n))
    print("The price for rod lengths are: " + str(price))
    for i in n:
        print("Max Value for a rod of length " + str(i) + " Is " + str(cut_rod(price, i)))

    possible_activites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print("\nActivity #   " + str(possible_activites))
    print("Start  Times " + str(start_activity))
    print("Finish Times " + str(finish_activity))

    print("\nThe following activites are selected by the greedy algorithm: ")
    greedy_activity_selector(start_activity, finish_activity)

main()
