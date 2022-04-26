import sys
import time
from time import sleep

def you_died(): #Death Tomb ASCII art
    print("""                
                                 _____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/                                       \|     |
              |                 You   Are   Dead               <
              |_____.-._________              ____/|___________|
                                | * --/--/-- |
                                | + 02/03/22 |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.!!|          -< @!!%
                           `\%`@|     v      |@@%@-!
                         .^^%@@@|%    |    % @@@!!@%@%
                    _.%@%@%@@@@@@@!@_/%\_%@@&&&@@@@@@@%@%@%""")

def slow_print(msg): #Typewriter text in place of print()
    for c in msg:
        print(c, end="", flush=True)
        time.sleep(0.05) #0.05 option to change

def typingInput(text): #Typewriter text in place of input()
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05) # 0.5 option to change
  value = input()
  return value

def play_again(): #Restart the game over
    answer = typingInput("\n Would you like to play again? ""\033[36m" "Yes/No " )
    if answer.lower() == "yes":
                escape_from_cannibal_island()
    else: 
        answer.lower() == "no"
        slow_print("\033[37m""Thank You for playing 'ESCAPE FROM CANNIBAL ISLAND'")

inventory = []
def add_to_inventory(item): #Add an item to the inventory
    inventory.append(item)

def escape_from_cannibal_island_intro_credits():
    
    time.sleep(1)
    print("""
    """)
    time.sleep(1)
    slow_print("TEAM-3 are proud to present...")
    time.sleep(1)
    print("""
    """)
    slow_print("A Python3 production...")
    time.sleep(1)
    print("""
    """)
    slow_print("Created by...")
    time.sleep(1)
    slow_print("Michael Farrell, Mujtabazeb Khan, Vladimir Matlak, Duncan James and Gareth Lloyd")
    time.sleep(2)
    print("""

    """)
escape_from_cannibal_island_intro_credits()#intro credit function, only runs at launch

