# Entry point
label start:
    stop music fadeout 1.5

    python:
        skits = sorted(skits, key=lambda skits: skits.skit_position)
        for script in skits:
            renpy.call_in_new_context(script.call_label, preserve_transition=False)
            renpy.call_in_new_context("skit_transition")

    #TODO: call credits from _call_credits
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
    window hide
    play music t4
    show screen scene_select()
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
