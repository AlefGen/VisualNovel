# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Pholis = Character("Pholis", Color = "blue")
define Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf")

# Define images

define cuarto = "images/Habitacion.png"
define black_screen = "images/black_screen.png"


# Define functions 
define centered_text = Character(what_size=40, what_color="#FFFFFF", what_align=(0.5,0.5))

image anim1 = Movie(play = "images/anim1.webm")
init python:
    def callback_Pholis(event, **kwargs):
        if event == "show":
            renpy.music.play("texto.mp3", channel=6)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel= 6)

    def callback_Sombra(event, **kwargs):
        if event == "show":
            renpy.music.play("texto 2.ogg", channel=6)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel= 6)

    Pholis = Character("Pholis", callback=callback_Pholis)
    Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf",callback=callback_Sombra)

    
$ renpy.music.set_volume() # Ajust general vol of the game WIP
    
#Firts cap Prologue
label start:
    jump recibir_llamada
    # jump recibir_llamada # WTF

    $ renpy.store.preferences.text_cps = 10

    # Scence worktrugh start -> cuarto -> call -> end scene
   
    # Initial dialog
    Sombra "Tranquilo..."   
    Sombra "...No te preucupes..."
    Sombra "Pronto acabará todo..."

    scene black with fade
    play movie "images/intro.webm" # k seconds
    
    # End initial dialog
    #$ renpy.pause(12.5, hard=True)   #para evitar que se siga jugando con el video puesto, lo quito para mas facil probar xd
    #stop movie
    #scene black with fade

    Sombra "...Pronto seras libre..."
    Sombra "...Pronto............"   

    scene black with fade
    show image "images/Bed1.png" 
    play music "audio/Track1.ogg" # Emotional music

    $ renpy.store.preferences.text_cps = 30

    # Initial dialog pholis scence
    Pholis "Otra vez el mismo sueño de siempre"
    Pholis "Que es lo que me querrá decir?"
    Pholis "Ha sido lo mismo por meses… o años?"
    Pholis "Siempre los mismos lugares y las mismas personas que alguna vez conocí"
    Pholis  "Pero por mas que le de vueltas, no logro sacarle algún significado"
    Pholis  "Para este punto ya ni sé si mis recuerdos son reales o de este sueño eterno…"
    Pholis   "..."
    Pholis   "Como sea, no vale la pena seguir pensando en ello"

    
    # Instructions for the player
    
    #"Pholis puede explorar su cuarto"
    #play music "audio/Track1.ogg"

    # First option menu
    #menu:
        #"Mirar alrededor del cuarto":
            #show image "images/Cuarto1.png" with dissolve # Change cuarto
            #Pholis "todo.. aqui.. se siente raro"
            #jump recibir_llamada
        
        #"Ir al baño":
            #show image "images/Bano.png" with dissolve
            #Pholis "..."
            #jump recibir_llamada
    
            
    # call interaction
    label recibir_llamada:
        show image "images/PC.png" with fade
        Pholis "Que estaba haciendo ayer?"
        stop music
        scene black with fade

        play movie "images/Reloj.webm" 
        # End initial dialog
        #$ renpy.pause(12.5, hard=True)   #para evitar que se siga jugando con el video puesto, lo quito para mas facil probar xd


        #stop movie
        #scene black with fade
        Pholis "..."
        show image "images/PC.png" with fade
        Pholis "Esto e-"
        scene anim1 

        play sound "audio/Ring.mp3" loop
        

        Pholis "What is that sound?"
        
        play music "audio/Track2.mp3"
        Pholis "mi... celular?"
        Pholis "Hacia rato que no lo escuchaba sonar" 
   
        menu:
            "Contestar llamada":
                stop sound
                Pholis "..."
                Sombra "ahshejeldle" # Sound effect, error with ***
                #TODO Sound effect strange dialog
                jump fin_escena
            
            "Ignorar":
                
                Pholis "... ... ..."
                stop sound
                jump fin_escena

        label fin_escena:
            Pholis "Volvere a mi cama rapido"
            "Debug purpose end scene 2"
            jump escena_2

    label escena_2:
        # Only history no player interaction 
        scene black_screen with fade
        "6 6 6"
        show image "images/Habitacion.png"
        play music "audio/Track1.ogg"


        #TODO Change scene to pc search 
        "Pholis se encuentra buscando algo por internet"
        Pholis "Aggggg.. ahora no lo encuentro"
        #TODO Sound effect of a subtle voice
        #TODO Scene of dialog of shawdow in his left/right

        Pholis "Ehh??"
        Sombra "Pholis const3ta, ayu..."
        #TODO Animation of pholis shutdown his pc in a slam
        "Pholis atemorizado decidio volver a su cama"
        #TODO Scene of fade of the screen and broken clock with some subtle noise of distorsion
        stop music
        "Debug purpose end scene 2"
        $ renpy.save("prologue") # Save game for avoiding lose information


   

    label capitulo_1:

        # Introduction to chapter 1
        scene black with dissolve  
        centered_text "{size=+20}{font=fonts/horror_font_2.ttf}{b}CAPITULO 1: El descenso{/b}{/font}"

        label escena_1_cap1:
            "Pholis abre los ojos atemorizado por lo de la vez anterior"
            show image "images/Habitacion.png"
            Pholis "¿Acaso debo salir para ver si esto me pasa??"
            menu:
                "Salir de la habitacion":
                    jump habitacion_fuera

                "Quedarse adentro":
                    jump se_queda_adentro

            label habitacion_fuera:
                show image "<ciudad>" with fade 
                Pholis "{i}No recuerdo que el ayer fuese tan distinto al hoy{/i}"
                #Background music of horror and lonelines
                jump escnea_2_cap1



            label se_queda_adentro:
                Pholis "{i}a para que salir … mejor me quedo aca … como siempre he estado{/i}"
                # TODO Update de image of the room as the dialog says
                ". . ."
                #TODO update 2 of room 

                menu:
                    "Salir de la habitacion":
                        jump habitacion_fuera

                    "Quedarse":
                        jump suicide_ending

                label suicide_ending:
                    Pholis "{i}Necesito-o{/i}"
                    #TODO Fade the room image 
                    scene black with fade
                    centered_text "{size=+10}{font=fonts/horror_font_2.ttf}{b}No hay escapatoria{/b}{/font}"

                    show text "Logro desbloqueado: Worst Ending suicide " 
                    pause(3)
                    #TODO Show suicide image 
                    $ renpy.load("prologue")



    return
