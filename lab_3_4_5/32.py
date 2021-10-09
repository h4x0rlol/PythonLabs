import random

global first
first = 0
global second
second = 0

def play():
    box_lose_indices = list(range(0, 3))
    win_index = box_lose_indices.pop(random.randint(0, 2))
    black_boxes = [False] * 3
    black_boxes[win_index] = True

    first_player_choise = random.randint(0, 2)
    if black_boxes[first_player_choise]:
        global first
        first += 1
    else:
        box_lose_indices.remove(first_player_choise)

    black_boxes[first_player_choise] = None
    presenter_choise = random.choice(box_lose_indices)
    black_boxes[presenter_choise] = None
    second_choice = list(filter(lambda x: x != None, black_boxes))
    if second_choice[0]:
        global second
        second += 1

play()

for i in range(0, 1000):
    play()

print("first", first)
print("second", second)
