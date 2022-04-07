
label ryann_adatp_start_pda:
label ryann_adatp_start_pda2:

c "If you don't mind me asking, how come you aren't working today?"
Ry smile "Well, Adine and I were planning on bringing Amely and Vara to the park today, so I took the day off work."
Ry normal "There are so few volunteers working at the orphanage, so they really could use getting to spend time outside with someone one on one, or in this case, two on two."
$ renpy.pause (1.5)
Ry smile "Actually, if you wanted, I wouldn’t mind if you came along with us."
Ry normal "I think it would be nice for Amely and Vara to spend time with someone else other than me or Adine, especially a human."
if adinestatus == "bad" or adinestatus == "abandoned":
    c "Wait, you said Adine will be there too, right?"
    Ry look "Yes. Would that be a problem?"
    c "Well, I don’t exactly think Adine is too fond of me… I don’t want to ruin the trip for the rest of you."
    Ry normal "Oh. Well, I won’t press either of you for details as it’s your business. It is a shame you can’t come along though."
    c "It’s fine. You go enjoy yourselves."
    Ry "Right. Anyway, I appreciate you delivering this to me."
    c "I'm just going to leave you to it, then."
    Ry "Thank you."
    c "Enjoy."
    $ c4clues += 1
    $ renpy.pause (0.5)
    show black with dissolvemed
    $ renpy.pause (0.5)
    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
    jump c4sections

menu:
    "Sure.":
        c "Sure, I’d love to come along."
        Ry "I’m glad to hear it, but aren’t you helping the police at the moment? Shouldn't that take priority?"
        c "Well, most of the stuff I could be helping with is just basic chores that could be done at any time. I’m sure it’ll be fine if I take a break for a while."
        Ry "Alright, if you say so. Just give me a few moments to get ready, then we’ll head to the orphanage."
        $ renpy.pause (0.5)
        scene black with dissolvemed
        $ renpy.pause (0.5)
        scene hatchery at Pan ((0, 0), (0, 180), 3.0) with dissolveslow
        $ renpy.pause (1.0)
        show adine normal b at Position(xpos=0.8) behind Vara
        show amely normal small at Position(xpos=0.67)
        show vara normal small at Position (xpos=0.9)
        with dissolve
        $ renpy.pause (1.3)
        show remy normal flip at Position(xpos=0.2) with easeinleft
        $ renpy.pause (0.5)
        Ad "There you are Remy. We already got ready to go while waiting for you."
        Ad think b "Wait, why is [player_name] with you?"
        Ry "I hope you don’t mind, but I invited [player_name] to come along with us. Is that okay?"
        Ad giggle b "Oh, sure. The more the merrier!"
        Ad normal b "I don’t have a problem with that, and I’m assuming Amely and Vara don’t either, right?"
        Am "Okay!"
        m "Vara nodded in silent agreement."
        Ry "Alright. Let’s get going then."
        $ renpy.pause (0.5)
        scene black with dissolveslow
        jump ryann_adatp_start_park


    "Sorry, I can’t.":
        c "Sorry, but I can’t. I’m helping the police at the moment, and that takes priority."
        Ry "Ah, of course. I understand."
        Ry "Maybe some other time then."
        c "Maybe, but I can’t promise I won’t be busy later too. "
        c "Sorry, I don’t mean to sound rude, but I have to get going. I’ll see you later."
        Ry "Alright, goodbye."
        $ c4clues += 1
        $ renpy.pause (0.5)
        show black with dissolvemed
        $ renpy.pause (0.5)
        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        jump c4sections


label ryann_adatp_start_orphanage_remy:
label ryann_adatp_start_orphanage_remy2:

