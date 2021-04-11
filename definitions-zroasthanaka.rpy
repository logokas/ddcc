## Definitions for Roast of Hanaka Skit
## Hanaka - by kyoryii (duh) [Only allowed in this skit]
## zroasthanaka_NS (psb) - Denelson83 by CC-BY-SA Unported 3.0 
## https://commons.wikimedia.org/wiki/File:SMPTE_Color_Bars.svg
## zroasthanaka_bleep.ogg (psbsfx) - Hughesj333 by CC-0
## https://freesound.org/s/99202/
## zroasthanaka_aud_laugh.ogg (zhlaugh) - lonemonk by CC-BY-SA Unported 3.0 | edited by skit maker
## https://freesound.org/s/72843/
## zroasthanaka_clap.ogg (clap) - lonemonk by CC-BY-SA Unported 3.0 | edited by skit maker
## https://freesound.org/s/72841/
## zroasthanaka_mech_load.wav (hml) - GregorQuendel, Paul368, danlucaz & Erokia | edited by Logokas
## https://freesound.org/s/422116/ by CC-BY-SA Unported 3.0
## https://freesound.org/s/264063/ by CC-0
## https://freesound.org/s/517754/ by CC-0
## https://freesound.org/s/417141/ by CC-BY-SA Unported 3.0
## zroasthanaka_splosion.ogg (nerfthis) - Chiff the Oblivious#4251 | edited by skit maker
## zroasthanaka_ddlc_bg.png (crf) & zroasthanaka_ddlc_podium.png (desk) - Kimagure After (T.O.P) | edited by yagamirai01

define h = DynamicCharacter('h_name', image='hanaka', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default h_name = "Hanaka"
define lm = Character('You & Moni', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define desk = DynamicCharacter('Desk', image='desk', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image hanaka 1 = "mod_assets/zroasthanaka/hanaka.png"
image hanaka 1g = "mod_assets/zroasthanaka/grin.png"
image hanaka 1m = "mod_assets/zroasthanaka/mad.png"
image hanaka 1ss = "mod_assets/zroasthanaka/slight smile.png"
image hanaka 1ses = "mod_assets/zroasthanaka/shut eye smirk.png"
image hanaka 1p = "mod_assets/zroasthanaka/pissed.png"
image hanaka 1s = "mod_assets/zroasthanaka/smirk.png"

image desk 1 = "mod_assets/zroasthanaka/zroasthanaka_ddlc_podium.png"

image bg crf = "mod_assets/zroasthanaka/zroasthanaka_ddlc_bg.png"
image bg psb = "mod_assets/zroasthanaka/zroasthanaka_NS.png"
image zroasthanaka_thumbnail = im.FactorScale("mod_assets/zroasthanaka/zroasthanaka_tn.png", 0.15, 0.15)

define audio.psbsfx = "mod_assets/zroasthanaka/zroasthanaka_bleep.ogg"
define audio.zhlaugh = "mod_assets/zroasthanaka/zroasthanaka_aud_laugh.ogg"
define audio.hml = "mod_assets/zroasthanaka/zroasthanaka_mech_load.wav"
define audio.nerfthis = "mod_assets/zroasthanaka/zroasthanaka_splosion.ogg"
define audio.clap = "mod_assets/zroasthanaka/zroasthanaka_clap.ogg"

transform t43b:
    tcommon(960)
transform f43b:
    focus(960)
transform t45:
    tcommon(1140)