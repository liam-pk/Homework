
Signs point to yes.
Yes.
Reply hazy, try again.
Without a doubt.
My sources say no.
As I see it, yes.
You may rely on it.
Concentrate and ask again.
Outlook not so good.
It is decidedly so.
Better not tell you now.
Very doubtful.
Yes - definitely.
It is certain.
Cannot predict now.
Most likely.
Ask again later.
My reply is no.
Outlook good.
Don't count on it.

8ball.py
import random
magicball = {}
counter = 0

##Read and import config file. Build dictionary containing possible answers
file = open("8ball.config")
for line in file:
magicball.update({counter:line.split("\n")[0]})
counter = counter+1

print "Seeing into " + str(counter) + " possible futures."

raw_input("Ask the Magic 8 Ball a question:")
answerkey = random.randrange(counter)
print ''
print ''
print magicball[answerkey]