init python:
    import random
    from functools import partial

    def sgn(x, sgn_zero=1):
        """ Return the signum (or numeric sign) of the input
        For x > 0, returns 1. For x < 0, returns -1.
        For x = 0, returns optional argument sgn_zero (defaults to 1).
        """
        return x/abs(x) if x else sgn_zero

    def get_wordlist(filename='poemwords.txt'):
        """ Return a list of words and their scores from file.
        Each element of the list is of type <dict> and is of the form:
            {'word': str, 's': float, 'n': float, 'y': float, 'm': float}
        """
        with renpy.file(filename) as f:
            words = []
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                word, s, n, y, m = line.split('\t')
                words.append({
                    'word': word,
                    's': float(s),
                    'n': float(n),
                    'y': float(y),
                    'm': float(m)
                })
        return words

    full_names = {'s': 'sayori', 'n': 'natsuki', 'y': 'yuri', 'm': 'monika'}

    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0

































































label poem_(transition=True):
    stop music fadeout 2.0
    play music t4  

    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping == False

    if chapter == 1:

        scene expression "bg/notebook_first.png" with dissolve_scene_full
        call screen dialog("It's time to write a poem!\n\nAt this point, I hardly have any idea for what I should write about,\nso I guess I'll just have to experiment a bit to find my inspiration and my style.", ok_action=Return())
    elif chapter == 2:


        scene expression "bg/notebook_second_{doki}.png".format(doki=poemwinner[0]) with dissolve_scene_full
        call screen dialog("Another day, another poem!\n\nThat could've gone worse, actually.\nI'm still not sure what to write about,\nbut I think I'll try to use what I've learned from everyone.", ok_action=Return())
    else:

        scene expression "bg/notebook_third.png" with dissolve_scene_full
        call screen dialog("Okay, playtime's over!\n\nIt seems that I'm hardly making any progress.\nI guess it's time for me to finally sort things out in my head.\nPerhaps I should indeed use something or even {i}someone{/i} as a source of inspiration.", ok_action=Return())

        show s_sticker at sticker_41
        show n_sticker at sticker_42
        show y_sticker at sticker_43
        show m_sticker at sticker_44

    python:

        progress = 0
        target = 20
        scores = {doki: 0 for doki in 'snym'}
        words = get_wordlist()

        times = {doki: random.uniform(4, 8) for doki in 'snym'}
        positions = {doki: 0 for doki in 'snym'}
        offsets = {doki: 0 for doki in 'snym'}
        zooms = {doki: 1 for doki in 'snym'}

        for progress in range(target):
            
            ystart = 160
            ui.text('{p}/{t}'.format(p=progress+1, t=target), style='poemgame_text', xpos=810, ypos=80, color='#000')
            for col in range(2):
                x = 440 if col == 0 else 680
                ui.vbox()
                for row in range(5):
                    word = random.choice(words)
                    words.remove(word)
                    ui.textbutton(word['word'], clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=ystart+56*row)
                ui.close()
            
            t = ui.interact()
            renpy.play(gui.activate_sound)
            for doki in 'synm':
                scores[doki] += t.get(doki, 0.0)
                if chapter == 3 and t.get(doki, 0.0) == 3:
                    renpy.show("{doki}_sticker hop".format(doki=doki))
                    renpy.pause(0.1)


        winner = sorted(scores, key=scores.get)[-1]
        poemwinner[chapter-1] = full_names[winner]

    $ config.allow_skipping = True
    $ allow_skipping == True
    scene black with dissolve_scene_full































































































image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

transform sticker_41:
    xcenter 80 yalign 0.9 subpixel True

transform sticker_42:
    xcenter 180 yalign 0.9 subpixel True

transform sticker_43:
    xcenter 280 yalign 0.9 subpixel True

transform sticker_44:
    xcenter 380 yalign 0.9 subpixel True


transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
