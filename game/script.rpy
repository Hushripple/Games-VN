# Declaración de personajes e imágenes

# anzu
define a = Character("Anzu")
image anzu neutral = "images/Custom/Anzu.png"
image anzu smile = "images/Custom/Anzu_Smile.png"
image anzu sad = "images/Custom/Anzu_Sad.png"
image anzu decided = "images/Custom/Anzu_Decided.png" 
image anzu surprised = "images/Custom/Anzu_Surprised.png"

# profe aiko
define pAiko = Character("Profesora Aiko")
image aiko neutral = "images/Custom/Aiko.png"
image aiko smile = "images/Custom/Aiko_Smile.png"
image aiko joy = "images/Custom/Aiko_Joy.png"
image aiko ex = "images/Custom/Aiko_Ex.png"

# alumno random
define aRandom = Character("Alumno #1")

# ???
define desconocido = Character("???")

# daika
define daika = Character("Daika")
image daika neutral = "images/Custom/Daika.png"
image daika smile = "images/Custom/Daika_Smile.png"
image daika sad = "images/Custom/Daika_Sad.png"
image daika surprised = "images/Custom/Daika_Surprised.png"

# gina
define gina = Character("Gina")
image gina neutral = "images/Custom/Gina.png"
image gina smile = "images/Custom/Gina_Smile.png"
image gina sad = "images/Custom/Gina_Sad.png"
image gina surprised = "images/Custom/Gina_Surprised.png"

# yuu
define yuu = Character("Yuu")
image yuu neutral = "images/Custom/Yuu.png"

# images
image bg classroom = "classroom.png"
image bg school = "school.png"
image bg stairs = "stairs.png"
image bg citt = "citt.png"
image qr = "images/Custom/qr.png"

transform jump:
    linear 0.5 yoffset -70
    linear 0.5 yoffset 0

transform pose:
    zoom 1.5

default leyo_programacion = False
default leyo_arte = False
default leyo_guion = False
default leyo_musica = False


# El juego comienza aquí.

