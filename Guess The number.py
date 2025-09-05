import random
import sys

print("🎮 Hi Welcome to the fun game: Guess the Number! 🎯")

while True:
    print("\nChoose difficulty level: ")
    print("1 - Easy (10 attempts)")
    print("2 - Medium (7 attempts)")
    print("3 - Hard (5 attempts)")
    print('99 - !!!!!🔥Crazy Mode🔥!!!!')
    cho = input('So, 1 or 2 or 3: ')

    if cho == '1':
        y = 10
        num = random.randint(1, 20)
        xx=[1,20]
        li=20
    elif cho == '2':
        y = 7
        num = random.randint(1, 50)
        xx=[1,50]
        li=50
    elif cho == '3':
        y = 5
        num = random.randint(1, 20)
        xx=[1,20]
        li=20
    elif cho=='99':
        print('''          ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\           /~         ~\  |  |
  ||  |             |         |             |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \_           /           \           _/   |
 |      ~~--_____-~    /~V~\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\  |                    |
 |                    ~~   ~~                    |
  \_         _                       _         _/
    ~--____-~ ~\                   /~ ~-____--~
         \     /\                 /\     /
          \    | ( ,           , ) |    /
           |   | (~(__(  |  )__)~) |   |
            |   \/ (  (~~|~~)  ) \/   |
             |   |  [ [  |  ] ]  /   |
              |                     |
               \                   /
                ~-_             _-~
                   ~--___-___--~''')
        y=1
        num = random.randint(1, 99)
        xx='1 to 99 💀💀💀💀'
        li=99
    else:
        print("😏 You are being punished for joking... Only 3 attempts for you!")
        y = 3
        num = random.randint(1, 99)
        li=99
        xx='1 to 100000000'

    x = input("Choose between " +str(xx)+' : ')
    try:
        x = int(x)
    except ValueError:
        print("Invalid input!")
        continue

    hints = ["👉 Give it another try: ",
             "👉 Your next guess: ",
             "👉 Try once more: "]

    while True:
        if y == 0:
            print("💀 GAME OVER! Better luck next time...")
            print(f"The hidden number was {num} 👀")
            break
        if x < 1 or x > li:
            print("🚫 Out of range! No game for you.")
            break

        elif x == num:
            print("🎉 BOOM! YOU CRACKED THE CODE 🎉")
            print(f"The secret number was indeed {num}! 🏆")
            break

        elif abs(num - x) in [1, 2, 3]:
            print("🔥 You're burning hot! Almost got it!")
        elif abs(num - x) in [4, 5, 6, 7]:
            print("😎 You're getting warmer... keep going!")
        elif abs(num - x) in [8, 9, 10, 11, 12]:
            print("🌥️ Hmm, you're drifting away a bit.")
        elif abs(num - x) in [13, 14, 15, 16]:
            print("❄️ Cold... very cold. Try changing direction.")
        elif abs(num - x) in [17, 18, 19]:
            print("🌌 You're lost in space... come back to Earth!")

        y -= 1
        if y > 0:
            if y == 1:
                print("⚠️ Last chance... make it count!")
            else:
                print(f"⚡ Attempts left: {y}")
            try:
                x = int(input(random.choice(hints)))
            except ValueError:
                print("Invalid input!")
                continue

    ask=input('Play Again? y/n : ')
    if ask.lower() != 'y':
        print('BYE')
        sys.exit()
