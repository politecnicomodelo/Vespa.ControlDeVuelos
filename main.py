from tripulacion import tripulacion
from pasajeros import pasajeros
from piloto import piloto
from servicio_abordo import servicio_abordo
from avion import avion
from persona import persona
from vuelos import vuelo

lista_personas=[]
lista_aviones=[]
lista_vuelos=[]

personas = open("personas.dat", "r")
    lista = []
    for line in personas:
        if (line==" "):
            break

        elif (line=="Pasajero"):
            new_pasajero=pasajeros()
            lista = line.split('|')
            new_pasajero.setNombre(str(lista[1]))
            new_pasajero.setApellido(str(lista[2]))
            new_pasajero.setFecha(lista[3])
            new_pasajero.setDni(str(lista[4]))
            new_pasajero.setVIP(lista[5])
            new_pasajero.addNecesidad(str(lista[6]))
            lista_personas.append(new_pasajero)

        elif (line=="Piloto"):
            new_piloto=piloto()
            lista = line.split('|')
            new_piloto.setNombre(str(lista[1]))
            new_piloto.setApellido(str(lista[2]))
            new_piloto.setFecha(lista[3])
            new_piloto.setDni(str(lista[4]))
            new_piloto.addAvion(lista[5].split(','))
            lista_personas.append(new_piloto)

        elif (line=="Servicio")
            new_servicio=servicio_abordo()
            lista = line.split('|')
            new_servicio.setNombre(str(lista[1]))
            new_servicio.setApellido(str(lista[2]))
            new_servicio.setFecha(lista[3])
            new_servicio.setDni(str(lista[4]))
            new_servicio.addAvion(lista[5].split(','))
            new_servicio.addIdioma(str(lista[6]))
            lista_personas.append(new_servicio)
        print("hola")

