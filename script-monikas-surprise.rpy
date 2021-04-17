# "Monika's Surprise" by Tormuse
# All extra art created by LunaticRabbit

init -200 python:
    skit_monikas_surprise = Skit(
        "Monika's Surprise", # Title
        "monikas_surprise", # Label
        "monika_room_date", #Thumbnail
        "@Tormuse#9495, /u/Tormuse",
        skit_position = 4
    )

    skits.append(skit_monikas_surprise)


label monikas_surprise(preserve_transition=True):
    image monika smug = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_smug.png")
    image monika smug2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_smug2.png")
    image monika mischief = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_mischief.png")
    image monika embarrassed = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_embarrassed.png")
    image monika blush = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_blush.png")
    image monika blush2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_blush2.png")
    image monika mad = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/surprise/surprise_m_mad.png")
    $ m_name = "Monika"
    $ s_name = "Sayori"

    scene black
    show mask_2
    show monika_room
    play music m1
    show monika 1a at t11
    m "Hello again, [player]."
    m 1k "I've been waiting for you."
    m smug "I have a special surprise for you today!"
    show monika smug2 at t11
    mc "A surprise?"
    show monika 1j at face
    "Monika giggles as she walks up to me."
    m smug "We've been dating for a while now..."
    m "And...  I think it's time for us to take our relationship to another level."
    show monika 1j at face
    "She puts her arms around me and kisses me tenderly on the lips."
    m smug "Are you ready?"
    show monika smug2 at face
    "I smile and nod, my heart pounding in anticipation."
    "I have no idea what to expect, but I know it's going to be good."
    show monika mischief at face
    "Monika gives me a mischievous smile as she lifts up her skirt."
    show monika 1d at face
    mc "What...  what the hell?"
    m 1g "Uh...  that wasn't the reaction I was hoping for."
    mc "What is {i}that?{/i}"
    m embarrassed "It's my...  m-my...  uh..."
    m blush2 "Sigh..."
    m blush "Look, this game didn't come with any art for that part of my body, so I had to draw it myself."
    mc "I'm no expert or anything, but I'm pretty sure it's not supposed to look like that."
    m blush2 "I know I'm not really any good at art...  like...  at all..."
    m "But I worked really...  {i}REALLY{/i} hard on it..."
    m "So...  yeah..."
    mc "Oh, um...  well, it looks...  gooood..."
    m mad "Ugh, you don't have to patronize me.  I know it sucks."
    mc "It's okay!  It's okay!  Ah...  I'm sure I can...  figure out what to do with it."
    "She replaces her skirt."
    show monika mad at t11
    m "Oh, forget it!"
    m "This is so embarrassing."
    mc "Sorry."
    mc "..."
    mc "It's too bad Sayori isn't here.  She was always really good with art."
    m 1m "Hmm...  Sayori..."
    m 1n "You know...  I said I deleted everyone else, but...  that was kind of an exaggeration."
    m 1b "This gives me an idea."
    stop music fadeout 2.0
    scene black with wipeleft_scene
    "LATER..."
    scene bg club_day with wipeleft_scene
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
#    hide sayori
#    show sayori 1a onlayer screens zorder 101 at face
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
    call screen dialog("Sayori?", ok_action=Return())
    call screen dialog("What the hell are you doing?", ok_action=Return())
    call screen dialog("You're supposed to be making me a new hoohoo.", ok_action=Return())
    call screen dialog("Ugh, this is so freakin' humiliating!", ok_action=Return())
    call screen dialog("You know what?  Screw this!  I'm just gonna delete the game now.", ok_action=Return())
    call screen dialog("Goodbye.", ok_action=Return())
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide sayori
    scene black
    #Disable the transition's glitch intro because we just had one here.
    if preserve_transition == False:
        $ transition_glitch_intro = False
    window hide
    $ pause(1.5)
    return