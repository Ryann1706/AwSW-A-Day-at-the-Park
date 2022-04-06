
init python:
    ryann_adatp_played = False

    ryann_adatp_park_choices = 0
    ryann_adatp_park_checked_amely = False
    ryann_adatp_park_checked_vara = False
    ryann_adatp_park_checked_adine_remy = False
    ryann_adatp_amely_chalk = ""

    # For the hide and seek minigame (why did I make these variables so long...)
    ryann_adatp_hide_and_seek_time_remaining = 10

    ryann_adatp_hide_and_seek_people_found = 0
    ryann_adatp_hide_and_seek_found_adine = False
    ryann_adatp_hide_and_seek_found_remy = False
    ryann_adatp_hide_and_seek_found_vara = False
    ryann_adatp_hide_and_seek_found_amely = False

    ryann_adatp_hide_and_seek_checked_playground = False
    ryann_adatp_hide_and_seek_checked_slide = False
    ryann_adatp_hide_and_seek_checked_bench = False
    ryann_adatp_hide_and_seek_checked_sandbox = False
    ryann_adatp_hide_and_seek_checked_fountain = False
    ryann_adatp_hide_and_seek_checked_bins = False
    ryann_adatp_hide_and_seek_checked_picnic = False
    ryann_adatp_hide_and_seek_checked_ditch = False
    ryann_adatp_hide_and_seek_checked_grass = False
    ryann_adatp_hide_and_seek_checked_bush = False

    ryannDisplayVar1name = ""
    ryannDisplayVar1 = 0
    ryannDisplayVar1unit = ""
    ryannDisplayVar2name = ""
    ryannDisplayVar2 = ""
    ryannDisplayVar2unit = ""


# Backgrounds
image ryann_forest = "bg/ryann_forest.jpg"
image ryann_park_street = "bg/ryann_park_street.jpg"
image ryann_playground_day = "bg/ryann_playground_day.jpg"

# Cgs
image ryann_chalk_flower = "cg/ryann_chalk_flower.png"
image ryann_chalk_all = "cg/ryann_chalk_all.png"
image ryann_chalk_adine = "cg/ryann_chalk_adine.png"
image ryann_chalk_remy = "cg/ryann_chalk_remy.png"
image ryann_chalk_vara = "cg/ryann_chalk_vara.png"

# Character sprites
image amely normal small = "cr/amely_normal_small.png"
image amely normal small flip = "cr/amely_normal_small_flip.png"
image amely sad small = "cr/amely_sad_small.png"
image amely sad small flip = "cr/amely_sad_small_flip.png"

image vara normal small = "cr/vara_normal_small.png" 
image vara normal small flip = im.Flip("cr/vara_normal_small.png", horizontal=True) 
image vara smile small = "cr/vara_smile_small.png" 
image vara smile small flip = im.Flip("cr/vara_smile_small.png", horizontal=True) 
image vara sad small = "cr/vara_sad_small.png" 
image vara sad small flip = im.Flip("cr/vara_sad_small.png", horizontal=True) 
image vara none small = "cr/vara_none_small.png" 
image vara none small flip = im.Flip("cr/vara_none_small.png", horizontal=True) 

# Flower crown character sprites
image amely normal small fl = "cr/amely_normal_small_fl.png"
image amely normal small fl flip = "cr/amely_normal_small_fl_flip.png"
image amely sad small fl = "cr/amely_sad_small_fl.png"
image amely sad small fl flip = "cr/amely_sad_small_fl_flip.png"

image vara none small fl = "cr/vara_none_small_fl.png"
image vara none small fl flip = im.Flip("cr/vara_none_small_fl.png", horizontal=True)
image vara normal small fl = "cr/vara_normal_small_fl.png"
image vara normal small fl flip = im.Flip("cr/vara_normal_small_fl.png", horizontal=True)
image vara smile small fl = "cr/vara_smile_small_fl.png"
image vara smile small fl flip = im.Flip("cr/vara_smile_small_fl.png", horizontal=True)

image remy normal fl = "cr/remy_normal_fl.png"
image remy normal fl flip = im.Flip("cr/remy_normal_fl.png", horizontal=True)
image remy shy fl = "cr/remy_shy_fl.png"
image remy shy fl flip = im.Flip("cr/remy_shy_fl.png", horizontal=True)
image remy smile fl = "cr/remy_smile_fl.png"
image remy smile fl flip = im.Flip("cr/remy_smile_fl.png", horizontal=True)

image adine annoyed fl = "cr/adine_annoyed_fl.png"
image adine annoyed fl flip = im.Flip("cr/adine_annoyed_fl.png", horizontal=True)
image adine giggle fl = "cr/adine_giggle_fl.png"
image adine giggle fl flip = im.Flip("cr/adine_giggle_fl.png", horizontal=True)
image adine normal fl = "cr/adine_normal_fl.png"
image adine normal fl flip = im.Flip("cr/adine_normal_fl.png", horizontal=True)
image adine think fl = "cr/adine_think_fl.png"
image adine think fl flip = im.Flip("cr/adine_think_fl.png", horizontal=True)


label ryann_adatp_vara_fix_adine:
show vara normal small flip at Position (xpos = 0.05) with easeinleft
Vr "..."
jump ryann_adatp_vara_adine_return

label ryann_adatp_vara_fix_adine2:
show vara normal small flip at Position (xpos = 0.05) with easeinleft
Vr "..."
jump ryann_adatp_vara_adine_return2

label ryann_adatp_vara_fix_remy:
show vara normal small flip at Position (xpos = 0.05) with easeinleft
Vr "..."
jump ryann_adatp_vara_remy_return

label ryann_adatp_vara_fix_remy2:
show vara normal small flip at Position (xpos = 0.05) with easeinleft
Vr "..."
jump ryann_adatp_vara_remy_return2

