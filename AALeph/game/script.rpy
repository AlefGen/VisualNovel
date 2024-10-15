# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define VieraT = Character("Viera", Color = "red")


# The game starts here.

label start:
    image Fondo = "Flow.png"
    scene Fondo


    "El inicio de una gran historia "

    image Viera = "Aloe Veraa.png"
    show Viera at Position(xalign=0.1, yalign=0.5)
    with fade

    VieraT "Hola Amigos Soy Viera"
    VieraT "Este esta es mi historia "

    VieraT "Todo Empezo el otro dia"

    hide Viera
    with dissolve




    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