$ renpy.pause (1.5)
Ry normal flip "Hmm…"
Ry smile flip "Actually, Adine, how about we invite [player_name] with us?"
Ad giggle b "Oh, Sure, the more the merrier!"
Ad normal b "I don’t have a problem with that, and I’m assuming Amely and Vara don’t either, right?"
show amely normal small at Position(xpos=0.7, ypos=1.0) with easeinbottom
$ renpy.pause (0.2)
Am "Okay!"
m "Vara nodded in silent agreement."
c "Wait, where would we be going?"
Ry normal flip "Oh, right, I completely forgot to say. We’re just planning on going to the park, then bring Amely and Vara to the playground."
Ry "So, what do you say [player_name]?"
menu:
    "Sure.":
        c "Sure, I’d love to come along."
        Ry "I’m glad to hear it, but aren’t you helping the police at the moment? Shouldn't that take priority?"
        c "Well, most of the stuff I could be helping with is just basic chores that could be done at any time. I’m sure it’ll be fine if I take a break for a while."
        Ry "If you say so, just give us a few moments to get ready."
        $ renpy.pause (0.5)
        scene black with dissolveslow
        jump ryann_adatp_start_park

    "Sorry, I can’t.":
        c "Sorry, but I can’t. I’m helping the police at the moment, and that takes priority."
        Ad sad b "Oh, that’s a shame."
        Ry normal flip "Maybe some other time then."
        show adine normal b with dissolve
        c "Maybe, but I can’t promise I won’t be busy later too."
        c "I don’t mean to sound rude, but I have to get going. I’ll see you later."
        Ry "Alright, goodbye."
        Am "Bye-bye!"
        $ c4clues += 1
        $ renpy.pause (0.5)
        show black with dissolvemed
        $ renpy.pause (0.5)
        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        jump c4sections


label ryann_adatp_start_orphanage_adine:
label ryann_adatp_start_orphanage_adine2:

$ renpy.pause (1.5)
Ad think b "Hmm…"
Ad normal b "Remy, would it be alright if [player_name] came with us?"
Ry smile flip "Well, I can’t see a reason to say no."
Ry normal flip "Amely, Vara, is it alright if [player_name] comes with us?"
show amely normal small at Position(xpos=0.7, ypos=1.0) with easeinbottom
Am "Yeah!"
m "Vara nodded in silent agreement."
c "Wait, where would we be going?"
Ad giggle b "Oh, right. I knew I was forgetting something. We’re going to the playground in the park."
Ad normal b "So, do you wanna come along?"
menu:
    "Sure.":
        c "Sure, I’d love to."
        Ad think b "Wait, you’re helping the police, right? Shouldn’t you be doing that instead?"
        c "Well, most of the stuff I could be helping with is just basic chores that could be done at any time. I’m sure it’ll be fine if I take a break for a while."
        Ad normal b "Alright, as long as it’s fine with you. We’ll just need a bit to get ready first, then we can go."
        $ renpy.pause (0.5)
        scene black with dissolveslow
        jump ryann_adatp_start_park

    "Sorry, I can’t.":
        c "Sorry, but I can’t. I’m helping the police at the moment, and that takes priority."
        Ad sad b "Oh, that’s a shame."
        Ry normal flip "Maybe some other time then."
        show adine normal b with dissolve
        c "Maybe, but I can’t promise I won’t be busy later too."
        c "I don’t mean to sound rude, but I have to get going. I’ll see you later."
        Ad "Alright, see ya later then."
        Am "Bye-bye!"
        $ c4clues += 1
        $ renpy.pause (0.5)
        show black with dissolvemed
        $ renpy.pause (0.5)
        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        jump c4sections


#==================================================================================================================================================================

label ryann_adatp_start_park:

