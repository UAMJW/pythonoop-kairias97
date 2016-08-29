from classes.producto import Producto
from classes.cliente import Cliente
from classes.item import Item
from classes.carritocompra import CarritoCompra
"""Instanciacion de 4 productos nuevos"""
print 'CREACION DE PRODUCTOS'
p1 = Producto('P01', 'Producto de prueba 1', 200)
p2 = Producto('P02', 'Producto de prueba 2', 300)
p3 = Producto('P03', 'Producto de prueba 3', 400)
p4 = Producto('P04', 'Producto de prueba 4', 500)
"""Se reduce el precio del producto 1 en 50"""
p1.reducirPrecio(50)

print "" 
"""Prueba de acceso a las propiedades de un Producto"""
print 'Accessando a las propiedades del primer objeto de tipo Producto instanciado'
print 'Codigo del producto: ' + p1._codigoProducto
print 'Descripcion: ' + p1._descripcion
print 'Precio Unitario: ' + str(p1._precioUnitario)

print""
"""Creo e instancio un nuevo cliente"""
cl = Cliente('Kevin Alexander Irias Hernandez', 19, 'Hombre', 'Soltero', 'CL01', True )
cl.presentarse()
"""Datos del nuevo cliente creado"""
print 'Datos del objeto cliente instanciado'
print cl

"""Instanciacion del objeto Carrito de Compras"""
carrito = CarritoCompra(cl)
"""Se agregan items al carrito"""
carrito.agregarItem(3, p1)
carrito.agregarItem(4, p2)
carrito.agregarItem(5, p3)
carrito.agregarItem(6, p4)

print ""
print 'Detalle del carrito antes de eliminar items: '
print carrito.obtenerDetalleCarrito()
print 'Resumen de montos del carrito antes de eliminar items:'
print carrito.obtenerResumenMontos()
print carrito.notificarDescuento()
print ""
"""Se elimina el producto en la segunda posicion dentro del carrito de compras"""
carrito.eliminarItem(1)

print 'Informacion del cliente asociado al carrito de compras'
print cl
print ""
print 'Detalle del carrito luego que se quito un item del carrito'
print carrito.obtenerDetalleCarrito()
print ""
print 'Resumen de montos del carrito despues de eliminar un item'
print carrito.obtenerResumenMontos()
print carrito.notificarDescuento()
