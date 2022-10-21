import numpy as np
import datetime as dt

# DEFINICION DE ESTRUCTURAS DE DATOS
#Registro de habitaciones
tipo_habitacion = np.dtype([('numerohabitacion', int),
                            ('tipohabitacion', 'U1'), ('precio', float),
                            ('estdiario', np.ndarray),
                            ('esthabitacion', 'U1')])
N = 11
M = 10
A = np.empty(N, dtype=tipo_habitacion)
#carga estatica de habitaciones
A[0] = (113, "D", 200,
        np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[1] = (114, "D", 200,
        np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[2] = (115, "D", 200,
        np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D",
                  "D"]), "Habilitada")
A[3] = (116, "D", 200,
        np.array(["R", "R", "R", "R", "R", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[4] = (117, "D", 200,
        np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[5] = (118, "T", 300,
        np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D",
                  "D"]), "Habilitada")
A[6] = (119, "T", 300,
        np.array(["R", "R", "R", "R", "R", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[7] = (120, "T", 300,
        np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[8] = (113, "C", 400,
        np.array(["D", "D", "D", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[9] = (114, "C", 400,
        np.array(["D", "O", "R", "D", "D", "D", "D", "D", "D",
                  "D"]), "Habilitada")
A[10] = (115, "C", 400,
         np.array(["D", "D", "D", "O", "O", "O", "O", "D", "D",
                   "D"]), "Habilitada")

#Registro de fechas
fecha = np.dtype([('dia', int), ('mes', int), ('anio', int)])
f = np.empty(10, dtype=fecha)

#Registro de reservas
reservas = np.dtype([('NroH', int), ('FechaDesde', fecha),
                     ('FechaHasta', fecha), ('DNI', int)])
r = np.empty(10, dtype=reservas)

#Registro de ocupacion
ocupacion = np.dtype([('NroH', int), ('DNIHuespCargo', int),
                      ('FechaIn', fecha), ('FechaOut', fecha)])
o = np.empty(10, dtype=ocupacion)

#Registro de Domicilio
Domicilio = np.dtype([('Calle', str), ('Nro', int), ('Ciudad', str),
                      ('Provincia', str)])
D = np.empty(10, dtype=Domicilio)

#Registro de Huespedes
huespedes = np.dtype([('DNI', int), ('NomAp', str), ('DomH', Domicilio),
                      ('FechaN', fecha), ('HuespedR', bool)('DNIHuespCargo',
                                                          int),
                      ('NroTC', int)])
HU = np.empty(10, dtype=huespedes)
"""
"""


def MayorDeEdad(dia, mes, anio):
    """
    Determina si un huesped es mayor de edad
    :param dia: entrada
    :param mes: entrada
    :param anio: entrada
    :return: un valor logico
    """
  if (dt.datetime.now().year - anio) >= 18:
      if dt.datetime.now().month >= mes:
            if dt.datetime.now().month == mes:
                if dt.datetime.now().day >= dia:
                    B = True
                else:
                    B = False
            else:
                B = False
        else:
            B = False
  else:
    B = False
  return B


def reservar(H, dim, i):
  H[i]['NomAp'] = input("Ingresa tu nombre y apellido:")
  print("Ingresa fecha de nacimiento")
  H[i]['FechaN']['dia'] = int(input("Ingrese el dia:"))
  H[i]['FechaN']['mes'] = int(input("Ingrese el mes:"))
  H[i]['FechaN']['anio'] = int(input("Ingrese el año:"))
  E = MayorDeEdad(H[i]['FechaN']['dia'], H[i]['FechaN']['mes'],
                  H[i]['FechaN']['anio'])
  if E:
    H[i]['DNIHuespCargo'] = int(input("Ingresa el DNI:"))
    while H[i]['DNIHuespCargo'] < 10000000 or H[i]['DNIHuespCargo'] > 99999999:
      print("El DNI solo contiene 8 dígitos")
      H[i]['DNIHuespCargo'] = int(input("Ingresa el DNI:"))
  else:
    print("No se pudo hacer la reserva por ser menor de edad")


#Programa Principal
dimHU = 10
i = 0
reservar(HU, dimHU, i)

#Menu
# def mostrar_menu():
#     print("****** HOTEL CALIFORNIA ******")
#     print("1 - Check in")
#     print("2 - Check out")
#     print("3 - Reservas")
#     print("4 - Salir")
#     return None

# salir = False
# dreal = 0
# while not salir:
#     mostrar_menu()
#     op = int(input("Ingrese una opcion: "))
#     if op == 1:
#         #ingresar huespedes
#     elif op == 2:
#         #generar factura
#     elif op == 3:
#         #verificar disponibilidad de habitaciones
#     elif op == 4:
#         salir = True
#     else:
#         print("Opción incorrecta")
#     print("")
