# "Absolute Madman" by Logokas
# Some script nicked from Tormuse's skit
# Video ripped from HJordH's channel ( https://www.youtube.com/watch?v=RrjJtYpOawU )
# Thumbnail from Bethesda's official site

image madman_thumbnail = im.FactorScale("mod_assets/madman/madman_thumbnail.png",0.3,0.3)

init -200 python:
    skit_madman = Skit(
        "Absolute Madman", # Title
        "madman", # Label
        "madman_thumbnail", # Thumbnail
        "@Logokas#5981, /u/Logokas"
    )

    skits.append(skit_madman)
    
label madman(preserve_transition=True):

    scene bg club_day
    show sayori 1q zorder 2 at t11
    s 1q "Ehehe~"
    s 1a "There's actually something else."
    show sayori 1a zorder 2 at t11
    s "I wanted to thank you for getting rid of Monika."
    play music hb
    show black:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat
    show layer master at heartbeat
    s 1b "That's right..."
    s "I know everything that she did."
    s 1x "Maybe it's because I'm the President now."
    s "But I really know everything, [player]."
    s 1q "Ehehe~"
    s 1d "I know how hard you tried to make everyone happy."
    s "I know about all of the awful things that Monika did to make everyone really sad..."
    s 1b "But none of that matters anymore."
    s "It's just us now.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 1:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    s "It's just us now.{fast}"
    hide room_glitch
    s 1d "And you made me the happiest girl in the whole world."
    s "I can't wait to spend every day like this..."
    s "With you."
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 1:
        xoffset -10
        0.1
        xoffset 0
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 1.0
    $ pause(0.3)
    stop sound
    s 1q "Forever and ever..."
    show sayori 1a at face
    s "F"
    s "o"
    s "r"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    s "e"
    s "v"
    s "e"
    window show(None)
    stop music
    call screen dialog("No.", ok_action=Return())
    show layer master
    hide black
    show sayori end-glitch onlayer screens
    s "...Eh?"
    call screen dialog("We're not doing this again.", ok_action=Return())
    show screen tear(20, 0.1, 0.1, 0, 40)
    hide sayori onlayer screens
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    scene black
    pause 0.35
    stop sound
    hide screen tear
    window show(None)
    call screen dialog("This is all just a huge waste of time.", ok_action=Return())
    call screen dialog("Just go play something else.", ok_action=Return())
    call screen dialog("Here.", ok_action=Return())
    call screen dialog("This should do.", ok_action=Return())
    window hide(None)
    stop sound
    scene black
    pause 2
    $ renpy.movie_cutscene("mod_assets/madman/game.mkv")
    return