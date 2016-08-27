class Producto:
    
    def __init__(self, cod_prod, desc, precio):
        self._descripcion = desc
        self._precioUnitario = precio
        self._codigoProducto = cod_prod
        
    """Setters"""    
    def setDescripcion(self, descp):
        self._descripcion = descp
        
    def setPrecioUnitatio(self, pu):
        self._precioUnitario = pu
    
    def setCodigoProducto(self, cod_prod):
        self._codigoProducto = cod_prod
        
	"""Getters"""
    def getDescripcion(self):
        return self._descripcion
    def getPrecioUnitario(self):
        return self._precioUnitario
    def getCodigoProducto(self):
        return self._codigoProducto
    
    def aumentarPrecio(self, monto):
        self._precio_unitario += monto
        
    def reducirPrecio(self, monto):
        if self._precioUnitario >= monto:
            self._precioUnitario -= monto
	else:
            print 'El monto a reducir no puede ser mayor que el precio.'

class Cliente:
    def __init__(self, id_cliente, nom_comp, pref):
        self._idCliente = id_cliente
	self._nombreCompleto = nom_comp
	self._esPreferencial = pref

    def mostrarInfoCliente(self):
	return ('Codigo del cliente: ' + self._idCliente + '\n' +  
	       'Nombre completo: ' + self._nombreCompleto + '\n' +
	       "Preferencial: " + ("SI" if self._esPreferencial else "No" ))
class Item:
    def __init__(self, cantidad, objeto_producto):
        self._cantidad = cantidad
	self._producto = objeto_producto

class CarritoCompra: 
    
    def __init__(self, cliente):
        self._cliente = cliente
        self._items = []
	self._subTotal = 0.00
	self._iva = 0.00
	self._total = 0.00
    def agregarItem(self, item):
	self._items.append(item)
	self.actualizarMontos()
    def eliminarItem(self, pos): 
        try:
	    eliminado = self._items.pop(pos)
            self.actualizarMontos() 
	except IndexError:
	    print 'El indice del elemento a eliminar no existe!'
    def actualizarMontos(self):
	st = 0.00
	iva = 0.00
	total = 0.00
	for item in self._items:
	    st += (item._cantidad * item._producto._precioUnitario)
	"""Si es cliente preferencial automaticamente se le reduce en 10% el subtotal"""
	if self._cliente._esPreferencial : 
	    st -= (st * 0.10)
	iva = st * 0.15
	total = st + iva
	self._subTotal = st
	self._iva = iva
	self._total = total

    def obtenerDetalleCarrito(self):
	detalle = ""
	iteracion = 1
	for item in self._items:
	    detalle += ('Item # ' + str(iteracion) + ':\n' + 
			'\tCodigo del Producto: ' + item._producto._codigoProducto + '\n' +
			'\tDescripcion: ' + item._producto._descripcion + '\n' + 
			'\tPrecio Unitario: ' + str(item._producto._precioUnitario) + '\n' + 
			'\tCantidad pedida: ' + str(item._cantidad) + '\n' +
			'\tSubtotal por el item: ' + str(item._cantidad * item._producto._precioUnitario) + '\n')
	    iteracion += 1
	return detalle
    def obtenerResumenMontos(self):
	return ('Subtotal: ' + str(self._subTotal) + '\n' + 'IVA: ' + str(self._iva) + '\n' + 'Total: ' + str(self._total) + '\n')
    def hayDescuento(self):
	return (("Se dio descuento de " + str (self._subTotal * 0.10) + " (10%) en el subtotal por ser cliente preferencial") if self._cliente._esPreferencial else "No recibe descuento por ser cliente normal.")

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
print 'Accessando a las propiedades del primer objeto de tipo producto instanciado'
print 'Codigo del producto: ' + p1._codigoProducto
print 'Descripcion: ' + p1._descripcion
print 'Precio Unitario: ' + str(p1._precioUnitario)

print""
"""Creo un nuevo cliente"""
cl = Cliente('CL01', 'Kevin Alexander Irias Hernandez', True )
"""Datos del nuevo cliente creado"""
print 'Datos del objeto cliente instanciado'
print cl.mostrarInfoCliente()

"""Instanciacion del objeto Carrito de Compras"""
carrito = CarritoCompra(cl)
"""Se agregan items al carrito"""
carrito.agregarItem(Item(3, p1))
carrito.agregarItem(Item(4, p2))
carrito.agregarItem(Item(5, p3))
carrito.agregarItem(Item(6, p4))

print ""
print 'Detalle del carrito antes de eliminar items: '
print carrito.obtenerDetalleCarrito()
print 'Resumen de montos del carrito antes de eliminar items:'
print carrito.obtenerResumenMontos()
print carrito.hayDescuento()
print ""
"""Se elimina el producto en la segunda posicion dentro del carrito de compras"""
carrito.eliminarItem(1)

print 'Informacion del cliente asociado al carrito de compras'
print cl.mostrarInfoCliente()
print ""
print 'Detalle del carrito luego que se quito un item del carrito'
print carrito.obtenerDetalleCarrito()
print ""
print 'Resumen de montos del carrito despues de eliminar un item'
print carrito.obtenerResumenMontos()
print carrito.hayDescuento()
