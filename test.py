import  random
print("welcome to the ROCK PAPER and SCISSORS")
print("please strictly make use of uppercase letters for playing this game ")
while True:
    user_input = input("enter a choice(for rock choose R, for scissors choose S and for paper choose P):")
    possible_inputs = ["R", "P", "S"]
    computer_input = random.choice(possible_inputs)
    if user_input == possible_inputs:
        
             print(f"\nyou choose {user_input}, computer choose {computer_input}.\n")
             print(f"both players selected {user_input}. it's a tie!")

        
    else:
                print("input not acceptable")
                break
    #if user_input == computer_input:
        if user_input == "R":
            if computer_input == "S":
                print("Rock smashes scissors! you win")
        else:
            print("paper covers rock! you loose.")
    elif user_input == "P":
        if computer_input =="R":
            print("paper covers rock! you win!")
        else:
            print("scissors cuts paper! you loose.")
    elif user_input =="S":
        if computer_input == "P":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you loose!")
    play_again = input("play again?  (Y/N): ")
    play_again = ["Y", "N"]

    if play_again == "Y":
               print("restarting game")
               True
    else:
               print("goodbye")
               break
