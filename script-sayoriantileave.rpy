# Skit template by Ceane
# This template should help you get going, and set up your own skit to be compatible with the rest of the game.
# Author of the skit, and any credits for assets or parts of code should be commented here, at the start of the file

# If you don't want to use one of the original game's thumbnails (e.g. club_date, corridor_date, class_date), then define it here.
image template_thumbnail = "images/bg/club.png"
transform t51:
    tcommon(140)
transform t61:
    tcommon(100)
transform t71:
    tcommon(60)
transform t72:
    tcommon(12)
transform t81:
    tcommon(5)
transform t91:
    tcommon(-100)
transform t101:
    tcommon(-200)
transform t111:
    tcommon(-290)
# First, we need to add our skit to the list of skits that the game looks at.
init -200 python:
    skit_antileave = Skit(
        "Don't let Sayori leave, I swear to god!", # Set this to be the title of your skit.
        "no_leave", # Set this to be the label that you call below.
        "template_thumbnail", # Set this to be the thumbnail you want for your skit. If you aren't using one from the original game, then you'll need to define its image.
        "@KarasilSothren#9772, /u/Karasilsothren",
        skit_position = 14
    )

    skits.append(skit_antileave) # Add your skit to the list! Make sure it matches the name above.
#this was so I could test it on it's own outside of the comedy club mod and have more control
#default preserve_transition = True
# Now, for the actual scene:
label no_leave(preserve_transition=True): # Don't change the preserve_transition part, but rename "template" to what you want your label to be.

    scene bg club_day # Whatever scene you want
    if preserve_transition == True:
        with dissolve_scene_full
        # You can have whatever transition effects you want at the start of your script, as long as you put them in this if block.
        # This is used for triggering the transition depending on whether or not someone is going through the game in "Play All" mode,
        # or through scene selection.
    play music t10
    show sayori 2l at t11
    s "Hey, I'm going to go home. Tell Monika I wasn't feeling good."
    "I almost feel myself say sure but something prevents me from doing so."
    stop music
    mc "You shouldn't leave. We still have other things to do."
    s 4h "What?"
    mc "Just come with me."
    "I take Sayori by the arm and drag her to everyone else."
    s 1p "What are you doing?"
    mc "Bringing you back to the rest of the club."
    show sayori 4m at t41
    s 3l "Hey, I said I wanted to go home..."
    "I ignore Sayori knowing it was for her own good."
    play music t3
    mc "Hey guys, can you make sure Sayori stays here for the rest of the meeting?"
    show monika 1d at f11
    m "Why would we need to do that?"
    show sayori at f41
    show monika at t11
    s 1k "I'm feeling under the weather."
    mc "And that's why you need to stay."
    show sayori at t41
    show monika at f11
    m 3i "I'm not sure about this."
    show monika at t42
    show natsuki 1m at f43
    n "What's going on?"
    mc "I'm trying to have Sayori not leave."
    show sayori at t51
    "Sayori starts walking away."
    show sayori 4n at t41
    mc "Sayori what are you doing?"
    show sayori at f41
    s 5b "Nothing."
    show sayori at t41
    show yuri 1f at f44
    y "What's going on?"
    show yuri at t44
    show natsuki at f43
    n "Apparently we are trying to prevent Sayori from leaving."
    show sayori 1k at t61
    m "It's not going well."
    show sayori at t72
    mc "Sayori!"
    show sayori 4p at t41
    mc "I swear she doesn't want to hang out with us or something."
    show sayori 1l at t51
    show natsuki at f43
    n 5w "Well {b}MAYBE{/b} it's because of you forcing her to stay here."
    show sayori at t61
    mc "I'm just worried about her is all."
    show sayori at t71
    n "Worried is a bit of an understatement."
    show sayori at t81
    y "I'm with Natsuki on this one."
    show sayori at t72
    m "Okay I'm done with this."
    show sayori 4p at t41
    mc "Sayori don't leave I swear to god!"
    python: 
        renpy.sound.play("sfx/interference.ogg", channel='sound', loop=True)
    window hide
    $ consolehistory = []
    call updateconsole("Raise class shields", "Raising")
    $ consolehistory = []
    call updateconsole("", "Raising{fast}.")
    $ consolehistory = []
    call updateconsole("", "Raising.{fast}.")
    $ consolehistory = []
    call updateconsole("", "Raising..{fast}.")
    $ consolehistory = []
    call updateconsole("", "Raising Complete")
    $ consolehistory = []
    call hideconsole
    stop sound
    show natsuki 1k
    show yuri 2g
    mc "What did you do?"
    m "I prevented Sayori from leaving, so that should do it."
    mc "So there's nothing here that would allow her to leave?"
    show sayori 3l at t51
    m 4r "The only thing that's here is rope, but what would she do with that?"
    show sayori at t61
    mc "Climb out the window?"
    show sayori at t71
    m "I blocked all points of access so there would still be no way she could leave."
    show sayori at t81
    mc "So there is no way out?"
    show sayori at t91
    m "No and if there was I'm sure I could cover that one as well if I had to."
    show sayori at t101
    mc "Are you sure, because I am really worried about her."
    show sayori at t111
    m "Yes now let's continue this meeting then."
    m "Sayori can't leave plain and simple."
    show screen tear(20, 0.1, 0.1, 0, 40)
    stop music
    pause 0.25
    hide sayori
    show s_kill at t61:
        yoffset -0.6
    hide screen tear
    show natsuki scream
    show yuri 3p
    show monika 1r at t42 zorder 2
    mc "What the hell happened!?"
    m "Nope I am not dealing with this, this is your fault."
    m "Should've let her leave."
    m 3i "But instead she hung herself!"
    m "So guess what she left and you won't be seeing her again."
    $ renpy.call_screen("dialog", "I'm done with this shit.", ok_action=Return())
    return