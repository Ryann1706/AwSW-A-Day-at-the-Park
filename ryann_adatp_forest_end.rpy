
label ryann_adatp_forest_start:

scene ryann_forest with dissolvemed
$ renpy.pause (0.5)
show amely normal small flip at Position(xpos=0.7) with easeinleft
show amely normal small with dissolve
$ renpy.pause (0.5)
show adine normal b at Position(xpos=0.9) behind amely with easeinright
$ renpy.pause (0.5)
show remy normal flip at Position(xpos=0.1) behind vara
show vara smile small flip at Position(xpos=0.2)
with easeinleft
$ renpy.pause (0.5)

Am "We here."
Ad think b "What did you want to show us here, Amely? Something to do with flowers?"
Am "Flowers!"
play sound "fx/bushes.ogg" fadein 1.0
if ryann_adatp_hide_and_seek_checked_grass == True:
    m "Amely then crouched down into the grass and started searching through it, just as I had earlier. She then rose with the daisies I had found earlier too."
else:
    m "Amely then crouched down into the dense grass and started searching through it. When she rose she had daisies in her little hands."

stop sound fadeout 0.5
Am "Crown!"
Ad giggle b "Oh, you want to make flower crowns? That’s adorable!"
Ry smile flip "Aw, that’s so precious."
Ry normal flip "I guess you and [player_name] are going to be pulling our weight, though."
c "Pulling your weight?"
show adine normal b with dissolve
Ry "Well, yes. Because of mine, Adine, and Vara’s lack of proper hands, you two will have to make them for us."
c "Well, I could if I actually knew how to…"
Ad "I’m sure Amely will teach you. She’s made them before, so she’s quite the expert."
Am "Crown!"
show amely normal small fl with dissolve
$ renpy.pause (0.5)
m "Somehow, in the time we were talking, Amely had already made a flower crown for herself."
Ad giggle b "See?"
Ad normal b "Amely, would you mind teaching [player_name] how to make flower crowns?"
Am "Okay. Am greatest teacher."
$ renpy.pause (2.0)
m "After a more visual-than-verbal tutorial from Amely, we were able to make the remaining flower crowns we needed for everyone."
$ renpy.pause (1.5)
show amely at Position(xpos=0.5) with ease
show vara none small flip with dissolve
$ renpy.pause (0.5)
Am "Hello!"
$ renpy.pause (0.5)
show vara none small fl flip with dissolve
$ renpy.pause (0.5)
show amely at Position(xpos=0.7) with ease
$ renpy.pause (0.5)
Am "Very good!"
Ry smile flip "Wow! Vara, that looks lovely on you."
Vr smile small fl flip "…"
show remy normal flip with dissolve
Ad " I guess it’s my turn now. But I'll have to take off my goggles first."
$ renpy.pause (0.7)
play sound "fx/undress.ogg"
show adine normal with dissolve
$ renpy.pause (0.5)
Ad giggle "Now I can put it on."
$ renpy.pause (1.0)
show adine giggle fl with dissolve
$ renpy.pause (1.0)
Am "Cute!"
c "I’d have to agree with Amely. It looks pretty good on you."
Ad normal fl "Why, thank you."
Ry "I guess it’s our turn now, [player_name]."
m "Me and Remy then simultaneously put our flower crowns on."
$ renpy.pause (0.5)
show remy normal fl flip with dissolve
$ renpy.pause (1.0)
if remyscenesfinished == 3 and remystatus == "good":
    c "Dang Remy, I have to say, that flower crown makes you look pretty handsome, or at least more so than usual."
    Ry shy fl flip "O-Oh, well, thank you [player_name]... It looks good on you too."
    Ad giggle fl "Oh my… Remy, is there something you didn’t tell me about you and [player_name]?"
    Ry "Well… We, um…"
    Ad normal fl "Remy, I’m just teasing. You don’t have to say anything. That’s your and [player_name]'s business."
    Ry normal fl flip "Right. A-Anyway..."

else:
    Ad "That looks pretty good on you, Remy. I think it’s quite charming."
    Ry smile fl flip "Thank you."
    show remy normal fl flip with dissolve 
    Ad "It suits you pretty well too, [player_name]."
    Am "Yeah, look good!"
    c "Thank you, Amely. That’s very kind of you to say."
    Am "Yes, me very kindest."

Ry "Vara, what do you think?"
Vr normal fl flip "…"
$ renpy.pause (1.5)
Vr "{size=-7}B-Both looks nice…{/size}"
Ry smile fl flip "Well, thank you very much, Vara." 
c "Yeah, that’s really nice to hear. Thank you, Vara."
show remy normal fl flip 
show vara smile fl flip
with dissolve 

