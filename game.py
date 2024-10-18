import random

Draw = 0
You_Wins = 0
Computer_Wins = 0

print("\nYou have total 10 chances.")
Chance = 10

for i in range(1,Chance+1):
    Chances =+ i
    print (f"\n\033[1m\033[4mChance {Chances}\033[0m\033[0m")

    Computer = random.randrange(1,3)
    User = int(input("\nChoose any no between 1 to 3: \n1 for Gun. \n2 for Snake. \n3 for Water.\n\nEnter the no: "))

    if (Computer==1) and (User==1):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 1}} \033[0m \n\n\033[91mDraw\033[0m\n")
        Draw += 1
    elif (Computer==2) and (User==2):
        print(f"\n\033[94m{{Computer: 2}} \n{{You: 2}} \033[0m \n\n\033[91mDraw\033[0m\n") 
        Draw +=1
    elif (Computer==3) and (User==3):
        print(f"\n\033[94m{{Computer: 3}} \n{{You: 3}} \033[0m \n\n\033[91mDraw\033[0m\n")
        Draw +=1
    elif (Computer==1) and (User==2):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mComputer Wins \033[0m\n")
        Computer_Wins +=1 
    elif (Computer==1) and (User==3):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mYou Wins \033[0m\n")
        You_Wins +=1
    elif (Computer==2) and (User==1):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mYou Wins \033[0m\n") 
        You_Wins +=1
    elif (Computer==2) and (User==3):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mComputer Wins \033[0m\n")
        Computer_Wins +=1 
    elif (Computer==3) and (User==1):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mComputer Wins \033[0m\n")
        Computer_Wins += 1  
    elif (Computer==3) and (User==2):
        print(f"\n\033[94m{{Computer: 1}} \n{{You: 2}} \033[0m \n\n\033[91mYou Wins \033[0m\n")
        You_Wins +=1

print("\nYou have reached maximum no of chances.\n")
print (f"\nNo of Draws: {Draw}")
print (f"No of times You Won: {You_Wins}")
print (f"No of times Computer Won: {Computer_Wins}\n")