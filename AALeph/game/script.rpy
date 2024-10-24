# ========== Main game script ==========
"""
Version 0.0.5
@Author: AALeph
@Date: 2024
@Description: This is the main script of the game, here is where the game starts,

"""


# ========== Character declaration ==========
define Pholis = Character("Pholis", Color = "red")
define Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf")

# ========== Image declaration ==========
define cuarto = "images/prologo/prologo_cuarto_pholis.png"
define black_screen = "aux_images/black_screen.png"


# ========== Aux Functions ==========
define centered_text = Character(what_size=40, what_color="#FFFFFF", what_align=(0.5,0.5)) 
image anim1 = Movie(play = "animations/prologo/prologo_animacion_1.webm")

# ========== Efecto asi bien blureado==========
define hpunch = hpunch

transform blurred:
    linear 0.75 blur 10
transform unblur:
    linear 1 blur 0
# ========== Python Aux Functions ==========
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

    Pholis = Character("Pholis", callback=callback_Pholis, Color = "Red")
    Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf",callback=callback_Sombra)



# ========== Game pre-configuration ==========    
$ renpy.music.set_volume() # Ajust general vol of the game WIP
    
# ========== Game start ==========
"""
This is the main script of the game, here is where the game starts,
its important that the init name is start or the game would fail.
"""

