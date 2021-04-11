image natsuki 1aa = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/Tormuse/NatsukisSecret_n_aa.png")
image natsuki 1ab = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/Tormuse/NatsukisSecret_n_ab.png")
image natsuki 1ac = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/Tormuse/NatsukisSecret_n_ac.png")
image natsuki 5ac = im.Composite((960, 960), (18, 22), "mod_assets/Tormuse/NatsukisSecret_n_ac.png", (0, 0), "natsuki/3.png")

image NatsukisSecret_thumbnail = "mod_assets/Tormuse/Natsukissecret_thumbnail.png"

init -200 python:
    skit_NatsukisSecret = Skit(
        "Natsuki's Secret",
        "NatsukisSecret",
        "NatsukisSecret_thumbnail",
        "@Tormuse#9495, u/Tormuse"
    )

    skits.append(skit_NatsukisSecret)

label NatsukisSecret(preserve_transition=True):
    scene bg club_day
    if preserve_transition:
        with Dissolve(1)
    play music t3
    show natsuki 1u at l11 zorder 2
    "Natsuki is the last to arrive at the club meeting."
    "She looks nervous."
    show natsuki 1n at t11 zorder 2
    mc "Hey Natsuki, you doing all right?"
    n 1m "Um...  I don't know yet..."
    n "I mean I sort of have an announcement to make."
    n 1ab "It's uh...  really embarrassing..."
    n 1aa "And...  and I'm kinda nervous about how you'll all react..."
    n 1ab "Especially because my dad didn't take it well."
    show natsuki 1u at t11 zorder 2
    show yuri 1e at t33 zorder 2
    show sayori 1b at t31 zorder 2
    "Everyone turns to Natsuki, looking concerned."
    show yuri 1f at f33 zorder 2
    y "Well, whatever it is, we won't judge you for it."
    show yuri 1a at t33 zorder 2
    show sayori 2x at f31 zorder 2
    s "Yeah, we're your friends, Natsuki."
    show sayori 1a at t31 zorder 2
    show natsuki 1l at f32 zorder 2
    n "Exactly, we're all friends!"
    n 1t "You all mean a lot to me...  which is why I thought you all deserve to know..."
    n 1w "I'm trans.  I was actually born a boy."
    show natsuki 1n at t11 zorder 2
    show yuri 1d at f33 zorder 2
    y "Aha!  I knew it!"
    show yuri 1c at t33 zorder 2
    show sayori 1n at t31 zorder 2
    show natsuki 1p at f32 zorder 2
    n "WHAT?"
    show natsuki 1p at t32 zorder 2
    show yuri 3n at hf33 zorder 2
    y "Aah!  S-sorry, that came out wrong..."
    y 3o "I mean...  I mean I suspected...  er...  I hoped...?"
    show yuri 3n at t33 zorder 2
    show sayori 1g at t31 zorder 2
    show natsuki 4o at f32 zorder 2
    n "Hey, I told you this is hard for me!  You don't have to be a jerk about it!"
    show natsuki 4i at t32 zorder 2
    show yuri 3p at f33 zorder 2
    y "N-no!  I just got a little overly excited about it...  be-because..."
    show sayori 1n at t31 zorder 2
    y 2l "I am also transgender."
    show yuri 3n at t33 zorder 2
    show natsuki 5h at f32 zorder 2
    n "Don't make fun of me, you asshole!"
    show natsuki 5i at t32 zorder 2
    show sayori 1g at t31 zorder 2
    show yuri 3p at f33 zorder 2
    y "I'm not making fun!  I swear, I was assigned male at birth!"
    show yuri 3n at t33 zorder 2
    show natsuki 5h at f32 zorder 2
    n "C'mon, with gazongas like those?"
    show natsuki 5i at t32 zorder 2
    show yuri 3q at f33 zorder 2
    y "Ah...  yes...  I suppose I did overcompensate a bit."
    y 3t "The fact that I'm so tall made my gender dysphoria quite severe..."
    show sayori 1f at t31 zorder 2
    show natsuki 5c at t32 zorder 2
    y 4c "I even hated my body enough to want to damage it sometimes."
    show yuri 4c at t33 zorder 2
    show natsuki 5m at f32 zorder 2
    n "Oh..."
    n 5ac "..."
    n 1m "Crap...  I'm sorry, Yuri."
    show natsuki 1ac at t32 zorder 2
    show sayori 1d at t31 zorder 2
    show yuri 2q at f33 zorder 2
    y "It's all right.  I'm much happier with how I look now..."
    show natsuki 1j at t32 zorder 2
    y 1d "And now, I have a new trans friend to share with."
    show yuri 1c at t33 zorder 2
    show sayori 1a at t31 zorder 2
    show natsuki 1l at f32 zorder 2
    n "Ehehe, yeah, I'm glad to have you too, trans buddy."
    show natsuki 1z at t32 zorder 2
    show sayori 4x at f31 zorder 2
    s "Aww, this is so sweet!"
    s 4s "I guess this is a good time to tell you all that I'm trans too."
    show sayori 4n at t31 zorder 2
    show natsuki 1k at t32 zorder 2
    show yuri 1e at t33 zorder 2
    mc "Sayori!  Really?"
    show sayori 1c at f31 zorder 2
    s "Huh?"
    show sayori 1b at t31 zorder 2
    mc "You never told me!"
    show natsuki 1c at t32 zorder 2
    show sayori 3j at f31 zorder 2
    s "[player], we've known each other our whole lives!  How could you not know?"
    show sayori 1i at t31 zorder 2
    show natsuki 1g at t32 zorder 2
    mc "W-well...  uh...  I guess it just didn't come up?"
    show sayori 1j at f31 zorder 2
    s "I've been on hormone replacement therapy for the past year."
    s 1l "It's why I was so excited that my boobs got bigger the other day."
    show sayori 1d at t31 zorder 2
    mc "I don't know, you've just...  you've always seemed girly to me, I guess?"
    show sayori 1g at t31 zorder 2
    show natsuki 4e at f32 zorder 2
    n "Jeez, [player], I knew you were dense, but...  come on!"
    show natsuki 4g at t32 zorder 2
    show sayori 1h at f31 zorder 2
    s "You're not upset about it, are you?"
    show sayori 1g at t31 zorder 2
    mc "No, no...  of course not!"
    mc "After all..."
    show sayori 1d at t31 zorder 2
    show natsuki 4k at t32 zorder 2
    mc "I'm trans too."
    show sayori 4r at f31 zorder 2
    s "That's right!  You big ol' handsome man, you!"
    show sayori 4q at t31 zorder 2
    show yuri 1g at t33 zorder 2
    show natsuki 3m at f32 zorder 2
    n "Huh?  He used to be a chick?  I wouldn't have guessed."
    show natsuki 3g at t32 zorder 2
    show sayori 4n at t31 zorder 2
    show yuri 1h at f33 zorder 2
    y "Natsuki!  That's not polite!"
    show yuri 1g at t33 zorder 2
    show natsuki 3e at f32 zorder 2
    n "What?  I was giving him a compliment!"
    show natsuki 3g at t32 zorder 2
    show sayori 1g at t31 zorder 2
    show yuri 2r at f33 zorder 2
    y "The preferred terminology is 'assigned female at birth.'  You should know this!"
    show yuri 2g at t33 zorder 2
    show natsuki 1f at f32 zorder 2
    n "Well, la di da, Miss Know-it-all!"
    show natsuki 1g at t32 zorder 2
    show sayori 1r at f31 zorder 2
    s "ANYWAY!  I used to be depressed until I found my true self, and I'm a lot happier now!"
    show sayori 1a at t41 zorder 2
    show natsuki 1g at t42 zorder 2
    show yuri 2g at t43 zorder 2
    show monika 1c at t44 zorder 2
    mc "Monika, you've been awfully quiet.  How do you feel about all of this?"
    show monika 2d at f44 zorder 3
    m "Eh...  I'm happy for you guys, I guess..."
    m 1d "But it's all pretty arbitrary to me."
    m 1b "Watch this..."
    show monika 3a at f44 zorder 3
    $ consolehistory = []
    call updateconsole ("Edit monika.chr", "$ gender = \"male\"")
    show natsuki 1j at t42 zorder 2
    show yuri 1a at t43 zorder 2
    m 1b "Tada!  I'm a boy now."
    m 1k "Ahaha!"
    show monika 3j at f44 zorder 3
    $ consolehistory = []
    call updateconsole ("Edit monika.chr", "$ gender = \"female\"")
    m 1b "And now I'm a girl again!"
    show monika 1a at t44 zorder 2
    show sayori 2x at f41 zorder 3
    call hideconsole
    s "There, see?  It's all right, Natsuki.  We all accept you."
    show sayori 1a at t41 zorder 2
    show natsuki 1t at f42 zorder 3
    n "Yeah...  yeah, you're right."
    n 1l "I don't know what I was so nervous about.  You guys are awesome."
    show natsuki 1j at t42 zorder 2
    mc "I hope your dad wasn't too hard on you about it."
    show natsuki 1l at f42 zorder 3
    n "Ehh...  it wasn't really that bad."
    n 1t "He has to accept me.  We're family!"
    n 1l "After all..."
    n 1z "He did give birth to me."
    return