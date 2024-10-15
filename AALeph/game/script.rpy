# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Pholis = Character("Pholis", Color = "blue")
define Sombra = Character("Unknow", Color = "grey")

# Define images

define cuarto = "cuarto.png"
define puerta_sobra = "puerta"


#Firts cap Prologue
label start:

    # Scence worktrugh start -> cuarto -> call -> end scene

    scene cuarto with fade 
    
    # Initial dialog
    Pholis "Hoy será otro día más..."
    # Instructions for the player
    "Pholis puede explorar su cuarto"
    # First option menu
    menu:
        "Mirar alrededor del cuarto":
            # Function to change of scene would be here
            Pholis "todo.. aqui.. se siente raro"
            jump recibir_llamada
        
        "Ir al baño":
            jump recibir_llamada
    # call interaction
    label recibir_llamada:
        show puerta_sobra with dissolve
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
