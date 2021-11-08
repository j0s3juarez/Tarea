import sqlite3
import datetime

articulos = [];
folio = 1;

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

print("********** MENU **********")

while (True):
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3. Obtener un reporte de una venta")
    print("4. Salir")
    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        print("REGISTRAR")
        descripcion = input('Descripcion del producto: ');
        cantidad = int(input('Cantidad de productos: '));
        precio = int(input('Precio del producto: '));
        today = datetime.date.today().strftime("%d-%m1-%Y");
        noFolio = str(folio).zfill(6);
        total = cantidad * precio;
        
        articulos.append({'folio': noFolio ,'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio, 'total': total, 'fecha': today});
        folio = folio + 1;

    if opcion == 2:
        montoTotalArticulos = 0
        
        print('****CONSULTAR VENTAS****');
        print("")
        print("{:>20} {:>20} {:>20} {:>20} {:>20}".format("FOLIO", "DESCRIPCION","CANTIDAD","PRECIO","TOTAL"))
        print("{:>20} {:>20} {:>20} {:>20} {:>20}".format("-----------------","-----------------", "-----------------", "-----------------","-----------------"))
        for articulo in articulos:
            print("{:>20} {:>20} {:>20} {:>20} {:>20}".format(articulo['folio'],articulo['descripcion'], articulo['cantidad'], articulo['precio'], articulo['total']))
            montoTotalArticulos = montoTotalArticulos + articulo['total']
        print("{:>20} {:>20} {:>20} {:>20} {:>20}".format("","", "", "", montoTotalArticulos))
        print("\n")
        cursor.execute("SELECT * FROM usuarios")
    
    if opcion == 3:
        listaArticulos = [];
        montoTotalArticulos = 0

        print('***Obtener una fecha***')
        
        fecha = input('Ingresa la fecha para mostrar el reporte de ventas, ejemplo: 23-04-2021 \n');
        
        for index, articulo in enumerate(articulos):
            if articulo['fecha'] == fecha:
                listaArticulos.append(articulo)
                
            if len(listaArticulos) != 0:
                for articulo in listaArticulos:
                    print('****REPORTE DE VENTAS POR FECHA****');
                    print("")
                    print("{:>20} {:>20} {:>20} {:>20} {:>20}".format("DESCRIPCION","CANTIDAD","PRECIO","TOTAL", "FECHA DE VENTA"))
                    print("{:>20} {:>20} {:>20} {:>20} {:>20}".format("-----------------", "-----------------", "-----------------","-----------------", "-----------------"))
                    for articulo in articulos:
                        print("{:>20} {:>20} {:>20} {:>20} {:>20}".format(articulo['descripcion'], articulo['cantidad'], articulo['precio'], articulo['total'], articulo['fecha']))
                    print("")
            else:
                print('****REPORTE DE VENTAS POR FECHA****');
                print(' NO SE CUENTA CON VENTAS EN LA FECHA INGRESADA ');

    if opcion == 4:
        print(' Ha salido del sistema ')
        breakpoint()
        
cursor.execute("CREATE TABLE usuarios (Descripcion VARCHAR(100), Precio  INTEGER, Cantidad INTEGER, Total VARCHAR(100), FechaVenta DATETIME)")
cursor.execute("SELECT * FROM listaArticulos")

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print("Descripcion:", usuarios[0]," - Fecha:", cantidad[2])

print(descripcion)

conexion.commit()

conexion.close()

if opcion == 4:
        print(' Ha salido del sistema ')
        breakpoint()
