# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random as rnd
import matplotlib.pyplot as plt

ELEMENTS_NUMBER = 3

def goats_and_car(name):
    print(name, ':')

    results_reverse = []
    results_not_reverse = []

    iterations_numbers = range(100, 5000, 100)

    results1 = []
    results2 = []
    for i in iterations_numbers:
        for j in range(0, i):
            print('REVERSE - FALSE:')
            results_not_reverse.append(get_result(False)) #player_choice_reverse = False
            print()
            print('REVERSE - TRUE:')
            results_reverse.append(get_result(True)) #player_choice_reverse = True
        not_reverse_percentage = results_not_reverse.count(True) / len(results_not_reverse) * 100
        results1.append(not_reverse_percentage)
        print(not_reverse_percentage)
        reverse_percentage = results_reverse.count(True) / len(results_reverse) * 100
        results2.append(reverse_percentage)
        print('              ', reverse_percentage)
        ###############################################################################################################
    plt.plot(results1)
    plt.plot(results2)
    plt.show()
    ###############################################################################################################

def get_result(player_choice_reverse):

    # init doors names
    doors_indexes = list(range(1, ELEMENTS_NUMBER + 1))
    doors_values = ['goat'] * ELEMENTS_NUMBER
    doors = dict(zip(doors_indexes, doors_values))

    doors_keys = list(doors.keys())

    car_door_key = rnd.choice(doors_keys)
    doors[car_door_key] = 'car'
    print('@', 'all doors: ',doors)

    # player choice (one of doors)
    player_door_key = rnd.choice(doors_keys)
    print('@@', 'player choice: ', player_door_key)

    # remove the player choice
    doors_keys.remove(player_door_key)
    print('@@@', 'without player_door_key: ', doors_keys)

    # showman remove all other doors except 1 door
    if player_door_key == car_door_key:
        showman_door_key = rnd.choice(doors_keys)
    else:
        showman_door_key = car_door_key
    print('@@@@@', 'showman remained door key: ', showman_door_key)

    # reverse
    if player_choice_reverse is True:
       player_door_key = showman_door_key
       print('@@@@@', 'new player_door_key: ', player_door_key)

    # result
    if player_door_key == car_door_key:
        print('@@@@@', 'result: ', doors[player_door_key])
        return True
    else:
        print('@@@@@@', 'result: ', doors[player_door_key])
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    goats_and_car('GOATS_AND_CAR')
