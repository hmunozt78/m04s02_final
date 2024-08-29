class Persona:
    def __init__(self, nombre:str, apellido:str, sexo:str, edad:int, estatura:float, peso:int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
#################################################################
#              Getter y Setter de Nombre
#################################################################        
    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre.capitalize()
        else:
            print("Error está vacío")

#################################################################
#              Getter y Setter de Apellido
################################################################# 

    @property
    def apellido(self):
        return self.__apellido.capitalize()
    
    @apellido.setter
    def apellido(self, nuevo_apellido:str):
        if nuevo_apellido != "":
            
            self.__apellido = nuevo_apellido.capitalize()
        else:
            print("Error está vacío")

#################################################################
#              Getter y Setter de Sexo
################################################################# 

    @property
    def sexo(self):
        return self.__sexo.upper()
    
    @sexo.setter
    def sexo(self, nuevo_sexo):
        if nuevo_sexo != "":
           
            self.__sexo = nuevo_sexo.upper()
        else:
            print("Error está vacío")

#################################################################
#              Getter y Setter de Edad
################################################################# 

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevo_edad:int):
        if nuevo_edad != "":
            
            self.__edad = nuevo_edad
        else:
            print("Error está vacío")


#################################################################
#              Getter y Setter de Estatura
################################################################# 

    @property
    def estatura(self):
        return self.__estatura
    
    @estatura.setter
    def estatura(self, nuevo_estatura:float):
        if nuevo_estatura != "":
            
            self.__estatura = nuevo_estatura
        else:
            print("Error está vacío")


#################################################################
#              Getter y Setter de Peso
################################################################# 

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, nuevo_peso:int):
        if nuevo_peso != "":
            
            self.__peso = nuevo_peso
        else:
            print("Error está vacío")

#La siguiente funcion, retorna la informacion de cada objeto Persona
#al usar triple comilla simple, me permite el uso de multilineas, y ademas
#manejarlo de manera mas simple
    def informacion_usuarios(self):
        return f'''\033[0;31mNombre:\033[0;37m {self.__nombre} 
\033[0;32mApellido:\033[0;37m {self.apellido} 
\033[0;33mSexo:\033[0;37m {self.sexo} 
\033[0;34mEdad:\033[0;37m {self.edad} 
\033[0;35mEstatura:\033[0;37m {self.estatura} 
\033[0;36mPeso:\033[0;37m {self.peso}'''

#################################################################
#             Definicion de los primeros objetos
################################################################# 

persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)


#################################################################
#              Getter y Setter de Nombre
################################################################# 

print(persona_1.informacion_usuarios())
print()
print(persona_2.informacion_usuarios())

# persona_1.edad = 21
# persona_2.apellido = "santiago"
print()
# print(persona_1.edad)
# print(persona_2.apellido)

print(persona_1.informacion_usuarios())
print()
print(persona_2.informacion_usuarios())


