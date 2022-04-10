
label ryann_adatp_hide_and_seek_playground:

label ryann_adatp_hide_and_seek_display_init:

    show screen ryannextrainfo
    $ ryannextradisplay = 2

    $ ryannDisplayVar1name = "Time remaining:"
    $ ryannlDisplayVar1 = ryann_adatp_hide_and_seek_time_remaining
    $ ryannDisplayVar1unit = "mins"

    $ ryannDisplayVar2name = "People found:"
    $ ryannDisplayVar2 = ryann_adatp_hide_and_seek_people_found
    $ ryannDisplayVar2unit = ""


scene ryann_playground_day with dissolvemed
$ renpy.pause (0.5)

label ryann_adatp_hide_and_seek_playground_show_characters:

if ryann_adatp_hide_and_seek_found_adine:
    show adine normal b flip at Position(xpos=0.3) with dissolve

if ryann_adatp_hide_and_seek_found_amely:
    show amely normal small at Position(xpos=0.7) with dissolve

if ryann_adatp_hide_and_seek_found_remy:
    show remy normal flip at Position(xpos=0.1) with dissolve

if ryann_adatp_hide_and_seek_found_vara:
    show vara normal small at Position(xpos=0.9) with dissolve

label ryann_adatp_hide_and_seek_playground_menu:

show screen ryannextrainfo
$ ryannlDisplayVar1 = ryann_adatp_hide_and_seek_time_remaining
$ ryannDisplayVar2 = ryann_adatp_hide_and_seek_people_found

if ryann_adatp_hide_and_seek_time_remaining == 0 or ryann_adatp_hide_and_seek_people_found == 4:
    jump ryann_adatp_hide_and_seek_end

menu:
    "Check playground equpiment." if not ryann_adatp_hide_and_seek_checked_playground:
        $ ryann_adatp_hide_and_seek_checked_playground = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(Maybe someone is hiding up on the playground equipment?)"
        play sound "fx/ryann_metal_ladder.mp3"
        $ renpy.pause (2.4)
        stop sound fadeout 0.5
        c "(Nope, no one up here.)"
        $ renpy.pause (0.5)

    "Check slide." if not ryann_adatp_hide_and_seek_checked_slide:
        $ ryann_adatp_hide_and_seek_checked_slide = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        m "There was a noticeably larger slide separate from the rest of the playground equipment, with some walls at the top tall enough for someone to hide behind."
        c "(I think someone might be up on that slide?)"
        play sound "fx/ryann_metal_ladder.mp3"
        $ renpy.pause (2.4)
        stop sound fadeout 0.5
        $ renpy.pause (0.5)
        c "(Guess I was wrong…)"
        play sound "fx/ryann_metal_ladder.mp3"
        $ renpy.pause (2.4)
        stop sound fadeout 0.5
        $ renpy.pause (0.5)

    "Check benches." if not ryann_adatp_hide_and_seek_checked_bench:
        $ ryann_adatp_hide_and_seek_checked_bench = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "Is anyone behind the benches?"
        $ renpy.pause (2.0)
        c "(Nothing but sand…)"

    "Check sandbox." if not ryann_adatp_hide_and_seek_checked_sandbox:
        $ ryann_adatp_hide_and_seek_checked_sandbox = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(Why is there a sandbox if the entire playground is covered in sand anyway?)"
        $ renpy.pause (2.0)
        c "(Nothing…)"
        $ renpy.pause (1.0)
        c "(Wait… What's that?)"
        m "Upon a closer look, there was a trail of footprints, that disappeared upon reaching some furrows in the sand."
        c "(Did someone…?)"

    "[[Look up.]"if ryann_adatp_hide_and_seek_checked_sandbox == True and  ryann_adatp_hide_and_seek_found_adine == False:
        if ryann_adatp_hide_and_seek_found_amely:
            hide amely with dissolve
        if ryann_adatp_hide_and_seek_found_remy:
            hide remy with dissolve
        if ryann_adatp_hide_and_seek_found_vara:
            hide vara with dissolve
        $ renpy.pause (0.5)

        $ ryann_adatp_hide_and_seek_found_adine = True
        $ ryann_adatp_hide_and_seek_people_found += 1
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        m "The furrows in the sand raised my suspicions, so I look up to see if it was what I expected."
        $ renpy.pause (2.0)
        c "Adine! I see you!"
        $ renpy.pause (1.0)
        play sound "fx/flap1.ogg" fadein 1.0
        $ renpy.pause (2.5)
        show adine giggle b with dissolvemed
        $ renpy.pause (0.5)
        Ad "Aww… How did you know?"
        c "The furrows in the sand gave you away."
        Ad normal b "Well, there wasn’t much I could do about them."
        $ renpy.pause (1.0)
        if adine3unplayed == False:
            c "Adine, are sure it’s a good idea to fly while your wing is still sprained?"
            Ad "Oh, don’t worry. It’s healed enough that I can fly with a bandage to stabilize it. I just can’t do any more exerting or advanced moves."
            c "Won’t that make it take longer to heal if you’re still using it? What if it doesn’t heal before your competition?"
            Ad giggle b "[player_name], seriously, don’t worry, I’ll be fine. Like I said, this kind of stuff happens. I know what I’m doing."
            c "If you say so…"

        elif adine2unplayed == True:
            m "It was only then I noticed a bandage on one of Adine’s wings."
            c "Hey, why is your wing bandaged? Did you get hurt?"
            Ad think b "Hmm?"
            Ad normal b "Oh, right. I just sprained my wing while I was practicing my stunt flying recently. I had a bit of a rough landing."
            c "Are you sure it’s a good idea to fly, then?"
            Ad "Well, it’s healed enough I can fly with the bandage to stabilize it. I just can’t do any more exerting or advanced moves. Don’t worry, I’ll be fine."
            c "If you say so…"

        else:
            pass

        $ renpy.pause (0.5)
        hide adine with dissolve
        $ renpy.pause (0.5)
        if ryann_adatp_hide_and_seek_people_found == 4:
            jump ryann_adatp_hide_and_seek_end
        else:
            jump ryann_adatp_hide_and_seek_playground_show_characters

    "[[Go somewhere else.]":
        menu: 
            c "(Where should I go to?)"

            "Street.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_park_street with dissolvemed
                jump ryann_adatp_hide_and_seek_street

            "Forest.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_forest with dissolvemed
                jump ryann_adatp_hide_and_seek_forest

            "Stay in the playground.":
                jump ryann_adatp_hide_and_seek_playground_menu

