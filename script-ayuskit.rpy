# Skit template by Ceane
# This template should help you get going, and set up your own skit to be compatible with the rest of the game.
# Author of the skit, and any credits for assets or parts of code should be commented here, at the start of the file


# Writer: PattAttack#3007
# Programmer: SuperHatGuy#1795
# Ayumi sprites: Cyrke#8043
# Music: Hyperfun by Kevin MacLeod (incompetech.com)
#    Licensed under Creative Commons: By Attribution 3.0 License
#    http://creativecommons.org/licenses/by/3.0
# SFX: Public domain sounds from https://freesound.org.
#    Licensed under Creative Commons: By Attribution 1.0 License
#    https://creativecommons.org/publicdomain/zero/1.0/

# If you don't want to use one of the original game's thumbnails (e.g. club_date, corridor_date, class_date), then define it here.
#image template_thumnail = "mod_assets/template/template_thumbnail.png"

# First, we need to add our skit to the list of skits that the game looks at.
image ayuskit_thumbnail = "mod_assets/ayuskit/ayuskit_thumbnail.png"
init -200 python:
    ayuskit_skit = Skit(
        "Flightless Comedy", # Set this to be the title of your skit.
        "ayuskit_label", # Set this to be the label that you call below.
        "ayuskit_thumbnail" # Set this to be the thumbnail you want for your skit. If you aren't using one from the original game, then you'll need to define its image.
    )

    skits.append(ayuskit_skit) # Add your skit to the list! Make sure it matches the name above.