def escape_from_cannibal_island():
    
    
    time.sleep(0)
    print("\033[33m"'''
        (                (         (    (       )    *     
     )\ )  (    (     )\ )      )\ ) )\ ) ( /(  (  `    
 (  (()/(  )\   )\   (()/((    (()/((()/( )\()) )\))(   
 )\  /(_)|((_|(((_)(  /(_))\    /(_))/(_)|(_)\ ((_)()\  
((_)(_)) )\___)\ _ )\(_))((_)  (_))_(_))   ((_)(_()((_) 
| __/ __((/ __(_)_\(_) _ \ __| | |_ | _ \ / _ \|  \/  | 
| _|\__ \| (__ / _ \ |  _/ _|  | __||   /| (_) | |\/| | 
|___|___/ \___/_/)\_\|)|(|___| |_|  |_|_\(\___/|_|  |_|

   (    (     ( /( ( /( )\ )  (    (     )\ )           
   )\   )\    )\()))\()|()/(( )\   )\   (()/(           
 (((_|(((_)( ((_)\((_)\ /(_))((_|(((_)(  /(_))          
 )\___)\ _ )\ _((_)_((_|_))((_)_ )\ _ )\(_))            
((/ __(_)_\(_) \| | \| |_ _|| _ )(_)_\(_) |             
 | (__ / _ \ | .` | .` || | | _ \ / _ \ | |__           
  \_(_/_( \_\|_|\_|_|\_|)_(||___//_/ \_\|____|

    )\ ))\ )   (     ( /( )\ )                          
 ( (()/(()/(   )\    )\()|()/(                          
 )\ /(_))(_)|(((_)( ((_)\ /(_))                         
((_|_))(_))  )\ _ )\ _((_|_))_                          
 (_) __| |   (_)_\(_) \| ||   \                         
 | \__ \ |__  / _ \ | .` || |) | _ _ _                  
 |_|___/____|/_/ \_\|_|\_||___(_|_|_|_)
  
    '''"\033[37m")
    slow_print('Welcome to "Escape From Cannibal Island". A TEXT-BASED Survival Game.')
    
    print("")
    answer = typingInput("Would you like to play? " "\033[36m" "Yes/No ")
    if answer.lower() == "yes":
        print("\033[37m""Great choice....Let's Begin!!!")
        print("""
                """)
        time.sleep(2)
        slow_print("\033[37m""You are the pilot of a small aircraft, flying somewhere over the Bermuda Triangle.......")
        print("""        
        """)
        slow_print("The situation is grim. You have hit some turbulence and have lost all radio contact. The instruments in the cockpit have gone completely haywire...")
        slow_print("You begin \nspriralling out of control and plunge from the sky towards the earth.......")
        print("\033[37m"""")                                       
                                                !#GJ7^.          :^!!.                              
                                                .5JP?J?7^.     :?5J?55                              
                                                 !7JP77?JJ?^.^?J?777JY                              
                                                  ?^?57777?JPP?77??JP?                              
                                                  .J.Y57777JPJ7?PYY5PYJ7!~!.                        
                                                   :?.G57?55?7JPJ77777?JJYGP                        
                                                    ~?!BP5J775P??JJJJJ??77~:                        
                                                   .!5YJ?777?P5YPYP7^:..                            
                                                  ^JJ777YJJ777???57                                 
                                                ~J?7777YGJYY77775?                                  
                                              :5Y?777YJ?YGG?777YJ                                   
                                             7PJ777?PB5YJJ?777?Y                                    
                                           :55?7777?JPBGY7777?5:                                    
                     .                     ^7?PJ?J??775&YYJ775~                                     
      :^~~^^^::^~~!!7??J5J~.            7YJJ7?Y?JGJ?57?BJ!75P7                                      
      5B55YJ?????????J5PB##G?^   .^~~::J5?7777??7?PJ5J7P~^?P7                                       
      .^7PGB5Y???777777JJJ???Y5?JYJJJ55?7777?YBJ???Y?7J?Y!::          .:^~~7JP5?7!^^:.              
    .... . :~JP5JJJJYJ?77JYYJ?JJJ???P#5YJ777?GG575?75??JY5.::    .:~??JJ???YGPP&#G#P?GG^:!^:.       
 :7JJJ?JP^     ^^~!!?YPPPY??JPYJJJG555P5YJY777JPB5777P^5BYJJ?J???JJJ??77777J??5J?5?7PBP5YJ?????77!^ 
?5JJJYJ?7. .^.      :?5J?7777JPY^!BY?7?JJ?J5???JYJ??7JG5JJY?JG#5YYYYYJYYYJ?????????Y5J??????????JYPY
:..^~:.7?YYYPY    ^YYJ?7??????JYG:^JYYJ7?Y5GB5YJJYYYYYP?!?YGGPYJJ?777~!7!77??JJJJ?J?777???????????YY
      .^:^~!!^    ~7!77??JJYYJ?7!  .~YYYP77577JYYYY555B5YY?P5JJJ??J77:       ....................   
             .:^!7???!: ..::.    :7??JYPY^     ...:^^~!:.   :~!7?BYJPY                              
      :!~!7???JJ55J?7Y!         .5YJ?777?JJ7^.                 .^?~^:.                              
      ?#BY??????JYY?7~^^.        .^7J????77?J??~.                                                   
      .^JY??JY7?JYJ?J?JJJ5Y         :^!7JYYJJJJJ?77~                                                
         ..   .?5BGYJJ?7!7!            .:~!~7?7JY?J5^                                               
              .GY?!~^:.                        ..                                                   
              """)
        
        slow_print ("""\033[37m You have awoken on the beach of what appears to be a deserted tropical island. \n The beach is surrounded by dense jungle and a large mountain is seen looming in the distance. \n With a sore head, you glance towards the setting sun and notice a winding path that leads to the top of the mountain...\n Could this be a path to safety? \n Bewildered, injured and frightened, you frantically look around your immediate area.\n Rubbing the blood and debris from your eyes, you see the wreckage of a small airplane, still smouldering from a fiery crash.""")
        
        print("")
        answer = typingInput(" You are cold and in need of shelter.\n Do you want to check the ""\033[36m" "Wreckage ""\033[37m" "for anything that may come in handy or proceed into the " "\033[36m" "Jungle ""\033[37m" "in search of food and shelter? ""\033[36m")
        print("")
        if answer.lower() == "wreckage":
            slow_print("\033[37m"" You search the wreckage and find a pocket knife and an old radio that still appears to be working...""\033[32m")
            add_to_inventory("pocket knife")
            add_to_inventory("old radio")
            time.sleep(4)
            print("\033[037m""""                           
                                                _________________________
             __,,..,-           _,.--''------'' |   _____  ______________`''--._
            \      `\   __..--''                |  /::: / /::::::::::::::\      `|
             \       `''                        | /____/ /___ ____ _____::|    .  |
              \                           ,.... |            `    `     \_|   ( )  |
               `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
                 `.                     |        ,'       `               `-.      |
                   `-._                 \                                    ``.. /
                       `---..............>""") 
            time.sleep(2)
            print("""
                         () 
                         ||
                         ||
                   ______||
                  / ____ o|
                 | / ;; \ |
                 | ______ |
                 ||______||
                 ||      ||
                 || #SOS ||
                 ||______||
                 |'\[--]/'|
                 |  ¨''¨  |
                 |  ''''  |
                 |        |
                 |        |
                 |        |
                 |________|
                           """)
            time.sleep(2)
            print("\033[32m""INVENTORY:")
            print(inventory)
            answer = typingInput("\033[37m""You hear some voices from afar, somewhere deep in the jungle. Could there be some survivors?\nThere is a mountain path in the distance that appears to be safe. \nDo you head up the ""\033[36m" "mountain path "  "\033[37m"" or follow the voices deeper into the " "\033[36m""jungle? ")
            if answer.lower() == "mountain path":
                head_up_mountain()
            elif answer.lower() == "jungle":
                head_into_the_jungle()
            else:
                slow_print("\033[37m""You are indecisive and have been standing too long in one spot... you are a mauled to death by a wandering bear")
                slow_print("\nYou Died!")
                inventory.clear()
                you_died()
                play_again()

            inventory.clear()
        elif answer.lower() == "jungle":
                head_into_the_jungle()
        else:
            slow_print("\033[37m""Incorrect choice, the game has restarted, pay attention and read carefully!")
            escape_from_cannibal_island()
            
        print("")
            
    else:
        slow_print("\033[037mYou Coward!")