stop music fadeout 1.5
$ renpy.pause (1.0)
play music "mx/serene.ogg" fadein 1.0
play sound "fx/steps/clean.wav"
scene ryann_park_street with dissolveslow
show adine normal b flip at Position(xpos=0.4) behind amely
show remy normal flip at Position(xpos=0.1) behind vara
show vara normal small flip at Position(xpos=0.1)
show amely normal small flip at Position(xpos=0.35)
with dissolve
$ renpy.pause (4.0)
show amely sad small flip with dissolve
$ renpy.pause (1.0)
Am "We there yet…?"
Ad "Almost, it’s just a bit further."
$ renpy.pause (0.5)
show amely normal small flip with dissolve
$ renpy.pause (2.0)
show amely sad small flip with dissolve
$ renpy.pause (1.0)
Am "We there yet…?"
Ad annoyed b flip "We’re nearly there Amely, just have some patience."
$ renpy.pause (0.5)
show amely normal small flip with dissolve
$ renpy.pause (2.0)
show amely sad small flip with dissolve
$ renpy.pause (1.0)
Am "We there yet…?"
Ad normal b flip "Yes, we are. Look, see? The park is just up ahead."
Am normal small flip "Yay!"
$ renpy.pause
show amely at Position(xpos=0.7) with ease
play sound "fx/impact.wav"
show amely:
    ease 0.4 ypos 1.35 xpos 0.8
$ renpy.pause (0.3)
show adine sad b flip
show remy look flip
show vara none small flip
show amely sad small flip
with dissolve
m "Upon hearing that the park was close, Amely started sprinting towards it, but almost immediately fell."
Ad "Oh no! Amely, are you okay?"
$ renpy.pause (0.5)
show amely at Position(ypos=1.0) with ease
$ renpy.pause(0.5)
Am "Ow!"
$ renpy.pause (1.5)
show amely normal small flip with dissolve
$ renpy.pause (0.5)
Am "Yay!"
hide amely with easeoutright
$ renpy.pause(0.5)
Ad annoyed b flip "This hatchling will be the death of me…"
hide adine with easeoutright
$ renpy.pause (0.5)
Ad "Amely, slow down! Wait for me!"
$ renpy.pause (2.0)
c "Amely is definitely… energetic, huh?"
Ry "I have no idea how Adine can handle looking after her without consistently feeling exhausted."
c "I have no clue either."
Ry normal flip "Anyway, we should probably try catch up with those two."
show vara normal small flip with dissolve
c "Yeah, let’s go."
$ renpy.pause (0.5)

scene black with dissolveslow
$ renpy.pause (0.5)
scene ryann_playground_day with dissolveslow
$ renpy.pause (0.5)
show remy normal flip at Position(xpos=0.1) behind Vara
show vara normal small flip at Position(xpos=0.2)
with easeinleft
$ renpy.pause (0.7)
show amely normal small at Position(xpos=0.7) with easeinright
$ renpy.pause (0.5)
show adine annoyed b at Position(xpos=0.8) behind amely with easeinright
$ renpy.pause (0.5)
Ry smile flip "Finally got her under control, huh?"
Ad "Yeah… Finally…"
Am "Heh heh heh…"
Ry normal flip "Well you two go ahead and play, just don’t go too far, okay?"
Am "Okay!"
show vara smile small flip with dissolve
show amely normal small flip with dissolve 
hide amely
hide vara 
with easeoutright
show adine normal b with dissolve
$ renpy.pause (1.5)

c "So, what will we do now?"
Ry "Well, Adine and I have a lot to catch up on. We’re going to sit by the benches and chat. You’re more than welcome to come join us if you wish."
Ad think b "Or you could check on what Amely and Vara are getting up to."
Ry "It’s up to you what you decide to do. You’re here to enjoy yourself after all."
show adine normal b with dissolve
c "Alright, I’ll keep it in mind."
$ renpy.pause (0.5)
show remy normal with dissolve
hide remy 
hide adine
with easeoutleft
$ renpy.pause (1.0)
c "(Guess I can do whatever I want now.)"

label ryann_adatp_park_menu:

