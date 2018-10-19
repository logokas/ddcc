## Attribution/Credit for assets used in Chronos' skits:
## - Alternate Monika expressions provided by LunaticRabbit and Yagamirai.
## - "Swoosh" SFX pulled from this file here: https://freesound.org/people/speedygonzo/sounds/257656/
## - "r##" positions originally defined by TsunCrazy
## - As well as most custom poses that aren't possible in the regular game's engine being helpfully created with AgentGold's posing tool, even if the actual posing tags were not used.

### Definitions and utilities used for Chronos' skits.
##############################################################
## Utilities:
## I've made these utilities just to make my life as a scripter a bit easier - I put a weird/long bit of code or function behind a label, and then anytime I want I just call that much shorter label to make it quicker on my end.  Boom, easy way to increase your productivity as a scripter.

## First one's to call that "swoosh" SFX used for when the characters fly onscreen.
## To do this, we'll use a little bit of python to basically call a random variable, and make it one of 4 variables randomly - that way, each of the 4 variants on the swoosh SFX has an equal chance of randomly being played whenever it's called.
label swoosh:
    python:
        import random
        swoosh_x = random.randint(0,3)
    if swoosh_x == 0:
        play sound "mod_assets/chronos/chronos_sfx01.ogg"
    if swoosh_x == 1:
        play sound "mod_assets/chronos/chronos_sfx02.ogg"
    if swoosh_x == 2:
        play sound "mod_assets/chronos/chronos_sfx03.ogg"
    if swoosh_x == 3:
        play sound "mod_assets/chronos/chronos_sfx04.ogg"
    
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
## Special definitions for Monika being annoyed.
## Unlike the other definitions - which are single images - we'll use compositing to make these images, so that the head can basically be thrown into any "regular" tagging pose that would work for her.
## To do that, we have to make a version for each variation on tags - 1 through 4 - for each head that can be attached - of which there are three versions.
## To make sure we don't accidentally step on someone else's tags, these are intentionally kind of long tags, but for your own project you should try and keep them shorter and simpler, so that you can write the tag out quickly.
## Personally, I prefer to use /u/AgentGold's posing utility, which completely bypasses this entire step of having to write definitions out yourself, and allows MUCH MUCH MORE flexibility with the poses you can make for the characters.
## But - worry about that once you're a bit more comfortable with this in general.
image monika 1chr_ce = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_closed_eyes_annoyed_head.png")
image monika 1chr_oecm = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_closed_mouth_head.png")
image monika 1chr_oeom = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_yelling_head.png")

image monika 2chr_ce = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_closed_eyes_annoyed_head.png")
image monika 2chr_oecm = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_closed_mouth_head.png")
image monika 2chr_oeom = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_yelling_head.png")

image monika 3chr_ce = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_closed_eyes_annoyed_head.png")
image monika 3chr_oecm = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_closed_mouth_head.png")
image monika 3chr_oeom = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_yelling_head.png")

image monika 4chr_ce = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_closed_eyes_annoyed_head.png")
image monika 4chr_oecm = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_closed_mouth_head.png")
image monika 4chr_oeom = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/chronos/chronos_m_open_eyes_annoyed_yelling_head.png")
    
    
    
## Sayori's glitch sprite definition:
## So this one will automatically cycle through all 4 of the below images, paused between each for the duration listed below each image, before returning to the top again.
image sayori glitch_chronos_skit:
    "mod_assets/chronos/chronos_s_glitch_u223112_d.png"
    pause 0.125
    "mod_assets/chronos/chronos_s_glitch_u223112_l.png"
    pause 0.125
    "mod_assets/chronos/chronos_s_glitch_u223112_u.png"
    pause 0.125
    "mod_assets/chronos/chronos_s_glitch_u223112_r.png"
    pause 0.375
    repeat
    
    
## Most of the rest of the images below are single images I created for the purpose of just having that image available for the character.
## Again, this is intended to be a learning exercise first and foremost for how to use the base game's systems - for that reason, I've intentionally not done what I would prefer to do, which is just use /u/AgentGold's posing tool; my own mod utilizes it exclusively.
## Special react image for Natsuki:
image natsuki react_chronos_skit:
    "mod_assets/chronos/chronos_n_react_1.png"
    
    
    
## Special "Point" image for Natsuki:
image natsuki point_1_chronos_skit:
    "mod_assets/chronos/chronos_n_point_1.png"
    
    
    
## Special "Pissed off" Sayori:
image sayori pissed_chronos_skit:
    "mod_assets/chronos/chronos_s_pissed.png"
    
    
    
## Special "Aroused" Sayori:
image sayori aroused_1_chronos_skit:
    "mod_assets/chronos/chronos_s_aroused_1.png"
    
    
    
## Second "aroused" Sayori:
image sayori aroused_2_chronos_skit:
    "mod_assets/chronos/chronos_s_aroused_2.png"
    
    
    
## Reusing the code for Yuri's death CG, but to namespace properly we'll need to use a new definition for the persistent in use.
default yuri_kill_chronos_skit = 0
    
    
    
## Repurposed code for Yuri's death CG:
## Basically, defining the image this way essentially makes it so that the definition of the picture is tied to a variable; when that variable changes, the images' definition also changes.  This is exactly the same way it's done in regular DDLC with Yuri's death scene, just simplified here since the image is only on screen for about a second because it automatically cycles through.
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
    
    
## Yuri self-stabbing definitions.  There's a lot, so here's a block of them.
image yuri chr_01:
    "mod_assets/chronos/chronos_y_stab_embarrassed_open_mouth.png"
image yuri chr_02:
    "mod_assets/chronos/chronos_y_stab_embarrassed_closed_mouth.png"
image yuri chr_03:
    "mod_assets/chronos/chronos_y_stab_admitting.png"
image yuri chr_04:
    "mod_assets/chronos/chronos_y_stab_train_open_mouth.png"
image yuri chr_05:
    "mod_assets/chronos/chronos_y_stab_train_closed_mouth.png"
image yuri chr_06:
    "mod_assets/chronos/chronos_y_stab_flustered_response.png"
image yuri chr_07:
    "mod_assets/chronos/chronos_y_stab_flustered_open_mouth.png"
image yuri chr_08:
    "mod_assets/chronos/chronos_y_stab_peeved_1.png"
image yuri chr_09:
    "mod_assets/chronos/chronos_y_stab_peeved_2.png"
image yuri chr_10:
    "mod_assets/chronos/chronos_y_stab_peeved_3.png"
image yuri chr_11:
    "mod_assets/chronos/chronos_y_stab_peeved_4.png"
image yuri chr_12:
    "mod_assets/chronos/chronos_y_stab_peeved_5.png"
    
    
    
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