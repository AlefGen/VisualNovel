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


#Firts cap Prologue
label start:

    $ text_speed = 15

    # Scence worktrugh start -> cuarto -> call -> end scene
    queue sound  "audio/texto.mp3" 
    
    # Initial dialog
    Sombra "Tranquilo..."
    
    stop sound
    queue sound  "audio/texto.mp3"
    
    Sombra "...No te preucupes..."
    stop sound

    queue sound  "audio/texto.mp3"
    
    Sombra "Pronto acabará todo..."
    stop sound

    play movie "images/intro.webm" # k seconds
    # End initial dialog

    Sombra "...Pronto seras libre..."
    Sombra "...Pronto............"   
    

    scene cuarto with fade 
    show image "images/Habitacion.png" # Wake up Pholis
    play music "audio/Track1.ogg" # Emotional music
    
     
    # Initial dialog pholis scence
    Pholis "Hoy será otro día más..."
    # Instructions for the player
    "Pholis puede explorar su cuarto"
    # First option menu
    menu:
        "Mirar alrededor del cuarto":
            show image "images/Cuarto1.png" with dissolve # Change cuarto
            Pholis "todo.. aqui.. se siente raro"
            jump recibir_llamada
        
        "Ir al baño":
            show image "images/Bano.png" with dissolve
            Pholis "..."
            jump recibir_llamada
            
    # call interaction
    label recibir_llamada:
        #TODO Modify this line to ring phone play music audio/ring
        Pholis "quien sera hace mucho no me llaman"

        menu:
            "Contestar llamada":
                Pholis "..."
                Sombra "ahshejeldle" # Sound effect, error with ***
                #TODO Sound effect strange dialog
                jump fin_escena
            
            "No contestar":
                Pholis "... ... ..."
                jump fin_escena

        label fin_escena:
            Pholis "Volvere a mi cama rapido"
            "Debug purpose end scene 2"
            jump escena_2

    label escena_2:
        # Only history no player interaction 
        scene black_screen with fade
        "6 6 6"
        scene cuarto with fade #TODO FIX CUARTO XD
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
