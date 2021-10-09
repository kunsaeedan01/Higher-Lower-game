import random
from art import logo
from art import vs
from game_data import data
from replit import clear

the_end = False
score = 0

primary_page = data[random.randint(0, len(data)-1)]
fresh_page = data[random.randint(0, len(data)-1)]


while the_end == False:

  while fresh_page == primary_page:
    fresh_page = data[random.randint(0, len(data)-1)]
  print(logo)
  print(f" Your score : {score}")
  print(f"Compare A: {fresh_page['name']} is {fresh_page['description']} from {fresh_page['country']}")
  print(vs)
  print(f"Against B: {primary_page['name']} is {primary_page['description']} from {primary_page['country']}")
  choice = input("Who has more followers? A or B:  ")
  if choice == "A" and fresh_page['follower_count'] > primary_page['follower_count']:
    score += 1
  elif choice == "B" and primary_page['follower_count'] > fresh_page['follower_count']:
    score += 1
  elif choice == "A" and fresh_page['follower_count'] < primary_page['follower_count']:
    the_end = True
  elif choice == "B" and fresh_page['follower_count'] > primary_page['follower_count']:
    the_end = True
  fresh_page = primary_page
  primary_page = data[random.randint(0, len(data)-1)]
  clear()

print(f"You are wrong. Your final score is: {score}")

  
  
    
  
