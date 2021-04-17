##"Under New Management" by Chronos#1609

init -200 python:
    skit_management = Skit(
        "Under New Management", # Title
        "under_new_management", # Label
        "club_date", #Thumbnail
        "@Chronos#1609, /u/chronoshag",
        skit_position = 3
    )

    skits.append(skit_management)


label under_new_management(preserve_transition=True):
    
    scene bg club_day
    show sayori 1b at t11
    if preserve_transition == True:
        with dissolve_scene_full
    play music t5
    
    
    mc "So...this is the club you run, Sayori?"
    s 2x "Yeah!  I'm the president, so it's my responsibility to manage it!"
    show sayori 1a at t32
    show yuri 1b at r33
    show yuri at f33
    y "Sayori has excelled at leading us, as well as keeping on top of the necessary administrative tasks."
    show sayori 1q
    show yuri 1a at t33
    show natsuki 3d at l31
    show natsuki at f31
    n "Yeah!  And best of all...she lets us read whatever we want, whenever we want, without bugging us!"
    show sayori 2f
    show yuri 1g
    n 5q "Not like that {i}fucking bitch{/i} who used to run this place..."
    show natsuki 5s at t31
    show yuri 2r at f33
    y "I'm inclined to agree...she was about as pleasant as Gonorrhea, minus the implied enjoyment that happens beforehand."
    show yuri 2g at t33
    mc "Wow...you guys must {i}really{/i} have hated her..."
    show sayori 4j at f32
    s "Oh, totally!  I can't think of a more mean-spirited, hateful, petty, selfish, jealous, {i}complete and utter cu-{/i}"
    show sayori 4i at t32
    
    $gtext1 = glitchtext(4)
    $gtext2 = glitchtext(10)
    $gtext3 = glitchtext(4)
    $gtext4 = glitchtext(100)
    
    $ m_name = "Mon[gtext1]ika"
    $ style.say_window = style.window_monika
    
    call st_e
    m "[gtext2]YOU KNOW I CAN STILL HEA-[gtext3]-R ALL OF YOU ASSHOLES!\n[gtext4]"
    call st_n
    
    ## Returning these to their normal values, both so that the scene can continue on normally (the style window) and out of courtesy for other skits (Monika's display name).
    $ m_name = "Monika"
    $ style.say_window = style.window
    
    show natsuki 5a
    show sayori 1q
    show yuri 3m
    mc "..."
    mc "Uhh...did...any of you hear that...?"
    show natsuki 3j
    show yuri 2a
    show sayori 4r at f32
    s "Mmm...nope!  Nothing important, anyway!"
    show sayori 1q at t32
    show natsuki 4d at f31
    n "I bet it was a bird...a colossally huge {i}bitch{/i} of a bird."
    show natsuki 4z at t31
    show yuri 1d at f33
    y "Perhaps it was the rare 'Spoon-billed-{i}go-fuck-yourself.'{/i}"
    
    return
