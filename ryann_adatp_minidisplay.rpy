
# I'm not taking ownership of this code, it was originally made by EvilChaosKnight

screen ryannextrainfo:

    if ryannextradisplay == 2:
        add "image/ui/ryannextras2.png" at zoom_fade_in

    else:
        pass

    hbox at zoom_fade_in:
        xalign 0.03
        yalign 0.0

        if ryannextradisplay == 2:
#           add "image/ui/ryannextras2.png"
            text _("[ryannDisplayVar1name]{b} [ryannlDisplayVar1]{/b}[ryannDisplayVar1unit]\n[ryannDisplayVar2name] {b}[ryannDisplayVar2]{/b}[ryannDisplayVar2unit]") style "status_text"

        else:
            pass

