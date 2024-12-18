﻿# ========== Main game script ==========
"""
Version 0.0.5
@Author: AALeph
@Date: 2024
@Description: This is the main script of the game, here is where the game starts,

"""


# ========== Character declaration ==========
define Pholis = Character("Pholis", Color = "red")
define Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf")
define notificacion_pc = Character("Notificacion", Color = "black", what_font = "fonts/PoiretOne-Regular.ttf")
define notificacion_celular = Character("Celular", Color = "black", what_font = "fonts/PoiretOne-Regular.ttf")


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

    def callback_notificacion_pc(event, **kwargs):
        if event == "show":
            renpy.music.play("Ring.mp3", channel=6)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel= 6)
        

    Pholis = Character("Pholis", callback=callback_Pholis, Color = "Red")
    Sombra = Character("???", Color = "grey", what_font = "fonts/horror_font_2.ttf",callback=callback_Sombra)
    notificacion_pc = Character("Notificacion", Color = "black", what_font = "fonts/PoiretOne-Regular.ttf", callback=callback_notificacion_pc)
    notificacion_celular = Character("Celular", Color = "black", what_font = "fonts/PoiretOne-Regular.ttf", callback=callback_notificacion_pc)



init python:
    # ========== Variables ==========

    locura = 0
    muertes = 0
    conexion_con_sombra = 0
    crash_game = 0



# ========== Game pre-configuration ==========    
$ renpy.music.set_volume() # Ajust general vol of the game WIP
    
# ========== Game start ==========
"""
This is the main script of the game, here is where the game starts,
its important that the init name is start or the game would fail.
"""

