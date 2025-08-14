import random


def main():
    level = get_level()
    attempts = 0
    score = 0


    while attempts < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            answer = int(input(f"{x} + {y} = "))
            print(attempts)

            while True:
                if (x + y) == answer:
                    score = score + 1
                    attempts = attempts + 1
                    break

                else:
                    incorrect = 0
                    while incorrect < 3:
                         print("EEE")
                         answer = int(input(f"{x} + {y} = "))
                         if (x + y) == answer:
                                score = score + 1
                                break
                         else:
                                incorrect = incorrect + 1
                                continue
        except ValueError:
            continue
    print(f"Score: {score}")



# collecting the level number from the user.
def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            continue

# generating random numbers(x,y) to use in sums(x + y)
def generate_integer(level):

    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
