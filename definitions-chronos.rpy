### Definitions and utilities used for Chronos' skits.
##############################################################
## Utilities:

## First one's just to vary up the "swoosh" sfx in use.
label swoosh:
    python:
        import random
        swoosh_x = random.randint(0,3)
    if swoosh_x == 0:
        play sound "mod_assets/SFX/swoosh1.ogg"
    if swoosh_x == 1:
        play sound "mod_assets/SFX/swoosh2.ogg"
    if swoosh_x == 2:
        play sound "mod_assets/SFX/swoosh3.ogg"
    if swoosh_x == 3:
        play sound "mod_assets/SFX/swoosh4.ogg"
    
    return
    
    
    
## Second one's to lessen the amount of typing for glitch text:
label st_e:
    $ style.say_dialogue = style.edited
    
    return
    
    
    
## Third one's to return the style to normal from the glitch text.
label st_n:
    $ style.say_dialogue = style.normal
    
    return
    
    
    
## End of Utilities
##############################################################
## Definitions:

## Sayori's glitch sprite definition:
image sayori glitch_chronos_skit:
    "mod_assets/Special/Sayori_glitch_u223112_d.png"
    pause 0.125
    "mod_assets/Special/Sayori_glitch_u223112_l.png"
    pause 0.125
    "mod_assets/Special/Sayori_glitch_u223112_u.png"
    pause 0.125
    "mod_assets/Special/Sayori_glitch_u223112_r.png"
    pause 0.375
    repeat
    
    
    
## Special react image for Natsuki:
image natsuki react_chronos_skit:
    "mod_assets/Special/Natsuki_react_1.png"
    
    
    
## Special "Pissed off" Sayori:
image sayori pissed_chronos_skit:
    "mod_assets/Special/Sayori_pissed.png"
    
    
    
## Special "Aroused" Sayori:
image sayori aroused_1_chronos_skit:
    "mod_assets/Special/Sayori_aroused_1.png"
    
    
    
## Second "aroused" Sayori:
image sayori aroused_2_chronos_skit:
    "mod_assets/Special/Sayori_aroused_2.png"
    
    
    
## Reusing the code for Yuri's death CG, but to namespace properly we'll need to use a new definition for the persistent in use.
default yuri_kill_chronos_skit = 0
    
    
    
## Repurposed code for Yuri's death CG:
image y_kill_chronos_skit = ConditionSwitch(
    "yuri_kill_chronos_skit  >= 10", "images/cg/y_kill/3a.png",
    "yuri_kill_chronos_skit  >= 9", "images/cg/y_kill/3c.png",
    "yuri_kill_chronos_skit  >= 8", "images/cg/y_kill/3b.png",
    "yuri_kill_chronos_skit  >= 7", "images/cg/y_kill/3a.png",
    "yuri_kill_chronos_skit  >= 6", "images/cg/y_kill/2c.png",
    "yuri_kill_chronos_skit  >= 5", "images/cg/y_kill/2b.png",
    "yuri_kill_chronos_skit  >= 4", "images/cg/y_kill/2a.png",
    "yuri_kill_chronos_skit  >= 3", "images/cg/y_kill/1c.png",
    "yuri_kill_chronos_skit  >= 2", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png",
    )
    
    
## End of Definitions
#################################################################
## Transforms:

## The only transforms here are the ones that define being able to come in from the right side of the screen; these were originally created by TsunCrazy, with the exception of rhide; I (Chronos) did that, though it's basically just an inverted copy of lhide anyway.

transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

#Fly in rapidly from the right
transform rightin(x=640, z=0.80):
    xcenter 1500 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

#Same positioning, but fly in from the right
transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)