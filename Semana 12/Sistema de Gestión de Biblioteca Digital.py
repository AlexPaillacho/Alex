class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Se inicializa un objeto Libro con sus atributos.
        """
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """
        Devuelve una representación en cadena del libro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un objeto Usuario con su nombre e ID, y una lista vacía de libros prestados.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        """
        Devuelve una representación en cadena del usuario, incluyendo el número de libros prestados.
        """
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        """
        Inicializa la biblioteca con diccionarios para libros y usuarios, y un conjunto para IDs de usuario únicos.
        """
        self.libros = {}  # Diccionario: ISBN (clave) -> Libro (valor)
        self.usuarios = {}  # Diccionario: ID Usuario (clave) -> Usuario (valor)
        self.ids_usuarios = set()  # Conjunto para verificar la unicidad de IDs de usuario

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca si su ISBN no existe ya.
        """
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El ISBN '{libro.isbn}' ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca por su ISBN.
        """
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN '{isbn}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró ningún libro con ISBN '{isbn}'.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario si su ID es único.
        """
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con ID '{usuario.id_usuario}'.")
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está en uso.")

    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario existente.
        """
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print(f"No se encontró ningún usuario con ID '{id_usuario}'.")

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro a un usuario si ambos existen y el libro no está ya prestado.
        """
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' ya tiene prestado el libro '{libro.titulo}'.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Registra la devolución de un libro por un usuario.
        """
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene prestado el libro '{libro.titulo}'.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        """
        Busca libros por título, autor o categoría.
        """
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con el criterio de búsqueda.")

    def listar_libros_prestados(self, id_usuario):
        """
        Lista los libros prestados a un usuario específico.
        """
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a '{usuario.nombre}':")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"El usuario '{usuario.nombre}' no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("la leyenda de cantuña", "Juan de velasco", "Ciencia ficción", "9798985247824")
libro2 = Libro("TORMENTA", "rey well", "Ciencia ficción", "9780451524955")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("leo tores", "0001")
usuario2 = Usuario("lorena vell", "0002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("0001", "9798985247824")
biblioteca.prestar_libro("0002", "9780451524955")

biblioteca.buscar_libros("autor", "Orwell")
biblioteca.listar_libros_prestados("0001")

biblioteca.devolver_libro("0001", "9798985247824")
biblioteca.listar_libros_prestados("0001")
biblioteca.dar_baja_usuario("0002") # Se da de baja un usuario.