def head_into_the_jungle():
    answer = typingInput("\033[37m""You head into the jungle towards the voices you hear in the distance.\nYou are curious and begin to wonder if the mysterious voices you are hearing are friendly...\n""Do you ""\033[36m""investigate ""\033[37m""the mysterious voices or head into the ""\033[36m" "jungle" "\033[37m"" in search of shelter and food? ""\033[36m")
    if answer.lower() == "jungle":
        slow_print("\033[37m"" You go deeper into the jungle, becoming frustrated, disoriented and lost.....\n After walking for hours in circles,  you just give-up and collapse to the ground, helpless.. \n You eventually succumb to the elements and your corpse is eaten by wandering animals...and possibly humans!")
        print("")
        slow_print(" You Died...")
        you_died()
        play_again()
        inventory.clear()
        
    elif answer.lower() == "investigate":
        slow_print("\033[37m""Creeping towards the sound of the voices, \nyou step on a branch which makes a loud snapping noise....")
        
        time.sleep(1)
        slow_print("OH NO !!! A figure in the distance has heard you! \nIt's your worst nightmare...You have been spotted by a tribe of cannibals!!!")
        print("""
        
        """)
        time.sleep(1.5)
        print("""
   \\\|||///
 .  ======= 
/ \| O   O |
\ / \`___'/ 
 #   _| |_
(#) (     )  
 #\//|* *|\\ 
 #\/(  *  )/   
 #   =====  
 #   ( U ) 
 #   || ||
.#---'| |`----.
`#----' `-----'  
         
           """)
               
        slow_print("You look weak, tasty and unable to defend yourself. You are quickly captured and bound with rope...")
        slow_print("\nHelpless and bound, you sit and watch as they prepare a cauldron in which to boil you alive.\nIt seems you are the main course for dinner!")
        
        time.sleep(1.5)
        print("""
           (
               )  )
           ______(____
          (___________)
          |/         \|
         |/  Cannibal \|
         |    Stew     |
     ____\             /____
    ()____'.__     __.'____()
         .'` .'```'. `-.
        ().'`       `'.()
        
        """)
        time.sleep(1.5)
        print("""        
      .-.                                             .-.
     (o.o) \\\W///                             \\\V/// (o.o)
      |=|  #######                           #######  |=|
       Y  //9 , 9\\                          //6 , 6\\   Y
       |   \  =  /                           \  =  /   |
       8'---:---:-.                         .-:---:---'B
       |'--, `&`   \         (             /   `@` ,--'|
       |   |'   '|> )         )  )        ( <|'   '|   |
       |   \__.__/ /      ______(____      \ \__.__/   |
       |   />>>>>\`      (___________)      `/|||||\   |
       |  (<<<<<<<)       /         \       (|||||||)  |
       |  `"|"|"|"`      /           \      `"|"|"|"`  |
       |    | |_|       |             |       |_| |    |
       |    | |_)   ____\             /____   (_| |    |
       |  .-' | '-.()____'.__     __.'____().-' | '-.  |
          `''''''''`     .'` .'```'. `-.    `'''''''`
                       ().'`       `'.()
""")
    
        print("\033[32m""INVENTORY:")
        print(inventory)
        answer = typingInput("\033[37m""Is there anything you can use in your inventory to help you escape this terrible ordeal?""\033[32m ")
        if answer == "pocket knife":
            if "pocket knife" in inventory:
                slow_print("\033[37mYou manage to cut yourself free with the pocket knife you found earlier in the wreckage.")
                slow_print("\nYou quickly sneak away....but wait!")
                answer = typingInput("\nOn your way out of the village, you notice a spear leaning against a hut. \nDo you risk being heard again and take the spear? ""\033[36m""Yes/No ")
                print("\033[37m""""
                                                                           |''''''----....____
                                                                           |              ''''---...___
----------------------------------------------------------------------------\                          ""--..__
=============================================================================|                                  "-._
----------------------------------------------------------------------------/---------------------------------------`   
                      """)
                time.sleep(3)
                if answer == "yes":
                    add_to_inventory("spear")
                    print("\033[32m""INVENTORY:")
                    print(inventory)
                    slow_print("\033[37m""You grab the spear and begin your frantic escape from the jungle. \nYour only thought is to somehow make your way towards the mountain path to safety.")
                    head_up_mountain()
                else:
                    slow_print("You leave the spear behind and quietly sneak away...")
                    slow_print("Luckily nobody hears you...\nYou escape into the jungle and make your way up the mountain path")
                    head_up_mountain()
        else:
            slow_print("\033[37mYou are unable to escape your bounds. \nYou were slowly cooked and eaten by the cannibal tribe.")
            slow_print("\nYou Died...")
            you_died()
            play_again()
            
    else:
        slow_print("\033[37m""Your indecision meant you spent too long in one spot, you are a mauled to death by a wandering blood-thirsty bear.")
        slow_print("\n\033[37mYou Died!")
        you_died()
        play_again()
        print("")            
        inventory.clear()
        