jump ryann_adatp_hide_and_seek_playground_menu



label ryann_adatp_hide_and_seek_street:


if ryann_adatp_hide_and_seek_found_remy == False:
    $ ryann_adatp_hide_and_seek_found_remy = True
    $ ryann_adatp_hide_and_seek_people_found += 1
    m "I made my way onto the street near the park. The park was very pleasant, having a fountain, flower bed, and a picnic area off to the side."
    m "And most importantly, Remy; attempting to hide behind shrubbery that was clearly too small for him."
    c "Very inconspicuous, Remy."
    $ renpy.pause (0.5)
    show remy look with dissolve
    $ renpy.pause (0.5)
    Ry "It’s not exactly easy for someone of my size to hide very well…"
    c "Well, that was probably the best place you could have hidden."
    Ry normal "Yes, it probably was."
    Ry "I’ll go and wait in the playground for now. Good luck finding everyone else."
    $ renpy.pause (0.5)
    show remy normal flip with dissolve
    hide remy with easeoutright
    $ renpy.pause (1.0)

show screen ryannextrainfo
$ ryannlDisplayVar1 = ryann_adatp_hide_and_seek_time_remaining
$ ryannDisplayVar2 = ryann_adatp_hide_and_seek_people_found

if ryann_adatp_hide_and_seek_time_remaining == 0 or ryann_adatp_hide_and_seek_people_found == 4:
    jump ryann_adatp_hide_and_seek_end

