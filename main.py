import random

options = ["R", "P", "S"],

player = [] #empty list
cpu = []

play_option = input("Pick an option; R, S or P: ")

player.append(play_option) #adds what the user enters to the player list.
cpu.append(random.choice(options)) 
#the random module allows python to pick any value of its choice (using the choice() method) from options list.

print(player)
print(cpu)


#while loop: an indefinite loop
while True:
    if player == cpu:
        print("Player ({}) : CPU ({}). A tie".format(player, cpu))
        play_option = input("Pick an option; R, S or P: ")
        player.append(play_option)
        cpu.append(random.choice(options))

    elif ( "R" in player) and ("S" in cpu):
        print("Player ({}) : CPU ({}). Player wins".format(player, cpu,))
        break 
    #break keyword allows python to break out of the while loop when a condition have been met. 
    #continue keyword allows python to skip an iteration
    elif ("S" in player) and ("R" in cpu):
        print("Player ({}) : CPU ({}). CPU wins".format(player, cpu))
        break

    elif ("S" in player) and ("P" in cpu):
        print("Player ({}) : CPU ({}). Player wins".format(player, cpu))
        break

    elif ("P" in player) and ("S" in cpu):
        print("Player ({}) : CPU ({}). CPU wins".format(player, cpu))
        break

    elif ("R" in player) and ("P" in cpu):
        print("Player ({}) : CPU ({}). CPU wins".format(player, cpu))
        break

    elif ("P" in player) and ("R" in cpu):
        print("Player ({}) : CPU ({}). Player wins".format(player, cpu))
        break

    else:
        if player not in options:
            print("Invalid input. Try again")
            break

print("Thanks for playing!")



