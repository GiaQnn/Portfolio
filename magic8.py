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