label start:
    #jump recibir_llamada
    
    stop music
    $ renpy.store.preferences.text_cps = 10
    
    Sombra "Tranquilo..."   
    Sombra "...No te preocupes..."
    Sombra "...Todo acabara pronto..."

    scene black with fade
    play movie "videos/prologo/prologo_primera_escena_intro.webm" 
    
    # End initial dialog
    #$ renpy.pause(12.5, hard=True)   #para evitar que se siga jugando con el video puesto, lo quito para mas facil probar xd
    #stop movie
    #scene black with fade

    Sombra "...Pronto seras libre..."
    Sombra "Pronto......"   

    scene black with fade
    show image "images/prologo/prologo_cuarto_pholis.png" 
    play music "audio/Track1.mp3" 

    $ renpy.store.preferences.text_cps = 30

    
    Pholis "El mismo sueños otra vez, como siempre..."
    Pholis "¿Qué es lo que me querrá decir?"
    Pholis "Ha sido lo mismo por... ¿meses o años?"
    Pholis "Siempre los mismos lugares y las mismas personas que alguna vez conocí."
    Pholis "Pero por más que le dé vueltas, no logro sacarle algún significado."
    Pholis "A este punto ya ni sé si mis recuerdos son reales o parte de este sueño eterno…"
    menu:
        "Seguir pensando":
            show image "images/prologo/prologo_ojo.png" with dissolve
            Pholis "Es como si algo me estuviera observando."
            show image "images/prologo/prologo_manos.png" with fade
            Pholis "Sin embargo, no siento miedo..."
            Pholis "Tal vez no necesariamente quiere hacerme daño."
            Pholis "¿Pero entonces qué será?"
            Pholis "..."
            Pholis "Bueno, no puedo durar todo el día en esto."
            jump recibir_llamada

        "No vale la pena":
            Pholis "..."
            Pholis "Como sea, no vale la pena seguir pensando en ello."
            jump recibir_llamada

            
    # call interaction
    label recibir_llamada:
        show image "images/prologo/prologo_techo_pholis.png" with fade
        Pholis "¿Que estaba haciendo ayer?"
        stop music
        scene black with fade

        play movie "videos/prologo/prologo_reloj_moviendo.webm" 

        # End initial dialog
        #$ renpy.pause(12.5, hard=True)   #para evitar que se siga jugando con el video puesto, lo quito para mas facil probar xd


        #stop movie
        #scene black with fade
        Pholis "..."
        show image "images/prologo/prologo_techo_pholis.png" with fade
        Pholis "Esto e-"
        scene anim1 at blurred  # arreglar image not found xd #FIXME

        play sound "audio/Ring.mp3" loop
        

        Pholis "Que ha sido ese sonido?"
       
        play music "audio/Track2v2.wav"
        Pholis "mi... ¿celular?"
        scene anim1 at unblur with dissolve
        Pholis "Hacia rato que no lo escuchaba sonar" 
   
        menu:
            "Contestar llamada":

                # subir velocidad de texto para sombra
                stop sound
                Pholis "..."
                with hpunch
                Sombra "⌦⌰ℇ☊o̴̡̧̧͍̞̘͖̬̮̟̣͖̠̟̠̮̮̫ͫͨͮ̓͑ͭ́ͧ̀ͭ̐͆̉ͧ̈͛̂ͮ̆̀̈̍ͤ͟͜͜͜͝l͓̗̕ͅ⎎ ☊ê̶̶̳̗̹̈́͐͂ͣ͘s̯̼̦̘̥̙̗̣̠ͧͫ̉ͦͫ̎͛ͯ̌̇̋̿̽̽͌ͪ̏̈́̿ͪ̿̏̈́͘͘͢͢͝ͅℇ⎎, ⎎ℇ ℇ t̸̨̨̢̥͚͚̪̻̭̖̤̤͉̅̉͂ͯ̀̂͒͂͛̑̾̂̃͑̋̆ͮ̃͑ͯ̔ͮ͐̓̿͐̉ͮͩ͢͜͠⍧⌰ℇ o̴̡̧̧͍̞̘͖̬̮̟̣͖̠̟̠̮̮̫ͫͨͮ̓͑ͭ́ͧ̀ͭ̐͆̉ͧ̈͛̂ͮ̆̀̈̍ͤ͟͜͜͜͝l͓̗̕ͅ⍑☈⍲P̴̸̡̗̲͊̿h̷̶̴̶̢̬̻̹̻̬͉̼̮̼͚͖̫̪̥̠̝͕̳͖ͨͬ͗ͣͩ̆̅͐̂ͤ͒ͬͩ̓̈́̿̆̋̎͢͠o̴̡̧̧͍̞̘͖̬̮̟̣͖̠̟̠̮̮̫ͫͨͮ̓͑ͭ́ͧ̀ͭ̐͆̉ͧ̈͛̂ͮ̆̀̈̍ͤ͟͜͜͜͝l͓̗̕ͅį̸̨̧͖͙̹͇͔̤̖̻͈̳͔̹̘̹͎̙ͫ͗̈͗̋̽͋ͨ̔̍̌̾ͥ́̉̕̚͟͠͠ͅs͖̙̞̤ͭ̈́́́?" # Sound effect, error with ***
                Pholis "¿Di-Disculpe?"
                with hpunch

                Sombra "Pho̴̡̧̧͍̞̘͖̬̮̟̣͖̠̟̠̮̮̫ͫͨͮ̓͑ͭ́ͧ̀ͭ̐͆̉ͧ̈͛̂ͮ̆̀̈̍ͤ͟͜͜͜͝l͓̗̕ͅį̸̨̧͖͙̹͇͔̤̖̻͈̳͔̹̘̹͎̙ͫ͗̈͗̋̽͋ͨ̔̍̌̾ͥ́̉̕̚͟͠͠ͅs_͌ E̴̵͍̦̝͕̖̭̩̬̙ͫ͋͌̊́̅̎̋̿̅̉̅ͮ̊̓͟͝͡ŗ̻̩̣͖͎̱̘̙̲̪ͮ̔ͣ̾̌̈̑ͧ̔̓͘͠ê̶̶̳̗̹̈́͐͂ͣ͘s̯̼̦̘̥̙̗̣̠ͧͫ̉ͦͫ̎͛ͯ̌̇̋̿̽̽͌ͪ̏̈́̿ͪ̿̏̈́͘͘͢͢͝ͅ t̸̨̨̢̥͚͚̪̻̭̖̤̤͉̅̉͂ͯ̀̂͒͂͛̑̾̂̃͑̋̆ͮ̃͑ͯ̔ͮ͐̓̿͐̉ͮͩ͢͜͠ṹ̸̢͓͖̜̻̠̼͔̋̐ͤͣ̓ͫ̀ͭ͗̚͜͡?̶̴͍̤͇͇̓͌͑̄͑ͤ͋͑͗̀̕͠͠?"


                Pholis "¿Quien me esta hablando? ¿Sabe quien soy?"

                        
                menu:
                    "Seguir":
                        Pholis "¿Qu- Quien habla?"


                        Sombra "No m̡̬̬̼̺̂̔́͞e͉͕͓̬̫̠͓̬͕͚̖̼̼̟̎ͣ̀̀̐̋́ͧ̃̓ͩ̃ͫͪ̋̿̏̽ͧͬ ȓ͞ȩ̶̪̞͕̰̺̥̺͇̳͇̀̂̽̉̉͌̊͊̐̽ͨ̐ͭͧͥ͌ͦ̆̀ͨ̕͜͝͞cuṵ̶̦̤̬̮̼̹̙͙͕̲̎ͮ̽̎̐̿ͨ̒̂ͨ̎̂̽̆͑̀ͤͬͦ̚͜͜͡ḛ̶̵̢̮͚̪̞̞͖͉̪͓̰͕̭̮̞͖̟̥̅̀͊̇̀̆͗͆́ͤ́̓̍̿̚͝ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅd̏̈́̅das_̺͙̘͂̽̇̍ͨ̍͐͋? ⎎⌾⍦Ma ⍦t"

                        Pholis "¿?"

                        Sombra "Q҉u҉e҉ t҉a҉l҉ ҉,҉ c҉o҉m҉o҉ h҉a҉s҉ e҉s҉t҉a҉d҉o҉"

                        Sombra "¿Cuánto ha ḛ̶̵̢̮͚̪̞̞͖͉̪͓̰͕̭̮̞͖̟̥̅̀͊̇̀̆͗͆́ͤ́̓̍̿̚͝ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅḑ̢̣͔̤͍̠̯̏̈́̅̒̇͛̍̏͑_̊ã̸̳̮͖͠s̶̛̭̎͐̑͟_̺͙̘͂̽̇̍ͨ̍͐͋, como 4 años no? ¿Como ȓ͞ȩ̶̪̞͕̰̺̥̺͇̳͇̀̂̽̉̉͌̊͊̐̽ͨ̐ͭͧͥ͌ͦ̆̀ͨ̕͜͝͞cu ȓ͞ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅu todo?"

                        Pholis "(¿Porque me cuesta tanto entenderlo?, siempre me pasa lo mismo...)"

                        Pholis "(¿Estoy seguro de que esto siquiera es real? Será otro de esos sueños?"

                        #imagen sombra

                        Sombra "Es҉҉ás a҉҉í"



                        # imagen recuerdo matt silueta brillan
                        

                        
                        #imagen alucinacion 
                    "Colgar":
                        jump fin_escena

                        
                #TODO Sound effect strange dialog
                
            
            "Ignorar":
                
                Pholis "... No debe ser importante ..."
                stop sound
                jump fin_escena

        label fin_escena:
            Pholis "Volvere a mi cama rapido"
            "Debug purpose end scene 2"
            jump escena_2

    label escena_2:
        # Only history no player interaction 
        scene black_screen with fade # FIXME
        "6 6 6"
        show image "images/prologo/prologo_cama_pholis.png"
        play music "audio/Track1.mp3"


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
