

label stalker:
    stop music fadeout 2.0

    #Thanks for guiding me so far with the programming Karl... it's # to re-write, huh?
    $ persistent.playthrough = 0
    scene bg stalker_bg
    with dissolve_scene_full

    #'Hold on, let me just put this in.'
    if player == m_name:
        m "Imitation is the sincerest form of flattery, [currentuser]."
        m "But I prefer your real name."
        $ player = currentuser

    elif player == "Karl": #'Inspired by people who use Karl as a name'
        m "Are we de-bugging, [player]?"
        play sound "sfx/giggle.ogg"

    elif player == "Francis": #'Here's to the MBS artist, cheers!'
        m "Oooh, [player]!"

    $ m_name = '????'
    $ s_name = '????'
    $ y_name = '????'
    $ n_name = 'Bandits'
    #maybe I should set up the mood a bit

    play music stalker
    y "Oh my..."
    y "This..."
    y "...This should be the place."
    $ y_name = 'Yuri'
    show yuri 1q at t11
    y "The Zone of Markov."

    #a little music here~
    y "It's {i}grassier{/i} than they put out in the books."
    y 2i "I wonder if the landmarks are right..."
    play sound "utsounds/army1.ogg"
    show yuri 3e
    y "Ooh-!"
    y "..."
    y "..."
    y 3d "This is indeed the place!"
    y 2i "I should begin surveying the locations."
    y "Perhaps enjoy some tea as well."
    y 2c "Perfect place to read!"
    show yuri 3p at t43
    play sound "utsounds/breeki.ogg"
    y "Eaahh!!"
    y "Bandits!!"
    s "Papali-!"
    s "Papali suka!"
    play sound "utsounds/shotgun.ogg"
    show sayori 6p at h41
    s "Uwaaaa-!!!"
    s "Heeeeeelp mee!!!"
    show yuri 2n
    y "What do I do???"
    hide sayori
    show yuri 1o at t11
    y "I should call the army."
    y "They'll be of quaint assistance!"
    play sound "utsounds/army2.ogg"
    scene bg stalker_bg2
    with dissolve_scene_full
    pause 1.0
    show yuri at t11
    y 3p "HEEEEEEEEELP!!!!"
    y "SOMEONE!!!"
    y "There are bandits prowling about!!!"
    y 3o "...."
    y "..."
    show yuri at t41
    show monika 1h at t44
    m "..."
    show yuri 3p
    m 2i "Kakogo cherta ty zdes' delayesh'?"
    y 2q "I'm sorry, I don't speak Markov!"
    $ m_name = 'Monika'
    show monika 1c
    m "..."
    show yuri 2s
    m 1d "I see."
    m 1a "Are you traveling alone, or in a group?"
    y 2t "Loner..."
    show monika 1e
    y "I..."
    y "I'm alone..."
    play sound "utsounds/army3.ogg"
    m 3k "Perfect!"
    show monika 3j
    y 2q "Ahaha..."
    y "How so...?"
    m 1a "Say goodbye."
    y 1e "Goodbye?"
    y "But I just got here..."
    play sound "utsounds/shotgun2.ogg"
    m 1e "I know, Yuri."
    m 1j "I know..."
    stop music
    stop sound
    show yuri at t11
    hide monika
    y 3p "Eahhh!"
    scene black
    hide yuri
    play sound "utsounds/shotgun.ogg"
    y "..."
    y "..."
    y "..."
    play music stalker
    y "Am I dead?"
    scene bg stalker_bg
    with dissolve_scene_full
    show sayori 4a at t22
    show yuri 3w at t21
    s "Are you alright?"
    y 3n "..."
    y "..."
    show sayori 3n
    y 3s "You saved me..."
    s 3m "I did?"
    y "Thank you..."
    show yuri 2n
    s 4p "I shot the army!!!!"
    s 1w "I thought it was a bandit!!!"
    show sayori 1u
    y 1t "Well..."
    y "...No matter..."
    y "At least we're safe now."
    s 2y "I actually don't have any bullets left."
    y 1f "Oh?"
    y 1a "Well what's the worst that can happen?"
    play sound "utsounds/breeki.ogg"
    show yuri 2n
    show sayori 4n
    n "Anu cheeki breeki iv damke!"
    scene black
    stop music
    hide sayori
    hide yuri
    "FIN."
    return