#Run a magic 8 ball. Changes the response based on whether the name or the question has been answered.


name = "Bob"

question = "Will I win the lottery tonight?"

answer = ""

import random

random_number = random.randint(1,12)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Yeah, right"
elif random_number == 11:
  answer = "Totally"
elif random_number == 12:
  answer = "Don't hold your breath"
else:
  answer = "Error"

if question == "":
  print("Dude, you didn't ask anything. Try again.")
if name == "" and question != "":
  print("Question: " + question)
  print("Magic 8 Ball's answer: " + answer)
if name != "" and question != "":
  print(name + " asks: " + question)
  print("Magic 8 Ball's answer: " + answer)


