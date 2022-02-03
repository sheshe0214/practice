import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Reply ask agin later'
    elif answerNumber == 6:
        return 'Concentrtate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook is not good'
    elif answerNumber == 9:
        return  'Very doubtful'

print(getAnswer(random.randint(1,9)))

#could also be:
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
