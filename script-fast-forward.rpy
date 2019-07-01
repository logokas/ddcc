# Fast-Forward - MrGraves#9413

image fast-forward_thumbnail = im.FactorScale("mod_assets/fast-forward/fast-forward_thumbnail.png",0.3,0.3)

init -200 python:
    skit_fast_forward = Skit(
        "Fast-Forward", # Title
        "fast_forward", # Label
        "fast-forward_thumbnail", # Thumbnail
        "@MrGraves#9413, /u/DiabloGraves" # Author
    )

    skits.append(skit_fast_forward) # Add your skit to the list! Make sure it matches the name above.

label fast_forward(preserve_transition=True): 
    $ s_name = "???"
    $ n_name = "???"
    $ y_name = "???"
    $ m_name = "???"
    
    scene bg residential_day
    play music t2

    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    menu:
        "Seriously, this again?":
            pass
    menu:
        "SKIP!":
            pass
    "{cps=100}That girl is Sayori, my neighbor and good friend since we were children.{/cps}{nw}"
    "{cps=100}You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?{/cps}{nw}"
    "{cps=100}We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up.{/cps}{nw}"
    "{cps=100}But if she's going to chase after me like this, I almost feel better off running away.{/cps}{nw}"
    "{cps=100}However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me.{/cps}{nw}"
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "{cps=20}Haaahhh...haaahhh...{/cps}{w=0.2}{nw}"
    s "{cps=20}I overslept again!{/cps}{w=0.2}{nw}"
    s "{cps=20}But I caught--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Maybe, but only because I decided to stop and wait for you.{/cps}{nw}"
    show sayori at s11
    s 5c "{cps=20}Eeehhhhh, you didn't even let me finish talking!{/cps}{w=0.2}{nw}"
    s "{cps=20}That's mean--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Well, if people stare at you for acting weird then I don't want them to think we're a couple or something.{/cps}{nw}"
    show sayori 5a zorder 2 at t11
    s "{cps=20}Hey, [player], what gives?{/cps}{w=0.2}{nw}"
    s "{cps=20}Why are you in such a--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Whatever you say, Sayori...{/cps}{nw}"
    show sayori zorder 1 at thide
    hide sayori
    "{cps=100}We cross the street together and make our way to school.{/cps}{nw}"
    "{cps=100}As we draw near, the streets become increasingly speckled with other students making their daily commute.{/cps}{nw}"
    show sayori 1m zorder 2 at t11
    s "{cps=20}Agh, [player], wait up, I'm still--{/cps}{w=0.2}{nw}"
    mc "{cps=100}A club?{/cps}{nw}"
    mc "{cps=100}I told you already, I'm really not interested in joining any clubs.{/cps}{nw}"
    mc "{cps=100}I haven't been looking, either.{/cps}{nw}"
    show sayori 1l at s11
    s 4h "{cps=20}Eh? I didn't even say anything about--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Did I...?{/cps}{nw}"
    "{cps=100}I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about.{/cps}{nw}"
    "{cps=100}Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime.{/cps}{nw}"
    s 2j "{cps=20}Seriously, [player] what's gotten into--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Alright, alright...{/cps}{nw}"
    mc "{cps=100}I'll look at a few clubs if it makes you happy.{/cps}{nw}"
    mc "{cps=100}No promises, though.{/cps}{nw}"
    s 2i "{cps=20}What--{/cps}{w=0.2}{nw}"
    mc "{cps=100}Yeah, I guess I'll promise you that.{/cps}{nw}"
    "{cps=100}Why do I let myself get lectured by such a carefree girl?{/cps}{nw}"
    "{cps=100}More than that, I'm surprised I even let myself relent to her.{/cps}{nw}"
    "{cps=100}I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head.{/cps}{nw}"
    s 4p "{cps=20}Agh, [player] slow down... haaaahh...{/cps}{w=0.2}{nw}"
    
    scene bg class_day
    with wipeleft_scene

    play sound "gui/sfx/select.ogg"
    "The school day is as ordinary as ever, and it's over before I know it."
    menu:
        "This is taking too long!":
            pass
    menu:
        "SKIP FASTER!":
            pass
    "{cps=200}After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation.{/cps}{nw}"
    mc "{cps=200}Clubs...{/cps}{nw}"
    "{cps=200}Sayori wants me to check out some clubs.{/cps}{nw}"
    "{cps=200}I guess I have no choice but to start with the anime club...{/cps}{nw}"

    s "{cps=40}Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa--{/cps}{nw}"
    show sayori 4p zorder 2 at t11
    mc "{cps=200}Sayori...?{/cps}{nw}"
    "{cps=200}Sayori must have come into the classroom while I was spacing out.{/cps}{nw}"
    "{cps=200}I look around and realize that I'm the only one left in the classroom.{/cps}{nw}"
    s 4w "{cps=40}[player] what's happening everything is moving so fast I can't--{/cps}{w=0.2}{nw}"
    mc "{cps=200}You don't need to wait up for me if it's going to make you late to your own club.{/cps}{nw}"
    mc "{cps=200}Know what?{/cps}{nw}"
    mc "{cps=200}Sayori...{/cps}{nw}"
    mc "{cps=200}...There is no way I'm going to your club.{/cps}{nw}"
    s 4w "{cps=40}Eeeehhhhh?! I didn't even ask you yet--{/cps}{w=0.2}{nw}"
    "{cps=200}Sayori is vice president of the Literature Club.{/cps}{nw}"
    "{cps=200}Not that I was ever aware that she had any interest in literature.{/cps}{nw}"
    "{cps=200}In fact, I'm 99%% sure she only did it because she thought it would be fun to help start a new club.{/cps}{nw}"
    "{cps=200}Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\".{/cps}{nw}"
    "{cps=200}That said, my interest in literature is guaranteed to be even less.{/cps}{nw}"
    mc "{cps=200}Yeah. I'm going to the anime club.{/cps}{nw}"
    show sayori zorder 2 at t11
    s 4p "{cps=40}Okay, I just--{/cps}{w=0.2}{nw}"
    mc "{cps=200}Why do you care so much, anyway?{/cps}{nw}"
    mc "{cps=200}Don't make promises you can't keep!{/cps}{nw}"
    "{cps=200}I can't tell if Sayori is really that much of an airhead, or if she's so cunning as to have planned all of this out.{/cps}{nw}"
    "{cps=200}I let out a long sigh.{/cps}{nw}"
    mc "{cps=200}Fine... I'll stop by for a cupcake, okay?{/cps}{nw}"
    show sayori at h11
    s "{cps=40}Aaaaaaaaaa wait no let go--{/cps}{w=0.2}{nw}"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    play sound "gui/sfx/select.ogg"
    "And thus, today marks the day I sold my soul for a cupcake."
    menu:
        "Just how long IS this first part?":
            pass
    menu:
        "FAST FORWARD!":
            pass
    "{cps=400}I dejectedly follow Sayori across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities.{/cps}{nw}"
    "{cps=400}Sayori, full of energy, swings open the classroom door.{/cps}{nw}"

    scene bg club_day
    play music t3
    show yuri 1a zorder 2 at t43
    show natsuki 4q zorder 3 at t44
    n "So then I said--{w=0.2}{nw}"
    show yuri 1e zorder 2 at t43
    show natsuki 4c zorder 2 at t44
    s "{cps=60}Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa--{/cps}{nw}"
    show sayori 4p at l43
    play sound "sfx/fall.ogg"
    pause 0.3
    show natsuki 4v at t44
    show sayori 4p at t44
    show yuri 1p at t44
    play sound "sfx/fall.ogg"
    pause 0.3
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    mc "{cps=400}I told you, don't call me a 'new member--'{/cps}{nw}"
    "{cps=400}Eh? I glance around the room.{/cps}{nw}"
    mc "{cps=400}...{/cps}{nw}"
    "{cps=400}All words escape me in this situation.{/cps}{nw}"
    "{cps=400}This club...{/cps}{nw}"
    "{cps=400}{i}...is full of incredibly cute girls!!{/i}{/cps}{nw}"
    show natsuki 1v zorder 2 at t44
    pause 0.3
    show natsuki 1p zorder 3 at h44
    n "{cps=60}What the heck just happened--{/cps}{w=0.2}{nw}"
    "{cps=400}The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize.{/cps}{nw}"
    $ n_name = "Natsuki"
    "{cps=400}Her small figure makes me think she's probably a first-year.{/cps}{nw}"
    "{cps=400}She is also the one who made cupcakes, according to Sayori.{/cps}{nw}"
    n "{cps=60}Who the heck are you--{/cps}{w=0.2}{nw}"
    show natsuki 1u zorder 2 at t44
    show yuri 3n zorder 3 at t43
    y "{cps=60}Natsuki, are you all right--{/cps}{w=0.2}{nw}"
    "{cps=400}Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Sayori and Natsuki.{/cps}{nw}"
    $ y_name = "Yuri"
    mc "{cps=400}Ah... Well, it's nice to meet both of you.{/cps}{nw}"
    y "{cps=60}Uuuu... I don't believe we've properly--{/cps}{w=0.2}{nw}"
    show yuri zorder 2 at t43
    show sayori 2w zorder 3 at t42
    s "{cps=60}Owowowow... I'm gonna look like a unicorn--{/cps}{w=0.2}{nw}"
    "{cps=400}Monika smiles sweetly.{/cps}{nw}"
    "{cps=400}We do know each other - well, we rarely talked, but we were in the same class last year.{/cps}{nw}"
    "{cps=400}Monika was probably the most popular girl in class - smart, beautiful, athletic.{/cps}{nw}"
    "{cps=400}Basically, completely out of my league.{/cps}{nw}"
    "{cps=400}So, having her smile at me so genuinely feels a little...{/cps}{nw}"
    mc "{cps=400}Y-You too, Monika.{/cps}{nw}"
    $ m_name = "Monika"
    m "{cps=60}What on earth is going on around here!{/cps}{w=0.2}{nw}"
    show monika 5b at l42
    show sayori 4p at t43
    play sound "sfx/fall.ogg"
    pause 0.3
    show natsuki 4v at t44
    show sayori 4p at t44
    show yuri 1p at t44
    play sound "sfx/fall.ogg"
    pause 0.3
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show monika 5b zorder 3 at t11
    m "{cps=60}[player], what do you think you're doing--{/cps}{w=0.2}{nw}"
    show monika 2o zorder 2 at t32
    show sayori 4w zorder 3 at t33
    s "{cps=60}Monika, this has been happening all day! Do you know--{/cps}{w=0.2}{nw}"
    show sayori 4w zorder 2 at t33
    "{cps=400}The girls have a few desks arranged to form a table.{/cps}{nw}"
    "{cps=400}As Sayori mentioned, it's been widened so that there is one space next to Monika and one space next to Sayori.{/cps}{nw}"
    "{cps=400}Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet.{/cps}{nw}"
    show monika 2p zorder 2 at t32
    show sayori 4k zorder 2 at t33
    ny "{cps=60}Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa--{/cps}{nw}"
    "{cps=400}Still feeling awkward, I take a seat next to Sayori.{/cps}{nw}"
    "{cps=400}Natsuki proudly marches back to the table, tray in hand.{/cps}{nw}"
    "{cps=400}Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats.{/cps}{nw}"
    "{cps=400}The whiskers are drawn with icing, and little pieces of chocolate were used to make ears.{/cps}{nw}"
    show monika 2f zorder 2 at t32
    show sayori 4m zorder 2 at t33
    n "{cps=60}SOMEBODY STOP THIS I'M GONNA *HURK*--{/cps}{w=0.2}{nw}"
    "{cps=400}Sayori talks with her mouth full and has already managed to get icing on her face.{/cps}{nw}"
    "{cps=400}Is she waiting for me to take a bite?{/cps}{nw}"
    mc "{cps=400}This is really good.{/cps}{nw}"
    "{cps=400}{i}(Haven't I heard this somewhere before...?){/i}{/cps}{nw}"
    "{cps=400}I give up on Natsuki's weird logic and dismiss the conversation.{/cps}{nw}"
    "{cps=400}Yuri returns to the table, carrying a tea set.{/cps}{nw}"
    "{cps=400}She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray.{/cps}{nw}"
    mc "{cps=400}Well, tea and reading might not be a pastime for me, but I at least enjoy tea.{/cps}{nw}"
    "{cps=400}Yuri faintly smiles to herself in relief.{/cps}{nw}"
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    "{cps=400}Something tells me I shouldn't tell Monika that I was practically dragged here by Sayori.{/cps}{nw}"
    mc "{cps=400}Weren't you a leader of the debate club last year?{/cps}{nw}"
    mc "{cps=400}It must be hard to start a new club.{/cps}{nw}"
    "{cps=400}Though I still don't really know if I can keep up with their level of enthusiasm about literature...{/cps}{nw}"
    "{cps=400}It looks like she wants to say something, but she keeps quiet.{/cps}{nw}"
    "{cps=400}I spoke without thinking after seeing Yuri's sad smile.{/cps}{nw}"
    "{cps=400}Yuri goes on, clearly passionate about her reading.{/cps}{nw}"
    mc "{cps=400}Ah, I read a horror book once...{/cps}{nw}"
    "{cps=400}At this rate, Yuri might as well be having a conversation with a rock.{/cps}{nw}"
    play sound "gui/sfx/select.ogg"
    mc "Natsuki, you write your own poems?"
    stop music
    menu:
        "Oh.":
            pass
    "Can I really impress the class star Monika with my mediocre writing skills?"
    menu:
        "Oh no.":
            pass
    "And I guess that starts with writing a poem tonight..."
    menu:
        "I am NOT reading through those poem responses AGAIN.":
            pass
    menu:
        "Who should I show my poem to first?"
        "Sayori":
            pass
        "Natsuki":
            pass
        "Yuri":
            pass
        "Monika":
            pass
    menu:
        "...":
            pass
    menu:
        "FAST.":
            pass
    menu:
        "FORWARD.":
            pass            
    play music t7g
    show yuri 3p zorder 2 at i21
    show natsuki 5v zorder 3 at i22
    n "AAA--{fast}{w=0.2}{nw}"
    show yuri 3p zorder 3 at i21
    show natsuki 5v zorder 2 at i22
    y "Uuu--{fast}{w=0.2}{nw}"
    hide yuri
    hide natsuki
    scene bg residential_day
    show sayori 4p zorder 3 at i11
    s "EEE--{fast}{w=0.2}{nw}"
    hide sayori
    scene bg sayori_bedroom
    show sayori 4bp zorder 3 at i11
    s "HELP--{fast}{w=0.2}{nw}"
    hide sayori    
    scene bg club_day
    show monika 5b zorder 3 at i11
    m "YOU--{fast}{w=0.2}{nw}"
    hide monika
    show s_kill_bg2
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    stop sound
    hide s_kill2
    hide s_kill
    show sayori glitch zorder 2 at t11
    pause 0.3
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    hide screen tear
    play sound "sfx/crack.ogg"
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.3
    hide natsuki
    hide sayori
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.15
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    play sound "sfx/yuri-kill.ogg"
    pause 0.15
    show yuri stab_1
    pause 0.05
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 0.15
    show yuri stab_3
    pause 0.05
    show yuri stab_2
    show blood:
        pos (610,485)
    hide yuri
    pause 0.05
    stop sound
    hide s_kill_bg
    show image "images/cg/y_kill/1a.png"
    pause 0.2
    show image "images/cg/y_kill/2a.png"
    pause 0.2
    show image "images/cg/y_kill/3a.png"
    pause 0.2
    scene black
    show monika_bg
    pause 0.3
    hide monika_bg
    play sound "<to 0.75>sfx/mscare.ogg"
    show monika_scare
    pause 0.3
    hide monika_scare    
    show monika_body_glitch2
    pause 0.3
    scene black
    stop music
    play sound "gui/sfx/select.ogg"    
    "..."
    pause 2.0
    play sound "gui/sfx/select.ogg"    
    show image "mod_assets/fast-forward/fast-forward_bg00.png"
    pause 4.0
    show image "mod_assets/fast-forward/fast-forward_bg01.png"
    pause 2.0
    play sound "gui/sfx/hover.ogg"    
    show image "mod_assets/fast-forward/fast-forward_bg02.png"
    pause 2.0
    play sound "gui/sfx/select.ogg"    
    scene black
    pause 1.0    
    return