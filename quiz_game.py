#coding: utf-8

#func greating
#func load questions
#func ask
#func end

def main():
	print("Welcome to my quiz!")

	playing = input("Do you want to play? ")

	if playing.lower() != "yes":
  		quit()
  
	score = 0

	print("Starting now:")
	answer = input("What does CPU stand for? ")
	if answer.lower() == "central processing unit":
  		print("Correct")
  		score += 1
	else:
  		print("Incorrect")

	answer = input("What does GPU stand for? ")
	if answer.lower() == "graphics processing unit":
  		print("Correct")
  		score += 1
	else:
		print("Incorrect")


	print("You've got " + str(score) + " questions right!")
	print("That's " + str(score/2*100) + "%.")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()