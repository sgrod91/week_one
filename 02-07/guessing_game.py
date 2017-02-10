import random
my_random_number = random.randint(1, 10)
count = 5
while True:
    my_random_number = random.randint(1, 10)
    count = 5
    while True:
        guess_number = int(raw_input("I'm thinking of a number between 1 and 10, what's the number? "))
        if guess_number == my_random_number:
            print "That's correct"
            break
        elif guess_number < my_random_number:
            print "Too low"
            count -= 1
            print "You have %d guesses left" % count
        elif guess_number > my_random_number:
            print "Too high"
            count -= 1
            print "You have %d guesses left" % count
        if count == 0:
            print "You ran out of guesses!"
            break
    play_again = raw_input("Do you want to play again? (Y/N)")
    if play_again == "N":
        print "Bye!"
        break
