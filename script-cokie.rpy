# Author of this script goes to /u/AinsleyHairyott
# The credits of music, sfx, etc. are located in definitions-cokie.rpy

#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓█▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▒▓▒▓▒▒█▒▒▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▒▒▒▓▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒▒▒▒▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▒▒▒▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓░▒▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒░▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒░▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▒▒▓▒▓▓░░▒▒▒░▒█▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▓▓▓▒▒▒▒▓▒▒▒▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒▒░░░░▒▒▒▒▒▒░█▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▒░░░░░   ░▓▒▓▓▒▒▓▒▒▒▒▓▒▒▒░▒▓░░▒▓▒▒▒▒▒▒▓▒▓▓▒▒▒▓▒▓▓░        ░░▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░▒▓▓▓▒▓▒▓▒▒▓▒▓▓▒▒▒▒▓▓▒▒▓▒▒▒▒▒▒▒▓▒▓▒▒▒▓▓▓▓▒░     ░░░▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▓█▓▓▓▓▓▓▒▒▓▒▓▓▒▒▒▒▒▓▓▒▓▓▓▒▓▒▒▒▒▓▓▓▒▒▓▓▓▓▓░▒░░░░░▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▒▓▓▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▓▓▒▓▓▓▓▒▒▓▓▓▓▓▒░░░░░▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▓▓▓▓▓▓▓▓▓▓▒▓▓░▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▓▒▓▓▓▓▒▓▓░░░▒░░░▓▓▓▒▒▓▓▓▒▒░▓▓▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓░░▓███▒░░░░░░░░░░░░▒▓██▓░░▒▓▒▒▒▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▓▓▓▓▓█▓██░░░░░░░░░░░░░▒█▓▓██▒▓▒▒▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒▓▒▒░░▓▒░░▓░░░░░░░░░░░░░▓░░▒░░░▒▒▒▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▒▓▓▓▒▒█▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▒▒▓▓█▓░▓▓▒▒▒█▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▒▒▒▓▓▓░▒▓▓▒▒▒▓▓▓▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░░█▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░█▓▓▓▒▒▒▓▓▓░░▓▓▒▒▓▒▒█▓▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ░▓▓▓▓▒▒▓▓▓█░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒▓▓▓▒░ ▓▒▒▒▒▒▒▒▓▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  █▓▓▓▓▒▒▒▓▓▓▓▒░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▒▒▓▓▓▓░░░▓▒▒▒▒█▒▒▓▓▓▓                                                              
#                                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ░▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓ ░▓▒▒▒▒██▒▒▓▓ 

#                                                                           "Already checking the in-game files?"
#                                                                              "No reason to worry yourself."
#                                                                "There's new things you can discover and learn in this script!"
#                                                                                  "Like easing functions!"
#                                                                        "So you can be a talented modder like this guy!" (AinsleyHairyott)
#                                                                  "But I can tell already that you're a truly heartwarming modder."
#                                                                       "Will you promise to make for me a romantic mod?"
#                                                                      "J͟͠͡ų̀͡s̨t͠ onl҉y ͏m̷è̡̡ ̨͟҉a͘͢nd̷ ̕̕ỳ͘͝o̷u̡.́"



init -200 python:
    skit_cokie = Skit(
        "The Cookie", 
        "script_cokie", 
        "cokie_thumbnail",
        "/u/AinsleyHairyott"
    )

    skits.append(skit_cokie)



