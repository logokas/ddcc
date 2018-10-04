# Transition Setup and Resetting of Variables for next Skit

# This file is to generate a transition between skits while playing through them
# and to wipe/reset all changes to variables and other material to ensure residual
# leftovers are not carried over from one skit to the next.

# Defining the Transition assets
define audio.transition1 = "mod_assets/transition1.wav"
image bg transition_image = "mod_assets/shared_assets/transition_image.png"

# Transition Code
label skit_transition:

    # We insert a screen tear first to ease in
    window hide
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.3)
    stop sound
    hide screen tear
    $ quick_menu = False
    stop music
    show bg transition_image zorder 4
    play music transition1
    
    # While the music is playing, lets reset everything back to normal
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    $ m_name = "Monika"
    
    # Finally a screen tear to ease out
    $ pause (3)
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