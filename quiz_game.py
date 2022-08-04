#coding: utf-8

#func greating
#func load questions
#func ask
#func end
def greetings(GameName):
    print("Welcome to " + GameName +"!")

    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        print("k thx by!")
        quit()
    print("Starting now:")
    
def ask_question(question, canswer, score):
    answer = input(question)
    if answer.lower() == canswer:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    return score

def end_message(score, aoq):
    print("You've got " + str(score) + " questions right!")
    print("That's " + str(score/aoq*100) + "%.")
        
def main():
    greetings("my quiz")
    score = 0
    score = ask_question("What does CPU stand for? ", "central processing unit", score)
    score = ask_question("What does GPU stand for? ", "graphics processing unit", score)
    end_message(score, 2)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()

'''
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
'''
