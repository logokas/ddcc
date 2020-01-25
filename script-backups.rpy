### "Good thing she keeps backups" - By Chronos#1609

init -200 python:
    skit_backups = Skit(
        "Good thing she keeps backups", # Title
        "backups", # Label
        "club_date", #Thumbnail
        "@Chronos#1609, /u/chronoshag"
    )

    skits.append(skit_backups)


label backups(preserve_transition=True):
    
    scene bg club_day
    show monika 2i at f21
    if preserve_transition == True:
        with dissolve_scene_full
    play music t6
    
    m "...So...would that...be where...?"
    show monika 2c at t21
    show yuri 2h at r22
    show yuri at f22
    y "Monika, can I ask when we're..."
    y 2e "..."
    y 1f "Wait...what are you doing?"
    show yuri 1e at t22
    show monika 2d at f21
    m "I'm trying to figure out something."
    show monika 2c at t21
    show yuri 3h at f22
    y "Oh dear..."
    y 3f "Does this 'something' involve the game's...'code' again?"
    show yuri 3e at t22
    show monika 1g at f21
    m "Yeah, but I'm trying to be as gentle as possible with what I'm tracking down."
    show monika 1f at t21
    show yuri 1h at f22
    y "May I ask...what exactly it is you're attempting to 'track down...?'"
    show yuri 1g at t22
    show monika 1g at f21
    m "It's something in our own character files..."
    m 3d "Oh!  Since you're here anyway, can I ask that you give me a hand?"
    show monika 3c at t21
    show yuri 3n at f22
    y "O-Of course!  Though..."
    show monika 1a
    y 2q "I'm not sure how {i}I{/i} could assist...?"
    show yuri 2e at t22
    show monika 2b at f21
    m "Oh, it's easy!"
    m 4b "Just watch Sayori and Natsuki for a minute, and let me know if you see anything that seems odd."
    show monika 2a at t21
    show yuri 1h at f22
    y "...Alright.  That seems simple enough."
    show monika at lhide
    hide monika
    show yuri at lhide
    hide yuri
    
    # Scene pans over to Sayori and Natsuki, who are obviously talking.  Yuri walks up to the two of them.
    
    show natsuki 5g at r33 zorder 2
    show sayori 2c at r32 zorder 3
    pause 0.5
    show yuri 1a at l31 zorder 2
    show natsuki 3d at f33
    show sayori 2b
    n "Hey Yuri.  What's up?"
    show natsuki 3a at t33
    show yuri 2q at f31
    y "Oh...nothing.  Please, don't let me interrupt your conversation."
    y 1d "In fact...may I ask what you were talking about...?"
    show yuri 1a at t31
    show sayori 4r at f32
    s "Natsuki showed me a recipe from her manga, and I was trying to get her to make it!"
    show sayori 1i at t32
    show natsuki 4e at f33
    n "Sayori...it's not as simple as you're making it out to be!"
    show natsuki 4f at t33
    show sayori 2j at f32
    s "Of course it is!  All you do is mix the {nw}"
    call st_e
    show sayori glitch_chronos_skit
    show yuri 1y2
    show natsuki scream
    s "Of course it is!  All you do is mix the {fast}{i}donkey transmission along a semicircular journey whilst consuming intricately leavened scissors!{/i}"
    call st_n
    show yuri at t41
    show sayori at t32
    show natsuki react_chronos_skit at f44
    n "I...{i}what now!?{/i}"
    show natsuki at t44
    show yuri 4d at f41
    y "Uuuu...M-Monika..."
    show yuri at t41
    m "Did something change, Yuri?"
    show yuri 2y4 at f41
    y "Y-You...could certainly say that, yes!"
    show yuri at t41
    show natsuki 2h at f44
    n "Wait...what...?"
    n 4p "Oh no, you are {i}not{/i} screwing with the code again, are you!?"
    show natsuki 5o at t44
    show yuri 3y2 at f41
    y "I...{i}I'm{/i} not...!"
    show yuri at t41
    show sayori at f32
    call st_e
    s "Desiccant applies itself most gradually inside the interiors of exteriors whose interiors have exteriors containing interiors housed within exteriors surrounding-"
    call st_n
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1.0
    hide screen tear
    show sayori 1n
    show yuri 3n
    show natsuki 5c
    s "..."
    show yuri 2e at t31
    show natsuki 2k at t33 zorder 3
    show sayori at t32
    m "There - is that better?"
    show sayori pissed_chronos_skit at t43 zorder 2
    s "Listen {i}here{/i} you miserable excuse for a fracking walking piece of worthless doo-doo..."
    show yuri 3y4
    show natsuki 2m
    s "Either you find a way to pull your own poopy-covered head out of your own behind and {i}make me some gosh darned baked goods this freaking instant...{/i}"
    show yuri 3y2
    show natsuki react_chronos_skit
    s "...Or I'm going to gut you like a danged pickled herring and hang what's left in the doorway for club decorations."
    show natsuki scream at t44
    show yuri 4d at f41
    show sayori at t43
    y "M-monika...this is absolutely {i}not{/i} an improvement!"
    show yuri 3y2 at t41
    show natsuki 1v at f44
    n "FIX HER NOW!"
    show natsuki at t44
    m "Uuhhh~!  I think this might do it...?"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1.0
    hide screen tear
    show sayori aroused_1_chronos_skit
    show natsuki 5g
    show yuri 2y6
    s "But first...Natsuki..."
    show sayori aroused_2_chronos_skit
    s "I think I want to take the time to... {i}really{/i} show you how much I appreciate you..."
    show yuri 3y4
    show natsuki 1k zorder 3
    s "The closet is right over there...why don't we head inside, lock the door, and you can show me your entire 'manga collection...'"
    show sayori at t33 zorder 2
    show natsuki 3h
    show yuri 3y2
    s "I guarantee that it'll be the best 'reading session' your tight little body has ever had..."
    show natsuki 12a
    show yuri 4d at f41
    y "M-Monika...!"
    show natsuki 12b
    show yuri at t41
    m "Still!?  Alright...I'll just have to restore her from a backup."
    show natsuki 12c at f44
    show yuri 3y6
    n "Ummm...actually, I'm okay if you leave her like this for a bit..."
    
    return
