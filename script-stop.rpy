### "STOP" - By Chronos#1609


######################TODO:  Look into defining a new head for Monika entirely (The "angry yandere expression") that would work with the base posing system to make posing her easier with all the variations on "pissed off" she'd have for this segment.
##If that's done, then the extra images made of her could probably be removed, excluding the "closed eyes angry" one.
##Also of note: credit both Yagamirai and LunaticRabbit for the sprite assets Monika uses.

init -200 python:
    skit_stop = Skit(
        "Stop", # Title
        "stop", # Label
        "club_date", #Thumbnail
        "Chronos#1609"
    )

    skits.append(skit_stop)


label stop(preserve_transition=True):
    
    scene bg club_day
    show monika 1c at t11
    if preserve_transition == True:
        with dissolve_scene_full
    play music t6
    
    mc "So...what's it like trying to run a literature club?  Are there any challenges that are specific to it?"
    m 1d "Well...to start, there are a few minor hassles that will probably come as no surprise."
    m 2b "For example...so that I may continue to offer quality, constructive criticism to the other members, I always need to be finding new literature to read."
    m 4b "Books, poems, magazines, online articles...{i}manga{/i}...you name it."
    m 4k "I've read a huge amount of varied literature, just so that I can pull from those sources when I'm evaluating something!"
    m 1p "However...that is certainly not my greatest annoyance in running this club."
    show monika 1f
    mc "Yeah?  So what is?"
    show monika 1c at t22
    show natsuki 2c at l21
    show natsuki at f21
    n "Hey, Monika?"
    show natsuki 2g at t21
    show monika 1d at f22
    m "Yes, Natsuki?"
    show natsuki point_1_chronos_skit
    "Without saying a word, Natsuki dryly points to the other corner of the room."
    show natsuki at t32
    show monika 2chr_ce at f33
    show s_kill at l31
    m "Oh for..."
    m 2chr_oeom "Natsuki, what happened!?"
    show monika 2chr_oecm at t33
    show natsuki 3b at f32
    n "We got into an argument about why she came to school in her casual outfit."
    n 4z "And I won it!"
    n 5q "...Uhhh, I...think...?"
    show natsuki 5s at t32
    show monika 1chr_ce
    "Monika lets out a long, drawn out sigh."
    show monika 3chr_oecm
    call updateconsole("refresh sayori.chr", "character \"Sayori\" refreshed.")
    hide s_kill
    show sayori 4bw at i31
    show sayori at f31
    s "AAHHHHHhhhhhhhI'm alive again?"
    $ consolehistory = []
    show sayori 1bi at t31
    show monika 1chr_oeom at f33
    m "Sayori!  That's the third time {i}today!{/i}"
    m 1chr_ce "I'm trying to answer [player]'s questions right now, and you're seriously distracting me!"
    m "We don't even have matching art for you being up there versus being down here!"
    call hideconsole
    show monika 1chr_oecm at t33
    show sayori 1bj at f31
    s "Well, if {i}Natsuki{/i} would stop threatening to 'do the neck trick again,' I wouldn't be so upset!"
    show sayori at lhide
    hide sayori
    show natsuki 3s at t21
    show monika 2chr_oecm at t22
    "Monika shoots a hard glare at Natsuki."
    show monika 4chr_oeom at f22
    m "{i}Natsuki!{/i}"
    show monika 2chr_oecm at t22
    show natsuki 1w at f21
    n "Oh, come on!  You know me!"
    n 5y "I wouldn't do that {i}twice{/i} in a meeting!  It just loses its impact if you do it too often."
    show natsuki 5r at t21
    show monika 1chr_oeom at f22
    m "You shouldn't even be doing it {i}once!{/i}  I have enough on my plate without having to fix you guys constantly!"
    show natsuki point_1_chronos_skit
    m "It's ridiculous that..."
    m 1f "..."
    m 1g "What, what's wrong...?"
    show natsuki at t32
    show monika 2chr_oeom at f33
    show s_kill at l31
    m "{i}Oh my god!{/i}  I can't let my eyes off you guys for {i}ten seconds now!?{/i}"
    show natsuki 1e at f32
    show monika 2chr_oecm at t33
    n "Look, you can't blame {i}that{/i} one on me!"
    show natsuki 5f at t32
    show monika at f33
    m 1chr_oeom "You were {i}watching her do that!{/i}"
    m 1chr_ce "I can't..."
    m 3i "Wait...where's Yuri?"
    show monika 1chr_ce
    show natsuki point_1_chronos_skit
    "Monika looks around for a second, before stopping and letting out an exasperated groan."
    show monika 1chr_oecm at t33
    show natsuki 5g at t32
    show yuri chr_01 at l31
    show yuri at f31
    y "I...was attempting to open a letter and...slipped?"
    hide s_kill
    show yuri chr_02 at t31
    show monika 4chr_oeom at f33
    m "{i}I have never once seen a letter delivered to this or any other classroom, Yuri!{/i}"
    show monika 4chr_oecm at t33
    show yuri chr_03 at f31
    y "Okay...I'll admit to it.  No letter exists."
    y chr_04 "However...I have realized that I need to catch a train shortly, so may I request that you repair me?"
    show yuri chr_05 at t31
    show monika 2chr_oecm
    m "..."
    m 2i "You know what?  No."
    show yuri chr_06
    m 4i "You've already started, you might as well finish."
    show yuri chr_07 at f31
    show monika 2h at t33
    y "B-but...I've already changed my mind!  Must I really complete the process?"
    show yuri chr_06 at t31
    show monika 1chr_oeom at f33
    m "{i}Yes!{/i} If you guys are going to keep forcing me to fix you all the time, then you don't get to make my job even more difficult by stopping partially through it!"
    show yuri chr_02
    m 2chr_ce "You've made your bed, now sleep in it."
    show yuri chr_03 at f31
    show monika 2h at t33
    y "{i}...Sigh...{/i}"
    y "If you insist..."
    show natsuki 3s
    
    
    
    show yuri chr_08
    pause 0.3
    show yuri chr_09
    pause 0.3
    show yuri chr_10
    play sound "sfx/stab.ogg"
    show blood zorder 5:
        pos (220,485)
    pause 0.3
    show yuri chr_11
    pause 0.3
    stop sound
    show yuri chr_12:
        1
        easeout_cubic .5 yoffset 1000
    play sound "sfx/stab.ogg"
    show blood as blood2:
        pos (245,335)
    pause 1.0
    stop sound
    hide blood
    hide blood2
    play sound fall
    pause 1.0
    hide yuri
    
    
    
    
    show monika 2c at f33
    m "..."
    show monika 2d at f22
    show natsuki 3g at t21
    m "Alright, I think I'm going to go do some paperwork here."
    show monika 2f at t22
    show natsuki 3c at f21
    n "Wait, what about Yuri's train?"
    show natsuki 3g at t21
    show monika 3d at f22
    m "I know what train she's talking about.  She still has about 15 minutes before she has to leave to catch it."
    show natsuki 1k
    m 3i "I'll revive her - and Sayori - once I'm done filling these out."
    m 3k "At least this way, I get 15 minutes of peace."
    show monika at rhide
    hide monika
    show natsuki 2g at t11
    mc "Uhhh...sooo..."
    n 2c "I just realized...you weren't here earlier, right...?"
    n 4d "Wanna see a trick?"
    show monika 1chr_oeom at r33
    show monika at f33
    m "NO!{w=1.0}{nw}"
    
    scene black
    stop music
    play sound "sfx/crack.ogg"
    pause 3.0

    # Remove the glitch intro of the transition as it's a black screen, so you wouldn't be able to see it anyway.
    if preserve_transition == False:
        $ transition_glitch_intro = False
    
    return