if ryann_adatp_park_choices == 3:
    $ renpy.pause (1.5)
    Ad "Hey! Amely, Vara, [player_name], can you three come over here?"
    c "(Huh? I wonder what Adine wants?)"
    $ renpy.pause (1.5)
    show adine normal b flip at Position(xpos=0.3) behind remy
    show remy normal flip at Position(xpos=0.05)
    show amely normal small at Position(xpos=0.7) 
    show vara normal small at Position(xpos=0.95)
    with dissolvemed
    $ renpy.pause (0.5)
    Am "Hello!"
    c "So, what did you call us over for?"
    jump ryann_adatp_hide_and_seek_start

menu:
    "Check on Amely" if not ryann_adatp_park_checked_amely: # Starts on line 298
        $ ryann_adatp_park_choices += 1
        $ ryann_adatp_park_checked_amely = True
        jump ryann_adatp_park_amely

    "Check on Vara" if not ryann_adatp_park_checked_vara: # Starts on line 391
        $ ryann_adatp_park_choices += 1
        $ ryann_adatp_park_checked_vara = True
        jump ryann_adatp_park_vara

    "Check on Adine and Remy" if not ryann_adatp_park_checked_adine_remy: # Starts on line 453
        $ ryann_adatp_park_choices += 1
        $ ryann_adatp_park_checked_adine_remy = True
        jump ryann_adatp_park_adine_remy



label ryann_adatp_park_amely:

m "After a quick glance around, I spotted Amely at the top of the stairs leading into the park."
$ renpy.pause (1.5)
show amely normal small with dissolve
$ renpy.pause (0.5)
c "Hey Amely."
Am "Hello!"
c "What are you up to there?"
Am "Chalk!"
c "You’re drawing with chalk? Can I see?"
Am "Yeah!"
$ renpy.pause (0.5)
show ryann_chalk_flower with dissolvemed
$ renpy.pause (4.0)
hide ryann_chalk_flower with dissolvemed
$ renpy.pause (0.5)
c "Oh, wow! That’s a really beautiful flower Amely."
Am "Thank you!"
$ renpy.pause (1.5)
Am "Draw!"
c "Do you want me to draw something?"
Am sad small "No!"
Am normal small "Who me draw?"
c "You… want to know who you should draw a picture of?"
Am "Yeah!"
c "Alright, how about…"
menu: 
    "Adine":
        c "How about you draw Adine?"
        Am "Okay!"
        $ ryann_adatp_amely_chalk = "adine"

    "Remy":
        c "How about you draw Remy?"
        Am sad small "Hmm…"
        Am normal small "Okay!"
        $ ryann_adatp_amely_chalk = "remy"

    "Vara":
        c "How about you draw Vara?"
        Am "Okay!"
        $ ryann_adatp_amely_chalk = "vara"

    "Everyone":
        c "How about you draw everyone? That way, no one feels left out."
        Am sad small "Hmm…"
        Am normal small "Okay!"
        $ ryann_adatp_amely_chalk = "all"

play sound "fx/scribbles.ogg"
$ renpy.pause (5.0)
stop sound fadeout 1.5
$ renpy.pause (0.5)
Am "Done. Look!"
$ renpy.pause (0.5)

if ryann_adatp_amely_chalk == "adine":
    show ryann_chalk_adine with dissolvemed
    $ renpy.pause (4.0)
    hide ryann_chalk_adine with dissolvemed

elif ryann_adatp_amely_chalk == "remy":
    show ryann_chalk_remy with dissolvemed
    $ renpy.pause (4.0)
    hide ryann_chalk_remy with dissolvemed

elif ryann_adatp_amely_chalk == "vara":
    show ryann_chalk_vara with dissolvemed
    $ renpy.pause (4.0)
    hide ryann_chalk_vara with dissolvemed

elif ryann_adatp_amely_chalk == "all":
    show ryann_chalk_all with dissolvemed
    $ renpy.pause (4.0)
    hide ryann_chalk_all with dissolvemed

$ renpy.pause (0.5)
c "Wow! That’s amazing! You’re a really great artist Amely."
Am "Yaaaaay!!!"
show amely normal small flip with dissolve
hide amely with easeoutright
$ renpy.pause (1.5)
c "(And there she goes…)"
$ renpy.pause (1.5)
c "(Wait, where did she even get this chalk from?)"
c "(Well, she’s gone too far to ask now…)"
$ renpy.pause (1.0)

