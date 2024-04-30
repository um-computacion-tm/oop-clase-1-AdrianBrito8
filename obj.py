import unittest

class Alumno:
    def __init__(self, nombre, legajo):
        self.__nombre__ = nombre
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_legajo(self):
        return self.__legajo__

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__

class TestMateria(unittest.TestCase):
    def test_constructor(self):
        profesor = Profesor("Juan", "Docente", "123")
        materia = Materia("Matemáticas", [profesor])
        self.assertEqual(materia.obtener_profesores(), [profesor])

    def test_obtener_alumnos(self):
        materia = Materia("Matemáticas", [])
        alumno1 = Alumno("Carlos", "001")
        alumno2 = Alumno("Maria", "002")
        materia.obtener_alumnos().append(alumno1)
        materia.obtener_alumnos().append(alumno2)
        self.assertEqual(materia.obtener_alumnos(), [alumno1, alumno2])

class TestProfesor(unittest.TestCase):
    def test_constructor(self):
        profesor = Profesor("Juan", "Docente", "123")
        self.assertEqual(profesor.obtener_nombre(), "Juan")
        self.assertEqual(profesor.obtener_cargo(), "Docente")
        self.assertEqual(profesor.obtener_legajo(), "123")

class TestAlumno(unittest.TestCase):
    def test_constructor(self):
        alumno = Alumno("Carlos", "001")
        self.assertEqual(alumno.obtener_nombre(), "Carlos")
        self.assertEqual(alumno.obtener_legajo(), "001")

if __name__ == '__main__':
    unittest.main()
