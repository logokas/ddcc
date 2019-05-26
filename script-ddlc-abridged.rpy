## "DDLC Abridged" - By Chronos#1609

init -200 python:
    skit_ddlc_abridged = Skit(
        "DDLC Abridged", # Title
        "ddlc_abridged", # Label
        "residential_day_date", #Thumbnail
        "Chronos#1609"
    )

    skits.append(skit_ddlc_abridged)

label ddlc_abridged(preserve_transition=True):
    
    stop music fadeout 2.0
    scene bg residential_day
    if preserve_transition == True:
        with dissolve_scene_full
    play music t2
    
    mc "I'm both bored and boring."
    show sayori 4r at r11
    call swoosh
    s "I'm your childhood friend who you have somehow never noticed has both deep-rooted depression issues and also has developed feelings for you!"
    s "Join my book club!"
    show sayori 1i
    mc "No."
    s 3j "Every other member besides you would be a girl and one of them made you food already."
    show sayori 1a
    mc "Okay!"
    show sayori at lhide
    hide sayori
    call swoosh
    "I then followed along because otherwise the plot wouldn't go anywhere."
    
    stop music
    scene bg club_day
    play music t6
    
    show yuri 1d at r11 zorder 2
    call swoosh
    y "I'm Yuri!  I'm the socially awkward bookworm of the club who is the most mature both mentally and physically if you somehow couldn't tell from my enormous breasts.  Also, I like knives too much."
    show yuri 1a at t21
    show natsuki 4d at r22 zorder 3
    show natsuki at f22
    call swoosh
    n "I'm Natsuki!  I'm the petite tsundere who is ostracized for partaking in a perfectly normal hobby for some reason and who can't ever accept a compliment without being upset about it!  Also, I have daddy issues."
    show yuri at t31
    show natsuki 4a at t32
    show monika 4b at r33
    show monika at f33 zorder 4
    call swoosh
    m "I'm Monika, and I'm just a background character who relays game state information to you."
    m 1i "...And nothing more."
    show monika 1c at t33
    mc "So what do we do here?"
    show monika 3d at f33
    m "Crush dreams, mostly."
    show monika 1c at t44
    show natsuki at t43
    show yuri at t42
    show sayori 2w at l41 zorder 3
    show sayori at f41
    call swoosh
    s "By the way, I really love you player!"
    show sayori 2v
    menu:
        "Okay!":
            pass
        "Okay...?":
            pass
    s 2w "Nooo!"
    show sayori at lhide
    hide sayori
    call swoosh
    pause 0.5
    show s_kill at l41 zorder 3
    call swoosh
    mc "...Aaaand she's dead.  Huh.  Didn't see that one coming."
    show monika 3l at f44
    m "Uhh...look! A distraction!"
    mc "Where!?"
    $ srf = screenshot_srf()
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    hide yuri
    hide s_kill
    hide natsuki
    hide monika
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1.0
    
    scene bg class_day
    hide screen tear
    
    stop music
    play music t2
    
    show monika 3g at i11
    m "Forget about that.  All of that."
    show monika 1f
    mc "Okay...?"
    m 1b "You want to join my book club?"
    show monika 1f
    mc "No."
    m 4i "Look, if you don't, then nothing here has any meaning."
    show monika 2a
    mc "Okay!"
    show monika at rhide
    hide monika
    call swoosh
    "I then followed along because otherwise the plot wouldn't go anywhere."
    
    stop music
    scene bg club_day
    play music t6
    
    
    show yuri 3y1 at r11
    call swoosh
    y "I'm Yuri, and I {i}really{/i} like you, and knives, and also have too much blood at the moment."
    show yuri 3y3 at t21
    show natsuki 3m at r22
    show natsuki at f22
    call swoosh
    n "I'm Natsuki, and I'm somehow now the most reasonable person here.  Also, I get shafted out of an ending, unlike everyone else."
    show yuri at t31
    show natsuki 3u at t32
    show monika 4l at r33
    show monika at f33
    call swoosh
    m "We've already met before, and I'm no one new. Just Monika!"
    m 2i "Remember that, it's going to be a meme someday."
    show monika 2h at t33
    y stab_1 "Hey! I figured out how to fix that ‘too much blood' problem!"
    
    show yuri stab_2
    play sound "sfx/stab.ogg"
    show blood:
        pos (220,485)
    pause 0.2
    stop sound
    show yuri stab_3
    pause 0.2
    stop sound
    show yuri stab_2
    play sound "sfx/stab.ogg"
    show blood zorder 5:
        pos (220,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 0.2
    stop sound
    show yuri stab_5
    pause 0.2
    show yuri stab_6:
        0.2
        easeout_cubic 0.2 yoffset 1000
    play sound "sfx/stab.ogg"
    show blood as blood2:
        pos (245,335)
    pause 0.2
    stop sound
    hide blood
    hide blood2
    play sound fall
    pause 0.2
    hide yuri
    
    
    mc "...Aaaand she's dead.  Huh.  Didn't see that one coming."
    mc "I could be wrong though.  I better stare at her in case she's trying to trick me."
    
    stop music
    play music t7g
    
    show y_kill_chronos_skit
    label yuri_kill_loop_chronos_skit:
        $ yuri_kill_chronos_skit += 1
        if yuri_kill_chronos_skit < 11:
            pause 0.1
            jump yuri_kill_loop_chronos_skit
        else:
            jump DDLC_abridged_after_the_bit_where_yuri_dies
    
label DDLC_abridged_after_the_bit_where_yuri_dies:
    
    stop music
    scene bg club_day
    play music t6
    
    show natsuki 3c at i21
    show natsuki at f21
    show monika 2c at i22
    n "Look, this is getting old.  Can I just go now?"
    show natsuki 3g at t21
    show monika 2d at f22
    m "Yeah, sure."
    show natsuki at lhide
    hide natsuki
    call swoosh
    show monika 2g at t11
    m "So, I might have ruined everything.  Are we cool...?"
    show monika 2f
    mc "No."
    
    show monika g2
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide monika
    pause 1.0
    
    m "Alright, fine.  Here's everyone else back."
    show natsuki 3k at r11
    call swoosh
    n "That was weird."
    show natsuki 1j at t21
    show yuri 3f at r22
    show yuri at f22
    call swoosh
    y "Yeah, right?"
    show natsuki at t31
    show yuri 1e at t32
    show sayori 3c at r33
    show sayori at f33
    call swoosh
    s "Yeah, totally.  Oh, hey, did you get the good ending or the bad one?"
    show sayori 3b at t33
    mc "I...don't know?"
    show sayori 4r at f33
    s "Well either way it's still depressing - just one is less depressing than the other.  Anyway, have fun making a mod with those new emotional scars!"
    
    return