def head_up_mountain():
    slow_print("\033[37m""\nYou begin to make your way up the long mountain path, trembling with fear and anxiety.\nYou wonder if you are safe to stop, but you are too exhausted to keep climbing the mountain path. \nYou stop for a quick break, finally thinking you are safe...")
    slow_print('"Phew..." You say to yourself.. "That was close!".....')
    time.sleep(4)
    slow_print("\nYou are quietly resting, thinking about the lousy predicament you are in, when suddenly a giant grizzly bear appears on the path in front of you! \nThe wild beast is hungry, growling and ready to eat you alive!")
    time.sleep(3)
    print(""" 
                       / _.'               `.  ;/ _(
                      ;,'     ;    `.        `.;    `-.
                     ;' .'   :    `. `.       / \, \ \ |
                     :,'     :      `. `. \  ; ::\_/_/_/::
                   .-=:.-"  -,-   "-.,=-.\ ;.; :::; ; ;::
                   |(`.`     :       .')| \: `.  :::::::
                    \\/      :       \//   ;   \              
                     :      .:.       :  _/     ;             
           /         ;                ;  ;      |              
         .'          :    _     _    ;  /       ;              /|
        /             `.  \;   ;/  .' .'       /              /:|
       |                !  :   :  !_.'        /           .--::/
       |\___             `.:   :.'/\         ;      ____.':|:|/
       \:::|\              \ _ /  | :       :   ___/|:::|:''''
        `  |:\             ;'^''   | !       :__/|::|/''''
           \::\_____     .-'      | ;       |::|/''
            \:|::::|\   / / /    / /       /'''
             \|::::|:`--\_\_\__.'-|       ;
               '''' \::::::::::::/      .'
                     ''''''''''.-'      (
              __,------.__.--/ , ,  , |/--._
             /              :\|  |  |v'     \_
            |\              :::v-;v-'::       |
            \:\              :::::::::         |
             \|`-.                             /|
               `: \          ____         ____/:/
                 \|:-.______/|::|\       /|:::|/
                  |::|:::::|:/'''\\_____/:/---
                  `-:|:::::|/     \|::::|/
                     `-----'       `-----""")
    print("\033[32m""INVENTORY:")
    print(inventory)
    answer = typingInput("\033[37m""The bear will surely maul you to death. \nThere must be something that you can use to defend yourself from this crazed animal...But what? ""\033[32m")
    if answer.lower() == "spear":
        if "spear" in inventory:
            slow_print("\033[37mGreat choice. The spear is very useful.\nYou manage to dispatch the bear quite easily and thwart it's attacks with deft precision\nThe length of the spear allows you to stab the bear to death at range... \nIt's a scene too gruesome to picture...\nThe bear is eventually neutralised. ")
            time.sleep(3)
            

            print("""
            
            """)
            print("\033[37m""""  

                       /_\       
                      /   \               _/ \           
         _        .--'\/\_ \             /    \      ___
        / \_    _/ ^      \/\'__        /\/\  /\  __/   \ 
       /    \  /    .'   _/  /  \     /    \/  \/ .`'\_/\   
      /\/\  /\/ :' __  ^/  ^/  \ `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^\____ \_   .'\   _/ \ .  __/ |_
   /\  .-   `. \/     \ / -.   _/ \ -\ \`_/   \ /    `._/  ^  
  /  `-.__ ^   / .-'.--'    . /    `--\.\/ .-'  `-.  `-. `.  -  `.
 /        `.  / /      `-.   /  .-'   /\ \.   .'   \    \  \  .- 
                                        \ \ _ _ _
                                         \_ The Mountain Path...
            """)
            
            print("")
            slow_print("You continue up the mountain path, keeping an eye out for man-eating humans and blood-thirsty bears...\nYou eventually reach the top of the great mountain, exhausted you drop to your knees...")
            answer = typingInput("Is there anything in the inventory we could use to signal for help? ""\033[32m")
            if answer.lower() == "old radio":
            
             time.sleep(3)
             print("""                                                                       
                                                                       
   SSSSSSSSSSSSSSS           OOOOOOOOO             SSSSSSSSSSSSSSS     
 SS:::::::::::::::S        OO:::::::::OO         SS:::::::::::::::S    
S:::::SSSSSS::::::S      OO:::::::::::::OO      S:::::SSSSSS::::::S    
S:::::S     SSSSSSS     O:::::::OOO:::::::O     S:::::S     SSSSSSS    
S:::::S                 O::::::O   O::::::O     S:::::S                
S:::::S                 O:::::O     O:::::O     S:::::S                
 S::::SSSS              O:::::O     O:::::O      S::::SSSS             
  SS::::::SSSSS         O:::::O     O:::::O       SS::::::SSSSS        
    SSS::::::::SS       O:::::O     O:::::O         SSS::::::::SS      
       SSSSSS::::S      O:::::O     O:::::O            SSSSSS::::S     
            S:::::S     O:::::O     O:::::O                 S:::::S    
            S:::::S     O::::::O   O::::::O                 S:::::S    
SSSSSSS     S:::::S     O:::::::OOO:::::::O     SSSSSSS     S:::::S    
S::::::SSSSSS:::::S      OO:::::::::::::OO      S::::::SSSSSS:::::S    
S:::::::::::::::SS         OO:::::::::OO        S:::::::::::::::SS     
 SSSSSSSSSSSSSSS             OOOOOOOOO           SSSSSSSSSSSSSSS       
                                                                       
                                                                       
             
            """)         
            print("You use the old radio you found in the wreckage to try and call for help. \nThankfully, you hear a faint crackled reply from the radio and realise that your cries for help have been heard! \nYou rejoice and sing with glee, the ship in the distance is coming to rescue you! \nAs the rescue ship finally approaches and the tears of joy stream down from your weary eyes, a sudden panic begins to sink in... \nYou realise that the men coming to rescue you, are not rescuers at all! \nIn fact, the men coming towards you are a motley crew of pirates!")
            print('"Seriously....What are the odds...?" you think to yourself...')
            print("""
            
            """)
            time.sleep(6)
            print("""
 ()                                
 ||-.,.,.,.,,.,.,...-'" ;                     Ahoy!
 ||     _          _    |          /(o)\       Ahoy!  
 ||   _( )        ( )_  |         /  ()/ /)
 ||  (_  \ /\\//\ / ._) |        /.;.))'".) 
 ||    '\ ( o)(o ) /    |       //////.-'
 ||       \\//\\//      |   =====))=))===() 
 ||        .))((.       |     ///'       
 ||      _/ |||| \_     |    //  
 ||    ('  /''''\  ')   |   '           
 ||     "(_)    (_)"    |    
 ||-.,.,.,.,.,.,.,.,..-' 
 ||   
 ||  
 ||   
 || """)
            slow_print("In your weakened state, you are unable to defend yourself from the hungry pirates. \nThe pirates have now captured you...\nOnce again you are bound with rope and taken on board of their nearby vessel!")
            slow_print("")
            slow_print(" Congratulations, you have now 'Escaped from Cannibal Island!' \nWe hope you had fun!")
            print("")
            slow_print("Is there anything you can do to save yourself from this terrible ordeal?'")
            print("")
            slow_print("Stay tuned for the upcoming sequel from Team3 - 'Escape from the Cannibal Pirates!'")
            print("""            
            """)
            slow_print("Thank you for playing 'Escape From Cannibal Island'")
            play_again()
            inventory.clear()
            
        elif "spear" not in inventory:
            slow_print("You have nothing useful in your inventory to defend yourself.  You are easily caught by the blood-thirsty bear. \n You are brutally mauled to death and eaten for dinner, such a sad ending.....")
            inventory.clear()
            you_died()
            play_again()   
            
    elif answer.lower() == "pocket knife":
        if "pocket knife" in inventory:
         slow_print("\033[37m""You pull out the pocket knife, a useless weapon that cuts your hand as you take a pathetic swipe at the bear\nYou manage to hurt the wild beast, but unfortunately your knife is no match for the blood-thirsty bear.\nYou are brutally mauled to death and eaten for dinner, such a sad ending.....")
         slow_print("\nThank You for playing 'ESCAPE FROM CANNIBAL ISLAND'")
         inventory.clear()
         you_died()
         play_again()

    elif answer.lower() == "old radio":
        if "old radio" in inventory:
            slow_print("\033[37m""You pull out the old radio, wondering if this would help? Maybe it likes music?\nYou throw the radio at the bear hoping to scare it off...")
            time.sleep(1)
            slow_print("\nUnfortunately this just angers the bear even more, you get brutally mauled to death and eaten for dinner.")
            slow_print("\nThank You for playing 'ESCAPE FROM CANNIBAL ISLAND'")
            inventory.clear()
            you_died()
            play_again()
    else:
         slow_print("You have nothing useful in your inventory to defend yourself. You are easily caught by the blood-thirsty bear")
         slow_print("You are brutally mauled to death and eaten for dinner, such a sad ending.....")
         slow_print("\nThank You for playing 'ESCAPE FROM CANNIBAL ISLAND'")
         inventory.clear()
         you_died()
         play_again()


escape_from_cannibal_island()
