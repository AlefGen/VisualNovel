# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Pholis = Character("Pholis", Color = "blue")
define Sombra = Character("???", Color = "grey")

# Define images

define cuarto = "Habitacion.png"
define puerta_sobra = "puerta"



#Firts cap Prologue
label start:

    $ text_speed = 15

    # Scence worktrugh start -> cuarto -> call -> end scene
    queue sound  "audio/texto.mp3"
    
    Sombra "Tranquilo..."
    stop sound
    queue sound  "audio/texto.mp3"
    
    Sombra "...No te preucupes..."
    stop sound

    queue sound  "audio/texto.mp3"
    
    Sombra "Pronto acabará todo..."
    stop sound

    

    play movie "images/intro.webm"

    Sombra "...Pronto seras libre..."
    Sombra "...Pronto............"



    
    
    
   
    

    scene cuarto with fade 
    show image "images/Habitacion.png"

    play music "audio/Track1.ogg"
    
     
    # Initial dialog
    Pholis "Hoy será otro día más..."
    # Instructions for the player
    "Pholis puede explorar su cuarto"
    # First option menu
    menu:
        "Mirar alrededor del cuarto":
            show image "images/Cuarto1.png" with dissolve
            # Function to change of scene would be here
            Pholis "todo.. aqui.. se siente raro"
            jump recibir_llamada
        
        "Ir al baño":
            jump recibir_llamada
    # call interaction
    label recibir_llamada:
        show image "images/Bano.png" with dissolve
        Pholis "quien sera hace mucho no me llaman"

        menu:
            "Contestar llamada":
                Pholis "..."
                Sombra "characters" # Sound effect, error with ***
                jump fin_escena
            
            "No contestar":
                Pholis "... ... ..."
                jump fin_escena

        label fin_escena:
            Pholis "fin de escena"



    return