jump ryann_adatp_park_menu



label ryann_adatp_park_vara:

m "A look around the playground led me to spot Vara playing on some of the playground equipment. As she stepped off it, I made my way over."
$ renpy.pause (1.5)
show vara normal small with dissolvemed
$ renpy.pause (0.5)
show vara none small with dissolve
c "Hey Vara."
$ renpy.pause (1.0)
Vr normal small "…"
c "Are you doing okay?"
Vr "…"
m "She didn’t say anything, but nodded instead."
c "Alright, but if you need anything, just let me, Adine, or Remy know. Okay?"
$ renpy.pause (2.0)
m "I turned and started to walk away, but was stopped by something tugging my leg."
m "I looked to check and saw it was Vara grabbing my leg, and upon my notice of her, she pulled again and started to walk off, glancing back indicating I should follow."
$ renpy.pause (2.0)
if persistent.varasaved == True:
    m "I trailed behind her for a few moments (getting a sense of deja vu,) as she led me to some swings."
else:
    m "I trailed behind her for a few moments as she led me to some swings."

c "Oh, do you want me to push you on the swings?"
m "She again nodded in silence."
m "I moved towards the swing set and realized that they weren't the usual rectangular design I recognized, but rather it had a much bigger surface area, with some kind of harness strapping."
c "(So this is why she didn’t ask Remy or Adine…)"
c "I’ll hold steady it while you get on, then I’ll do up this harness for you."
play sound "fx/undress.ogg"
$ renpy.pause (1.5)
m "It took surprisingly little time or effort to set everything up, and once it was, I started pushing Vara gently, unsure of my technique when it came to pushing a dragon instead of a human."
m "I didn’t want to accidentally hurt Vara, so I didn’t push her too hard, trying to keep only a low and slow pace."
m "She did seem to be enjoying it though, so I started pushing a bit harder."
show vara none small with dissolve
m "She was initially surprised by the extra speed but soon got into the rhythm of it."
show vara smile small with dissolve
m "Then she started flapping her wings in time with her swinging, further increasing her momentum, which I took as a sign to push her even higher."
m "She was now going fairly high at this point, higher than I assumed Remy or Adine could push her with their lack of proper hands. Surprisingly enough, she didn’t seem scared at all."
m "I noticed she even started slightly wagging her tail and that there was a bright smile on her face."
$ renpy.pause (2.0)
m "After swinging at this height for a bit longer, she glanced back at me, letting me know she wanted to stop, and after she slowed down, I grabbed the swing stopping it entirely."
m "I undid the harness, and she hopped down with surprising ease and turned to face me."
c "Did you enjoy that?"
m "She responded with a more enthusiastic nod than usual."
show vara none small with dissolve
$ renpy.pause (0.5)
Vr "{size=-7}T…{/size}"
$ renpy.pause (1.0)
show vara smile small with dissolve
$ renpy.pause (0.5)
Vr "{size=-7}Thank you…{/size}"
c "You’re welcome."
m "She then pranced off, back to playing on the other playground equipment."
hide vara with easeoutleft
$ renpy.pause (1.5)
c "(How can someone who barely speaks be such a sweetheart?)"
$ renpy.pause(1.0)

jump ryann_adatp_park_menu



label ryann_adatp_park_adine_remy:

