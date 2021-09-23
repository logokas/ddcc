# Entry point
label start:
    stop music fadeout 1.5

    python:
        skits = sorted(skits, key=lambda skits: skits.skit_position)
        for script in skits:
            renpy.call_in_new_context(script.call_label, preserve_transition=False)
            renpy.call_in_new_context("skit_transition")
    
    if not persistent.ddcc_complete:
        call endgame
    call endgame2
    return

screen scenechoice1:
    if len(skits) > 0:
        imagebutton idle skits[0].thumbnail action [SetVariable('jumpLabel',skits[0].call_label), Jump(label="cleanJump")]  xcenter .42 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[0].name xcenter .42 ycenter .317 style "monika_text"
    if len(skits) > 1:
        imagebutton idle skits[1].thumbnail action [SetVariable('jumpLabel',skits[1].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[1].name xcenter .6 ycenter .317 style "monika_text"
    if len(skits) > 2:
        imagebutton idle skits[2].thumbnail action [SetVariable('jumpLabel',skits[2].call_label), Jump(label="cleanJump")] xcenter .42 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[2].name xcenter .42 ycenter .571 style "monika_text"
    if len(skits) > 3:
        imagebutton idle skits[3].thumbnail action [SetVariable('jumpLabel',skits[3].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[3].name xcenter .6 ycenter .571 style "monika_text"
    if len(skits) > 4:
        imagebutton idle skits[4].thumbnail action [SetVariable('jumpLabel',skits[4].call_label), Jump(label="cleanJump")] xcenter .42 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[4].name xcenter .42 ycenter .826 style "monika_text"
    if len(skits) > 5:
        imagebutton idle skits[5].thumbnail action [SetVariable('jumpLabel',skits[5].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[5].name xcenter .6 ycenter .826 style "monika_text"
    if len(skits) > 6:
        textbutton "Next >>>" action Jump("Choice1") xcenter .64 ycenter .95 style "monika_text" hover_sound "gui/sfx/hover.ogg" activate_sound "sfx/pageflip.ogg"


screen scenechoice2:
    if len(skits) > 6:
        imagebutton idle skits[6].thumbnail action [SetVariable('jumpLabel',skits[6].call_label), Jump(label="cleanJump")] xcenter .42 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[6].name xcenter .42 ycenter .317 style "monika_text"
    if len(skits) > 7:
        imagebutton idle skits[7].thumbnail action [SetVariable('jumpLabel',skits[7].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[7].name xcenter .6 ycenter .317 style "monika_text"
    if len(skits) > 8:
        imagebutton idle skits[8].thumbnail action [SetVariable('jumpLabel',skits[8].call_label), Jump(label="cleanJump")] xcenter .42 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[8].name xcenter .42 ycenter .571 style "monika_text"
    if len(skits) > 9:
        imagebutton idle skits[9].thumbnail action [SetVariable('jumpLabel',skits[9].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[9].name xcenter .6 ycenter .571 style "monika_text"
    if len(skits) > 10:
        imagebutton idle skits[10].thumbnail action [SetVariable('jumpLabel',skits[10].call_label), Jump(label="cleanJump")] xcenter .42 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[10].name xcenter .42 ycenter .826 style "monika_text"
    if len(skits) > 11:
        imagebutton idle skits[11].thumbnail action [SetVariable('jumpLabel',skits[11].call_label), Jump(label="cleanJump")] xcenter .6 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
        text skits[11].name xcenter .6 ycenter .826 style "monika_text"
    textbutton "<<< Previous" action Jump("Choice2") xcenter .38 ycenter .95 style "monika_text" hover_sound "gui/sfx/hover.ogg" activate_sound "sfx/pageflip.ogg"

label choose:
    stop music fadeout 2.0
    window hide
    show screen scene_select()
    with dissolve_scene_full
    play music t4
    pause
    #scene bg notebook with Dissolve(0.5, alpha=True)
    #play music t4
    #label Choice2:
    #   hide screen scenechoice2
    #   show screen scenechoice1
    #if False:
    #   label Choice1:
    #       hide screen scenechoice1
    #       show screen scenechoice2
    #while True:
    #   pause 50.0
    jump choose #This return will send us back to the title screen after the skit we picked is done.

label cleanJump:
   hide screen scenechoice1
   hide screen scenechoice2
   hide screen main_menu
   stop music fadeout 2.0
   #jump expression jumpLabel

label endgame:
    scene black
    $ pause (1.0)
    show hanaka 1g at t11
    h "Sorry to keep you waiting!"
    scene bg club_day
    show hanaka 1g at t11
    with dissolve_cg
    h "Much better."
    h 1ses "I just wanted to thank you for playing [config.name]!"
    h 1m "I know this project has taken over three years to complete, but it's not my fault it is finally out the 4th anniversary of DDLC."
    h 1g "A-Anyways."
    h 1 "I hope you enjoyed all the skits that were made by the DDMC community!"
    h 1g "Everyone put a lot of dedication towards these skits and appreciate everyone that submitted one to be part of DDMC history."
    h 1 "Now that you reached the end, you might be wondering what to do next."
    h "Why not play through everyone's skits again?"
    h 1m "What? Is that not enough?"
    h "Fine. Here."
    $ pause (1.0)
    $ persistent.ddcc_complete = True
    $ renpy.notify("DDCC Completed")
    h 1s "I added a special \"Play\" button in the game for you."
    h "This will allow you to play through a skit of your choosing without going through the headache of playing every other skit."
    h 1 "With that out of the way, thank you again for playing DDCC 2!"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if list(set(process_list).intersection(stream_list)):
        h 1s "But before you go, I have one last thing to say."
        $ pause (1.0)
        h 1g "Hi Influencer! Hi Everyone Else!"
        h 1ses " Ahaha~. I always wanted to do that."
    return

# the end label of the game. Not the credits.    
label endgame2(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
    