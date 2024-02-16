print('Welcome to the quiz game!')

playing = input('Would you like to play: ')

if playing.lower() == 'no':
    quit()

print("Okay, Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does GPU? ")
if answer.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score is:", score)
print("You got:",str(score/4 * 100) + "%")