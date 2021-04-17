## Main Script for DDCC

init -200 python:
    skit_ddcc = Skit(
        "What is DDCC?", # Title
        "ddcc", # Label
        "club_date", #Thumbnail
        "The DDCC Team",
        skit_position = 17
    )

## The Explanation
## Radio sound effects from Freesound.org

label ddcc(preserve_transition=True):

    scene bg club_day
    if preserve_transition == True:
        with dissolve_scene_full
    play music t5b

    show mc 3 zorder 2 at r11
    call swoosh
    voice "mod_assets/ddcc/ddcc_mc01.wav"
    imc 3c "So, you wanted to make a mod."

    voice "mod_assets/ddcc/ddcc_mc02.wav"
    imc 3s "But it didn't quite go according to plan."

    voice "mod_assets/ddcc/ddcc_mc03.wav"
    imc 5s "Things changed, parts that seemed easy, actually aren't."

    voice "mod_assets/ddcc/ddcc_mc04.wav"
    imc 5b "The question is, how are you going to release anything?"

    voice "mod_assets/ddcc/ddcc_mc05.wav"
    imc 5 "Well, it doesn't have to be hard, nor take a long time."

    voice "mod_assets/ddcc/ddcc_mc06.wav"
    imc 5c "In fact, this is your chance!"

    voice "mod_assets/ddcc/ddcc_mc07.wav"
    imc 3k "Welcome, to the Doki Doki #Comedy Club."

    voice "mod_assets/ddcc/ddcc_mc08.wav"
    imc 3c "A compilation mod that gives the entire community a chance to make something!"

    voice "mod_assets/ddcc/ddcc_mc09.wav"
    imc 3l "All you need to do is put together a suitable scenario, and submit it!"

    voice "mod_assets/ddcc/ddcc_mc10.wav"
    imc 4z "I don't have time to go over all the specifics right now..."

    voice "mod_assets/ddcc/ddcc_mc11.wav"
    imc 4h "Since I'm not getting paid enough to do so..."

    stop music
    voice "mod_assets/ddcc/ddcc_mc12.wav"
    imc 1w "Wait...you're not paying me for any of this."

    voice "mod_assets/ddcc/ddcc_mc13.wav"
    "Just read the lines!"

    voice "mod_assets/ddcc/ddcc_mc14.wav"
    imc 3e "...Fine."

    play music t5b
    voice "mod_assets/ddcc/ddcc_mc15.wav"
    imc 1a "For more information and specifics for how to submit, check r/DDLCMods by clicking the Help button in the main menu."

    voice "mod_assets/ddcc/ddcc_mc16.wav"
    imc 1c "Or, alternatively, if you're exceptionally lazy, click the link {a=http://www.reddit.com/r/DDLCMods}RIGHT HERE{/a}!"

    voice "mod_assets/ddcc/ddcc_mc17.wav"
    imc 4a "The full mod is planned for release very soon, so get your creativity going!"

    voice "mod_assets/ddcc/ddcc_mc19.wav"
    imc 3c "To help give you some idea of the sorts of skits we're looking for, please enjoy the following cavalcade of nonsensical examples."

    voice "mod_assets/ddcc/ddcc_mc20.wav"
    imc 3w "This way, {i}we don't get flooded with a bunch of questions about what kind of skits we want.{/i}"

    voice "mod_assets/ddcc/ddcc_mc18.wav"
    imc 5c "That is all. Happy modding!"

    return