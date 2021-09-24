# The Missing Notebook by Terra

init -200 python:
    skit_template = Skit(
        "The Missing Notebook",
        "terra_ddcc",
        "club_date",
        "@Terra#2060, /u/wingedterra",
        skit_position = 6
    )
    skits.append(skit_template)


label terra_ddcc(preserve_transition=True):

    # Stuff this does!:
        # Imagemap/hotspots and how they work
            # Related, how to use them to make an interactable environment
        # The "tear" glitch effect
        # "Edited" style dialog
        # Hard pauses - forcing the player to wait the duration of the pause
        # Timers in screens - do an action after a specified length of time
        # Also featured - questionable quality writing
    python:
        #Variable initialization 
        poster_clicked = 0
        cookie_clicked = 0
        natsu_clicked = 0
        skill_clicked = 0

    stop music fadeout 2.0
    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    play music t3
    show monika 5a at f11 zorder 2
    m "Hi, [player]!"
    m "I was wondering if you could help me with something before club meeting today."
    mc "Sure, Monika, what's up?"
    m 3a "After the festival, we packed up everything in the closet."
    m 1p "And well, now I can't find my notebook. Do you mind looking for me?"
    mc "Sure thing."
    "That's strange.."
    "Try as I might, I can't seem to walk away from her.."
    m 1l "Oh, that's right, you can't actually walk around.."
    m "Hold on one second. I can fix that."
    $ srf = screenshot_srf()
    show screen tear(20, 0.1, 0.1, 0, 40, srf)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    stop sound
    stop music
    hide monika
    jump walkabout_1
    return

label walkabout_1:
    play music t4
    call screen walkabout_1() #Calling a screen (as opposed to "show") prevents the player from being able to dismiss it, which is the desired effect here.
    screen walkabout_1():
        imagemap:
            #How-to imagemap:
            #Ground is what you want the background image to be.
            #The numbers in hotspot are (xpos,ypos,width,height) of the interactable rectangle.
            #You can easily generate these values with the "Image picker" tool in the dev menu (shift + D)
            #You'll have to scroll through -all- the images in the game till you find your ground image.
            #Preferably, we'd use the "Call" action here instead of "Jump". However, the Call screen action is bugged or not implemented in 6.99.12 and doesn't work; forcing us to do flow control ourselves with Jump instead.
            #I wanted it to be incredibly obvious when you moused over something interactable, so I made the hotspots make the button hover sound when you mouse over them.
            ground "bg/club.png"
            hotspot (915, 278, 121, 176) action Jump("closet_inv") hover_sound gui.hover_sound
            if skill_clicked == 0: #Each time the hotspot is interacted with, the variable increases by 1. This if statement makes the hotspot interactable twice, then goes away.
                hotspot (785, 277, 80, 66) action Jump("poster_desc") hover_sound gui.hover_sound
            elif skill_clicked == 1:
                hotspot (785, 277, 80, 66) action Jump("poster_desc_2") hover_sound gui.hover_sound
        #I wanted to make it pretty obvious what was going on, but just in case - this will pop up a dialog box after 30 seconds if the player hasn't figured out what's up.
        #This also helps conform to the time limit in the guidelines.
        timer 30.0 action Show(screen="dialog", message="It seems you might be stuck. Helpful hint: Click the closet.", ok_action=Hide("dialog"))
    return

label closet_inv:
    stop music fadeout 2.0
    scene bg closet
    with dissolve_scene_full
    play sound audio.closet_open
    $ renpy.pause(delay=1.0, hard=True)
    play music t4
    call screen walkabout_2()
    screen walkabout_2():
        imagemap:
            ground "bg/closet.png"
            hotspot (457, 237, 30, 49) action Jump("monika_notebook") hover_sound gui.hover_sound
            if poster_clicked == 0:
                hotspot (698, 376, 106, 111) action Jump("yuri_poster") hover_sound gui.hover_sound
            elif poster_clicked == 1:
                hotspot (698, 376, 106, 111) action Jump("yuri_poster_2") hover_sound gui.hover_sound
            if cookie_clicked == 0:
                hotspot (726, 537, 82, 88) action Jump("cookie_box") hover_sound gui.hover_sound
            elif cookie_clicked == 1:
                hotspot (726, 537, 82, 88) action Jump("cookie_box_2") hover_sound gui.hover_sound
            if natsu_clicked == 0:
                hotspot (643, 263, 76, 66) action Jump("natsu_prons") hover_sound gui.hover_sound
            elif natsu_clicked == 1:
                hotspot (643, 263, 76, 66) action Jump("natsu_prons_2") hover_sound gui.hover_sound
    return

label poster_desc:
    "There's something strange about this particular chart."
    "I can't really put my finger on it, though.."
    "Maybe if I hang around long enough, it'll come to me."
    $ skill_clicked += 1
    call screen walkabout_1()
    #As mentioned before, we have to call the screen back up at the end of these labels because we don't have the Call screen action.
    #If we did, we could just Return at the end here.
label poster_desc_2:
    show monika 2m at t11 zorder 2
    m "[player]?"
    m "What's so interesting about that chart?"
    show monika 2n at t11 zorder 2
    m "It's not going to magically change into something else..."
    show monika 1h at t11 zorder 2
    m "...Like my notebook."
    $ skill_clicked += 1
    show monika at thide zorder 1
    hide monika
    call screen walkabout_1()

label monika_notebook:
    jump ending

label yuri_poster:
    "This is the banner Yuri and I made for the festival."
    "I'm gonna take a stab in the dark and say she would want this left here."
    $ poster_clicked += 1
    call screen walkabout_2()
label cookie_box:
    "This box has a bunch of flyers for the Culinary Arts club in it."
    "I notice something poking out underneath them."
    "....A pile of cookies?"
    "Oh, right, Sayori..."
    $ cookie_clicked += 1
    call screen walkabout_2()
label natsu_prons:
    "This box looks like it has more of Natsuki's manga in it."
    "I wonder why they're not lined up on the shelf with the others..."
    stop music
    play sound audio.page_turn 
    "....what's \"Yaoi\"?"
    #This is just directly copy/pasted from Act 3 with some of the glitchy particles taken out.
    #...I may have had too much fun with this.
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    $ renpy.pause(delay=2.5, hard=True) #Setting hard=True prevents the player from clicking through the pause.
    "{i}We will never speak of this.{/i}"
    play music t4
    $ natsu_clicked += 1
    call screen walkabout_2()
label yuri_poster_2:
    "I'm leaving the banner alone."
    "Not about to upset the girl with a knife collection..."
    $ poster_clicked += 1
    call screen walkabout_2()
label cookie_box_2:
    "I taste test one of the cookies."
    "It's... {i}really good.{/i}"
    "Okay, leaving that alone now."
    "The last thing I need is Monika catching me eating cookies instead of finding her notebook."
    $ cookie_clicked += 1
    call screen walkabout_2()
label natsu_prons_2:
    $ style.say_dialogue = style.edited
    "There is nothing in the world that would make me open that box again."
    $ style.say_dialogue = style.normal
    $ natsu_clicked += 1
    call screen walkabout_2()

label ending:
    "Ah, here it is."
    "I should get this back to Monika now."
    "I wonder what she needed it for.."
    return