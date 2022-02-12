from msilib.schema import Class
from re import A
from turtle import title


class Book:
    # métodos que es una función asociada a un objeto, se define e inicializa con def y __init__():
    def __init__(self, titulo, autor, precio, stock, oid):
       
    # atributos de nuestra clase o propiedades
        self._titulo = titulo
        self._autor = autor   
        self._precio = precio
        self._stock = stock
        self._oid = oid     
        
    # método para mostrar la información    
    def get_informacion(self):
        return f""" \n\n Título: {self._titulo}\n Autor: {self._autor}\n Precio: {self._precio}\n Stock: {self._stock}\n ID: {self._oid}"""

# público => accesible para todos
# protegido => solo debería accederse desde la propia clase y sus subclases
# privado => solo es accesible por la propia clase

# Getters / Setters 
# get => obtener (lectura)
# set => setear/establecer (escritura)
# métodos para hacer validaciones!!!!!

# validar título

    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

# validar autor

    def get_autor(self):
            return self._autor
    
    def set_autor(self, nuevo_autor):
        self._autor = nuevo_autor

# validar precio
       
    def get_precio(self):
            return self._precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print(" El precio de un libro debe ser un valor mayor a 0 ")

# validar stock

    def get_stock(self):
            return self._stock
    
    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock
        
# validar ID
    
    def get_oid(self):
            return self._oid
    
    def set_oid(self, nuevo_oid):
        self._stock = nuevo_oid


#class Comics(Book):
#    def __init__(self, titulo, autor, precio, stock, oid, ilustradores, volumen):
#        super().__init__(titulo, autor, precio, stock, oid)
#        self._ilustradores = ilustradores
#        self._volumen = volumen

class Comics(Book):
    def __init__(self, titulo, autor, precio, stock, oid, ilustradores, volumen):
        super().__init__(titulo, autor, precio, stock, oid)
        self._ilustradores = ilustradores
        self._volumen = volumen
        
    def get_informacion(self):
        #return super().get_informacion()
        #print("Soy el método get_informacion de la clase comics ")
        
        info = super().get_informacion()
        str_ilustradores = ', '.join(self._ilustradores)
        return info + f"""\n Ilustradores: {str_ilustradores}\n Volumen {self._volumen}\n """
        # return info + """ Ilustradores: {self._ilu}\n Volumen: {self._volumen} """
        
# instanciar un objeto de la clase Book => book1 es una instancia de la clase Book
book1 = Book( "Hola Mundo", "Mauricio", 2500, 100, 1)
book2 = Book( "Macana", "Martín", 1230, 30, 2)

# print(" Título: ", book1.titulo, " --- ", " Autor: ", book1.autor, " --- ", " Precio: ", book1.precio, " --- ", " Stock: ", book1.stock, " --- ", " ID: ", book1.oid)
# print(" Título: ", book2.titulo, " --- ", " Autor: ", book2.autor, " --- ", " Precio: ", book2.precio, " --- ", " Stock: ", book2.stock, " --- ", " ID: ", book2.oid)

print(book1.get_informacion(), book2.get_informacion())

# self es tal cual como si fuere el objeto de la clase, para que la clase sepa qué objeto estamos trabajando

book1.set_titulo(" Este es el nuevo título del libro")
book1.set_precio(10)
print(book1.get_titulo())


print(book1.get_informacion())

comics1 = Comics(" Chau ", "Guerrero", 300, 34, 3, ['Karina', 'Tamara'], 3)
print(comics1.get_informacion())
