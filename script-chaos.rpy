# "Chaos" by Logokas

image monika 6 = im.Composite((960, 960), (0, 0), "mod_assets/chaos/super-monika.png")

label chaos(preserve_transition=True):

    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    play music t5

    show sayori 1d zorder 2 at i33
    #voice "mod_assets/chaos/chaos_s01.wav"
    s "Uh, Monika?"
    #voice "mod_assets/chaos/chaos_s02.wav"
    s "The..Club and I were wondering.."
    #voice "mod_assets/chaos/chaos_s03.wav"
    s 1h "What're those colored stones you've been using to make this place go funny lately?"
    show monika 1b zorder 3 at l32
    voice "mod_assets/chaos/chaos_m01.wav"
    m "Ahaha!"
    show monika 3a zorder 3 at f32
    voice "mod_assets/chaos/chaos_m02.wav"
    m "You mean, the Chaos Emeralds?"
    show monika 3a zorder 3 at t32
    show sayori 1h zorder 2 at f33
    #voice "mod_assets/chaos/chaos_s04.wav"
    s "Uh..\"{space=5000}{w=0.5}{nw}"
    show sayori 1h zorder 2 at t33
    show monika 1a zorder 3 at f32
    voice "mod_assets/chaos/chaos_m03.wav"
    m "I'm going to assume you mean the Chaos Emeralds."
    show monika 5a zorder 3 at hf32
    voice "mod_assets/chaos/chaos_m04.wav"
    m "If that's what you're wondering about, I've got all of them, right here!"
    #Monika Shifts to Super Monika
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    play sound "mod_assets/chaos/chaos_sfx01.wav"
    show monika 6 zorder 3 at h32
    pause 1
    show sayori 4o zorder 2 at hf33
    #voice "mod_assets/chaos/chaos_s05.wav"
    s "Whoa!"
    #use forced dialogue movement
    show natsuki 1o zorder 1 at l31
    #voice "mod_assets/chaos/chaos_n01.wav"
    n "Are you fucking serious?! You can't just-\"{space=5000}{w=0.75}{nw}"
    show monika 6 zorder 3 at hf32
    stop music fadeout 1.5
    play sound "mod_assets/chaos/chaos_sfx02.wav"
    voice "mod_assets/chaos/chaos_m05.wav"
    m "Chaos Delete!\"{space=5000}{w=0.75}{nw}"
    show monika 6 zorder 3 at t32
    show natsuki scream zorder 1 at hf31
    #voice "mod_assets/chaos/chaos_n02.wav"
    n "Wait no no no-!\"{space=5000}{w=0.4}{nw}"
    #Cut to black with an explosion sound
    window hide(None)
    scene black
    pause 3
    # Remove the glitch intro of the transition as it's a black screen, so you wouldn't be able to see it anyway.
    if preserve_transition == False:
        $ transition_glitch_intro = False
    return