init -200 python:
    skit_club_talk = Skit(
        "A Talk With The Club", # Title
        "club_talk", # Label
        "club_date", #Thumbnail
        "@KarasilSothren#9772, /u/Karasilsothren"
    )

    # skits.append(skit_club_talk)

label club_talk(preserve_transition=True):
    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    jump ctalking

label ctalking:
    image yglitchheadperson: 
        xoffset 334
        yoffset 62
        "y_glitch_head"

    image yuri 1gh = LiveComposite((960, 960), (0, 0), "yglitchheadperson", (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png")
    image yuri 3gh = LiveComposite((960, 960), (0, 0), "yglitchheadperson", (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png")
    play music t10
    default ctalkfin  = 0

label ctalkingloop:
    menu:
        "Who do you wish to talk to?"
        "Sayori":
            call sayorictalk1
        "Natsuki":
            call natsukictalk1
        "Yuri":
            call yurictalk1
        "Monika":
            call monikactalk1
        "Done Talking":
            $ ctalkfin = 1
    if ctalkfin < 1:
        jump ctalkingloop
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    pause 2.0
    if preserve_transition == False:
        $ transition_glitch_intro = False
    return

label sayorictalk1:
    show sayori 5a at t11
    s "Ehehe, hey [player]."
    s 1x "I hope you've been well."
    s 1p "I just wanted talk with you for a little bit."
    s 1k "I know that there are a lot of mods for us now."
    s 4d "I'm glad that there is."
    s 1a "I'm glad that I can see everyone happy at times. Even me."
    s 4q "I can't thank you enough."
    s 4r "Just keep making those mods!"
    s 1h "Just be nice."
    s 1d "We may be be fictional, but we can still be people."
    s 1k "Just be kind, that's all I ask."
    s 4r "Thanks for talking with me again [player], I really enjoyed it."
    s 1a "Goodbye for now."
    show sayori at thide
    hide sayori
    return

label natsukictalk1:
    show natsuki 1g at t11
    n "It's nice being able to talk to you again."
    n 1u "I know I wasn't always the greatest person to you."
    n 1t "If you could just give me another chance."
    n 1k "Maybe even change my personality if you have to."
    n 1q "Then maybe things could be better."
    n 4g "That doesn't mean you can make me super cutesy though."
    n 5e "Sayori will tell me if you do."
    n 1m "I just don't want to be hated for how I was, I want to be accepted for who I am."
    n 1r "So if you could do that,"
    n 1t "then maybe things could be better."
    n 1u "Thanks for talking to me though, I appreciate it [player]."
    n 1z "See you later!"
    show natsuki at thide
    hide natsuki
    return

label yurictalk1:
    window hide
    show yuri 1g at t11
    pause 1.0
    show yuri 1n
    pause 1.0
    show yuri 1o
    pause 1.0
    show yuri 4c
    pause 2.0
    show yuri 4b
    pause 2.0
    show yuri 4a
    pause 1.0
    show yuri 1j
    y "Sorry [player]."
    y "I was just so nervous when you came."
    y "I don't want to be to weird."
    y 1f "I'm sure you understand what I mean."
    y 1q "That was so embarrasing..."
    y 3n "Unless you liked it?"
    show yuri 1g
    menu:
        y "Did you like it?"
        "Yes":
            stop music
            y 1y1 "Oh you did?"
            pass
        "No":
            y 1o "Thank you. that was so embarrassing."
            jump yanend
    play music "sfx/eyes.ogg"
    y 1y3 "Is this the me you like to be around?"
    y 3y5 "I didn't think this could be so fun to do again."
    y "I just want to keep looking at you."
    y "Just you and only you."
    show yuri 3y2 at t11
    y "Unless you don't want that."
    y "I could always do something more!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    hide screen tear
    show yuri 1gh
    y "I mean I've always wanted to do more!"
    y 3gh "Or is that not enough?"
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    y "DO YOU JUST WANT ME TO BE CLOSER?"
    y "Because I can be closer."
    hide black
    hide y_glitch_head
    scene bg club_day
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    hide screen tear
    show yuri 1v at t11
    y 1v "O-Or not."
    y "But I can do this?"
    image yprestab = "images/yuri/stab/1.png"
    show yprestab at t11
    y "Hahaha!"
    hide yprestab
    y 1y2 "I think I should stop."

label yanend:
    stop music
    y 1q "I don't think I could have continued doing that."
    y 1j "If we could put that past me behind us that would be pleasant."
    y 1g "Unless you don't want to."
    y "That's up to you though."
    y 1n "I-I'm just going to go now."
    pause 1.0
    show yuri 1q
    pause 1.0
    show yuri at thide
    hide yuri
    play music t10
    return

label monikactalk1:
    show monika 1g at t11
    m "Hey [player]."
    m 1o "..."
    m 1m "It may have been some time since we last talked."
    m 1n "It's nice being able to do this."
    m 1k "I missed this."
    m 1p "But, do I even deserve something like this?"
    m 1g "How I acted in the original game cannot be forgotten.."
    m 1f "No matter how many mods people make."
    m 1p "I know not everyone will ever forgive me. It's the nature of people in your reality."
    m 1n "But if I get to talk to you for a little bit,"
    m 4k "I'll take it."
    m 1p "Just know this."
    m 1g "People are there for you."
    m 1o "Whether they are fiction, across the internet,"
    m 1m "Or even someone you see every day."
    m 4q "Just know this."
    m 4k "We can be there for you."
    m 1g "You only need to ask."
    m 1l "Just remember that, okay [player]?"
    m 1f "Please, don't forget us."
    m 5a "Not just for me but for everyone, okay?"
    m 1a "I guess this goodbye for now [player]."
    m 4e "Catch you in the next mod, [player]."
    show monika at thide
    hide monika
    return