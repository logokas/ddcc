init -200 python:
    skit_nocallnatcute = Skit(
        "Don't Call A Tsundere Cute", # Title
        "natcute", # Label
        "club_date", #Thumbnail
        "@KarasilSothren#9772, /u/Karasilsothren"
    )

    skits.append(skit_nocallnatcute)
transform rocket(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0
    pause 1.0
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0
    pause 1.0
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0
    pause 1.0
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -2000
transform irocket(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -1000
transform irocket41:
    irocket(200)
transform irocket42:
    irocket(493)
transform irocket43:
    irocket(786)
transform irocket44:
    irocket(1080)
transform irocket31:
    irocket(240)
transform irocket32:
    irocket(640)
transform irocket33:
    irocket(1040)
transform irocket21:
    irocket(400)
transform irocket22:
    irocket(880)
transform irocket11:
    irocket(640)
transform rocket41:
    rocket(200)
transform rocket42:
    rocket(493)
transform rocket43:
    rocket(786)
transform rocket44:
    rocket(1080)
transform rocket31:
    rocket(240)
transform rocket32:
    rocket(640)
transform rocket33:
    rocket(1040)
transform rocket21:
    rocket(400)
transform rocket22:
    rocket(880)
transform rocket11:
    rocket(640)
label natcute(preserve_transition=True):
    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    show natsuki 4a at t11
    "I walk into the club room seeing Nat waiting."
    mc "Hey cutie."
    n 1q "I-I'm not cute."
    mc "But-"
    show natsuki at t22
    show sayori 4r at l21
    "Before the words leave my mouth Sayori walks in."
    s "Hey Natsuki, looking cute today."
    n 1r "I am still not cute."
    "Then Yuri walks in."
    show natsuki at t32
    show sayori at t33, behind natsuki
    show yuri 1a at l31
    y "Hey Natsuki, you're looking cuter than normal."
    show natsuki 1x at hop
    n "Yuri I am not cute."
    "Then Monika walks in last."
    show natsuki at t42 zorder 5
    show yuri at t43, behind natsuki
    show sayori at t44
    show monika at l41
    m 4k "Hey who brought the cutie. Oh wait never mind it's just Natsuki"
    show natsuki 1w
    "It looks like Nat's about to blow a fuse."
    show natsuki 1v at rocket42
    n "I {w=1.0}am {w=1.0}not {w=1.0}CUTE!!!!!{nw}"
    $ _history_list.pop()
    show sayori 4p at h44
    show yuri 3p at h43
    show monika 4n at h41
    n "I {w=1.0}am {w=1.0}not {w=1.0}CUTE!!!!!{fast}"
    m 4n "Oh, I think she just popped a fuse..."
    s 5a "Whoops, ehehe."
    y 4e "..."
    m "Let me fix this real quick."
    window hide
    call updateconsole("Restore \"natsuki.chr\"", "Character restored")
    call hideconsole
    pause 1.0
    show natsuki 1v at t42
    pause 2.0
    show natsuki 1v at irocket42
    pause 1.0
    show monika 1r
    call updateconsole("Restore \"natsuki.chr\"", "Character restored")
    call hideconsole
    show natsuki 1v at t42
    show monika at t21
    m "Now Natsuki don't cutely rocket off now."
    n "AHHHH!!"
    show natsuki at irocket42
    m "I'm just going to restart the day."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    scene bg club_day
    show natsuki 1a at t11
    hide screen tear
    "I walk in and see Nat."
    mc "Hye cutie."
    n 1q "I-I'm not cute."
    mc "But you so are, I mean look at you."
    show natsuki at t22
    show sayori 4r at l21
    "But before she can argue. Sayori walks in."
    s "Hey Natsuki, looking cute today. Really cute actually."
    n 1r "I-I am still not cute."
    "Then Yuri walks in."
    show natsuki at t32
    show sayori at t33, behind natsuki
    show yuri 1a at l31
    y "Hey Natsuki, you're looking cuter than normal."
    show natsuki 1x at hop
    n "I am not cute. Everyone."
    "Then Monika walks in last."
    show natsuki at t42 zorder 5
    show yuri at t43, behind natsuki
    show sayori at t44
    show monika at l41
    m 4r "Can you guys stop calling her cute, she's going to blow a fuse otherwise."
    show natsuki 1y
    n "Thank you Monika."
    mc "But come on she's undeniably cute."
    show sayori 4r at h44
    s "Yeah, no one cuter!"
    show natsuki 1w
    y "The cutest."
    show natsuki 1v at rocket42
    n "I!{w=1.0} AM!{w=1.0} NOT!{w=1.0} CUTE!!!!!!!!!!!!!!!!!!!!"
    show monika at t11
    show sayori at t44
    show yuri at t41, behind monika
    m "Nope I am not dealing with this."
    call screen dialog("Whe have launched Natsuki enough times.", ok_action=Return())
    return