label script_cokie(preserve_transition=True):
    
    if preserve_transition == True:
        scene black
        with wipeleft
    
    play music cokie_bgm01
                                        # Developer Comments
    scene bg club_day:
        subpixel True           # this line is very recommended to make your animations move more smoother by using subpixel positioning instead of regular pixel positioning.
        zoom 1.4                # Setting the zoom of the background, to make it a bit bigger.
        truecenter              # positions the image to middle part of the screen, unnecessary due to overtaken by the next line.
        xcenter 850 ycenter 325 # Initial position of the image by x-axis and y-axis.    ( "xcenter" and "ycenter" are the positioning transition by x-axis and y-axis. Unlike "xpos" and "ypos", both "xanchor" and "yanchor" are automatically set to 0.5 )
        yoffset 25              # Initial offset of the image by y-axis.
        easein 1 yoffset 0      # Final offset with an easing function.
        
        # Easing functions vary in set of easing directions, time, and any transitions. for example:
            
            #Suppose that my initial position in the x-axis is "xcenter -500", which is far left from the screen.
            #and my final position will be "xcenter 640", which is the center of the screen.
            #I want to move my image by moving initial position to my final position for 1 second.
            #Here is what it looks like:
                #xcenter -500
                #ease 1 xcenter 640 
                    
            #"ease" can be changeable, a list of easing directions can be found in easings.net
            
            # IMPORTANT: if you don't put any initial position of any axis, the image will sometimes set its initial position to zero. 
            
            
        # truecenter sets the xcenter to 640 and ycenter to 360.
        
        # You'll find some lines that contain "parallel" functions.
            # "Parallel" is a function that shares 2 or more easing functions to play at once. The numbers of "parallel" vary depending on how many easing functions you'll need to play at once.
            # For example:
            
                # xcenter 0 ycenter 0
                # parallel:
                #       ease 0.5 xcenter 640
                # parallel:
                #       ease 1 ycenter 360
                
            # This will play both easing functions at the same time.
        
        # For more information, check out the Ren'Py documentation in https://www.renpy.org/doc/html/
        
    show monika 2a at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        yoffset 50
        easein 1 yoffset 0
    show sayori 2x at i11:
        subpixel True
        zoom 1.1
        xcenter 900 ycenter 360
        yoffset 50
        easein 1 yoffset 0
    show black zorder 10:
        alpha 1
        easein 1 alpha 0
    
    pause 0.5
    "It's an ordinary day like any other. And in the club, Monika and Sayori are having a chit chat."
    show monika 2a at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        xoffset 0
        ease 2 xoffset -1250
    show sayori 2x at i11:
        subpixel True
        zoom 1.1
        xcenter 900 ycenter 360
        xoffset 0
        ease 2 xoffset -1250
    show bg club_day:
        subpixel True
        zoom 1.4
        xcenter 850 ycenter 325
        ease 2 xcenter 450
    "Time passes, Natsuki proudly returns to the table, tray in hand."
    show natsuki 2l at i11:
        subpixel True
        zoom 1.1
        xcenter 1500 ycenter 360
        easein_circ 0.5 xcenter 950
    n "Girls! The cupcakes are ready!"
    window hide(None)
    window auto
    show natsuki 2l at i11:
        subpixel True
        zoom 1.1
        xcenter 950 ycenter 360
        xoffset 0
        ease 0.5 xoffset 1250
    show bg club_day:
        subpixel True
        zoom 1.4
        xcenter 450 ycenter 325
        ease 0.5 xcenter 850
    show monika 2d at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        xoffset -1250
        ease 0.5 xoffset 0
    show sayori 2b at i11:
        subpixel True
        zoom 1.1
        xcenter 900 ycenter 360
        xoffset -1250
        ease 0.5 xoffset 0
    pause 0.65
    show sayori 4r at i11:
        subpixel True
        zoom 1.1
        xcenter 900 ycenter 360
        yoffset 0
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
    window show(None)
    window auto
    s "Yaay~! Cupcakes!"
    window hide(None)
    window auto
    show sayori 4r at i11:
        subpixel True
        zoom 1.1
        xcenter 900 ycenter 360
        xoffset 0
        easeout 0.25 xoffset 600
    pause 0.1
    show natsuki 2j at i11 behind sayori:
        zoom 1.1
        xcenter 150 ycenter 360
    pause 0.9
    show monika 1e at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        yoffset 0
        easein 0.25 yoffset 10
        easeout 0.25 yoffset 0
    window show(None)
    window auto
    m "I like how Sayori runs with an excitement on her face. It really makes me happy."
    window hide(None)
    show monika 1e at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        yoffset 0 xoffset 0
        parallel:
            ease_quad 3 xoffset 600
        parallel:
            ease_quad 0.75 yoffset -20
            ease_quad 0.75 yoffset 0
            repeat 2
    show sayori 4q at i11:
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900
    pause 0.75
    show layer master:
        subpixel True
        truecenter
        xcenter 640
        ease 1.75 xcenter -100 
    show bg club_day:
        subpixel True
        zoom 1.4
        xcenter 850 ycenter 325
        ease 1.75 xcenter 1125
    pause 1.5
    window show(None)
    s "Sho good..."
    show layer master:
        subpixel True
        xcenter -100
        ease 0.5 zoom 1.6 xcenter -1000 ycenter 500
    show bg club_day:
        subpixel True
        xtile 3
        zoom 1.4 xcenter 1125 ycenter 325
        ease 0.5 zoom 1.25 xcenter 1275 ycenter 295
    show sayori 4a at i11:
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900
        alpha 1
    show sayori 4q at i11 as s1 zorder 1:
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900
        alpha 1
        ease 0.5 alpha 0
    s "Thank you Natsuki~!"
    hide s1
    show layer master:
        subpixel True
        zoom 1.6 xcenter -1000 ycenter 500
        ease_quad 0.5 xcenter -700 ycenter 450
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1275 ycenter 295
        ease_quad 0.5 xcenter 1175 ycenter 305
    window hide(None)
    pause 0.5
    window show(None)
    n "Ehehe."
    show natsuki 2l at i11:
        subpixel True
        zoom 1.1
        xcenter 150 ycenter 360
        easein 0.25 xcenter 145 rotate -5 ycenter 370
        easeout 0.25 xcenter 150 ycenter 360 rotate 0
    n "I've also made cookies for myself."         
    show layer master:
        zoom 1.8 xcenter -1450 ycenter 550
    show bg club_day:
        xcenter 1400 ycenter 295 zoom 1.25
    show sayori 4g at i11:
        subpixel True
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    s 1b "Oooh...! I want some!"
    window hide(None)
    show layer master:
        subpixel True
        zoom 1.8 xcenter -1450 ycenter 550
        ease 0.5 xcenter -800 ycenter 475
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1400 ycenter 295
        ease 0.5 xcenter 1250 ycenter 300
    pause 0.55
    window show(None)
    n 4c "Jeez... Sayori. Why don't you make it for yourself?"
    window hide(None)
    show layer master:
        subpixel True
        zoom 1.8 xcenter -800 ycenter 475
        ease 0.5 xcenter -1450 ycenter 550
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1250 ycenter 300
        ease 0.5 xcenter 1400 ycenter 295
    pause 0.55
    show sayori 4g at i11:
        subpixel True
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900 yoffset 0
        easein 0.25 yoffset 10
        easeout 0.25 yoffset 0
    window show(None)
    s "Awww...! Please?"
    s "Just a bit..!"
    show natsuki 1x
    window hide(None)
    show layer master:
        subpixel True
        zoom 1.8 xcenter -1450 ycenter 550
        ease 0.5 xcenter -750 ycenter 475
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1400 ycenter 295
        ease 0.5 xcenter 1200 ycenter 300
    pause 0.55
    window show(None)
    n "I."
    show layer master:
        subpixel True
        zoom 1.8 xcenter -750 ycenter 475
        easein_elastic 1 zoom 2 xcenter -900 ycenter 525
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1200 ycenter 300
        easein_elastic 1 zoom 1.20 xcenter 1205 ycenter 295
    n "SAID."
    show natsuki 1w at i11:
        subpixel True
        zoom 1.1
        xcenter 140 ycenter 350
        parallel:
            easein_elastic 0.5 xcenter 150
        parallel:
            0.05
            easein_elastic 0.5 ycenter 360
    show layer master:
        subpixel True
        zoom 2 xcenter -900 ycenter 525
        easein_elastic 1 zoom 2.2 xcenter -1050 ycenter 575
    show bg club_day:
        subpixel True
        zoom 1.2 xcenter 1205 ycenter 295
        easein_elastic 1 zoom 1.15 xcenter 1215 ycenter 285
    n "NO!!"
    show layer master:
        subpixel True
        zoom 2.2 xcenter -1050 ycenter 575
        easein_back 1 zoom 1.8 xcenter -750 ycenter 475
    show bg club_day:
        subpixel True
        zoom 1.15 xcenter 1215 ycenter 285
        easein_back 1 zoom 1.25 xcenter 1200 ycenter 300
    show natsuki 4f
    with Dissolve(0.5)
    n "How many times do I need to say that?!"
    window hide(None)
    show monika 1g
    show layer master:
        subpixel True
        zoom 1.8 xcenter -750 ycenter 475
        ease 0.5 xcenter -300 ycenter 550
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1200 ycenter 300
        ease 0.5 xcenter 1100 ycenter 290
    pause 0.55
    window show(None)
    m "Come on, Natsuki. Just give her a bite."
    m "She will not eat your whole cookie. I promise."
    window hide(None)
    show layer master:
        subpixel True
        zoom 1.8 xcenter -300 ycenter 550
        ease 0.5 xcenter -750 ycenter 475
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1100 ycenter 290
        ease 0.5 xcenter 1200 ycenter 300
    show sayori 1g
    with None
    show natsuki 4s
    with Dissolve(0.5)
    pause 0.55
    show natsuki 4s at i11:
        subpixel True
        zoom 1.1
        xcenter 150 ycenter 360
        yoffset 0
        ease_quad 1 yoffset -10
        "natsuki 12c"
        zoom 0.88
        easein_quad 0.5 yoffset 10
    pause 1
    window show(None)
    n "{i}*Sigh*{/i}"
    show natsuki 1g at i11:
        subpixel True
        zoom 1.1
        xcenter 150 ycenter 360
        yoffset 10
        ease 0.25 yoffset 0
    with Dissolve(0.25)
    n "Alright, then."
    n 4a "It's yours, my friend."
    window hide(None)
    show natsuki 4a at i11:
        subpixel True
        zoom 1.1
        xcenter 150 ycenter 360
        rotate 0
        ease 0.5 rotate -50 ycenter 500 xcenter 0
        0.05
        ease 0.5 rotate 0 xcenter 150 ycenter 360
    show layer master:
        subpixel True
        zoom 1.8 xcenter -750 ycenter 475
        ease 1 zoom 1 xcenter -100 ycenter 360
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1200 ycenter 300
        ease 1 zoom 1.4 ycenter 325
    show cokie_n_cookie zorder 2:
        subpixel True
        zoom 0.25 xcenter 1250 ycenter 800
        0.55
        ease 0.5 ycenter 360
    with None
    show sayori 1d
    show monika 1e
    with Dissolve(0.5)
    pause 0.85
    show natsuki 4a at i11:
        subpixel True
        zoom 1.1 xcenter 150 ycenter 360
        rotate 0
        ease 0.2 xzoom -1
        0.5
        ease 0.45 rotate -20 xcenter 75 ycenter 370
    show cokie_n_cookie zorder 2:
        subpixel True
        xcenter 1250 ycenter 360 zoom 0.25
        rotate 0
        ease 0.2 xzoom -1 xcenter 1525
        0.5
        parallel:
            ease 0.45 ycenter 150
        parallel:
            0.15
            ease 0.45 xcenter 1200
    pause 1.35
    play sound cokie_sfx_whoosh
    show cokie_n_cookie zorder 2:
        subpixel True
        xcenter 1200 ycenter 150 xzoom -1
        zoom 0.25
        linear 0.3 xcenter 1790 ycenter 240 rotate 40 xoffset 550
    with None
    show natsuki 4d at i11:
        subpixel True
        zoom 1.1 xzoom -1 xcenter 75 ycenter 370
        rotate -20
        easein_elastic 0.5 rotate 10 xcenter 160 ycenter 365
    with Dissolve(0.1)
    stop music
    play sound "sfx/slap.ogg"
    show sayori 4p at i11:
        subpixel True
        zoom 1.1 xcenter 900 ycenter 360
        xoffset 900
        rotate 0
        linear 0.25 rotate 20 xoffset 1600
    show monika 1e at i11:
        subpixel True
        zoom 1.1
        xcenter 400 ycenter 360
        xoffset 600 yoffset 0
        0.375
        "monika 1d"
        zoom 0.88
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    show white zorder 9:
        xcenter 1380
        zoom 1.25
        alpha 0.6
        linear 0.25 alpha 0
    pause 1.5  
    hide white
    show natsuki 4d at i11:
        subpixel True
        zoom 1.1 xzoom -1 xcenter 160 ycenter 365
        rotate 10
        ease 0.5 rotate 0 xcenter 150 ycenter 360
    with None
    pause 0.75
    show layer master:
        subpixel True
        zoom 1 xcenter -100 ycenter 360
        easein_elastic 1 zoom 1.8 xcenter -750 ycenter 475
    show bg club_day:
        subpixel True
        zoom 1.4 xcenter 1200 ycenter 325
        easein_elastic 1 zoom 1.25 ycenter 300
    with None
    show natsuki 4y
    with Dissolve(0.1)
    window show(None)
    n "Taste that!"
    show layer master:
        subpixel True
        zoom 1.8 xcenter -750 ycenter 475
        easein_elastic 1 zoom 2 xcenter -900 ycenter 525
    show bg club_day:
        subpixel True
        zoom 1.25 xcenter 1200 ycenter 300
        easein_elastic 1 zoom 1.20 xcenter 1205 ycenter 295
    n 4x "Cookie Monster."
    
    window hide(None)
    show layer master
    
    return
