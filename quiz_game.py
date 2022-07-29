#coding: utf-8

print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
  quit()

print("Start now")
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
  print("Correct")
else:
  print("Incorrect")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
  print("Correct")
else:
  print("Incorrect")
