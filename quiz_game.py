#coding: utf-8

print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Starting now:")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct")
else:
  print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("Correct")
else:
  print("Incorrect")
