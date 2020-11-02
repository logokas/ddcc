transform breasts:
    tcommon(690)
    
transform fbreasts:
    focus(690)

image YurisFriends_thumbnail = "mod_assets/Tormuse/YurisFriends_thumbnail.png"

init -200 python:
    skit_YurisFriends = Skit(
        "Yuri's Friends",
        "YurisFriends",
        "YurisFriends_thumbnail",
        "@Tormuse#9495, u/Tormuse"
    )

    skits.append(skit_YurisFriends)

label YurisFriends(preserve_transition=True):
    scene bg club_day
    if preserve_transition:
        with Dissolve(1)
    play music t3
    show yuri 3o at l32 zorder 2
    "Yuri is the last one to arrive at the club meeting."
    "She looks like she's in distress."
    show yuri 3n at t32 zorder 2
    mc "Yuri, are you okay?"
    y 3o "It's nothing.  It's nothing.  I j-just...  need a moment to calm down."
    show sayori 1g at t31 zorder 2
    show monika 1f at t33 zorder 2
    "Everyone else turns to look at her with concern."
    show monika 1g at f33 zorder 3
    m "What happened, Yuri?"
    show monika 1f at t33 zorder 2
    show yuri 4c at f32 zorder 3
    play music t9 fadeout 1
    y "It's really nothing I can't handle."
    y "Just...  some of my classmates having fun at my expense."
    y "The only reason it troubles me at all is..."
    y 4d "B-because it's a reminder that I don't have any friends."
    show yuri 4c at t32 zorder 2
    show sayori 2h at f31 zorder 3
    s "Oh, Yuri!  That's not true!"
    show monika 1e at t33 zorder 2
    show sayori 1q at t42 zorder 1
    "Sayori goes up to Yuri and gives her a big hug..."
    show sayori 1r at f42 zorder 1
    s "We're your friends.  We care about you!"
    show sayori 1q at t42 zorder 1
    show monika 1b at f33 zorder 3
    m "That's right."
    show monika 1j at t43 zorder 1
    "Monika goes up to Yuri and hugs her from the other side."
    show monika 1k at f43 zorder 1
    m "You can always turn to us if you're feeling down."
    show monika 1j at t43 zorder 1
    show yuri 4e at t32 zorder 2
    "I can see Yuri smiling weakly behind her hair."
    show yuri 4e at f32 zorder 2
    y "Th-thank you...  it's nice to know there are people I can turn to."
    show yuri 4e at t32 zorder 2
    show natsuki 1e at t33 zorder 2
    n "Yeah, your classmates are a bunch of jerks.  Don't listen to them."
    show natsuki 1g at breasts zorder 3
    show sayori 1n at t42 zorder 1
    show monika 1f at t43 zorder 1
    show yuri 1o at t32 zorder 2
    "Natsuki goes over and puts her hands on Yuri's breasts."
    show yuri 1t at f32 zorder 2
    y "Ah...  Natsuki..."
    show yuri 1t at t32 zorder 2
    show natsuki 1e at fbreasts zorder 3
    n "What?"
    show natsuki 1g at breasts zorder 3
    show monika 1g at f43 zorder 1
    m "Natsuki, that's a little inappropriate."
    show monika 1f at t43 zorder 1
    show natsuki 1h at fbreasts zorder 3
    n "Well, it was the only part of her I could reach."
    show natsuki 1i at breasts zorder 3
    show sayori 1o at f42 zorder 1
    s "Uh..."
    show sayori 1o at t42 zorder 1
    show natsuki 4w at fbreasts zorder 3
    n "Look...  I just think they're cool, okay?  Don't judge me!"
    show natsuki 4s at breasts zorder 3
    "..."
    mc "Anyway..."
    mc "You can count on my friendship too, Yuri."
    show yuri 1b at f32 zorder 2
    y "Thank you, [player]."
    y 1u "..."
    show monika 1m at t43 zorder 1
    show sayori 4m at t42 zorder 1
    show natsuki 1p at breasts zorder 3
    y 4e "If you want to join in, there's still some space on my butt."
    return