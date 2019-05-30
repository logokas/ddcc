# Pun Club
# Author: KC (VirtualKibou#0811 on Discord)

define audio.badumtss = "mod_assets/punclub/punclub_sfx_badumtss.wav"

#image punclub_thumbnail = "mod_assets/punclub/punclub_thumbnail.png"
image punclub_thumbnail = im.FactorScale("mod_assets/punclub/punclub_thumbnail.png",0.3,0.3)
image sayori wink = "mod_assets/punclub/punclub_s_wink.png"
image yuri wink = "mod_assets/punclub/punclub_y_wink.png"
image natsuki wink = "mod_assets/punclub/punclub_n_wink.png"

init -200 python:
    skit_punclub = Skit(
        "Pun Club",
        "punclub",
        "punclub_thumbnail"
    )

    skits.append(skit_punclub)

label punclub(preserve_transition=True):

    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    
    play music t5b

    show yuri 1h zorder 3 at f21
    show natsuki 1s zorder 2 at t22
    y "You know, Natsuki..."
    show natsuki 1e zorder 3 at f22
    show yuri 1h zorder 2 at t21
    n "What?"
    show yuri 1b zorder 3 at f21
    show natsuki 1g zorder 2 at t22
    y "I had plans to tell you something about knives..."
    y "...but I don't know if you're {i}sharp{/i} enough to understand it."
    show yuri wink zorder 3 at hf21
    play sound audio.badumtss
    show layer master: # zoom entire screen in to designated position (in this case Yuri's winking face)
        subpixel True
        linear .2 zoom 2.0 pos (-200, -50)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    show yuri 1c zorder 2 at t21
    show natsuki 1w zorder 3 at f22
    n "DAMMIT, YURI!"
    show natsuki 1x zorder 3 at f22
    n "You're worse at puns than you are at being sane."
    show yuri 1q zorder 3 at f21
    show natsuki 1x zorder 2 at t22
    y "Oh...is that so..."
    show yuri 1q zorder 2 at t21
    show natsuki 1k zorder 3 at f22
    n "Yes."
    show yuri 1h zorder 2 at t21
    show natsuki 4t zorder 3 at hf22
    n "Actually, that reminds me..."
    show natsuki 1d zorder 3 at f22
    n "I was gonna crack a joke about pencils, but you would've missed the {i}point{/i}."
    show natsuki wink zorder 3 at hf22
    play sound audio.badumtss
    show layer master:
        subpixel True
        linear .2 zoom 2.0 pos (-1000, -200)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    show yuri 1d zorder 3 at f21
    show natsuki wink zorder 2 at t22
    y "That was terrible."
    show yuri 1c zorder 2 at t21
    show natsuki 1o zorder 3 at hf22
    n "Ghhhhhhhh-!"
    show natsuki 5f zorder 3 at f22
    n "You're saying that as though-\"{space=5000}{w=0.0}{nw}"
    show sayori 4r zorder 3 at l31
    show yuri 1j at t32
    show natsuki 1q zorder 2 at t33
    s "Hiiiiii everyone~!"
    show sayori 4x zorder 3 at f31
    s "What are you doing?"
    show sayori 1a zorder 2 at t31
    show natsuki 1r zorder 3 at f33
    n "Noth-\"{space=5000}{w=0.0}{nw}"
    show yuri 2d zorder 3 at f32
    show natsuki 1r zorder 2 at t33
    y "Puns, Sayori."
    show yuri 1c zorder 2 at t32
    show natsuki 1v zorder 3 at f33
    n "YURI, NO!"
    show sayori 4n zorder 3 at hf31
    show natsuki 1v zorder 2 at t33
    s "P-puns...?"
    show sayori 4l zorder 3 at f31
    s "W-well...now that you've said so..."
    show sayori 1s zorder 3 at f31
    s "I would've brought glue, but this already seems like a {i}sticky{/i} situation."
    show sayori wink zorder 3 at hf31
    play sound audio.badumtss
    show layer master:
        subpixel True
        linear .2 zoom 2.0 pos (0, -100)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    show sayori 1q zorder 2 at t31
    show yuri 1g zorder 2 at t32
    show natsuki 5f zorder 3 at f33
    n "Now look what you've done..."
    show yuri 1p zorder 3 at f32
    show natsuki 5f zorder 2 at t33
    y "W-what {i}I{/i} did?!"
    show yuri 1p zorder 2 at t32
    show natsuki 12c zorder 3 at f33
    n "I KNOW WHAT I SAID!"
    show sayori 1v zorder 3 at f31
    s "Wait, why are we-\"{space=5000}{w=0.0}{nw}"
    show monika 1k zorder 3 at l41
    show sayori 1m zorder 2 at t42
    show yuri 1o zorder 2 at t43
    show natsuki 1q zorder 2 at t44
    m "Okay, everyone - I'm here!"
    show monika 1l zorder 3 at f41
    m "Sorry for being late ag-\"{space=5000}{w=0.0}{nw}"
    show monika 1k zorder 2 at t41
    show sayori 1c zorder 3 at f42
    s "Monika, are you a circus thief?"
    show sayori 1b zorder 2 at t42
    show monika 1c zorder 2 at t41
    pause .5
    show monika 1d zorder 3 at f41
    m "A what now?"
    show monika 1c zorder 2 at t41
    show sayori 1r zorder 3 at f42
    s "A circus thief!"
    show sayori 1l zorder 3 at f42
    s "Because, after all..."
    show sayori 1r zorder 3 at f42
    s "...you kinda {i}stole the show{/i} just now."
    show sayori wink zorder 3 at hf42
    play sound audio.badumtss
    show layer master:
        subpixel True
        linear .2 zoom 2.0 pos (-275, -100)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    show monika 1d zorder 3 at f41
    show sayori 1q zorder 2 at t42
    m "I..."
    show monika 1c zorder 2 at t41
    show yuri 1d zorder 3 at f43
    show natsuki 1f zorder 2 at t44
    y "Your voice makes you sound like falling rain."
    y "Are you feeling at all under the {i}weather{/i} today, Monika?"
    show yuri wink zorder 3 at hf43
    play sound audio.badumtss
    show layer master:
        subpixel True
        linear .2 zoom 2.0 pos (-900, -50)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    show monika 1d zorder 3 at f41
    show yuri 1c zorder 2 at f43
    m "..."
    show monika 1c zorder 2 at t41
    show natsuki 12c zorder 3 at f44
    n "Oh, for crying out loud..."
    show natsuki 4t zorder 3 at f44
    n "I was tempted to say something about birds..."
    n "...but it woulda {i}flown{/i} right over your head!"
    show natsuki wink zorder 3 at hf44
    play sound audio.badumtss
    show layer master:
        subpixel True
        linear .2 zoom 2.0 pos (-1280, -50)
        pause .5
        ease .2 zoom 1.0 pos (0, 0)
    pause 1
    stop music
    show monika 1h zorder 3 at f41
    show natsuki wink zorder 2 at t44
    m "..."
    show monika 1r zorder 3 at f41
    m "I'm fucking deleting the game."
    show monika 1r zorder 2 at t41
    show sayori 4m zorder 2 at h42
    show yuri 3p zorder 2 at h43
    show natsuki scream zorder 3 at hf44
    n "SON OF A-\"{space=5000}{w=0.0}{nw}"
    window show(None)
    call screen dialog("These puns are too much.", ok_action=Return())
    call screen dialog("Goodbye.", ok_action=Return())
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    scene black
    if preserve_transition == False:
        $ transition_glitch_intro = False
    window hide
    $ pause(1.5)
return
