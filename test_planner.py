from ai.brain import Brain

brain = Brain()

while True:

    cmd = input("You : ")

    if cmd == "exit":
        break

    print()

    print(brain.ask(cmd))

    print()