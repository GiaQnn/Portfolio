import random

name = ""
question = ""
answer = ""
random_number = random.randint(1, 10)

# if statements of first three variables
if question == "" and name == "":
  print("The Magic 8-Ball can not provide a fortune unless you as it something.")
elif name == "":
  print("Your question:", question)
elif not name == "":
  print(name, "asks:", question)
else:
  print(random_number)

# if statements for random_number variable
if random_number == 1:
  answer = "Yes, definitely!"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = " Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no!"
elif random_number == 8:
  answer = "Outlook not so good..."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

# if statement if there is no question.
if question == "":
  print("Ask the question.")
else:
  print("Magic 8-Ball's answer: ", answer)