$ renpy.pause (2.0)
Ad giggle fl "You know, the more accustomed I get to seeing these flower crowns, the more stylish I think they are."
c "Maybe you could try to work it into your stunt flying routine?"
Am "Yeah! Bestest flyer!"
Ad think fl "Hmm…"
Ad normal fl "As much as I’d now like to, I’m pretty sure it would just end up falling off or breaking."
Am sad small fl "Aww…"
Ry "Don’t worry, Amely. You can wear flower crowns as much as you want."
Am normal small fl "Yaaay!"
Ad giggle fl "Next thing we’ll know, Amely would have gotten everyone in the orphanage to wear flower crowns."
Ry smile fl flip "That would be absolutely adorable."
$ renpy.pause (1.5)
Ry normal fl flip "Actually, while we’re on the topic of flowers, I  had an idea I wanted to share with you, Adine."
Ad think fl "Oh? Well, what is it?"
Ry "Well, I was thinking if we plant some flowers outside the orphanage, it could make it more appealing for people passing by."
Ad "Hmm…"
Ad giggle fl "Yeah! And if they decide to drop by, we could talk to them about volunteering, or maybe even adopting."
Ry smile fl flip "I think {i}thistle{/i} definitely work."
Ad normal fl "And maybe we can-{w=0.7}{nw}"
$ renpy.pause (0.5)
show adine annoyed fl with dissolve
$ renpy.pause (1.0)
Ad "Really?"
Ry normal fl flip "Oh, I’m sorry. Do you not like flower puns?"
Ry smile fl flip "Oopsie daisy!"
Am "Hehehe!"
Ad "You’re lucky we’re in front of Amely and Vara right now…"
Ry "Oh, come on, Adine. We’re just {i}pollen{/i} your leg!"
m "It was hard for me to refrain from chuckling at this point. I even heard a slight snicker from Vara too. "
Ad "Don’t encourage him, [player_name]..."
$ renpy.pause (2.0)
Ry normal fl flip "Okay, Adine, I’m sorry. I’ll stop with the puns."
Ry smile fl flip "I hope this won’t affect our friendship, {i}down-delion.{/i}"
Ad "…"
Ad "Like I said, you’re very lucky Amely and Vara are here…"
Am "Funny!"
c "Yes, it was very funny."
Ad "…"
$ renpy.pause (1.5)

Ry normal fl flip "Anyway, I’d say this was well worth the detour."
Ad normal fl "Minus the terrible puns, definitely."
Ry "We should start heading back to the orphanage now before it gets too late."
Ad think fl "Yeah, we have been here for a while now, huh?"
c "Well, time flies when you’re having fun."
Ad giggle fl "And this whole trip was extremely fun."
Am "Yes, funnest!"
Ry "Sadly, we’ve got to get going now."
Am sad small fl "Okay…"
$ renpy.pause (1.5)

scene black with dissolvemed
$ renpy.pause (1.0)
play sound "fx/steps/clean.wav"
m "After a quick walk, we made out way back to the orphanage."
$ renpy.pause (1.5)
scene hatchery
show remy normal fl flip at Position(xpos=0.1) behind amely
show adine normal fl at Position(xpos=0.9) behind vara
show amely normal small fl at Position(xpos=0.7)
show vara smile small fl flip at Position(xpos=0.2)
with dissolveslow
$ renpy.pause (0.5)
Ry "[player_name], would you mind staying for a bit longer before you go?"
c "Sure. What is it?"
Ry smile fl flip "We just wanted to say that we appreciate you coming along. It’s been a while since I’ve gotten to have a really good time with other people like this."
Ad giggle fl "I really enjoyed your company too. I doubt it would have been the same without you."
show adine normal fl 
show remy normal fl flip 
with dissolve
Ry "And I’m sure Vara and Amely really enjoyed you being there too, right?"
Am "Yeah!"
m "Vara once again nodded."
Ad "We should try and go out together like this again at some point."
c "I’d like to, but I’m not sure if I can. I can't tell if I’ll be busy or not yet."
Ad "Oh, that’s a bit of a shame. "
Ry "Anyway, we should be getting Amely and Vara inside. Hopefully we’ll see you later."
Am "Bye-bye!"
c "See ya."

$ renpy.pause (0.5)
stop music fadeout 1.5
scene black with dissolvemed
play sound "fx/steps/clean.wav"
$ renpy.pause (1.5)
play music "mx/elegant.ogg"
scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
$ renpy.pause (2.0)
show sebastian normal b with dissolve
$ renpy.pause (0.5)
Sb "There you are, [player_name]. I’ve been waiting here for you for a while now. What took you so long?"
Sb disapproval b "And what's with the flower crown?"
if c4hatcheryavailable == False:
    c "Oh, sorry about that. I just got a bit caught up with something after delivering the eggs to the hatchery."
elif c4libraryavailable == False:
    c "Oh, sorry about that. I just got a bit caught up with something after delivering the PDA to Remy."
c "You don’t have to worry about anything, though. I’m fine, and the delivery went smoothly."
Sb "Right. Just try to be more conscious of time in the future. I was starting to suspect something could have happened to you, and that’s the reason you were late."
Sb normal b "But I guess as long as you’re fine, it doesn't need to be worried about as long as it doesn't happen again. Anyway…"

$ ryann_adatp_played = True

jump c4postsections

