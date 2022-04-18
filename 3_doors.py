#Name: Judah Nava
#Date: 4/18/22
#Description: There is a math question the goes as follows...
#   1. You have 3 doors in front of you, one of them has the prize.
#   2. You are told to pick a door and lock it in as your choice.
#   2. The host reveals one of the other 2 doors to already not have the prize.
#   3. You are given the option to change your choice to the other door.
#   4. Is it better to swtcih doors, or stay on that first door.
import random, pprint
wins = {"won w/o switch": 0,
        "won by switch": 0}
debug = [] #[[TrueDoor, playerChoice, hostChoice, Switch?],]

def run(wins, loop, debug):
    for a in range(loop):
        doors = {1:False, 2: False, 3: False}

        # Assign prize
        prize = random.randint(1,3)
        doors[prize] = True

        # the players selection.
        selection = random.randint(1,3)

        # The hosts selection is made and "announced".
        check = True
        fail = 100
        while check:
            temp = random.randint(1,3)
            if temp != selection and (not doors[temp]):
                host_sel = temp
                """
                Why is this not being used?
                    Because the host will always open a door w/o the prize,
                    and if the player switches, it will always be the other door
                    the the host did not pick. but this code is added for debug.
                """
                check = False
            fail -= 1
            if fail <=0:
                break

        # player makes the desicion to switch.
        switch = random.randint(0,1)

        # results
        if doors[selection] and switch == 0:
            #print("True and False, the player won w/o switch.")
            wins["won w/o switch"] += 1
        elif doors[selection] and switch == 1:
            #print("True and True, the player lost.")
            pass
        elif (not doors[selection]) and switch == 0:
            #print("False and False, the player lost.")
            pass
        elif (not doors[selection]) and switch == 1:
            #print("Flase and True, the player won by switch.")
            wins["won by switch"] += 1
        debug.append([prize, selection, host_sel, switch])

def main():
    loop = 10000
    run(wins, loop, debug)
    pprint.pprint(wins)
    #pprint.pprint(debug)
    master_debug = [0,0,0,0,0,0,0,0,0,0,0]
    for a in debug: #there has to be a faster way to do this, i know it.
        if a[0] == 1:
            master_debug[0] += 1
        elif a[0] == 2:
            master_debug[1] += 1
        elif a[0] == 3:
            master_debug[2] += 1
        if a[1] == 1:
            master_debug[3] += 1
        elif a[1] == 2:
            master_debug[4] += 1
        elif a[1] == 3:
            master_debug[5] += 1
        if a[2] == 1:
            master_debug[6] += 1
        elif a[2] == 2:
            master_debug[7] += 1
        elif a[2] == 3:
            master_debug[8] += 1
        if a[3] == 0:
            master_debug[9] += 1
        elif a[3] == 1:
            master_debug[10] += 1
    print(master_debug)



if __name__ == "__main__":
    main()

# With the results of this, we can see that its better
# to switch to the other option then stay on your
# first option. 