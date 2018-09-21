# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

call chaos from _call_chaos

#currently semi-broken scene selector

#screen scenechoice1:
#    imagebutton idle "corridor_date" action [SetVariable('jumpLabel','chaos'), Jump(label="cleanJump")]  xcenter .42 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "Chaos" xcenter .42 ycenter .317 style "monika_text"
#    imagebutton idle "corridor_date" xcenter .6 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "Third floor" xcenter .6 ycenter .317 style "monika_text"
#    imagebutton idle "class_date" xcenter .42 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-A Classroom" xcenter .42 ycenter .571 style "monika_text"
#    imagebutton idle "class_date" xcenter .6 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-B Classroom" xcenter .6 ycenter .571 style "monika_text"
#    imagebutton idle "class_date" xcenter .42 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-C Classroom" xcenter .42 ycenter .826 style "monika_text"
#    imagebutton idle "club_date" xcenter .6 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "Literature Club" xcenter .6 ycenter .826 style "monika_text"
#    textbutton "Next >>>" action Jump("Choice1") xcenter .64 ycenter .95 style "monika_text" hover_sound "gui/sfx/hover.ogg" activate_sound "sfx/pageflip.ogg"
#
#
#screen scenechoice2:
#    imagebutton idle "corridor_date" xcenter .42 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "First floor" xcenter .42 ycenter .317 style "monika_text"
#    imagebutton idle "corridor_date" xcenter .6 ycenter .217 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "Third floor" xcenter .6 ycenter .317 style "monika_text"
#    imagebutton idle "class_date" xcenter .42 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-A Classroom" xcenter .42 ycenter .571 style "monika_text"
#    imagebutton idle "class_date" xcenter .6 ycenter .471 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-B Classroom" xcenter .6 ycenter .571 style "monika_text"
#    imagebutton idle "class_date" xcenter .42 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "2-C Classroom" xcenter .42 ycenter .826 style "monika_text"
#    imagebutton idle "club_date" xcenter .6 ycenter .726 hover_sound "gui/sfx/hover.ogg" activate_sound "gui/sfx/select.ogg"
#    text "Literature Club" xcenter .6 ycenter .826 style "monika_text"
#    textbutton "<<< Previous" action Jump("Choice2") xcenter .38 ycenter .95 style "monika_text" hover_sound "gui/sfx/hover.ogg" activate_sound "sfx/pageflip.ogg"
#
#label choose:
#    scene bg notebook with Dissolve(0.5, alpha=True)
#    play music t4
#    label Choice2:
#        hide screen scenechoice2
#        show screen scenechoice1
#    if False:
#        label Choice1:
#            hide screen scenechoice1
#            show screen scenechoice2
#    while True:
#        pause 50.0
#
#label cleanJump:
#    hide screen scenechoice1
#    hide screen scenechoice2
#    hide screen main_menu
#    stop music fadeout 2.0
#    jump expression jumpLabel