# Now, for the actual scene:
label ayuskit_label(preserve_transition=True): # Don't change the preserve_transition part, but rename "template" to what you want your label to be.

    stop music fadeout 2.0
    scene black # Whatever scene you want
    if preserve_transition == True:
        with dissolve_scene_full
        # You can have whatever transition effects you want at the start of your script, as long as you put them in this if block.
        # This is used for triggering the transition depending on whether or not someone is going through the game in "Play All" mode,
        # or through scene selection.

    #Title across screen - black screen
    show expression "mod_assets/ayuskit/ayuskit_gfx_title.png" as ayuskit_title zorder 0:
        subpixel True rotate_pad True
        truecenter
        zoom 0.0 rotate 16
        easein_back 1.0 zoom 1.0 rotate 0
        2.0
        easeout_back 1.0 zoom 0.0 rotate -16
    pause 4.0
    hide ayuskit_title

    #bg DDLC classroom
    play music ayuskit_bgm01 fadein 2.0 loop
    scene bg ayuskit_bg01
    show bg ayuskit_bg01 zorder 0:
        truecenter
        subpixel True zoom 1.2
        xalign 0.5
        yalign 0.5
    with dissolve_scene_full

    #Show Ayumi Sprite
    show ayuskit_ayumi at ayuskit_tf(640, z=0.875) zorder 2
    ayuskit_a 21c2 "So, I just flew in from Seishin-tekina and boy are my arms tired~!{nw}"
    play sound ["<silence 0.5>", "mod_assets/ayuskit/ayuskit_sfx_sitcomlaugh01.ogg"]
    extend ""
    show ayuskit_ayumi 21a1 at ayuskit_tc(640, z=0.875)
    "..."

    #Show Natsuki Sprite
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime xcenter 400
    show natsuki zorder 2:
        subpixel True
        parallel:
            ayuskit_tf(1120)
        parallel:
            ease ayuskit_pantime xcenter 880
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime xalign 0.625

    n 2c "Um...{w=0.1}Monika, who's the new girl?"
    n 4e "And what's with that sense of humor?"

    #Show Monika sprite
    show monika zorder 2:
        subpixel True
        parallel:
            ayuskit_tf(-80)
        parallel:
            ease ayuskit_pantime xcenter 160
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime xcenter 640
    show natsuki:
        subpixel True
        parallel:
            ayuskit_tc(880)
        parallel:
            ease ayuskit_pantime xcenter 1120
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime xalign 0.5

    m 2b "Oh, come now Natsuki, I don't think it was that bad."
    show monika at ayuskit_tc(160)
    show natsuki at ayuskit_tf(1120)
    n 5g "Oh, please, you'd have to have the sense of humor of a kindergartner to think that was funny."

    play sound ["<silence {}>".format(0.5+(ayuskit_pantime*1.5)), "mod_assets/ayuskit/ayuskit_sfx_sitcomlaugh02.ogg"]
    #Show Sayori sprite
    show sayori zorder 2:
        subpixel True rotate_pad True
        xzoom -0.9*0.95 yzoom 0.9*0.95 alpha 0.0
        xcenter 400
        yanchor 0.5 ypos 1.7 yoffset -20
        rotate 45
        ayuskit_pantime*1.5
        parallel:
            easein 0.25 xzoom -0.9*1.05 yzoom 0.9*1.05 alpha 1.0 yoffset 0
        parallel:
            easein 1.0 ypos 0.57 rotate 0
        parallel:
            linear 0.05 xoffset 5
            linear 0.05 xoffset -5
            repeat
    show monika 1d:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 880
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 1360
    show natsuki 1k:
        subpixel True
        parallel:
            ayuskit_tc(1120)
        parallel:
            ease ayuskit_pantime*1.5 xcenter 1840
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.5 xalign 0.125

    s 4r "Bahahahahaha~"

    show sayori:
        subpixel True rotate_pad True
        xzoom -0.9*1.05 yzoom 0.9*1.05 rotate 0 alpha 1.0
        ypos 0.57 yoffset 0
        parallel:
            easein_cubic 0.25 yoffset -30
            easeout 0.25 yoffset 0
            easein_cubic 0.25 yoffset -60
            easeout 0.25 yoffset 0
        parallel:
            easein 0.1 xoffset 0

    s "Another one~ Another one~"

    show sayori:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter -320
    show monika 1d:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 160
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 640
    show natsuki 1k:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 1120
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.5 xalign 0.5

    n 4g "..."
    hide sayori
    show natsuki at ayuskit_tf(1120)
    n 4c "Well, that certainly doesn't {i}disprove{/i} my point."
    show monika at ayuskit_tf(160)
    show natsuki at ayuskit_tc(1120)
    m 3e "Maybe we should give her another chance?"

    #fade Natsuki/Sayori sprite
    show monika 1d:
        subpixel True
        ease ayuskit_pantime xcenter 400
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime xcenter 880
    show natsuki:
        subpixel True
        parallel:
            ayuskit_tc(880)
        parallel:
            ease ayuskit_pantime xcenter 1360
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime xalign 0.375

    m 2a "Okay, Ayumi-{w=0.1} Let's take it from the top, and remember this is supposed to be funny, so come up with the silliest joke that you can."
    show monika at ayuskit_tc(400)
    show ayuskit_ayumi at ayuskit_tf(880, z=0.875)
    ayuskit_a 23a2 "Ah, sure, I've got just the one."
    show monika at ayuskit_tf(400)
    show ayuskit_ayumi at ayuskit_tc(880, z=0.875)
    m 3b "Great, we can't wait to hear it."

    #Fade Monika Sprite
    show monika:
        subpixel True
        parallel:
            ayuskit_tc(400)
        parallel:
            ease ayuskit_pantime*1.25 xcenter -350
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*1.25 xcenter 400
    show natsuki 1k:
        subpixel True
        parallel:
            ayuskit_tf(1360)
        parallel:
            ease ayuskit_pantime*1.25 xcenter 880
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.25 xalign 0.625

    n 3g "...Speak for yourselves..."
    hide monika

    #Ayumi slides to center of the screen
    show ayuskit_ayumi 11a1:
        subpixel True
        ease ayuskit_pantime xcenter 640
    show natsuki:
        subpixel True
        parallel:
            ayuskit_tc(880)
        parallel:
            ease ayuskit_pantime xcenter 1580
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime xalign 0.5
    window hide
    window auto

    pause 0.5

    hide natsuki
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*3 zoom 1.2 yoffset 250
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*3 zoom 1.3

    pause ayuskit_pantime*3

    play sound "mod_assets/ayuskit/ayuskit_sfx_spotlight.ogg"
    show bg ayuskit_bg02
    show ayuskit_gfx_spotlight1 zorder 3:
        subpixel True
        truecenter
        alpha 0.878
    show ayuskit_gfx_spotlight0 zorder 3:
        subpixel True
        truecenter
        alpha 0.125
    show white zorder 4:
        subpixel True
        alpha 1.0
        easein 1.0 alpha 0.0

    pause 1.5

    ayuskit_a 3 "What do you call a group of birds that stick together?"

    show sayori 4x zorder 1:
        subpixel True
        zoom 0.9
        xcenter 200
        yanchor 0.0 ypos 1.0 yoffset -50
        easein_cubic 0.3 yanchor 1.0 ypos 1.15 yoffset 0
        easeout 0.3 ypos 1.2
        easein_cubic 0.3 ypos 1.1
        easeout 0.3 ypos 1.2

    s "What~?{w=0.1} What~?"

    show ayuskit_gfx_spotlight1 zorder 3:
        subpixel True
        alpha 0.925
        easein 1.0 alpha 0.878
    show ayuskit_gfx_spotlight0 zorder 3:
        subpixel True
        alpha 0.5
        easein 1.0 alpha 0.125

    #drums sfx
    ayuskit_a 21a2 "{i}...A vel-crows!{/i}{nw}"
    play sound ["<silence 0.5>", "mod_assets/ayuskit/ayuskit_sfx_badumtss.ogg"]
    play sound2 ["<silence 0.5>", "mod_assets/ayuskit/ayuskit_sfx_sitcomlaugh03.ogg"]
    extend ""

    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*2 zoom 0.875 yoffset 0
    show bg ayuskit_bg02:
        subpixel True
        parallel:
            ease ayuskit_pantime*2 zoom 1.2
        parallel:
            "bg ayuskit_bg01" with Dissolve(ayuskit_pantime*2, alpha=True)
    show sayori:
        subpixel True
        ease ayuskit_pantime*2 zoom 0.8 ypos 1.1 xcenter 225
    show ayuskit_gfx_spotlight1 zorder 3:
        subpixel True
        on hide:
            ease ayuskit_pantime*2 alpha 0.0
    show ayuskit_gfx_spotlight0 zorder 3:
        subpixel True
        on hide:
            ease ayuskit_pantime*2 alpha 0.0
    hide ayuskit_gfx_spotlight1
    hide ayuskit_gfx_spotlight0

    ayuskit_a "Get it?"
    show sayori 1n
    "..."

    show sayori 4r:
        subpixel True rotate_pad True
        zoom 0.8 rotate 0
        xcenter 225
        ycenter 408
        parallel:
            easeout_cubic 0.75 rotate 90
        parallel:
            easeout_back 0.75 ycenter 883
    show ayuskit_ayumi:
        subpixel True
        0.75
        ease_cubic 0.1 yoffset -24
        ease_cubic 0.1 yoffset 16
        ease_cubic 0.1 yoffset -8
        ease_cubic 0.1 yoffset 4
        ease_cubic 0.1 yoffset -2
        ease_cubic 0.1 yoffset 0
    show bg ayuskit_bg01:
        subpixel True
        0.75
        ease_cubic 0.1 yoffset -24
        ease_cubic 0.1 yoffset 16
        ease_cubic 0.1 yoffset -8
        ease_cubic 0.1 yoffset 4
        ease_cubic 0.1 yoffset -2
        ease_cubic 0.1 yoffset 0
    play sound ["<silence 0.7>", "sfx/fall.ogg"]

    "Sayori tumbles over in laughter from the back of the room..."

    show sayori:
        subpixel True rotate_pad True
        xcenter 175
        parallel:
            easein 2.0 ycenter 683 rotate 45
        parallel:
            linear 0.1 yoffset -3
            linear 0.1 yoffset 3
            repeat
    show ayuskit_ayumi 21c1

    "She begins laughing so hard that she can't bring herself back up to standing."

    show sayori:
        subpixel True rotate_pad True
        parallel:
            easeout 2.0 ycenter 890 rotate 90
        parallel:
            linear 0.1 yoffset -3
            linear 0.1 yoffset 3
            repeat

    "This continues on for a while..."

    hide sayori
    #Fade Ayumi Sprite
    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter -80
    show natsuki 4g zorder 2:
        subpixel True
        parallel:
            ayuskit_tc(1120)
        parallel:
            ease ayuskit_pantime*1.5 xcenter 400
    #Show Yuri sprite
    show yuri zorder 2:
        subpixel True
        parallel:
            ayuskit_tf(1600)
        parallel:
            ease ayuskit_pantime*1.5 xcenter 880
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.5 xalign 0.875

    y 1h "She's...{w=0.1}actually quite bad at this, isn't she?"
    show natsuki at ayuskit_tc(400)
    show yuri at ayuskit_tf(880)
    y 1r "I feel as if taking two of my precious knives and using them as earplugs isn't as bad of an idea as it sounds..."
    show natsuki at ayuskit_tf(400)
    show yuri at ayuskit_tc(880)
    n 5f "You too?{w=0.1} I feel like jamming a couple of cupcakes into mine."

    show ayuskit_ayumi:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 640
    show natsuki:
        subpixel True
        parallel:
            ayuskit_tc(400)
        parallel:
            ease ayuskit_pantime*1.5 xcenter 1120
    show yuri:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 1600
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.5 xalign 0.5

    ayuskit_a 14a2 "What do you call an acid with an attitude problem?"
    show ayuskit_ayumi at ayuskit_tf(640, z=0.875)
    ayuskit_a 13b2 "...A mean-o' acid!{nw}"
    play sound ["<silence 0.5>", "mod_assets/ayuskit/ayuskit_sfx_sitcomlaugh04.ogg"]
    extend ""

    show ayuskit_ayumi:
        subpixel True
        parallel:
            ayuskit_tc(640, z=0.875)
        parallel:
            ease ayuskit_pantime*1.5 xcenter -160
    show natsuki 42b:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 400
    show yuri 2g:
        subpixel True
        ease ayuskit_pantime*1.5 xcenter 880
    show bg ayuskit_bg01:
        subpixel True
        ease ayuskit_pantime*1.5 xalign 0.875

    "..."
    "..."
    show natsuki at ayuskit_tf(400)
    n 42c "I'll go get the knives."
    show natsuki at ayuskit_tc(400)
    show yuri at ayuskit_tf(880)
    y 2h "Yes, and I shall retrieve the cupcakes."
    show yuri at ayuskit_tc(880)

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    return