label start:
    #jump recibir_llamada
    #jump capitulo_1     
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
            $ locura += 1
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
                $ conexion_con_sombra += 1

                # subir velocidad de texto para sombra
                stop sound
                Pholis "..."
                with hpunch
                # $ renpy.store.preferences.text_cps = 50

                # Tutorial de como hacer dialogos raros, 1. Hacer el texto original 2. Pomer {font=fonts/zalgo.ttf} al principio y {/font} al final del texto
                Sombra "{font=fonts/zalgo.ttf}Pholis estoy aquí{/font}" # Sound effect, error with ***
                Pholis "¿Di-Disculpe?"
                with hpunch

                Sombra "Pho̴̡̧̧͍̞̘͖̬̮̟̣͖̠̟̠̮̮̫ͫͨͮ̓͑ͭ́ͧ̀ͭ̐͆̉ͧ̈͛̂ͮ̆̀̈̍ͤ͟͜͜͜͝l͓̗̕ͅį̸̨̧͖͙̹͇͔̤̖̻͈̳͔̹̘̹͎̙ͫ͗̈͗̋̽͋ͨ̔̍̌̾ͥ́̉̕̚͟͠͠ͅs_͌ E̴̵͍̦̝͕̖̭̩̬̙ͫ͋͌̊́̅̎̋̿̅̉̅ͮ̊̓͟͝͡ŗ̻̩̣͖͎̱̘̙̲̪ͮ̔ͣ̾̌̈̑ͧ̔̓͘͠ê̶̶̳̗̹̈́͐͂ͣ͘s̯̼̦̘̥̙̗̣̠ͧͫ̉ͦͫ̎͛ͯ̌̇̋̿̽̽͌ͪ̏̈́̿ͪ̿̏̈́͘͘͢͢͝ͅ t̸̨̨̢̥͚͚̪̻̭̖̤̤͉̅̉͂ͯ̀̂͒͂͛̑̾̂̃͑̋̆ͮ̃͑ͯ̔ͮ͐̓̿͐̉ͮͩ͢͜͠ṹ̸̢͓͖̜̻̠̼͔̋̐ͤͣ̓ͫ̀ͭ͗̚͜͡?̶̴͍̤͇͇̓͌͑̄͑ͤ͋͑͗̀̕͠͠?"


                Pholis "¿Quien me esta hablando? ¿Sabe quien soy?"

                        
                menu:
                    "Seguir":

                        $ conexion_con_sombra += 1

                        Pholis "¿Qu- Quien habla?"


                        Sombra "No m̡̬̬̼̺̂̔́͞e͉͕͓̬̫̠͓̬͕͚̖̼̼̟̎ͣ̀̀̐̋́ͧ̃̓ͩ̃ͫͪ̋̿̏̽ͧͬ ȓ͞ȩ̶̪̞͕̰̺̥̺͇̳͇̀̂̽̉̉͌̊͊̐̽ͨ̐ͭͧͥ͌ͦ̆̀ͨ̕͜͝͞cuṵ̶̦̤̬̮̼̹̙͙͕̲̎ͮ̽̎̐̿ͨ̒̂ͨ̎̂̽̆͑̀ͤͬͦ̚͜͜͡ḛ̶̵̢̮͚̪̞̞͖͉̪͓̰͕̭̮̞͖̟̥̅̀͊̇̀̆͗͆́ͤ́̓̍̿̚͝ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅd̏̈́̅das_̺͙̘͂̽̇̍ͨ̍͐͋? ⎎⌾⍦Ma ⍦"

                        Pholis "¿?"

                        Sombra "Q҉u҉e҉ t҉a҉l҉ ҉,҉ c҉o҉ e҉s҉t҉ao҉"

                        Sombra "¿Cuánto ha ḛ̶̵̢̮͚̪̞̞͖͉̪͓̰͕̭̮̞͖̟̥̅̀͊̇̀̆͗͆́ͤ́̓̍̿̚͝ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅḑ̢̣͔̤͍̠̯̏̈́̅̒̇͛̍̏͑_̊ã̸̳̮͖͠s̶̛̭̎͐̑͟_̺͙̘͂̽̇̍ͨ̍͐͋,  4 ¿Como ȓ͞ȩ̶̪̞͕̰̺̥̺͇̳͇̀̂̽̉̉͌̊͊̐̽ͨ̐ͭͧͥ͌ͦ̆̀ͨ̕͜͝͞cu ȓ͞ṟ̶̵̘̲̠̜̜͚̥̱ͥ͌́͛ͣ̉̌͒̋̏̄̈́ͫ͠ͅu todo?"

                        Pholis "(¿Porque me cuesta tanto entenderlo?, siempre me pasa lo mismo...)"

                        Pholis "(¿Estoy seguro de que esto siquiera es real? Será otro de esos sueños?"

                        #imagen sombra

                        Sombra "Es҉҉í"

                        #sonido de colgar click bup



                       
                        

                        
                        #imagen alucinacion 
                        Pholis "..."
                    "Colgar":
                        jump fin_escena

                        
                #TODO Sound effect strange dialog
                
            
            "Ignorar":
                
                Pholis "... No debe ser importante ..."
                stop sound
                jump capitulo_1

        label fin_escena:
            #se detiene el sonido de latido + sonido de respirar como calmado??
            Pholis "¿Por qué?"
            Pholis "¿Cuando acabara todo esto?"
            Pholis "..."
            Pholis "Volvere a lo mio, debo tranquilizarme."


           
            
            
            stop music
            jump capitulo_1

    label capitulo_1:
        stop music
        scene black with dissolve  
        centered_text "{size=+20}{font=fonts/horror_font_2.ttf}{b}CAPITULO 1: El descenso{/b}{/font}" # nose si deberiamos poner capitulos porque yo creo que va a ser muy corto
        # Only history no player interaction 
        play movie "videos/Capitulo1/sueno1.webm"
        show image "aux_images/black_screen.png" with dissolve
        with hpunch
        "Pholis, despierta"
        Pholis "¿E-eh que fue eso?"
        with hpunch
        "Pholis, te dije que despiertes"
        #Pholis "¿Quien eres?"
        #with hpunch
        #"Tu me conoces bien..."
        Pholis "..."
        show image "images/prologo/prologo_cuarto_pholis.png"
        play music "audio/Track1.mp3"
        Pholis "Otra vez lo mismo..."
        Pholis "Aunque esta vez, habia algo mas estoy seguro"
        show image "images/Capitulo1/afuera.png" with dissolve
        Pholis "No recuerdo bien pero, era... ¿afuera?"
        # va al baño, se ve solo la silueta de pholis en el espejo - piensa acerca de "Cuando dejara de perseguirme" - no le da importancia



        #pholis se pone a pensar sobre eso ultimo "Cuanto tiempo ya llevo aqui?" y mas nose
        Pholis "¿Cuanto tiempo ya llevo aqui?"
        Pholis "Misma rutina, mismos sentimientos..."
        Pholis "Cada dia el mismo que el anterior."
        Pholis "¿Por cuanto tiempo mas?"
        Pholis "Aunque, debo de..."


        
        # Sonido de notificacion #TODO al igual que para cada una de las notificaciones 
        #FIXME tambien puede ser un sonido de ventana con un mensaje asi como nota

        # #FIXME Dionyss llega a la casa, en lugar de invitar afuera (Pholis aun no esta preparado para salir por su cuenta)
    
        #notificacion_pc "Tienes un mensaje" with hpunch
        #sonido de tocar puerta, en lugar de celular 
        #se escucha una voz familiar afuera llamando a pholis "ey pholis " 
        
        #deja una nota en la puerta - no se entiende nada mas que un "quieres salir"
        Pholis "¿Que ha sido eso?"
        show image "images/prologo/prologo_techo_pholis.png" with dissolve
        notificacion_pc "Dionyss: Hola Pholis, ¿como has estado?"
        Pholis "¿Dionyss?, quien es ese?"
        notificacion_pc "Dionyss: Mira que voy a pasar unos diás por tu ciudad, ¿quieres que nos veamos?"
        Pholis "¿De que habla?, no lo recuerdo"
        stop music
        "TODO NOT FINISHED"
        #knock knock puerta

        #luego de mensaje - nota

        Pholis "Sa-¿salir?"
        Pholis "Cuando fue la ultima vez que..."

        #Imagenes de afuera asi bien distorisionadas crazy 
        Pholis "Como sea, no es mas que una broma ¿no es asi?"
        Pholis "no es como que alguien me conozca... "
        #mira por la ventana 
        Pholis "..." #latido tactico xkibidi
        Pholis "¿Quien es ese?"
        Pholis "¿Es el quien estaba tocando?"
        Pholis "N-no...es... imposible... "
        #desaparece
        Pholis "..."
        Pholis "S-se abra equivocado de casa..."
        Pholis "..." #se relaja mi pana
        Pholis "En fin, volvere a lo mio"
        #otra animacion de pasar tiempo??
        $ renpy.save("prologue") # Save game for avoiding lose information


   

    label capitulo_2:

        # Introduction to chapter 1
        scene black with dissolve  
        centered_text "{size=+20}{font=fonts/horror_font_2.ttf}{b}CAPITULO 2: El Visitante {/b}{/font}"
        #TODO Dionyss llega a la casa 

        label escena_1_cap1:
            #Efecto de abrir los ojos con desenfoque - palabras en la pantalla al despsertar que desaparecen rapidamente - algun mensaje
            #Pholis "El de ayer quien habra sido Dionyss, no me suena de nada"
            #track 3
            
            show image "images/prologo/prologo_cuarto_2_pholis.png"
            Pholis "..."
            Pholis "No dejo de sentirme observado."
            Pholis "Cada dia se intensifica mas esta horrible sensacion"
            Pholis "Y la nota de ayer, ¿Por que?"
            Pholis "¿Nunca me dejara en paz?"
            Pholis "..."
            
            Pholis "debo tranquilizarme."
            Pholis "Seguire con lo de siempre."
            #Cambio a imagen de pc
            show image "images/prologo/prologo_cuarto_pholis.png"
            
            Pholis "..."
            Pholis "..."
            Pholis "Pronto..."
            Pholis "Todo aca-"

            #sonido de puerta sonando track 2 + latido

            Pholis "¿O-Otra vez?"
            Pholis "¿Esque nunca se cansa?"
            Pholis "¿Por que? pense que..."
            #mas instensificado el knock knock 
            Pholis "..."
            #
            Pholis "No parece que se vaya a detener pronto"
            Pholis "¿Que deberia hacer?"
            menu:
                "Abrir":
                    Pholis "¿Estoy... seguro de esto?"
                    Pholis "No creo que..."
                    #tocar puerta mas duro
                    Pholis "No, Debo hacerlo, el me entendera..."
                    jump habitacion_fuera

                "Ignorar":
                    Pholis "No, no no... aun no"
                    #toca de puerta mas duro + gritos
                    #imagen de pholis asi de bolita xdd bien crazy esperando a que acabe 
                    Pholis "Perdon..."
                    jump se_queda_adentro

            #Dionyss llega a la casa 
            #opcion de abrir o ignorar

            #abrir tendra animacion
            #ignorar solo pasara el dia 

            #FIXME Pholis aun no esta preparado para salir solo 
            #Pholis "Estoy pensado si salir un rato afuera, hoy me siento con la mente extraña"
            
         


            label se_queda_adentro:
                Pholis "{i}Mejor me quedo aca … como siempre he estado...{/i}"
                # TODO Update de image of the room as the dialog says
                ". . ."
                #TODO update 2 of room 

               

                
                    


                label suicide_ending:
                    #efecto abrir ojos - se ve sombra

                    Pholis "{i}¡NO! Alejate de mi{/i}"
                    Pholis "Ya me canse de esto"
                    Pholis "Dejame en paz!"
                    #se acerca la sombra
                    Pholis "Deja de mirarme"
                    Pholis "Lo que sucedio fue... FUE TU CULPA!"
                
                    #animacion de Pholis coje un cuchillo
                    #TODO creashea el juego xddd
                    # a sus ordenes
                    $ renpy.quit(relaunch=True)

                    #TODO Fade the room image 
                    scene black with fade
                    centered_text "{size=+10}{font=fonts/horror_font_2.ttf}{b}No hay escapatoria{/b}{/font}"

                    show text "Logro desbloqueado: Worst Ending suicide " 
                    pause(3)
                    #TODO Show suicide image 
                    $ renpy.load("prologue")

            label habitacion_fuera:
                #animacion abrir puertta - la historia esta guida por las voces y recuerdos de dionyss
                #pholis sigue a esas voces que lo llevan hasta el lugar del accidente
                show image "images/Capitulo1/capitulo1_ciudad_1.png" with fade 
                Pholis "{i}No recuerdo que el ayer fuese tan distinto al hoy{/i}"
                Pholis "Veo como personas, pero fragmentadas en colores"
                notificacion_celular "Dionyss: Pholis, Hola, como te comentaba ayer"
                notificacion_celular "Dionyss: Podemos vernos en la cafeteria de la esquina de tu casa"
                notificacion_celular "Dionyss: Estare ahi sobre las 4 de la tarde, te espero."
                Pholis "E-h-h otra vez él ¿sera que le hago caso?"
                "Pholis, quedate con nostros"
                "Tu sabes quienes son tus verdaderos amigos"

                play music "audio/menu-music.mp3"
                #Background music of horror and lonelines
                jump escena_2_cap1

        label escena_2_cap1:
            menu: 
                "Encontrarse en el cafe con Dionyss":
                    #TODO Mostrar imagenes de la calle
                    Pholis "Este mundo esta tan cambiando qué habra pasado"
                    #IMAGE
                    Pholis "Las calles estan distorsionadas"
                    # IDEA NO FINAL
                    Sombra "Pholis, me escuchas" #Distorsionar letras pero que se entienda pls
                    Pholis "E-h-h quien eres?"
                    #IMAGE
                    Sombra "Eso no importa, he venido a salvarte" #FIXME no tan explicito 
                    Pholis "de quien??"
                    #IMAGE 
                    Sombra "De tí, no los escuches, no les hagas caso, hazle caso a tu corazon." #FIXME no tan explicito
                    Pholis "Ok (Confundido)?"
                    #IMAGE
                    Pholis "Bueno no importa, en que estaba. ¡Ah sí! Dionyss"
                "No ir":
                    Pholis "Mejor no voy, quiero estar en mi zona"
                    with hpunch
                    "Muy bien Pholis"
                    $ locura += 3
                    









    return
