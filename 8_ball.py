import random
answers = [
"No!", "Yes!", "Ask sometime later.", "Don't count on it.", "You betcha!",
"Ask your mum!", "There's an 80 percent chance!", "Yikes, there's only a 20 percent chance."]
random_answer = random.choice(answers)

def question():
	question = input("\nYou shake a magic 8 ball!\n" + 
		"What fortune would you like to be told? ")
	while not question:
		question = input("\nYou didn't give me a question!\n" +
			"What fortune would you like to be told? ")
	print("\nThinking...\n")
	print(random_answer)
	next_question()

def next_question():
	next_question = input("\nWould you like to shake the magic 8 ball again? (y/n) \n")
	while not next_question:
		next_question = input("You didn't give me an answer!\n" +
			"Would you like to shake the magic 8 ball again? (y/n) ")
	if next_question == "y":
		main()
	else:
		quit

def main():
	question()

question()