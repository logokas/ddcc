# Skit template by Ceane
# Sayo-nara: Mania Adventures edition by CPG Yuri - SEGA and Sonic Team allows using Sonic assets and content for fangames and fan material: https://www.destructoid.com/sega-gives-sonic-fans-the-okay-to-make-games-386389.phtml
# Hanged Sonic sprite extracted from Sonic Mania Adventures: Part 1 video, https://www.youtube.com/watch?v=rDYbwdEn7rs
# Song credits: [Sonic CD] Palmtree Panic - "B" Remixed - SHiRUBA シルバー, https://www.youtube.com/watch?v=V87X51g0n-Q

#Definitions of stuff used for the skit
#DJ Scratch stop sound
define audio.djstop = "mod_assets/sayomania/sayomania_djstop.ogg"
# Song
define audio.sayomania_01 = "mod_assets/sayomania/sayomania_bgm01.ogg"
# Sonic hanged image
image s_kill_sonic:
    subpixel True
    "mod_assets/sayomania/sayomania_sonic_kill.png"

init -200 python:
    skit_template = Skit(
        "Sayo-nara: Mania Adventures edition",
        "sayomania", 
        "sayori_room_date" 
    )

    skits.append(skit_template)

# Now, for the actual scene:
label sayomania(preserve_transition=True):

    scene bg club_day 
    if preserve_transition == True:
        with dissolve_scene_full
    
    play music t2
    $ n_name = "Sonic" #Borrowing Natsuki's name variable and changing it to Sonic for this skit only
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again as always. She doesn't even answer my calls."
    m 1k "Ahaha~!"
    $ currentpos = get_pos(channel="music")
    stop music
    $ audio.t2moni = "<from " + str(currentpos) + " loop 0>bgm/2.ogg"
    m "{i}You kind of left her hanging this morning, you know?{/i}"
    show monika 4a
    $ renpy.music.play(audio.t2moni)
    mc "Monika?"
    mc "Oh crap, what is this...?"
    "{i}I got a pit in my stomach all of a sudden, again.{/i}"
    "{i}Is this some kind of deja vu?{/i}"
    m 1d "What's wrong?"
    mc "I-I changed my mind, Monika! I'm going to go get Sayori!!!"
    m 5a "Don't strain yourself, [player]~!"
    
    scene bg residential_day with wipeleft_scene
    "No no no no no no no no no no no no no no no no no no no no no no no no no no no..."
    "Not again!"
    "I need to move at a faster change in the position of my entire body, divided by the time, in direction to the place where the subject called 'my best friend' has her place of habitation!"

    scene bg house with wipeleft
    mc "Sayori! Are you there???"
    mc "No answer... That's it! I will not wait this time!"
    scene black with wipeleft
    mc "Sayori?"
    stop music fadeout 2.0
    "There's no response."
    "She really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    show s_kill_bg
    show s_kill_sonic at s_kill_start
    pause 4.0
    stop music
    play sound djstop
    show sayori 1v at h22 zorder 5
    "..."
    play music sayomania_01
    mc "Sayori!!!"
    mc "Seriously???"
    mc "I almost died of a heart attack, you dummy!!!"
    mc "Can you please explain what is going on right now???"
    s 4w "Please don't judge me, [player]...!"
    s 4p "I just wanted to have Sonic all for myself! He is so fluffy and cute!!!"
    s "So I set a trap for him, sent him a poem to rescue me and he arrived and I captured him with the rope I was supposed to use for..."
    s "Anyway! Please forgive me!!! I will accept the restitution!"
    show sayori 5a at t22 zorder 5
    n "Retribution."
    n "And also, hello there, you two! Can you release me from this stupid rope? Thank you!"
    "And that's the story about how Sayori and I missed the Festival Day. It was the best day ever, after all."
    $ n_name = "Natsuki" #giving Natsuki her name back.

    return