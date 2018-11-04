# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
screen hp_show():
    frame:
        align(0.05,0.05)
        hbox:
            spacing 10
            text "HP" style "button_text" yalign 0.5
            bar value AnimatedValue(hp,100,1.0) yalign 0.5 xsize 200

screen stats_screen():
    frame:
        align(0.95,0.15)
        xysize(180, 100)
        vbox:
            align(0.0, 0.5)
            text "{u}Stats:{/u}"
            null height 10
            text "HP: [hp]"
            null height 10
            text "Day: [day]"

screen one_button_screen():
    textbutton "스탯" action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen")) align (0.95, 0.05)