m "I looked around and saw Adine and Remy sitting together on a bench. Or more accurately, Adine was sitting on the bench, and Remy was sitting on the ground next to it."
$ renpy.pause (1.5)
show remy normal flip at left
show adine normal b at right
with dissolvemed
$ renpy.pause (0.5)
Ad giggle b "Hey [player_name]."
Ry smile flip "I’m glad that you decided to come over."
c "I’m not interrupting anything over here, am I?"
show adine normal b with dissolve
Ry normal flip "Not at all."
Ad "We’ve just been catching up on what’s been happening in each other's lives."
Ad giggle b "I was just about to tell the story of how I met Amely."
c "I wouldn’t mind hearing that."
Ry smile flip "I’d really like to hear it as well."
show remy normal flip
show adine normal b
with dissolve
Ad "Alright, so… This was before I volunteered at the orphanage. I was at the beach, practicing my stunt flying."
Ad "I was there for a while, then I suddenly hear a little dragon cheering me on from the beach. I look, and there she is."
Ad "So, I fly down and ask where her parents were, as there were very few people on the beach and none who seemed to be her parents."
Ad giggle b "I ask, but she ignores the question and starts cheering me on again, saying, “Flying cool!”, and “Bestest flyer ever!”."
Ad annoyed b "At that point, all the other people on the beach start staring at the now screeching hatchling, singing my praises. I felt so embarrassed that they were judging me that I couldn’t control her, even though I wasn’t her parent or guardian."
Ry "I can’t begin to imagine how I would have felt in that situation."
Ad "Trust me, it’s not a good feeling."
Ad normal b "Anyway, a few moments later, a very panicked runner spots us and sprints over. Then she starts thanking me for finding her and tells me that she went missing from the orphanage that morning."
Ad giggle b "She then explains Amely had a habit of running out of the orphanage and, in her words, “Going adventure!”. That mess is the reason they have hatchling-proof locks on most doors, cabinets, and pretty much everything else in the orphanage now."
Ad normal b "She then leads me and Amely back to the orphanage, and explains about volunteering there, and, as you both already know, I agreed to."
c "After Amely’s first impression, I doubt I would’ve volunteered."
Ry "If I didn’t decide to volunteer, I wouldn't have gotten to meet Vara."
Ry smile flip "It seems like a lot at first, but once you actually start, it’s entirely worth it."
Ad giggle b "Exactly. I wouldn’t have gotten to know Amely more either."
Ad normal b "You just need something to give you that first push to actually get into it, and then when you get to know the hatchlings better, you’ll understand."
Ry normal flip "I agree. If you have the opportunity to, I think it would be lovely for both them and you if you spent more time with them and know them better."
menu:
    "Amely is an agent of chaos.":
        c "After that story, and seeing how she acted on the way here, I don’t need to spend any more time to see Amely is a pure agent of chaos."
        Ry look flip "She isn’t that bad, [player_name]."
        Ad giggle b "I don’t want to lie, but I don’t want to admit the truth of how I feel about that comment."
        Ry shy flip "Really, Adine?"
        Ad normal b "You should have seen her when she was younger. She’s definitely gotten better, but not by a huge amount."
        show remy normal flip with dissolve

    "Vara is a sweetheart.":
        c " I don’t need to spend much more time to see that Vara is an absolute sweetheart."
        Ry smile flip "Exactly."
        $ renpy.pause (1.0)
        show remy normal flip with dissolve
        $ renpy.pause (0.5)
        Ry sad flip "I really don’t understand how she {i}can{/i} be such a sweetheart after everything she’s been through…"
        Ad disappoint b "That poor girl didn’t deserve anything that happened to her…"
        $ renpy.pause (2.0)
        Ad normal b "But at least she gets a second chance to be happy with you, Remy."
        Ry normal flip "Yes, I guess you’re right."

    "They're similar to both of you.":
        c "Well, I don’t need to spend any more time with them to see that, in a way, they’re both similar to the two of you."
        Ry "What do you mean, [player_name]?"
        c "Well, Vara is extremely quiet, and Remy is pretty reserved. Amely is very… energetic, and Adine is pretty lively."
        c "It's kind of like they’re more intense versions of you two."
        Ry smile flip "I never thought of it that way. It’s actually a really sweet way of thinking about them."
        Ad giggle b "I guess it also explains why they just naturally gravitated towards us."
        show remy normal flip 
        show adine normal b 
        with dissolve

