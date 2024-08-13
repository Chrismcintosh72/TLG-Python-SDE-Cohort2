#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""


def main():
    score = 0
    incorrect_count = 0
    max_incorrect = 3

    print("Welcome to the Game of Thrones Quiz!")
    print("""

      ____    _    __  __ _____    ___  _____
 / ___|  / \  |  \/  | ____|  / _ \|  ___|
| |  _  / _ \ | |\/| |  _|   | | | | |_
| |_| |/ ___ \| |  | | |___  | |_| |  _|
 \____/_/  _\_\_|  |_|_____| _\___/|_|___
|_   _| | | |  _ \ / _ \| \ | | ____/ ___|
  | | | |_| | |_) | | | |  \| |  _| \___ \
  | | |  _  |  _ <| |_| | |\  | |___ ___) |
  |_| |_| |_|_| \_\\___/|_| \_|_____|____/

                                ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-' `
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \
                   {\__--_/}    / \\_>-|)<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
  """)

    print("Please answere the following questions or face being sent North of the Wall!")

    #Question 1
    print("\n1. Who is the author of the 'A Song of Ice and Fire' series?")
    print("1. George R.R. Martin")
    print("2. J.K. Rowling")
    print("3. J.R.R. Tolkien")
    print("4. Chris McIntosh")

    while True:
        answer = str(input("Select the correct option (1/2/3/4):  ").strip())#Something new I found out this takes out white space from input.
        if answer == "1":
            print("Correct!")
            score += 1
            break
        elif answer in ["2", "3", "4"]:
            print("Incorrect. The correct answer was: George R.R. Martin prepare yourself to be banished! ")
            incorrect_count += 1
            if incorrect_count >= max_incorrect:
                print(f"You have reached the ({max_incorrect}). SAY GOODBYE! ")
                print(f"Your final score is {score}/{4 - max_incorrect + score}.")
                return
            break
        else:
            print("Invalid choice. Please select one of the following options: 1, 2, 3, or 4.") 

   #Question 2
    print("\n2. What is the name of Jon Snow's direwolf?")
    print("1. Ghost")
    print("2. Nymeria")
    print("3. Summer")
    print("4. Lady")

    
    while True:
        answer = str(input("Select the correct option (1/2/3/4): ").strip())
        if answer == "1":
            print("Correct!")
            score += 1
            break
        elif answer in ["2", "3", "4"]:
            print("Incorrect. The correct answer was: Ghost. You know nothing John Snow ")
            incorrect_count += 1
            if incorrect_count >= max_incorrect:
                print(f"Sorry, you've reached the maximum number of incorrect answers ({max_incorrect}).")
                print(f"Your final score is {score}/{4 - max_incorrect + score}.")
                return
            break
        else:
            print("Invalid choice. Please select one of the following options: 1, 2, 3, or 4.")
 
    #Question 3
    print("\n3. Which House has the motto 'Winter is coming'? ")
    print("1. House Lannister")
    print("2. House Stark")
    print("3. House Targaryen")
    print("4. House Baratheon")

    while True:
        answer = str(input("Select the correct option (1/2/3/4): ").strip())
        if answer == "2":
            print("Correct!")
            score += 1
            break
        elif answer in ["2", "3", "4"]:
            print("Incorrect. The correct answer was: House Stark. Prepare to join the Knight Kings army! ")
            incorrect_count += 1
            if incorrect_count >= max_incorrect:
                print(f"Sorry, you've reached the maximum number of incorrect answers ({max_incorrect}).")
                print(f"Your final score is {score}/{4 - max_incorrect + score}.")
                return
            break
        else:
            print("Invalid choice. Please select one of the following options: 1, 2, 3, or 4.")

    #Question 4
    print("\n.Who is the 'Mother of Dragons'?")
    print("1. Cersei Lannister")
    print("2. Daenerys Targaryen")
    print("3. Sansa Stark")
    print("4. Arya Stark")

    while True:
        answer = str(input("Select the correct option (1/2/3/4): ").strip())
        if answer == "2":
            print("Correct!")
            score += 1
            break
        elif answer in ["1", "3", "4"]:
            print("Incorrect. The correct answer was: Daenerys Targaryen. Prepare to serve the king byond the wall! ")
            incorrect_count += 1
            if incorrect_count >= max_incorrect:
                print(f"Sorry, you've reached the maximum number of incorrect answers ({max_incorrect}).")
                print(f"Your final score is {score}/{4 - max_incorrect + score}.")
                return
            break
        else:
            print("Invalid choice. Please select one of the following options: 1, 2, 3, or 4.")

    #Final Score
    print (f"Your final score is: {score}/4") 
    print (""" 

    THE IRON THRONE IS YOURS!

    _..._
                     /MMMMM\
                    (I8H#H8I)
                    (I8H#H8I)
                     \WWWWW/
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I.,.I
                     / /#\ \
                   .dH# # #Hb.
               _.~d#XXP I 7XX#b~,_
            _.dXV^XP^ Y X Y ^7X^VXb._
           /AP^   \PY   Y   Y7/   ^VA\
          /8/      \PP  I  77/      \8\
         /J/        IV     VI        \L\
         L|         |  \ /  |         |J
         V          |  | |  |          V
                    |  | |  |
                    |  | |  |
                    |  | |  |
                    |  | |  |
 _                  |  | |  |                  _
( \                 |  | |  |                 / )
 \ \                |  | |  |                / /
('\ \               |  | |  |               / /`)
 \ \ \              |  | |  |              / / /
('\ \ \             |  | |  |             / / /`)
 \ \ \ )            |  | |  |            ( / / /
('\ \( )            |  | |  |            ( )/ /`)
 \ \ ( |            |  | |  |            | ) / /
  \ \( |            |  | |  |            | )/ /
   \ ( |            |  | |  |            | ) /
    \( |            |   Y   |            | )/
     | |            |   |   |            | |
     J | ___...~~--'|   |   |`--~~...___ | L
     >-+<...___     |   |   |     ___...>+-<
    /     __   `--~.L___L___J.~--'   __     \
    K    /  ` --.     d===b     .-- '  \    H
    \_._/        \   // I \\   /        \_._/
      `--~.._     \__\\ I //__/     _..~--'
             `--~~..____ ____..~~--'
                    |   T   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    I   '   I
                     \     /
                      \   /
                       \ /









            """)


if __name__ == "__main__":
    main ()
           
