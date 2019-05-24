# Skit template by Ceane
# This template should help you get going, and set up your own skit to be compatible with the rest of the game.
# Author of the skit, and any credits for assets or parts of code should be commented here, at the start of the file


# If you don't want to use one of the original game's thumbnails (e.g. club_date, corridor_date, class_date), then define it here.
image ctalks_thumnail = "images/bg/club.png"


# First, we need to add our skit to the list of skits that the game looks at.
init -200 python:
  skit_ctalk = Skit(
      "A talk with the club", # Set this to be the title of your skit.
      "ctalks", # Set this to be the label that you call below.
      "ctalks_thumbnail" # Set this to be the thumbnail you want for your skit. If you aren't using one from the original game, then you'll need to define its image.
  )


  skits.append(skit_ctalk) # Add your skit to the list! Make sure it matches the name above.


# Now, for the actual scene:
label ctalk(preserve_transition=True): # Don't change the preserve_transition part, but rename "template" to what you want your label to be.


  scene bg club_day # Whatever scene you want
  if preserve_transition == True:
      with dissolve_scene_full
# You can have whatever transition effects you want at the start of your script, as long as you put them in this if block.
      # This is used for triggering the transition depending on whether or not someone is going through the game in "Play All" mode,
      # or through scene selection.
label ctalking:
  default ctalkfin  = 0
  menu:
           "Who do you wish to talk to?"
       "Sayori":
              call sayorictalk1
       "Natsuki":
              call natsukictalk1
       "Yuri":
              call yurictalk1
       "Monika":
              call monikactalk1
       "Done Talking":
              $ ctalkfin = 1
  if ctalkfin < 1:
        jump ctalking
  return




label sayorictalk1:
   show sayori 5a at t11
   s "Ehehe, hey [player]."
   s 1x "I hope you've been well."
   s 1p "I just wanted talk with you for a little bit."
   s 1k "I know that there is a lot of mods for us now."
   s 4d "I'm glad that there is."
   s 1a "I'm glad that I can see everyone happy at times. Even me."
   s 4q "I can't thank you enough."
   s 4r "Just keep making those mods!"
   s 1h "Just be nice."
   s 1d "we maybe be fictional but we can still be people."
   s 1k "Just be kind that's all I ask."
   s 4r "Thanks for talking with me again [player] I really enjoyed it."
   s 1a "Good bye for now."
   show sayori at thide
   hide sayori
   return


label natsukictalk1:
   show natsuki 1g at t11
   n "It's nice being able to talk to you again."
   n 1u "I know I wasn't always the greatest person to you."
   n 1t "If you could just give me another chance."
   n 1k "Maybe even change my personality if you have to."
   n 1q "Then maybe things could be better."
   n 4g "That doesn't mean you can make me super cutesy though."
   n 5e "Sayori will tell me if you do."
   n 1m "I just don't want hated for how I was, I wanted excepted for who I am."
   n 1r "So if you could do that,"
   n 1t "Then maybe things could be better."
   n 1u "Thanks for talking to me though, I appreciate it [player]."
   n 1z "See you later!"
   show natsuki at thide
   hide natsuki
   return


label yurictalk1:
   window hide
   show yuri 1g at t11
   pause 1.0
   show yuri 1n
   pause 1.0
   show yuri 1o
   pause 1.0
   show yuri 4c
   pause 2.0
   show yuri 4b
   pause 2.0
   show yuri 4a
   pause 1.0
   show yuri 1j
   y "Sorry [player]."
   y "I just was so nervous when you came."
   y "I don't want to be to weird."
   y 1f "I'm sure you understand what I mean."
   y 1q "That was so embarrasing..."
   y 3n "Unless you liked it?"
   y 1g
   menu:
       y "Did you like it?"
       "Yes":
           y 1y1 "Oh you do?"
           pass
       "No":
           y 1o "Thank you that was so embarrassing."
           jump yanend
    y 1y3 "Is this the me you like to be around?"
    y 3y5 "I didn't think this could be so fun to do again."
    y "I just want to keep looking at you."
    show dark 100
    hide yuri
    show yuri eyes
    y "Just you and only you."
    hide dark
    show layer master
    hide yuripupils
    show yuri 3y2 at t11
    y "Unless you don't want that."
    show black 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    y "DO YOU JUST WANT CLOSER."
    y "Because I can be closer."
    hide black
    hide y_glitch_head
    y 1v "Or not."
    y "But I can do this?"
    image yprestab = "images/yuri/stab/1.png"
    show yprestab
    y "Hahaha!"
    y 1y2 "I think I should stop."
    label yanend:
        y 1q "I don't think I could have continued doing that."
        y 1j "If we could put that past me behind us that would be pleasent."
        y 1g "Unless you don't want to."
        y "That's up to you though."
        y 1n "I-i'm just going to go now."
        pause 1.0
        yuri 1q
        pause 1.0
        show yuri at thide
        hide yuri
   return


label monikactalk1:
   show monika 1g at t11
   m "Hey [player]."
   m 1o "..."
   m 1m "It might have been sometime since we last talked."
   m 1n "It's nice being able to do this."
   m 1k "I missed this."
   m 1p "But do I even deserve something like this."
   m 1g "How I acted in the original game can not be forgotten."
   m 1f "No matter how many mods people make."
   m 1p "I know not everyone will ever forgive me, it's the nature of people in your reality."
   m 1n "But if I get to talk to you for a little bit."
   m 4k "I'll take it."
   m 1p "Just know this."
   m 1g "People are there for you."
   m 1o "Whether they are fiction, across the internet,"
   m 1m "or even someone you see everyday."
   m 4q "Just know this."
   m 4k "We can be there for you."
   m 1g "You only need to ask."
   m 1l "Just remember that okay [player]."
   m 1f "Please, don't forget us."
   m 5a "Not just for me but for everyone okay."
   m 1a "I guess this goodbye for now [player]."
   m 4e "Catch you in the next mod [player]."
   show monika at thide
   hide monika
   return