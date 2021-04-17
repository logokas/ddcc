# Super Smash Bros for Natsuki
# Written by u/ImTheRealSlayer (discord tag: ImTheRealSlayer#7976)
# JoJo's Bizarre Adventure is property of Hirohiko Araki
# Image of link being fucked (up by cloud, presumably) is property of me.

image template_thumnail = "mod_assets/ssb4n/ssb4n_thumbnail.png"
image bg ssb4n_final = "mod_assets/ssb4n/final.png"
image natsuki ssb4n_gcn = im.Composite((960, 960), (0, 0), "mod_assets/ssb4n/gcn.png")
image natsuki ssb4n_gcns = im.Composite((960, 960), (0, 0), "mod_assets/ssb4n/gcns.png")
image ssb4n_menacing default = im.Composite((960,960), (400,0), "mod_assets/ssb4n/go.png")
image ssb4n_menacing2 default = im.Composite((960,960), (200,0), "mod_assets/ssb4n/go.png")
image natsuki ssb4n_dio = im.Composite((960,960), (0,0), "mod_assets/ssb4n/natsudio.png")
image bg ssb4n_bedroom_menacing = "mod_assets/ssb4n/bedroom-stand.png"
image ssb4n_stando world = im.Composite((960,960), (0,0), "mod_assets/ssb4n/world.png")
define audio.ssb4n_yareyare = "mod_assets/ssb4n/yareyare.mp3"

init -200 python:
    skit_ssb4n = Skit(
        "Super Smash Bros. for Natsuki",
        "ssb4n",
        "ssb4n_thumbnail",
        "@ImTheRealSlayer#7976 (/u/ImTheRealSlayer)"
    )

    skits.append(skit_ssb4n)


label ssb4n(preserve_transition=True):

    scene bg club_day 
    if preserve_transition == True:
        with dissolve_scene_full
        with wipeleft_scene
        # You can have whatever transition effects you want at the start of your script, as long as you put them in this if block.
        # This is used for triggering the transition depending on whether or not someone is going through the game in "Play All" mode,
        # or through scene selection.
    
    play music t5
    show natsuki 1 zorder 2 at t11
    n "Hey [player]."
    mc "Hey Natsuki, what's up?"
    n 5u "I was wondering... If we could, y'know..."
    mc "Y'know...?"
    stop music fadeout 1.0
    "She leans over to whisper in my ear"
    n 5s "If we could smash."
    "W-w-w-"
    "WHATTT??!!"
    n 2w "You don't have to if you don't want to, but..."
    mc "No! I mean yes! It's fine!"
    stop music fadeout 1.0
    "This is gonna be great! I've always wanted to do this for the longest time."
    n 1t "Is it okay if we do it at your house?"
    mc "Yeah, my parents aren't home, so it'll be fine."
    n 1l "Alright, cool. Thanks [player]. See you tomorrow!"
    hide natsuki with dissolve
    scene black
    with wipeleft_scene
    
    play music t6
    scene bg bedroom
    with wipeleft_scene
    mc "Today's the day! I'm finally gonna smash Natsuki!!"
    "*{i}knock knock knock{/i}*"
    "She's here~!"
    
    scene bg house
    with wipeleft_scene
    show natsuki 1bj zorder 2 at t11
    n "Well, [player], I made it."
    n 2bz "Despite your directions,"
    mc "Okay {i}super intendant{/i}, enough with the meme references. {i}Come{/1} on inside."
    "This is my chance."
    "I will smash Natsuki!"
    hide natsuki with dissolve

    scene bg kitchen
    with wipeleft_scene
    "*{i}thud{/i}*"
    mc "So, uh, what's in the bag?"
    show natsuki 1ba zorder 2 at t11
    n 4bb "Heh, it's a surprise. You'll find out {i}later{/i}."
    mc "I'm just gonna go to the bedroom to get everything sorted. Come up when you're ready."
    n 1ba "Alright, I'll only be a minute."
    hide natsuki with dissolve
    
    scene bg bedroom
    with wipeleft_scene
    "Alright, alright, alright!"
    "We're gonna do this!"
    "*{i}knock knock{/i}*"
    n "Are you in there [player]?"
    "Ah shit! Quickly! Get into position!!"
    "I rush to sit on the bed in a sexy looking position."
    mc "Y-Yeah, come in!"
    stop music fadeout 2.0
    show natsuki 2 zorder 2 at t11
    n ssb4n_gcn "Who's ready to sma-{nw}"
    play music t7
    n ssb4n_gcns "OH MY GOD!!"
    "I see natsuki walk in holding a gamecube controller her Snake amiibo."
    n "W-w-w-w-w-"
    mc "It's not what it looks like!{nw}"
    n 1bv "WHAT THE HELL DID YOU THINK WE WERE GONNA DO?!"
    "Well, I didn't think this trough at all."
    stop music fadeout 2.0
    play music t6
    n 2be "*sigh*, Well, I came here to smash I suppose."
    n 2bf "Might as well just play anyways."
    mc "A-Alright..."
    "On one side, I'm really dissapointed that I didn't get to smash."
    "But on the other side..."
    "I finally have a formiddable opponent!"
    mc "Let me get it ready real quick..."
    "I pull out the Wii U gamepad, and-"
    n 1bm "Is that..."
    n 1bn "The Wii U?"
    mc "..."
    mc "yes."
    n 5bx "You're telling me you {i}don't{/i} have Ultimate???"
    mc "..."
    mc "perhaps?"
    n 5bw "Ugh, you're useless sometimes!"
    n 1bv "Now I can't even use my amiibo."
    mc "Speaking of, why did you bring that thing?"
    n 3bk "Oh, this?"
    n 3bl "I brought it just in case I needed a formiddable oponent."
    stop music fadeout 2.0
    mc "Oh really?"
    play music ssb4n_yareyare
    "I walk up and put the Super Smash Bros. disc into the console"
    mc "Then prepare your ass to be kicked."
    scene bg ssb4n_bedroom_menacing
    show ssb4n_menacing default zorder 2 at t41
    show ssb4n_menacing2 default zorder 2 at t44
    show natsuki ssb4n_dio zorder 3 at h11
    n "Oh? You're approaching me?"
    mc "I can't beat the shit out of you without getting closer."
    show natsuki ssb4n_dio zorder 3 at t43
    show ssb4n_stando world zorder 2 at s42
    n "Oh ho ho! Then come as close as you like!"
    hide natsuki
    hide ssb4n_menacing
    hide ssb4n_menacing2
    hide ssb4n_stando
    with dissolve
    scene bg ssb4n_final
    with dissolve_scene_full
    "Natsuki ended up kicking [player]'s ass, as they were a mediocre Link main."
    "Natsuki wasn't able to use her Snake amiibo and resorted to playing against level 9 computers while [player] cried in the corner"
    return
