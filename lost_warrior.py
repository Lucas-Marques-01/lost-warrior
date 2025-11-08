print('''           ..
                           ;:
                          .::.
                         . ::`.                      `;.
                        :  ::  :                      ; :.
                       :   ::   :                    .;  :.
                      :    ::    :                   ::   :.
                     :     ::     :                .::    ::
                     :     ::     :               .::      ::
                     `.    ::    .               .::       ::
                      `.   ::   .               .::         ::
                        `. :: .               .::           ::
                         :    :            .:::             :;
                      _--.   :....:       ...::::               :::
              __-`    `-.:....:.---:::::::                  ::;
    ___----           ..............                        ::;
--==___===============..............                        ::;
       ----___          .........:::::..                    ::;
              ``-_    .  :\\//: ```
                  `--    ://\\:        ``:::::.             :;
                         :\\//:            ``:::.           :;
                         ://\\:               `::.         :;
                         :\\//:                :::.        :;
                         ://\\:                :::;       :;
                         :\\//:                ::::      :;
                         ://\\:                :::      :;
                         :\\//:                :::      :
                         ://\\:               :::      :
                         :\\//:               :::     :
                         ://\\:               ;;     :
                         :\\//:               ;     :
                         :____:              ;     :
                         [____]              ;    :
                         [____]             ;    :
                         [____]            .    :
                         [____]           .    :
                         [____]          .   .:`
                         [____]         .    :
                         :\\//:         :    :
                         ://\\:         `.   `.
                         :\\//:          `.   `.
                         ://\\:            `.   ;
                         [____]              `..
                         [____]
                         [____]
                         [____] 
                         [____]
                         [____]
                         :....:
                       .-  :: `-.
                     .     ::  ..`.
                    /      ::  `   /
                   :       ::       ;
                   ::::::::::::::::::
                   :       ::       ;
                    \      ::      /
                     `.    ::    .
                       `-..::..-)
''')

print("Welcome to Lost Warrior")
print("Your mission is to escape the forest")

print("You wake up in a forest not knowing how you got there. After grabbing your axe, you find yourself at a crossroads.\nOn one path, you can hear a waterfall nearby, and the other leads deeper into the forest.")

choice = input("Which path do you choose? Type Lake or Forest: ").strip().lower()

if choice == "lake":
    print('''                  _.._
  _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                          |   |     |
                                          | |   |  ||
                                          |  |  |   |
                                          |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
     --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
      ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
      .-~~-.          ------     /          '    . `     `    `  \
     (_^..^_)-------           /  '    '      '      `
--------------       --------/     '     '   ')
''')
    print("You arrive at a river with a waterfall and a large tree nearby.\nYou think to yourself that you can cross this river either by swimming or by cutting down the tree to make a bridge.")
    choice2 = input("What do you do? Type swim or cut: ").strip().lower()
    if choice2 == "swim":
        print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄


''')
        print("You try to swim, but your axe and wet clothes pull you down, and you drown.")
    elif choice2 == "cut":
        print("You use your axe to cut the tree; it falls on the other side of the river, and you use it to cross.")
        print("After walking a bit, you come across an abandoned cabin.")
        choice3 = input("What do you do? Type enter or pass: ").strip().lower()
        if choice3 == "enter":
            print("After many attempts, you manage to pull open the door that was stuck.")
            print("As soon as you enter, you feel the atmosphere grow heavier; something in this cabin doesn't feel right.")
            print("You find a bed to rest on and a partially open chest.")
            choice4 = input("What do you do? Type sleep, open, or leave: ").strip().lower()
            if choice4 == "sleep":
                print("You put down your axe next to the bed, grab a nearby sack to use as a pillow, and close your eyes to sleep.")
                print("After a while, you hear the door opening. It seems the cabin’s owner has arrived.")
                print("You open your eyes and realize that the owner is actually a monster with an axe, ready to attack you.")
                print('''               (    )
              ((((()))
              |o\ /o)|
              ( (  _')
               (._.  /\__
              ,\___,/ '  ')
'.,_,,       (  .- .   .    )
 \   \\     ( '        )(    )
  \   \\    \.  _.__ ____( .  |
   \  /\\   .(   .'  /\  '.  )
    $$  \\.-' ( /    \/    $$
     '  ()) _'.-|/\/\/\/\/\|
         '\\ .( |\/\/\/\/\/|
           '((  \    /\    /
           ((((  '.__\/__.')
            ((,) /   ((()   )
             "..-,  (()("   /
        pils  _//.   ((() ."
      _____ //,/" ___ ((( ', ___
                       ((  )
                        / /
                      _/,/'
                    /,/,"
------------------------------------------------
''')
                print("You roll to the side of the bed and grab your axe.")
                choice5 = input("What do you do? Type attack, flee, or talk: ").strip().lower()
                if choice5 == "attack":
                    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄


''')
                    print("You try to attack the monster, but it is faster than you. With just one strike, you die.")
                elif choice5 == "flee":
                    print("You try to escape through the window, but it is jammed.")
                    print("After some attempts, you turn around and face the monster, now closer to you.")
                    print("It prepares to attack, but you are faster to defend yourself. After exchanging some blows, you come out victorious.")
                    print('''__   __                     _         _ 
\ \ / /__  _   _  __      _(_)_ __   | |
 \ V / _ \| | | | \ \ /\ / / | '_ \  | |
  | | (_) | |_| |  \ V  V /| | | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
          ''')
                    print("After killing the monster, you leave the cabin and realize it is already dawn; you look and see a village nearby in the distance.")
                    print("Congratulations, you have won the game.")
                elif choice5 == "talk":
                    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄


''')
                    print("You try to talk to the monster to explain the situation, but it does not understand your language.")
                    print("After a while, you just give up and accept your final fate.")
            elif choice4 == "open":
                print("After opening the chest, you see a sack full of gold coins. You take it and decide to leave the cabin.")
                print("After walking for a while, you see a village.")
                print("Congratulations, you have won the game.")
                print('''__   __                     _         _ 
\ \ / /__  _   _  __      _(_)_ __   | |
 \ V / _ \| | | | \ \ /\ / / | '_ \  | |
  | | (_) | |_| |  \ V  V /| | | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
          ''')
            else:
                print('''__   __                     _         _ 
\ \ / /__  _   _  __      _(_)_ __   | |
 \ V / _ \| | | | \ \ /\ / / | '_ \  | |
  | | (_) | |_| |  \ V  V /| | | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
          ''')
                print("After walking for a while, you see a village.")
                print("Congratulations, you have won the game.")
        else:
            print('''__   __                     _         _ 
\ \ / /__  _   _  __      _(_)_ __   | |
 \ V / _ \| | | | \ \ /\ / / | '_ \  | |
  | | (_) | |_| |  \ V  V /| | | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
          ''')
            print("After walking for a while, you see a village.")
            print("Congratulations, you have won the game.")
    else:
        print("You walk andfo walk, but you feel like you're not leaving the forest. You realize you are even more lost than when you started.")
else:
    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄


''')
    print("You walk and walk, but you feel like you're not leaving the forest. You realize you are even more lost than when you started.")
