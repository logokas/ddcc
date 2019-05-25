# "The Annoying Printer" By AinsleyHairyott
# Enabling voices is recommended.
# For Developer comments, check in script_cokie.rpy


define audio.printer_sfx_print = "mod_assets/printer/printer_sfx_print.wav" #Printer SFX from Team Fortress 2
define audio.printer_sfx_pickup = "mod_assets/printer/printer_sfx_pickup.wav" #Pick up SFX from Half life
define audio.printer_bgm01 = "<to 74.341 loop 5.777>mod_assets/printer/printer_bgm01.ogg" #DDLC - Poem Panic! (Act 2) by SiIvaGunner
define audio.printer_sfx_error = "mod_assets/printer/printer_sfx_error.ogg" #Windows XP Error SFX.
image printer_p_printer = "mod_assets/printer/printer_p_printer.png" #A printer I just found in google. Can't remember the name of it.
image printer_p_magenta = "mod_assets/printer/printer_p_magenta.png" #A Magenta cartridge I also just found in google.
image printer_thumbnail = im.FactorScale("mod_assets/printer/printer_thumbnail.png", 0.3, 0.3) #Thumbnail

#List of Text-To-Speech (Paul) voices below by Oddcast.
define audio.printer_v01 = "mod_assets/printer/printer_v01.ogg" # "Printing error. Give me the magenta ink."
define audio.printer_v02 = "mod_assets/printer/printer_v02.ogg" # "I said give me the magenta ink now."
define audio.printer_v03 = "mod_assets/printer/printer_v03.ogg" # "Magenta!"
define audio.printer_v04 = "mod_assets/printer/printer_v04.ogg" # "Now give me cyan ink."

#########
#   NOTE FROM THE DEV: Is defining text style allowed like this? although it doesn't appear in the guidelines so is it ok?
style printer_text is splash_text:
    size 30
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#888", 0, 0), (2, "#888", 2, 2)]
image printer_text01 = ParameterizedText(style="printer_text", xalign=0.5, yalign=0.5)
#   I'm not changing the text style in the window, I'm adding captions above the printer.
#########



init -200 python:
    skit_printer = Skit(
        "The Annoying Printer", 
        "script_printer", 
        "printer_thumbnail" 
    )

    skits.append(skit_printer) 

