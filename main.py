from classes.producto import Producto
from classes.cliente import Cliente
from classes.item import Item
from classes.carritocompra import CarritoCompra
from classes.empleado import Empleado

"""Objeto instancia de la clase  Cliente"""
cliente = Cliente('Maria Alejandra Cuadra Hernandez', 20, 'Mujer', 'Casada', 'CL02', True)

"""Objeto instancia de la clase Empleado"""
empleado = Empleado('Ernesto Enrique Morazan Delgado', 35, 'Hombre', 'Viudo', 'EM01','Gerente general', 7800.00)

print 'Comparacion entre representacion de cadena de un objeto Cliente y un objeto Empleado.'
print '***Objeto Cliente***'
print str(cliente)
cliente.presentarse()
print ''
print '***Objeto empleado***'
print str(empleado)
empleado.presentarse()
print ''

"""Instanciacion de 4 productos nuevos"""  
p1 = Producto('P01', 'Producto de prueba 1', 200)
p2 = Producto('P02', 'Producto de prueba 2', 300)
p3 = Producto('P03', 'Producto de prueba 3', 400)
p4 = Producto('P04', 'Producto de prueba 4', 500)

"""Prueba de acceso a las propiedades de un Producto"""
print 'Prueba de acceso directo a las propiedades de una instancia de Producto'
print 'Codigo del producto: ' + p1._codigoProducto
print 'Descripcion: ' + p1._descripcion
print 'Precio Unitario: ' + str(p1._precioUnitario) + '\n'

"""Se reduce el precio del producto 1 en 50"""
p1.reducirPrecio(50)

print 'Representacion de cadena de 4 instancias de la clase Producto'
print 'Producto #1' + '\n' + str(p1)
print 'Producto #2' + '\n' + str(p2)
print 'Producto #3' + '\n' + str(p3)
print 'Producto #4' + '\n' + str(p4)

"""Creo e instancio un nuevo cliente"""
cl = Cliente('Kevin Alexander Irias Hernandez', 19, 'Hombre', 'Soltero', 'CL01', True )

"""Instanciacion del objeto Carrito de Compras"""
carrito = CarritoCompra(cl)
"""Se agregan 4 productos al carrito"""
carrito.agregarItem(3, p1)
carrito.agregarItem(4, p2)
carrito.agregarItem(5, p3)
carrito.agregarItem(6, p4)

print 'Informacion del carrito de compras antes de eliminar items: '
print carrito
print carrito.notificarDescuento()
print ''

"""Se elimina el producto en la segunda posicion dentro del carrito de compras"""
carrito.eliminarItem(1)

print 'Informacion del carrito de compras luego que se eliminara un item:'
print carrito
print carrito.notificarDescuento()
