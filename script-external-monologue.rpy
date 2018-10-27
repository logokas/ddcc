#"External Monologue" by Tormuse

init -200 python:
    skit_external_monologue = Skit(
        "External Monologue", # Title
        "external_monologue", # Label
        "club_date" #Thumbnail
    )

    skits.append(skit_external_monologue)


label external_monologue(preserve_transition=True):
    $ y_name = "Girl 1"
    $ n_name = "Girl 2"
    $ m_name = "Girl 3"
    scene bg club_day
    if preserve_transition == True:
        with wipeleft
    play music t3
    show sayori 4x at l21
    s "Everyone! The new member is here~!"
    show sayori 4a at t21
    mc "I told you, don't call me a 'new member--'"
    show sayori 1a at t21
    "Eh? I glance around the room."
    show yuri 3n zorder 2 at f22
    y "W-what?  Who said that?"
    show yuri 3n zorder 2 at t22
    show sayori 1c at f21
    s "Oh, right, sorry, I forgot to tell you..."
    s 1l "[player] has a strange voice that follows him around and narrates his life."
    s 1x "I know it's a little weird, but I promise he's super nice, so give him a chance."
    show sayori 1a at t21
    show yuri 3j zorder 2 at f22
    y "Well, in that case..."    
    y 1b "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."
    show yuri 1a zorder 2 at t33
    show sayori 1a at t31
    show natsuki 4c zorder 2 at t32
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    show yuri zorder 2 at t44
    show natsuki zorder 2 at t43
    show sayori 1a at t41
    show monika 1k zorder 2 at f42
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a at t42
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"
    show monika 2n zorder 2 at f42
    m "Ahaha, is that so?"
    show monika 2m zorder 2 at t42
    show yuri 4e zorder 2 at f44
    y "Oh...  oh my..."
    show yuri 4e zorder 2 at t44
    show sayori 1l at f41
    s "Aww, [player], you're gonna make me blush."
    show sayori 1y at t41
    show natsuki 1v zorder 2 at f43
    n "I'M NOT CUTE!"
    show natsuki 1v zorder 2 at t43
    show sayori at thide
    show monika zorder 1 at thide
    show natsuki zorder 3 at f32
    hide sayori
    hide monika
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "Hmph."
    show natsuki zorder 2 at t32
    show yuri at thide
    hide yuri
    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    show natsuki 1p zorder 2 at f32
    n "What?  What the hell?"
    n 5w "Just because I'm short, you think I'm a little kid?"
    n "I'm 18, damn it!"
    show natsuki 5g zorder 2 at t32
    "She is also the one who made cupcakes, according to Sayori."
    show natsuki 4f zorder 2 at f32
    n "If you only came here for the cupcakes, I'm gonna kick your ass."
    show natsuki 4f zorder 2 at t32
    show sayori 2r zorder 3 at f31
    s "You can just ignore her when she gets moody~"
    show sayori 2a zorder 3 at t31
    "Sayori says that quietly into my ear, then turns back toward the other girls."
    show natsuki 1e zorder 2 at f32
    n "Says what?  Hey, are you talking about me over there?"
    show natsuki 1g zorder 2 at t32
    show sayori 1x zorder 3 at f31
    s "Anyway! This is Natsuki, always full of energy."
    show yuri 1e zorder 2 at t33
    s "And this is Yuri, the smartest in the club!"
    $ y_name = 'Yuri'
    show sayori 1a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "D-Don't say things like that..."
    show yuri zorder 2 at t33
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Sayori and Natsuki."
    show yuri zorder 3 at f33
    y 1f "Mature?"
    y 3n "Are you talking about my..."
    y 4d "M-my..."
    y 4c "Oh my..."
    show yuri 4c zorder 2 at t33
    mc "Ah... Well, it's nice to meet both of you."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1x "And it sounds like you already know Monika, is that right?"
    $ m_name = 'Monika'
    show sayori 1a zorder 2 at t31
    show monika 2b zorder 3 at f32
    m "That's right."
    m "It's great to see you again, [player]."
    show sayori at thide
    hide sayori
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    m 2b "Out of your league?  Come on, give yourself some credit.  You're doing fine."
    show monika 2a at t21
    show natsuki 1f at f22
    n "Monika, don't encourage him.  He's creepy!"
    show natsuki 1f at t22
    show monika 2d at f21
    m "Natsuki, be nice.  We want to make our guest feel welcome."
    show monika 2c at t21
    "I was feeling really nervous about meeting new people, but hearing Monika defend me makes me feel more comfortable.  I could really enjoy my time here in the Literature Club."
    show monika 2b at f21
    m "There, see?  He just wants to make friends.  It's all good."
    show monika 2a at t21
    "I can't help fantasizing about her.  I bet she's a good kisser."
    show monika 1d at f21
    m "Whoa...  that was a little...  uh..."
    show monika 1c at t21
    show natsuki 2h at f22
    n "See?  I told you!"
    show natsuki 2i at t22
    "Natsuki's so feisty, I wonder what it would be like to be with her too.  I bet she's a big softie under that rough exterior."
    show natsuki 1p at f22
    n "Ew ew ew!  You're not touching my soft interior!"
    show natsuki 1o at t32
    show monika 1c at t31
    show yuri 2h at f33
    y "I would have to agree that this train of dialogue has gotten somewhat inappropriate."
    show yuri 2g at t33
    "Yuri would be fun to get close to as well.  You know what they say about the quiet ones.  I bet she's wild in bed..."
    show yuri 3p at hf33
    y "W-W-WHAT?"
    show yuri 3p at t33
    "And I love the way she jiggles when she's flustered."
    show yuri 4d at f33
    y "Oh...  oh, this is so embarrassing!"
    show yuri 4c at t33
    "Yes, if harem animes have taught me anything, the four of us will have an amazing time."
    show yuri 4c at t44
    show natsuki 1o at t43
    show monika 1c at t42
    show sayori 1o at f41
    s "Wait a second..."
    show sayori 1o at t41
    "Sayori does a quick count on her fingers."
    show sayori 1m at f41
    s "But there are five of us!"
    s 4m "[player], did you forget about me?"
    show sayori 4f at t41
    "Sayori looks upset, but I could never do that with her.  She'll always be my dearest friend."
    show sayori 4w at f41
    s "Nooooo!  Why can't I be part of your fantasy too?"
    show sayori 1v at t41
    show monika 2i at f42
    m "Okay, I've had enough.  Let's put it to a vote.  Show of hands, who thinks we should kick [player] out?"
    show monika 2h at t42
    "Monika and Yuri each raise a hand.  Natsuki raises both hands."
    "Sayori slowly, reluctantly raises her hand too."
    show monika 2i at f42
    m "Great!  [player], get the hell out.  I'll just have to find another way to reach the player."
    show monika 2h at t42
    show yuri 3v at f44
    y "Reach the what?"
    show yuri 3g at t44
    show monika 2r at f42
    m "Never mind."
    show monika 2q at t42
    scene bg corridor with wipeleft
    stop music fadeout 2
    "Well...  that's another club I've been kicked out of.  Now I'm never gonna get a girlfriend!"
    "And I didn't even get a cupcake!"
    return