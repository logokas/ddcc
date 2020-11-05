# Transition Setup and Resetting of Variables for next Skit

# This file is to generate a transition between skits while playing through them
# and to wipe/reset all changes to variables and other material to ensure residual
# leftovers are not carried over from one skit to the next.

import random

# Defining the Transition assets
define audio.transition1 = "mod_assets/shared_assets/transition1.wav"
define audio.transition2 = "mod_assets/shared_assets/transition2.ogg"
image bg transition_image = "mod_assets/shared_assets/transition_default.png"
image bg transition_alt = "mod_assets/shared_assets/transition_alt.png"
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
    if randint(1,100) <= 10:
        show bg transition_alt zorder 4
        play music transition2
    else:
        show bg transition_image zorder 4
        play music transition1
    
    # While the music is playing, lets reset everything back to normal
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    $ m_name = "Monika"
    $ transition_glitch_intro = True
    
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