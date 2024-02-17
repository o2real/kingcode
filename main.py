line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a" , "b" , "c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# import random

# RPC = [rock , paper, scissors]

# myRPC = random.choice(RPC)
# comRPC = random.choice(RPC)

# my = print("my" , myRPC)

# com = print("com", comRPC)

# if myRPC == comRPC :
#   print("DRAW")

# elif myRPC 
import random

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))

com_choose = int(random.randint(0, 2))

RPC_list = [rock , paper , scissors]

if user_choose >= 0 and user_choose < 3 :

  print(RPC_list[user_choose])
  print("COM")
  print(RPC_list[com_choose])


  if com_choose > user_choose :
    print("You Win")

  elif com_choose == 2 and user_choose == 0 :
    print("You win")

  elif com_choose == 0 and user_choose == 2:
    print("You Lose")

  elif com_choose < user_choose :
    print("You Lose")

  elif com_choose == user_choose :
    print("It's Draw")

else:
 print("Choose again.")