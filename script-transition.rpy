# Transition Setup and Resetting of Variables for next Skit

# This file is to generate a transition between skits while playing through them
# and to wipe/reset all changes to variables and other material to ensure residual
# leftovers are not carried over from one skit to the next.

# Defining the Transition assets
define audio.transition1 = "mod_assets/shared_assets/DDLC_Ditty_Grand_Piano.ogg"
define audio.transition2 = renpy.random.choice(["mod_assets/shared_assets/DDLC_Ditty_Choir_Aahs.ogg", "mod_assets/shared_assets/DDLC_Ditty_Oboe.ogg", "mod_assets/shared_assets/DDLC_Ditty_Orchestra_Hit.ogg", "mod_assets/shared_assets/DDLC_Ditty_Overdrive_Guitar.ogg", "mod_assets/shared_assets/DDLC_Ditty_Steel_Drums.ogg", "mod_assets/shared_assets/DDLC_Ditty_Viola.ogg"])
image bg transition_image = "mod_assets/shared_assets/transition_default.png"
define transition_glitch_intro = True

# Transition Code
# NOTE: For this transition to work properly both in and out, all played skits
# must not use any transitions, and avoid using the screen tear type of
# effects to avoid anything doubling up and awkward fades.

label skit_transition:

    # We insert a screen tear first to ease in
    window hide
    if transition_glitch_intro == True:
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.3)
        stop sound
        hide screen tear
    $ quick_menu = False
    stop music
    show bg transition_image zorder 4
    if renpy.random.randint(1,100) == 100:
        play music transition1
    else:
        play music transition2
    
    # While the music is playing, lets reset everything back to normal
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    $ m_name = "Monika"
    $ transition_glitch_intro = True
    
    # Finally a screen tear to ease out
    $ pause (2)
    stop music
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.5)
    stop sound
    hide screen tear
    #window show(None)
    stop music
    $ quick_menu = True
    return