menu:
    "Check fountain." if not ryann_adatp_hide_and_seek_checked_fountain:
        $ ryann_adatp_hide_and_seek_checked_fountain = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(Is there anything near the fountain?)"
        $ renpy.pause (1.5)
        c "(What about anything in it?)"
        play sound "fx/water1.ogg"
        $ renpy.pause (1.5)
        c "(Just rusty coins.)"

    "Check flower beds." if not ryann_adatp_hide_and_seek_found_vara:
        $ ryann_adatp_hide_and_seek_found_vara = True
        $ ryann_adatp_hide_and_seek_people_found += 1
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(Let’s check the flower beds.)"
        play sound "fx/bushes.ogg" fadein 1.0
        $ renpy.pause (2.0)
        stop sound fadeout 1.5
        $ renpy.pause (0.5)
        show vara none small with dissolve
        $ renpy.pause (0.5)
        c "Found you, Vara."
        Vr normal small "…"
        c "I have to say, you picked a very good hiding spot."
        Vr smile small "…"
        c "Remy is waiting in the playground. Do you want to wait with him?"
        m "Vara nodded, then walked off to the playground."
        $ renpy.pause (0.5)
        show vara smile flip with dissolve
        hide vara with easeoutright
        $ renpy.pause (1.5)
        c "(Vara hiding in a flower bed… The true definition of adorably precious.)"

    "Check bins." if not ryann_adatp_hide_and_seek_checked_bins:
        $ ryann_adatp_hide_and_seek_checked_bins = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(I think I’ll be more glad if I {i}don’t{/i} find anyone around here…)"
        $ renpy.pause (1.5)
        c "(I think it’s for the best that there’s no one here…)"

    "Check picnic tables." if not ryann_adatp_hide_and_seek_checked_picnic:
        $ ryann_adatp_hide_and_seek_checked_picnic = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "Anyone hiding under here?"
        $ renpy.pause (2.0)
        c "(Nope...)"

    "[[Go somewhere else.]":
        menu:
            c "(Where should I go to?)"

            "Playground.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_playground_day with dissolvemed
                jump ryann_adatp_hide_and_seek_playground

            "Forest.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_forest with dissolvemed
                jump ryann_adatp_hide_and_seek_forest

            "Stay on the street.":
                jump ryann_adatp_hide_and_seek_street

jump ryann_adatp_hide_and_seek_street



label ryann_adatp_hide_and_seek_forest:

show screen ryannextrainfo
$ ryannlDisplayVar1 = ryann_adatp_hide_and_seek_time_remaining
$ ryannDisplayVar2 = ryann_adatp_hide_and_seek_people_found

if ryann_adatp_hide_and_seek_time_remaining == 0 or ryann_adatp_hide_and_seek_people_found == 4:
    jump ryann_adatp_hide_and_seek_end

menu:
    "Check ditch." if not ryann_adatp_hide_and_seek_checked_ditch:
        $ ryann_adatp_hide_and_seek_checked_ditch = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "Anyone in this ditch?"
        $ renpy.pause (1.5)
        c "(Unsurprisingly, there’s nothing except some dirt.)"

    "Check tree." if not ryann_adatp_hide_and_seek_found_amely:
        $ ryann_adatp_hide_and_seek_found_amely = True
        $ ryann_adatp_hide_and_seek_people_found += 1
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(I wonder if there’s anyone up in this tree?)"
        $ renpy.pause (2.0)
        c "Wait… Is that-{w=0.5}{nw}"
        play sound "fx/impact.wav"
        $ renpy.pause (0.4)
        show black with dissolve
        $ renpy.pause (1.5)
        m "Before I could process what was up in the tree, it suddenly jumped on top of me."
        $ renpy.pause (1.0)
        c "(Ow... What was that?)"
        $ renpy.pause (0.5)
        hide black with dissolvemed
        $ renpy.pause (0.5)
        show amely normal small with easeinbottom
        $ renpy.pause (0.5)
        Am "Hello!"
        c "Hello Amely…"
        Am "Am bestest hunter!"
        c "Yep, you got me good…"
        c "But, it also means I found you."
        Am sad small "Yeah…"
        c "Can you wait in the playground for now?"
        Am normal small "Okay!"
        hide amely with easeoutleft
        $ renpy.pause (1.5)
        c "(Can’t wait to find the lovely bruise that left me with later…)"

    "Check grass." if not ryann_adatp_hide_and_seek_checked_grass:
        $ ryann_adatp_hide_and_seek_checked_grass = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        c "(This grass is pretty dense. Maybe there’s someone hiding in it?)"
        play sound "fx/bushes.ogg" fadein 1.0
        $ renpy.pause (2.0)
        stop sound fadeout 1.5
        c "(No one here, but there are some daisies, so I guess that’s nice.)"

    "Check bushes." if not ryann_adatp_hide_and_seek_checked_bush:
        $ ryann_adatp_hide_and_seek_checked_bush = True
        $ ryann_adatp_hide_and_seek_time_remaining -= 1
        if chap2shrubberysearched > 0:
            c "(Let’s check some more bushes…)"
        else:
            c "(Let’s see if there’s anyone hiding in the bushes…)"
        play sound "fx/bushes.ogg" fadein 1.0
        $ renpy.pause (2.0)
        stop sound fadeout 1.5
        c "(Just your everyday bushes here, nothing interesting.)"

    "[[Go somewhere else.]":
        menu:
            c "(Where should I go to?)"

            "Playground.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_playground_day with dissolvemed
                jump ryann_adatp_hide_and_seek_playground

            "Street.":
                $ renpy.pause (0.5)
                scene black with dissolvemed
                $ renpy.pause (1.0)
                scene ryann_park_street with dissolvemed
                jump ryann_adatp_hide_and_seek_street

            "Stay in the forest.":
                jump ryann_adatp_hide_and_seek_forest

