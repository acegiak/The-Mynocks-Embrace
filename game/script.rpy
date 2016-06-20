# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


# Declare characters used by this game.

define m = Character('Me', color="#ffffff")


define b = Character('Bacta', color="#aaaaff")
define tam = Character('Tamlin', color="#aaaaaa")
define t = Character('Tryst', color="#ffffaa")
define l = Character('Leenik Geelo', color="#aaffaa")
define lyn = Character('Lyn', color="#ffccaa")



# The game starts here.
label start:

    $ marked_for_death = False

    "You enter the suspicious Skipray Blastboat with the word \"Mynock\" painted on the side over terrible camoflage patterns"
    "Immediately you glance around the hallway and then back outside the ship. There are too many doors here."
    
    "A clone appears, cleaning his hands on a rag"

    b "Oh! Hallo there inspectah!"
    b "We weren't expecting you until this evening! I think leenik was planning on making a roast!"
    b "Not that that's necessarily a good thing..."

    tam "Uncle Bacta! Uncle Bacta!"
    "A zabrak child hurtles around the corner, nearly colliding with the clone."
    tam "Uncle Bacta, Uncle Lyn says we need to stash the lizards are endangered so we need to hide them before the inspector - oh!"
    
    "The clone looks sheepish."
    b "Uh, excuse me inspectah, I need to help Tamlin... Tidy his room. Maybe you should head up to the kitchen, I'm sure Leenik will make you some tea."

    jump awkward_hallway

label awkward_hallway:    
    menu:
        "Head up to the kitchen":
            jump kitchen
        "Follow the clone":
            jump quarters
        "Forcibly kiss the clone":
            jump clone_passion
    
    return

label clone_passion:
    "You kiss the clone, he is flustered, apologises and hurries away."
    $ marked_for_death = True
    jump awkward_hallway
    return

label kitchen:
    "A Rodian stands arranging some kind of ceramic avian trinkets. He wears an obvious wig, an eyepatch and an apron over his space onesie."
    
    l "Oh! Hi! I'm Leenik Geelo, wanted bounty hunter!"
    return

label quarters:
    "The clone turns a little down the hall, opens one of the doors and heads inside. You sneakily follow him."
    if marked_for_death:
        "As you try to make your way through the door, a tidal wave of lizards tumbles out, knocking you backwards, as you fall you hit your head on a piece of loose piping."
        "Nearby a blonde man peeks his head around a corner."
        t "Shotgun NOT disposing of the body!"
        jump dead
         
    b "huh? Sorry, Inspectah, I thought you were going to the kitchen."
        
     

label dead:
    "You have passed away. Another piece of collateral damage in the STAR WARS."

    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    "It took you %(minutes)d minutes and %(seconds)d seconds for death to find you."
           
    $ renpy.full_restart()
        