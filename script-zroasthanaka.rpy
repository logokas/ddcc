
## The Roast of the Moderator who calls themselves Weiss
## Copyright 2020 GanstaKingofSA. Permission is granted for additional roast material.
## Thanks Nacho and Syner for suggestions on editing a few roasts!

init -200 python:
    skit_zroast_hanaka = Skit(
        "The Roast of Hanaka", #Title
        "zroast_hanaka", #Label
        "zroasthanaka_thumbnail", #Thumbnail
        "@GanstaKingofSA#0235, u/GanstaKingofSA", #Author
        skit_position = 17
    )

    skits.append(skit_zroast_hanaka)

label zroast_hanaka(preserve_transition=True):
    stop music fadeout 2.0
    scene bg crf
    show desk 1 at t21 zorder 3
    if preserve_transition == True:
        with dissolve_scene_full
    play music t2
    mc "Ladies and Gentleman!"
    mc "Welcome to the first ever DDMC Roast Stream!"
    mc "Today we have someone everyone has to deal with on a day to day basis."
    mc "{i}And the mod that calls himself Weiss almost everyday...{/i}{w=0.05}{nw}"
    mc "It's Hanaka!"
    show hanaka 1ss at t43b
    play audio clap
    h "*waves*"
    mc "Alright! Let the show begin!"
    show monika 2b behind desk at f21
    show desk at f21
    show hanaka 1 at t43b
    m "Thanks for having me here."
    m "Hanaka, I'm surprised you stayed two years in the community."
    m "Two years and you still haven't learned to grow up."
    show monika at t21
    show desk at t21
    play audio zhlaugh
    mc "Ooh! Looks like things are about to get spicy!"
    show hanaka at f43b
    h 1g "..."
    show hanaka at t43b
    show monika 2d at f21
    show desk at f21
    m "During those times you always liked to say I was yours alone."
    m 2h "Though now you picked up some ice girl from some place called \"Remnant\"."
    m 5b "I wonder how she's doing for you."
    m "Especially since she looks like a discount Elsa from Frozen."
    show monika at t21
    show desk at t21
    play audio zhlaugh
    show hanaka 1p
    mc "Ouch! Targetting his new waifu I see!"
    show monika at f21
    show desk at f21
    m "To be honest, I feel you made that name up and got her at a discount fisher price store."
    play audio zhlaugh
    show monika at t21
    show desk at t21
    show hanaka at f43b
    h 1m "..."
    show hanaka at t43b
    show monika at f21
    show desk at f21
    m "{cps=28}Here's some advice, stop dreaming up a reality with her because it's going to be your final fantasy, and-{nw}{cps=28}"
    m 2h "Oh wait you don't know what that is either."
    m "Why don't you Google that instead of wishing for horse simulators in your diary?"
    show monika at t21
    show desk at t21
    play audio zhlaugh
    mc "Oof! The comedy stream strikes a home run tonight!"
    show hanaka 1ses at f43b
    h "*smirks*"
    show hanaka 1s at t43b
    show monika 3m at f21
    show desk at f21
    m "Hanaka, who did your hair?"
    show hanaka at t33
    m 3n "And what's with your outfit?"
    show hanaka at t44
    m "It almost looks like you are just wearing a wig and bought them off the reject shop." #actual store in Australia, did research
    show hanaka at t45
    m 2k "You look so ridiculous that I can say that you don't look like a clown."
    show hanaka at rhide
    hide hanaka
    m "But the entire circus!"
    show monika at t21
    show desk at t21
    play audio zhlaugh
    $ skw = renpy.random.randint(0,1)
    if skw == 0:
        mc "So much comedy gold from our guest Monika."
    else:
        mc "So much comedy cringe from our guest Monika."
    play audio hml
    mc "Wait. Where the heck did Hanaka go?"
    show monika at f21
    show desk at f21
    m 1d "Huh?"
    m "{cps=25}Hanak-{nw}{cps=25}"
    show monika at t21
    show desk at t21
    play audio nerfthis
    h "NERF{w=1.0} THIS!{w=1.0}{nw}"
    show monika 5b at t21
    lm "{cps=15}AW CRA-{nw}{cps=15}"
    stop music
    stop audio
    scene bg psb
    play audio psbsfx
    $ pause(2.0)
    return
