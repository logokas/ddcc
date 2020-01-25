# Skit template by Ceane
# This template should help you get going, and set up your own skit to be compatible with the rest of the game.
# Author of the skit, and any credits for assets or parts of code should be commented here, at the start of the file

# It's by Chiff the Oblivious#4251, and the background is surprisingly enough from the DDLC store.

# If you don't want to use one of the original game's thumbnails (e.g. club_date, corridor_date, class_date), then define it here.
image merchandise_thumnail = "mod_assets/merchandise/merchandise_thumbnail.png"

# First, we need to add our skit to the list of skits that the game looks at.
init -200 python:
    skit_merchandise = Skit(
        "Merchandise", # Set this to be the title of your skit.
        "merchandise", # Set this to be the label that you call below.
        "merchandise_thumbnail", # Set this to be the thumbnail you want for your skit. If you aren't using one from the original game, then you'll need to define its image.
        "@Chiff the Oblivious#4251" # Author
    )

    skits.append(skit_merchandise) # Add your skit to the list! Make sure it matches the name above.

image merchandise_bg01 = "mod_assets/merchandise/merchandise_bg01.png"

# Now, for the actual scene:
label merchandise(preserve_transition=True): # Don't change the preserve_transition part, but rename "template" to what you want your label to be.

    scene bg black # Whatever scene you want
    if preserve_transition == True:
        with dissolve_scene_full
        # You can have whatever transition effects you want at the start of your script, as long as you put them in this if block.
        # This is used for triggering the transition depending on whether or not someone is going through the game in "Play All" mode,
        # or through scene selection.

    "I gently open the DDLC store."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    show merchandise_bg01
    pause 3.76
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    pause 3.00
    stop music

    return