if adine2unplayed == False:
    c "Also, while we’re on the topic of them, Remy, I wanted to know if you considered adopting Vara."
    Ry "Well, I have considered the thought of adopting."

else: 
    c "Also, while we’re on the topic of them, I wanted to know if either of you has considered adopting Amely and Vara."
    Ad disappoint b "I would if I could, but I don’t think I could care for her properly. Not as a single parent with my packed work schedule."
    Ry look flip "That’s a shame…"
    Ry normal flip "I have considered the thought of adopting myself though."
    show adine normal b with dissolve

Ry "I’m just not sure if I’m prepared to fully make that commitment yet."
Ad "Well, it’s good you’re properly thinking it through instead of just rushing into it."
Ad disappoint b "That’s the reason some of those poor kids are there in the first place."
c "Well, they could be in a lot worse of a situation."
Ad "Yeah, I guess you’re right."
$ renpy.pause (2.0)
Ad "Sorry for bringing down the mood…"
Ry "Don’t worry about it. I still really enjoyed the conversation."
show adine normal b with dissolve
$ renpy.pause (1.5)

if ryann_adatp_park_choices == 3:
    Ry smile flip "Actually, how about we get Amely and Vara together. I have an idea for something we could do."
    c "What did you have in mind?"
    Ry normal flip "It’ll be easier to say with everyone together so I’m not repeating myself."
    Ad "We'll bring them over then."
    $ renpy.pause (0.5)
    show adine normal b flip with dissolve
    hide adine with easeoutright
    hide remy with easeoutright
    $ renpy.pause (2.5)
    show adine normal b at Position(xpos=0.3) behind remy with easeinright
    show adine normal b flip with dissolve
    show remy normal at Position(xpos=0.1) with easeinright
    show remy normal flip with dissolve
    $ renpy.pause (0.5)
    show amely normal small at Position(xpos=0.7) 
    show vara normal small at Position(xpos=0.95)
    with easeinright
    $ renpy.pause (0.5)
    Am "Hello!"
    Ry "Hello Amely."
    c "So, Remy, what did you want to say?"
    jump ryann_adatp_hide_and_seek_start

else:
    Ry "Anyway, I had an idea something for the five of us could do, but I think it’s best if we wait for a bit longer before doing it."
    Ry "We’ll call you when we’re ready."
    c "Alright, I’ll see you two in a bit then."
    $ renpy.pause (0.5)
    hide remy
    hide adine 
    with dissolvemed
    $ renpy.pause (1.0)

    jump ryann_adatp_park_menu



label ryann_adatp_hide_and_seek_start:

Ry smile flip "Well, I was thinking that the five of us could play hide and seek together."
show vara smile small with dissolve
Am "Hide seek fun!"
Ry normal flip "Vara, do you want to play hide and seek?"
Vr "…"
m "Vara nodded."
Ad think b flip "So, who’s going to be the seeker?"
c "I wouldn’t mind being the seeker."
show adine normal b flip with dissolve 
Ry "Alright. You can count to, let’s say, 30? And you’ll have 10 minutes to find the four of us."
c "Sounds fair enough to me."
Ad "We won’t go too far, we’ll stay within the park and nearby street."
Am "Forest too!"
Ad think b flip "Hmm…"
Ad normal b flip "Alright, as long as you don’t go too far, okay?"
Am "Okay."
Ry "Start whenever you’re ready [player_name]."
c "Alright, I’ll start now then."
$ renpy.pause (0.5)
scene black with dissolvemed
$ renpy.pause (0.5)
c "1, {w=1.0}2, {w=1.0}3, {w=1.0}4, {w=1.0}5…{w=1.0}{nw}"
$ renpy.pause (2.5)
scene ryann_playground_day with dissolveslow
$ renpy.pause (0.5)
c "Ready or not, here I come!"

jump ryann_adatp_hide_and_seek_playground


