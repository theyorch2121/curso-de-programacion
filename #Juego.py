#Juego

print("--- BIENVENIDO A LA FORTALEZA DEL TIEMPO ---")
print("Despiertas en una celda de piedra. Frente a ti hay un FOSFORO y una LINTERNA.")

opcion1 = input("Que decides tomar? (FOSFORO / LINTERNA): ").lower()

# Nivel1
if opcion1 == "fósforo" or opcion1 == "fosforo":
    print("El fósforo ilumina poco, pero ves tres puertas: ROJA, AZUL y VERDE.")
    
    # Nivel2
    opcion2 = input("Que puerta eliges? (ROJA / AZUL / VERDE): ").lower()
    
    if opcion2 == "roja":
        print("Un dragón dormido! Tienes tres opciones: ATACAR, SIGILO o VOLVER.")
        
        # Nivel 3
        opcion3 = input("Que haces? (ATACAR / SIGILO / VOLVER): ").lower()
        if opcion3 == "sigilo":
            print("Pasas con exito. Encuentras un COFRE, una ESPADA o un MAPA.")
            
            # Nivel 4
            opcion4 = input("Que eliges? (COFRE / ESPADA / MAPA): ").lower()
            if opcion4 == "mapa":
                print("El mapa muestra tres rutas: MONTAÑA, RIO o BOSQUE.")
                
                # Nivel 5
                opcion5 = input("Ruta? (MONTAÑA / RIO / BOSQUE): ").lower()
                if opcion5 == "rio" or opcion5 == "rio":
                    print("Hay una balsa. Puedes REMAR, NADAR o ESPERAR.")
                    
                    # Nivel 6
                    opcion6 = input("Accion? (REMAR / NADAR / ESPERAR): ").lower()
                    if opcion6 == "remar":
                        print("Felicidades! Has escapado de la fortaleza por el rio. VICTORIA.")
                    elif opcion6 == "nadar":
                        print("El agua estaba muy fría. FIN DEL JUEGO.")
                    elif opcion6 == "esperar":
                        print("Los guardias te atraparon. FIN DEL JUEGO.")
                    else:
                        print("Opción no válida. El pánico te paraliza.")
                else:
                    print("Te perdiste en la ruta. FIN DEL JUEGO.")
            else:
                print("El objeto era una trampa. FIN DEL JUEGO.")
        else:
            print("El dragón se despierta. FIN DEL JUEGO.")
            
    elif opcion2 == "azul":
        print("Caes en una fosa de agua. FIN DEL JUEGO.")
    elif opcion2 == "verde":
        print("La puerta está bloqueada. FIN DEL JUEGO.")
    else:
        print("Esa puerta no existe. Te quedas atrapado para siempre.")

elif opcion1 == "linterna":
    print("La linterna revela un túnel largo. Escuchas un ruido: SEGUIR o BUSCAR.")
    
    # Nivel 2
    opcion2b = input("Que decides? (SEGUIR / BUSCAR): ").lower()
    if opcion2b == "seguir":
        print("Llegas a una sala con tres palancas: ORO, PLATA o BRONCE.")
        
        # Nivel 3
        opcion3b = input("Cual tiras? (ORO / PLATA / BRONCE): ").lower()
        if opcion3b == "plata":
            print("Se abre un portal. Hay tres destinos: PASADO, FUTURO o PRESENTE.")
            
            # Nivel 4
            print("(Continuars... )")
        else:
            print("La palanca activa una trampa. FIN DEL JUEGO.")
    else:
        print("algo te atrapa en la oscuridad. FIN DEL JUEGO.")

else:
    print("No elegiste nada y te quedaste a oscuras. Opción no válida.")