jump ryann_adatp_hide_and_seek_forest



label ryann_adatp_hide_and_seek_end:

$ renpy.pause (2.0)
hide screen ryannextrainfo

if ryann_adatp_hide_and_seek_people_found == 4:
    c "(That’s everyone.)"
    $ renpy.pause (0.5)
    scene black with dissolve
    $ renpy.pause (1.0)
    scene ryann_playground_day 
    show adine normal b flip at Position(xpos=0.3)
    show amely normal small at Position(xpos=0.7)
    show remy normal flip at Position(xpos=0.1) 
    show vara smile small at Position(xpos=0.9) behind amely
    with dissolve
    $ renpy.pause (0.5)
    c "Looks like I win."
    Ry smile flip "It looks like you do."
    Am "You good seeking!"

elif ryann_adatp_hide_and_seek_time_remaining == 0:
    c "(I think my time is up…)"
    $ renpy.pause (0.5)
    scene black with dissolve
    $ renpy.pause (1.0)
    scene ryann_playground_day
    scene ryann_playground_day 
    show adine normal b flip at Position(xpos=0.3)
    show amely normal small at Position(xpos=0.7)
    show remy normal flip at Position(xpos=0.1) 
    show vara smile small at Position(xpos=0.9) behind amely
    with dissolve  
    $ renpy.pause (0.5)
    Ad giggle b flip "Looks like you lose, [player_name]."
    c "I guess I do."
    Am "Yay! We winner!"
    show adine normal b flip with dissolve

else: # This is a basically a "just in case" thing to prevent a crash
    play sound "fx/system2.wav"
    s "Something broke, and somehow, you didn’t find everyone, yet you didn’t run out of time either? Let’s just skip over who won and lost for now…"

Ry normal flip "Well, regardless of who won or lost, I’m sure everyone had fun."
Am "Yeah!"
Ad giggle b flip "Honestly, it made me feel really nostalgic and young, like I was a hatchling again."
Ry smile flip "I’d have to agree with you there."
$ renpy.pause (1.0)
show remy normal flip 
show adine normal b flip
with dissolve
$ renpy.pause (1.5)
Ad think b flip " Well, what should we do now?"
Ry look flip "I’m not quite sure."
c "I can’t think of anything either."
$ renpy.pause (1.5)
Am "Flowers!"
show remy normal flip with dissolve
Ad "Flowers?"
Am "Flowers! Follow me!"
$ renpy.pause (0.5)
show amely normal small flip with dissolve
hide amely with easeoutright
$ renpy.pause (0.5)
Ry "I guess Amely has an idea for something to do."
Ad normal b flip "Let’s hurry after her before she starts doing something she shouldn’t."
c "Right."

$ renpy.pause (0.5)
scene black with dissolvemed
$ renpy.pause (0.5)

jump ryann_adatp_forest_start

