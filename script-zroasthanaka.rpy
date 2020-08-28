
## The Roast of the Moderator who calls themselves Weiss
## Copyright 2020 GanstaKingofSA. Permission is granted for additional roast material.
## Thanks Nacho and Syner for suggestions on editing a few roasts!

init -200 python:
    skit_zroast_hanaka = Skit(
        "Roast of Hanaka", #Title
        "zroast_hanaka", #Label
        "zroasthanaka_thumbnail", #Thumbnail
        "@GanstaKingofSA#0235, u/GanstaKingofSA" #Author
    )

    skits.append(skit_zroast_hanaka)

label zroast_hanaka(preserve_transition=True):
    stop music fadeout 2.0
    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    play music t2
    l "Ladies and Gentleman!"
    l "Welcome to the first ever DDMC Roast Stream!"
    l "Today we have someone everyone has to deal with on a day to day basis."
    l "{i}And the mod that calls himself Weiss almost everyday...{/i}"
    l "It's Hanaka!"
    show hanaka 1 at t11
    h "*smug*"
    l "Alright! Let the show begin!"
    show monika 2b at f21
    show hanaka at t22
    m "Thanks for having me here."
    m "Hanaka, I'm surprised you stayed two years in the community."
    m "Two years and you still haven't learned to grow up."
    show monika at t21
    play audio zhlaugh
    l "Ooh! Looks like things are about to get spicy!"
    show hanaka at f22
    h "*smug*"
    show hanaka at t22
    show monika 2d at f21
    m "During those times you always liked to say I was yours alone."
    m 2h "Though now you picked up some ice girl from some place called \"Remnant\"."
    m 5b "I wonder how she's doing for you."
    m "Especially since she looks like a discount Elsa from Frozen."
    show monika at t21
    play audio zhlaugh
    l "Ouch! Targetting his new waifu I see!"
    show monika at f21
    m "To be honest, I feel you made that name up and got her at a discount fisher price store."
    play audio zhlaugh
    show monika at t21
    show hanaka at f22
    h "*rolls eyes* *smugs*"
    show hanaka at t22
    show monika at f21
    m "Here's some advice, stop dreaming up a reality with her because it's going to be your final fantasy, and-"
    m 2h "Oh wait you don't know what that is either."
    m "Why don't you Google that instead of wishing for horse simulators in your diary?"
    show monika at t21
    play audio zhlaugh
    l "Oof! The comedy stream strikes a home run tonight!"
    show hanaka at f22
    h "*smirks*"
    show hanaka at t22
    show monika 3m at f21
    m "Hanaka, who did your hair?"
    show hanaka at t33
    m 3n "And what's with your outfit?"
    show hanaka at t44
    m "It almost looks like you are just wearing a wig and bought them off the reject shop." #actual store in Australia, did research
    m 2k "You look so ridiculous that I can say that you don't look like a clown."
    show hanaka at rhide
    hide hanaka
    m "But the entire circus!"
    show monika at t21
    play audio zhlaugh
    $ skw = renpy.random.randint(0,1)
    if skw == 0:
        l "So much comedy gold from our guest Monika."
    else:
        l "So much comedy cringe from our guest Monika."
    l "Wait. Where the heck did Hanaka go?"
    show monika at f21
    m 1d "Huh?"
    m "Hanak-{nw}"
    show monika at t21
    h "NERF THIS!"
    show monika 5b at t21
    lm "AW SHI-{nw}"
    stop music
    scene bg psb
    play audio psbsfx
    $ pause(2.0)
    return