label start:

    play music "audio/cicadas.mp3" volume 0.1

    scene bg school with fade

    "{cps=30}{i}Lunes por la mañana, 8:25 A.M.{/i}{/cps}"
    "{cps=30}{i}En apenas cinco minutos comenzará tu tercera clase de Programación de Algoritmos, a cargo de la profesora Aiko.{/i}{/cps}"

    show anzu neutral at center, pose

    a "{cps=30}{i}(Estoy bastante emocionada.){/i}{/cps}"
    a "{cps=30}{i}(Hasta ahora, la programación en Python ha sido mucho más divertida e interesante de lo que imaginaba.){/i}{/cps}"

    show anzu smile at center, pose
    a "{cps=30}{i}(He estado explorando todo lo que puedo hacer con este lenguaje... ¡y las posibilidades son prácticamente infinitas!){/i}{/cps}"

    show anzu sad at center, pose
    a "{cps=30}{i}(Aunque, siendo honesta...){/i}{/cps}"
    a "{cps=30}{i}(Me deprime un poco que no haya nada relacionado con el desarrollo de videojuegos en el curso.){/i}{/cps}"
    a "{cps=30}{i}(Desde pequeña, he soñado con crear mis propios juegos... y ahora siento que ese sueño está un poco lejos.){/i}{/cps}"

    play sound "audio/bell.mp3" volume 0.1

    show anzu decided at center, pose
    a "{cps=30}{i}(Bueno, mejor me enfoco en el presente. La clase está a punto de comenzar.){/i}{/cps}"
    a "{cps=30}{i}(¡Estoy segura de que aprenderé algo nuevo e increíble hoy!){/i}{/cps}"

    stop sound 
    scene bg classroom with fade
    play music "audio/class.mp3" volume 0.1

    "{cps=30}{i}8:35 A.M. La campana ya ha sonado, y los estudiantes toman asiento mientras la profesora se prepara para comenzar.{/i}{/cps}"

    show aiko neutral at center, pose
    pAiko "{cps=30}Buenos días a todos.{/cps}"
    pAiko "{cps=30}Hoy aprenderemos sobre un concepto fundamental: las funciones en Python.{/cps}"
    pAiko "{cps=30}Las funciones nos permiten agrupar bloques de código para reutilizarlos fácilmente, haciéndolos más ordenados y potentes.{/cps}"

    hide aiko neutral with dissolve

    "{cps=30}{i}La clase fluye de manera natural, y Anzu escucha con genuino interés, tomando nota de cada explicación.{/i}{/cps}"

    "{cps=30}{i}...{/i}{/cps}"
    "{cps=30}{i}...{/i}{/cps}"
    "{cps=30}{i}...{/i}{/cps}"

    show aiko neutral at center, pose
    pAiko "{cps=30}Bien, eso sería todo por hoy en cuanto a funciones.{/cps}"
    pAiko "{cps=30}Antes de despedirnos, quiero hablarles de una oportunidad que podría interesarles.{/cps}"

    "{cps=30}{i}Anzu levanta ligeramente la vista, intrigada.{/i}{/cps}"

    pAiko "{cps=30}Me gustaría invitarlos a participar en el {i}CITT{/i}, nuestro Centro de Innovación y Transferencia Tecnológica.{/cps}"
    pAiko "{cps=30}Es un espacio donde estudiantes, docentes y empresas colaboran en proyectos reales, más allá del currículo académico.{/cps}"

    "{cps=30}{i}El interés de Anzu crece con cada palabra.{/i}{/cps}"

    pAiko "{cps=30}Dentro del CITT, los proyectos se dividen en {i}tracks{/i}, o áreas temáticas específicas.{/cps}"

    aRandom "{cps=30}Profesora, ¿qué tipos de tracks existen?{/cps}"

    show aiko joy at center, pose
    pAiko "{cps=30}Excelente pregunta.{/cps}"
    pAiko "{cps=30}Actualmente, tenemos tracks de ciberseguridad, robótica, desarrollo de videojuegos, entre otros.{/cps}"

    hide aiko neutral with dissolve
    show anzu surprised at jump, pose, center

    a "{cps=30}{i}(¿¡Track de desarrollo de videojuegos!?){/i}{/cps}"
    a "{cps=30}{i}(¡Esta podría ser mi oportunidad!){/i}{/cps}"

    hide anzu neutral with dissolve
    show aiko neutral at pose, center

    pAiko "{cps=30}Si alguno de ustedes está interesado, no duden en acercarse a mí o visitar directamente el CITT.{/cps}"
    pAiko "{cps=30}Pidan hablar con el capitán del track que más les llame la atención.{/cps}"
    show aiko smile at pose, center
    pAiko "{cps=30}¡Les deseo un excelente día a todos!{/cps}"

    hide aiko neutral with dissolve

    "{cps=30}{i}El murmullo en la sala crece mientras los estudiantes empacan sus cosas con entusiasmo.{/i}{/cps}"

    show anzu neutral at center, pose
    a "{cps=30}{i}(Bien, supongo que ahora debo encontrar a ese capitán...){/i}{/cps}"
    a "{cps=30}{i}(¿Dónde estará exactamente?){/i}{/cps}"
    show anzu decided at center, pose
    a "{cps=30}{i}(Bueno, no puedo quedarme aquí dudando para siempre.){/i}{/cps}"

    show anzu sad at center, pose
    a "{cps=30}{i}(Espero que todo salga bien...){/i}{/cps}"

    hide anzu sad with dissolve
    scene bg stairs with fade
    "{cps=30}{i}Con paso decidido pero el corazón acelerado, Anzu sube al segundo piso.{/i}{/cps}"
    "{cps=30}{i}Una mezcla de emoción y nerviosismo la invade.{/i}{/cps}"

    scene bg citt with fade
    show anzu neutral at center, pose

    a "{cps=30}{i}(Este debe ser el lugar...){/i}{/cps}"

    hide anzu neutral

    "{cps=30}{i}Centro de Innovación y Transferencia Tecnológica — CITT DUOC.{/i}{/cps}"

    show anzu neutral at center, pose
    a "{cps=30}{i}(Muy bien, es ahora o nunca.){/i}{/cps}"

    hide anzu neutral with dissolve
    play sound "audio/knock.mp3" volume 0.1
    "{cps=30}{i}*Toc, toc, toc*{/i}{/cps}"
    "{cps=30}{i}...{/i}{/cps}"
    "{cps=30}{i}...{/i}{/cps}"

    show daika neutral at left, pose
    desconocido "{cps=30}Buenas, ¿en qué puedo ayudarte?{/cps}"

    show anzu neutral at right, pose
    a "{cps=30}{i}(¡Esta debe ser la capitana del track!){/i}{/cps}"

    a "{cps=30}Hola, soy Anzu. Estaba interesada en saber más sobre el track de desarrollo de videojuegos.{/cps}"

    show daika smile at left, pose
    daika "{cps=30}¡Qué bueno escuchar eso! Soy Daika, pasa, te mostraré un poco cómo trabajamos.{/cps}"

    hide daika smile with dissolve
    hide anzu neutral with dissolve

    scene bg classroom with fade

    "{cps=30}{i}Anzu entra y observa el lugar...{/i}{/cps}"

    show anzu sad at right, pose 
    show daika neutral at left, pose
    a "{cps=30}{i}(¿Este es el CITT? Es más pequeño de lo que imaginaba...){/i}{/cps}"
    daika "{cps=30}¿Te sorprende el poco espacio?{/cps}"

    a "{cps=30}Un poco, sí...{/cps}"

    daika "{cps=30}Entiendo. Mira, en nuestro caso, no necesitamos mucho espacio físico.{/cps}"
    daika "{cps=30}A diferencia de otros tracks como robótica o IoT, nosotros trabajamos principalmente en digital.{/cps}"
    daika "{cps=30}Mucho de nuestro trabajo es de programación, diseño y coordinación que podemos hacer cómodamente desde casa usando Discord.{/cps}"
    daika "{cps=30}¡Así que el tamaño no limita nuestras posibilidades!{/cps}"

    show anzu smile at right, pose
    a "{cps=30}{i}(Eso tiene mucho sentido... y suena perfecto para mí.){/i}{/cps}"

    daika "{cps=30}Ven, te presentaré a algunos integrantes.{/cps}"

    hide anzu smile with dissolve
    hide daika neutral with dissolve

    show gina neutral at left, pose
    show yuu neutral at right, pose

    daika "{cps=30}Gina y Yuu, ellas son parte del equipo de desarrollo.{/cps}"

    show gina smile at left, pose
    gina "{cps=30}Mucho gusto.{/cps}"

    yuu "{cps=30}Ho-Hola...{/cps}"
    
    hide gina neutral with dissolve
    hide yuu neutral with dissolve
    show anzu smile at right, pose

    a "{cps=30}{i}¡Es un placer!{/cps}"

    show daika neutral at left, pose
    daika "{cps=30}Cada una de nosotras tiene su especialidad, su pasión dentro del desarrollo.{/cps}"
    daika "{cps=30}Por ejemplo, Gina se dedica principalmente al diseño y a la creación de sprites de personajes.{/cps}"
    daika "{cps=30}Mientras tanto, Yuu se encarga de programar la mayoría de las funciones del juego.{/cps}"
    show daika smile at left, pose
    daika "{cps=30}¡Es increíblemente talentosa programando! Es rápida, precisa e inventiva.{/cps}"
    show daika neutral at left, pose
    daika "{cps=30}Como ves, hay muchísimas áreas en las que puedes especializarte.{/cps}"
    daika "{cps=30}Y si quieres, también puedes combinar habilidades y participar en varias a la vez.{/cps}"
    daika "{cps=30}Lo más importante es que trabajemos juntas como equipo, y que cada una de nosotras aprenda y crezca en el proceso.{/cps}"
    daika "{cps=30}Así que dime... {/cps}"
    daika "{cps=30}¿Qué área del desarrollo de videojuegos te interesa más?{/cps}"
    show anzu neutral at right, pose

    $ opcion = []

    menu opcionMenu:
        set opcion
        "Programación":
            daika "{cps=30}¡Buena elección! La programación es el esqueleto de un juego.{/cps}"
            daika "{cps=30}Sin ella, todo quedaría en ideas sin vida.{/cps}"
            daika "{cps=30}En los inicios, como en los años 60 y 70, los juegos se programaban en Assembly, muy cerca del lenguaje de la máquina.{/cps}"
            daika "{cps=30}Luego, en los 80s, surgieron lenguajes de alto nivel como C, BASIC y Pascal, que facilitaron el desarrollo.{/cps}"
            daika "{cps=30}Hoy usamos motores como Godot, Unity o Unreal, y lenguajes como C#, GDScript o C++.{/cps}"
            daika "{cps=30}¡En el track, si eliges programación, podrás crear la lógica y las mecánicas de los juegos!{/cps}"
            pass
            jump opcionMenu

        "Arte y Diseño":
            daika "{cps=30}¡El arte es lo primero que enamora al jugador!{/cps}"
            daika "{cps=30}Desde los pixel art simples de los 80s hasta los mundos 3D hiperrealistas de hoy, todo comienza con una idea visual.{/cps}"
            daika "{cps=30}En el track, podrás diseñar personajes, escenarios, interfaces... ¡todo lo que se ve en pantalla!{/cps}"
            pass
            jump opcionMenu

        "Guion y Narrativa":
            daika "{cps=30}¿Te gusta contar historias? Entonces la narrativa es tu camino.{/cps}"
            daika "{cps=30}Desde los juegos de texto de los 70s hasta los RPGs profundos de hoy, una buena historia puede marcar la diferencia.{/cps}"
            daika "{cps=30}Aquí podrás crear personajes, diálogos, tramas y mundos memorables.{/cps}"
            pass
            jump opcionMenu

        "Música y Sonido":
            daika "{cps=30}¿Sabías que una buena banda sonora puede hacer que un juego se quede en el corazón de los jugadores?{/cps}"
            daika "{cps=30}Desde los bips de los primeros arcades hasta las bandas sonoras orquestales modernas, el audio ha evolucionado muchísimo.{/cps}"
            daika "{cps=30}En el track, podrás crear música, SFXs y dar vida sonora a los proyectos.{/cps}"
            pass
            jump opcionMenu
    jump cH

    label cH:
        daika "{cps=30}No importa cuál sea tu especialidad, Anzu. Lo importante es que aquí puedes aportar de diversas maneras, y sobre todo, aprender en el proceso.{/cps}"
        show daika smile at left, pose
        daika "{cps=30}Una cosa más: este track es completamente autodidacta y flexible en cuanto a tiempos y horarios.{/cps}"
        daika "{cps=30}No es como una clase convencional, donde tienes que llegar a tiempo y seguir a un profesor.{/cps}"
        show daika sad at left, pose
        daika "{cps=30}Nos gustaría contar con un profesor, pero eso está un poco fuera de nuestro alcance por ahora.{/cps}"
        show daika smile at left, pose
        daika "{cps=30}Aunque, honestamente, esto nos da la oportunidad de aprender a nuestro propio ritmo.{/cps}"
        show daika smile at left, pose
        daika "{cps=30}Lo bueno de este track es que podemos trabajar como equipo, compartir recursos y buscar material, todo a base de nuestro propio esfuerzo e interés.{/cps}"
        daika "{cps=30}Así que, ¿te gustaría unirte a nosotros?{/cps}"
        menu:
            "Sí":
                show anzu smile at right, pose
                a "{cps=30}Claro, me encantaría formar parte.{/cps}"
                daika "{cps=30}Perfecto. Scannea este código QR para más información.{/cps}"
                window hide
                show qr at truecenter
                pause

                window show
                "{cps=30}{i}Anzu scannea el código.{/i}{/cps}"
                hide qr

                show daika smile at left, pose
                daika "{cps=30}Listo, oficialmente eres parte de Games.{/cps}"
                daika "{cps=30}Bienvenida al equipo.{/cps}"
                hide daika smile 
                hide anzu smile
                jump pantalla_creditos
            "No":
                show anzu sad at right, pose
                show daika neutral at left, pose
                daika "{cps=30}Aw, está bien, lamento si no es lo que buscabas.{/cps}"
                a "{cps=30}Lo siento, creo que quiero otra cosa...{/cps}"
                daika "{cps=30}No te preocupes, acá en CITT tienes muchas opciones y oportunidades.{/cps}"
                daika "{cps=30}Estoy segura que podrás encontrar algo que te guste.{/cps}"
                daika "{cps=30}Si aún estás interesada, puedes scannear este código.{/cps}"
                window hide 
                show qr at truecenter
                pause

                window show
                "{cps=30}{i}Anzu scannea el código.{/i}{/cps}"
                hide qr
                show anzu smile at right, pose
                daika "{cps=30}Muchas gracias.{/cps}"
                show daika smile at left, pose
                daika "{cps=30}¡Muchas gracias a ti por pasarte!{/cps}"
                hide daika smile 
                hide anzu smile
                jump pantalla_creditos

    label pantalla_creditos:
        show bg school with dissolve

        window hide  
        show text "Créditos" with dissolve

        $ credits = [
            ("Desarrollador Principal", "B"),
            ("Programación", "B"),
            ("Diseño de Personajes", "Kei Ogawa (https://picrew.me/en/image_maker/1820833)"),
            ("Fondos", "Noraneko Background Pack"),
            ("Música", "School Days (Instrumental) - Persona OST"),
        ]

        $ i = 0
        while i < len(credits):
            $ titulo, nombre = credits[i]
            show text "{cps=50}" + titulo + ": " + nombre with dissolve
            $ renpy.pause(2)  
            $ i += 1

        show text "Gracias por jugar." with dissolve
        $ renpy.pause(2)  

        return

