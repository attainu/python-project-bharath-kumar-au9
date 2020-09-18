# snake and ladder

import time
import random
import sys

# just for delay of action

Sleep_Time = 1.3
Max_Val = 100
Dice = 6

# snakes

snakes = {
    14: 3,
    25: 10,
    31: 24,
    44: 8,
    51: 19,
    69: 55,
    71: 18,
    85: 45,
    91: 86,
    99: 1,
}

# Ladders

ladder = {
    5: 21,
    6: 11,
    9: 55,
    22: 41,
    38: 77,
    58: 68,
    65: 92,
    70: 81,
    78: 96,
    89: 95,
}

Player_turn = [
  "your turn.",
   "go.", 
   "are you ready."
   ]

Snake_bite = [
    "bohoo",
    "snake bite",
    "oh no",
]

ladder_jump = [
    "wohoo",
    "nailed it",
    "yayy......."
    "wow",
]


def welcome_msg():
    msg = """

    Welcome to Snake And Ladder Game......
    Are you ready for game?......


    Rules:
        1. Initially both the players will start from starting position i.e 0.
        Take it in turns to roll the dice.
        move forward the num of spaces shown on the dice.
        2. If you land at the bottom of ladder you can move up.
        3. If you land at the head of snake , you must move down.
        4. The first player to reach Final position will be WINNER.
        5. Hit enter to start the game........

    """
    print(msg)


def Player_names():
    player1_name = None
    while not player1_name:
        player1_name = input(
            "Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input(
            "Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" +
          player2_name + "'\n")
    return player1_name, player2_name


def Get_Dice_Value():
    time.sleep(Sleep_Time)
    dice_value = random.randint(1, Dice)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(Snake_bite).upper() + "~~~~~~~~~~~~~~~~>")
    print("\n" + player_name + "got a snake bite. Down from " +
          str(old_value) + "to" + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(Sleep_Time)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > Max_Val:
        print("you need" + str(Max_Val - old_value) +
              "to win this game. keep trying......")
        return old_value

    print("\n" + player_name + " moved from" +" "+ str(old_value) + "to" +" " +
          str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladder:
        final_value = ladder.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(Sleep_Time)
    if Max_Val == position:
        print("\n\n\nThats it" + player_name + "won the game")
        print("congratulations" + player_name)
        print("Thank you")
        sys.exit(10)


def start():
    welcome_msg()
    time.sleep(Sleep_Time)
    player1_name, player2_name = Player_names()
    time.sleep(Sleep_Time)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(Sleep_Time)
        input_1 = input("\n" + player1_name + ": " + random.choice(Player_turn) + "Hit enter to roll the dice")
        print("Rolling the Dice................")
        dice_value=Get_Dice_Value()
        time.sleep(Sleep_Time)
        player1_current_position= snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)


        input_2 = input("\n" + player2_name + ": " + random.choice(Player_turn) + "Hit enter to roll the dice")
        print("Roling the dice ...............")
        dice_value=Get_Dice_Value()
        time.sleep(Sleep_Time)
        player2_current_position= snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()