label script_printer(preserve_transition=True):

    scene bg club_day
    show black zorder 9
    if preserve_transition == True:
        with wipeleft
    window hide(None)
    $ renpy.music.set_volume(1)
    play music t6
    show bg club_day:
        subpixel True
        zoom 1.6 xcenter 350 ycenter 330
        easein_circ 2 zoom 1.4 xcenter 400
    show vignette:
        alpha 1
        linear 1.6 alpha 0
    show black:
        alpha 1
        linear 2 alpha 0
    pause 0.8
    "It's a usual day at the Literature Club."
    "Natsuki is rummaging around the closet, looking for her manga."
    "Meanwhile, Monika is assembling her poetry pam-{nw}"
    show layer master:
        subpixel True
        parallel:
            xoffset -15
            easein_elastic 0.75 xoffset 0
        parallel:
            yoffset -15
            0.05
            easein_elastic 0.75 yoffset 0
    show layer screens:
        subpixel True
        parallel:
            xoffset -4
            easein_elastic 0.75 xoffset 0
        parallel:
            yoffset -4
            0.05
            easein_elastic 0.75 yoffset 0
    n "{cps=75}{i}Monika!!{/i}{/cps}"
    "Natsuki's voice resonates out from inside the closet."
    "She seems to be annoyed by something."
    show layer master 
    show layer screens
    window hide(None)
    window auto
    show bg club_day:
        subpixel True
        zoom 1.4 xcenter 400 ycenter 330
        easein_back 1 zoom 1.6 xcenter 315
    with None
    scene bg closet:
        subpixel True
        truecenter
        zoom 1.05 xcenter 690
        easein_back 1 zoom 1.125 xcenter 660
    show natsuki 1f at i11:
        subpixel True
        ycenter 360
        zoom 1 xcenter 700
        easein_back 1 zoom 1.185 xcenter 640
    with Dissolve(0.5)
    window show(None)
    n "Did you move my manga again?!"
    n 5x "Ugh...! You're such an irritating mutt sometimes!"
    n 5c "Look."
    show bg closet:
        subpixel True
        truecenter
        zoom 1.125 xcenter 660 ycenter 360
        ease 2 zoom 1.35 ycenter 390
    show natsuki at i11:
        subpixel True
        truecenter
        zoom 1.185
        ycenter 360
        ease 2 zoom 1.75 ycenter 425
    n "I don't care if the teacher got mad at you and you had to organize it."
    show bg closet:
        subpixel True
        truecenter
        zoom 1.35 xcenter 660 ycenter 390
        xoffset -10 yoffset -10
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.075
            easein_elastic 0.75 yoffset 0
    show natsuki at i11:
        subpixel True
        truecenter
        zoom 1.75 ycenter 425
        xoffset -25 yoffset -25
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.075
            easein_elastic 0.75 yoffset 0
    show layer screens:
        subpixel True
        xoffset -6 yoffset -6
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.075
            easein_elastic 0.75 yoffset 0
    n 5b "You just organized my manga collection and placed them on the ceiling. Making it difficult for me to reach it!"
    n 5g "So, why don't you bring my manga and put it on somewhere else I can reach?"
    window hide(None)
    show bg closet:
        subpixel True
        zoom 1.35 xcenter 660 ycenter 390
        easein_circ 0.5 zoom 1.05 xcenter 690 ycenter 360
    show natsuki at i11:
        subpixel True
        zoom 1.75 xcenter 640 ycenter 425
        easein_circ 0.5 zoom 1.05 xcenter 700 ycenter 360
    with None
    scene bg club_day:
        subpixel True
        zoom 1.6 xcenter 315 ycenter 330
        easein_circ 0.5 zoom 1.4 xcenter 400
    with Dissolve(0.35)
    pause 0.15
    show bg club_day:
        subpixel True
        zoom 1.4 xcenter 400 ycenter 330
        ease 0.5 xcenter 800
    show monika 1d at i11:
        subpixel True
        zoom 1.1 xcenter -600 ycenter 370
        ease 0.5 xcenter 350
    pause 0.65
    show monika 1l at i11:
        subpixel True
        zoom 1.1 xcenter 350 ycenter 370
        yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    m "Ah, sorry, Natsuki!"
    m "I shouldn't have done that."
    m 3l "I forgot there are empty sections on the lower shelf I can place them."
    m 1b "I'll be there in a moment, but I'm printing the poetry pamphlets."
    show monika 1b at i11:
        subpixel True
        zoom 1.1 xcenter 350 ycenter 370
        ease 1 xcenter 775
    show monika 1a at i11 zorder 1 as m1: 
        subpixel True
        zoom 1.1 xcenter 350 ycenter 370
        alpha 0
        parallel:
            ease 1 xcenter 775
        parallel:
            ease 0.5 alpha 1
    show bg club_day:
        subpixel True
        zoom 1.4 xcenter 800 ycenter 330
        ease 1 xcenter 895
    show printer_p_printer:
        subpixel True
        xzoom -1
        zoom 0.25 xcenter -225 ycenter 500
        parallel:
            ease 1 xcenter 300
        parallel:
            xoffset -10 yoffset -10
            parallel:
                easein_elastic 0.45 xoffset 0
            parallel:
                0.05
                easein_elastic 0.45 yoffset 0
            parallel:
                0.4
                xoffset -10 yoffset -10
                parallel:
                    easein_elastic 0.45 xoffset 0
                parallel:
                    0.05
                    easein_elastic 0.45 yoffset 0
            repeat
    play sound printer_sfx_print fadein 1
    pause 2.5
    stop sound
    stop music
    play sound printer_sfx_error
    show printer_p_printer:
        subpixel True
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        xoffset 0 yoffset 0 yzoom 1
        easein 0.02 yoffset -50 yzoom 1.5
        easein_elastic 0.75 yzoom 1 yoffset 0
    pause 0.8
    play sound printer_v01
    show printer_p_printer:
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        yoffset 0
        0.05
        yoffset -30
        0.15
        yoffset 0
        0.1
        yoffset -30
        0.15
        yoffset 0
        0.05
        yoffset -30
        0.2
        yoffset 0
        0.01
        yoffset -30
        0.09
        yoffset 0
    pause 0.05
    show printer_text01 "Printing error." as p1:
        xcenter 200 ycenter 225
    pause 0.75
    show printer_p_printer:
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        0.35
        yoffset -30
        0.1
        yoffset 0
        0.2
        yoffset -30
        0.05
        yoffset 0
        0.05
        yoffset -30
        0.15
        yoffset 0
        0.05
        yoffset -30
        0.25
        yoffset 0
        0.025
        yoffset -30
        0.075
        yoffset 0
        0.05
        yoffset -30
        0.2
        yoffset 0
    pause 0.3
    show printer_text01 "Give me the\n{color=#ff99ff}magenta{/color} ink." as p1:
        xcenter 200 ycenter 225
    pause 1.5
    hide p1
    play music printer_bgm01
    $ renpy.music.set_volume(0.75)
    hide m1
    show monika 1c at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    window show(None)
    m "Eh?"
    m "...Magenta?"
    show monika 1d at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        yoffset 0
        easein 0.25 yoffset 15
        easeout 0.25 yoffset 0
    m "You're supposed to print in black, not magenta."
    window hide(None)
    show layer master:
        topleft
        zoom 1.3 ycenter 300
    show bg club_day:
        zoom 1.3 xcenter 825 ycenter 350
    play sound printer_v02
    show printer_p_printer:
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        yoffset 0
        0.05
        yoffset -30
        0.2
        yoffset 0
        0.1
        yoffset -30
        0.2
        yoffset 0
        0.1 
        yoffset -30
        0.1
        yoffset 0
        0.2
        yoffset -30
        0.05
        yoffset 0
        0.05
        yoffset -30
        0.15
        yoffset 0
        0.05
        yoffset -30
        0.25
        yoffset 0
        0.025
        yoffset -30
        0.075
        yoffset 0
        0.05
        yoffset -30
        0.2
        yoffset 0
        0.1
        yoffset -30
        0.35
        yoffset 0
    pause 0.05
    show printer_text01 "I said give me the\n{color=#ff99ff}magenta{/color} ink now." as p1:
        xcenter 200 ycenter 225
    pause 2.5
    hide p1
    show layer master:
        xcenter 500 ycenter 450 zoom 1.3
    show bg club_day:
        zoom 1.3 xcenter 900 ycenter 325
    show monika 2q at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        yoffset 0
        easein 0.5 yoffset 15
    m "Listen..."
    show monika 2q at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        yoffset 15
        ease 0.25 yoffset 0
    show monika 2h at i11 as m1 zorder 1:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        yoffset 15
        alpha 0
        ease 0.25 alpha 1 yoffset 0
    m "The document is in black and white."
    hide m1
    show monika 4h
    m "And since it's in black and white, you don't need colors to print it."
    show layer master:
        topleft
        zoom 1.3 ycenter 300
    show bg club_day:
        zoom 1.3 xcenter 825 ycenter 350
    play sound printer_v03
    show printer_text01 "{color=#ff99ff}Magenta{/color}!" as p1:
        subpixel True
        xcenter 200 ycenter 225
        xoffset -15 yoffset -15
        parallel:
            easein_elastic 0.65 xoffset 0
        parallel:
            0.05
            easein_elastic 0.65 yoffset 0
        0.1
        repeat 3
    show printer_p_printer:
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        0.05
        yoffset -30
        0.05
        yoffset 0
        0.05
        yoffset -30
        0.15
        yoffset 0
        0.075
        yoffset -30
        0.125
        yoffset 0
        0.25
        repeat 3
    pause 0.75
    play sound printer_v03
    show layer master:
        subpixel True
        topleft
        zoom 1.3 ycenter 300
        easein_elastic 0.6 zoom 1.4 ycenter 275
    pause 0.75
    play sound printer_v03
    show layer master:
        subpixel True
        topleft
        zoom 1.4 ycenter 275
        easein_elastic 0.6 zoom 1.5 ycenter 250
    pause 0.4
    show layer master:
        xcenter 500 ycenter 450 zoom 1.3
    show bg club_day:
        zoom 1.3 xcenter 900 ycenter 325
    hide p1
    show monika 5b at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        xoffset 20 yoffset -20
        parallel:
            easein_elastic 0.5 xoffset 0
        parallel:
            0.05
            easein_elastic 0.5 yoffset 0
    stop music
    m "Alright! Fine!"
    window hide(None)
    show monika at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370
        easeout 0.3 xcenter 1550
        0.65
        easein 0.3 xcenter 775
    show printer_p_magenta zorder 1:
        subpixel True
        truecenter
        zoom 0.1 xcenter 1515
        0.95
        easein 0.3 xcenter 640
    pause 1.05
    m "Here, take your stupid magenta!"
    show monika at i11:
        subpixel True
        zoom 1.1 xcenter 775 ycenter 370 rotate 0
        ease 0.25 rotate 10
        0.35
        easein_elastic 0.35 rotate -10
        0.5
        ease 0.5 rotate 0
    show printer_p_magenta:
        subpixel True
        truecenter
        zoom 0.1 xcenter 640 ycenter 360 rotate 0
        ease 0.25 rotate 10 xcenter 645 ycenter 335
        0.35
        easeout 0.1 xcenter 300 ycenter 500 rotate -360
        alpha 0
    show layer master:
        subpixel True
        xcenter 500 ycenter 450 zoom 1.3
        ease 0.3 xcenter 833 ycenter 300
    show bg club_day:
        subpixel True
        zoom 1.3 xcenter 900 ycenter 325
        ease 0.3 xcenter 825 ycenter 350
    pause 0.7
    play sound printer_sfx_pickup
    pause 2
    hide printer_p_magenta
    play sound printer_v04
    show printer_p_printer:
        xzoom -1 zoom 0.25 xcenter 300 ycenter 500
        0.05
        yoffset -30
        0.15
        yoffset 0
        0.15
        yoffset -30
        0.1
        yoffset 0
        0.1
        yoffset -30
        0.05
        yoffset 0
        0.15
        yoffset -30
        0.1
        yoffset 0
        0.05
        yoffset -30
        0.1
        yoffset 0
        0.1
        yoffset -30
        0.2
        yoffset 0
    
    pause 0.05
    show printer_text01 "Now give me {color=#99ffff}cyan{/color} ink." as p1:
        xcenter 200 ycenter 225
    pause 1.55
    show layer master:
        xcenter 500 ycenter 450 zoom 1.3
    show bg club_day:
        zoom 1.3 xcenter 900 ycenter 325
    hide p1
    pause 0.75
    show layer master:
        zoom 1.6 xcenter 550 ycenter 525
    pause 0.75
    show layer master:
        zoom 1.9 xcenter 600 ycenter 600
        dizzy(1, 0.01)
    show image "#f00" as r1 zorder 10:
        alpha 0
        linear 1 alpha 0.25
    pause 1
    show layer master
    hide r1
    $ renpy.music.set_volume(1)
    return