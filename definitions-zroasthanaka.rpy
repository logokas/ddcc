## Definitions for Roast of Hanaka Skit
## Hanaka - by kyoryii (duh) [Probably only allowed here]
## zroasthanaka_NS - Denelson83 by CC-BY-SA Unported 3.0 
## Link: https://commons.wikimedia.org/wiki/File:SMPTE_Color_Bars.svg
## zroasthanaka_bleep.ogg - Hughesj333 by CC-0
## Link: https://freesound.org/people/hughesj333/sounds/99202/
## zroasthanaka_aud_laugh.ogg - lonemonk by CC-BY-SA Unported 3.0 | edited by skit maker
## Link: https://freesound.org/people/lonemonk/sounds/72843/

define h = DynamicCharacter('h_name', image='hanaka', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default h_name = "Hanaka"
define l = Character('Logokas', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define lm = Character('Logo & Moni', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image hanaka 1 = "mod_assets/zroasthanaka/hanaka.png"

image bg psb = "mod_assets/zroasthanaka/zroasthanaka_NS.png"
image zroasthanaka_thumbnail = im.FactorScale("mod_assets/zroasthanaka/zroasthanaka_tn.png", 0.15, 0.15)

define audio.psbsfx = "mod_assets/zroasthanaka/zroasthanaka_bleep.ogg"
define audio.zhlaugh = "mod_assets/zroasthanaka/zroasthanaka_aud_laugh.ogg"
