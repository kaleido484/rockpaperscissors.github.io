import random
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
choice=int(input("What is your choice?Press 0 for Rock,1 for Paper,2 for Scissors? "))

if choice==0:
  print(rock)
elif choice==1:
  print(paper)
elif choice==2:
 print (scissors)


print("Computer chose:")
random_choice=random.randint(0,2)
if random_choice==0:
  print(rock)
elif random_choice==1:
  print(paper)
elif random_choice==2:
 print (scissors)

if choice==random_choice:
  print("It's a tie.Try again!")

elif choice==0 and random_choice==2:
  print("You win!")

elif choice==1 and random_choice==0:
  print("You win!")

elif choice==2 and random_choice==1:
  print("You win!")

else:
  print("You Lose")
