from item import Item
class CarritoCompra(object): 
    def __init__(self, cliente):
        self._cliente = cliente
        self._items = []
	self._subTotal = 0.00
	self._iva = 0.00
	self._total = 0.00
    def agregarItem(self, cantidad, producto):
	self._items.append(Item(cantidad, producto))
	self.actualizarMontos()
    def eliminarItem(self, pos): 
        try:
	    eliminado = self._items.pop(pos)
            self.actualizarMontos()
	except IndexError:
	    print 'El indice del elemento a eliminar no existe!'
    def actualizarMontos(self):
	st = 0.00
	for item in self._items:
	    st += item.calcularValorTotalItem()
	"""Si es cliente preferencial automaticamente se le reduce en 10% el subtotal"""
	st = self.aplicarDescuento(st)
	self._subTotal = st
	self._iva = self._subTotal * 0.15
	self._total = self._subTotal + self._iva
    def aplicarDescuento(self, subtotal):
	return ((subtotal - (subtotal * 0.10)) if self._cliente._esPreferencial else subtotal) 
    def obtenerDetalleCarrito(self):
	detalle = ""
	iteracion = 1
	for item in self._items:
	    detalle += ('Item # ' + str(iteracion) + ':\n' + 
			str(item) + '\n')
	    iteracion += 1
	return detalle
    def obtenerResumenMontos(self):
	return ('Subtotal: ' + str(self._subTotal) + '\n' + 'IVA: ' + str(self._iva) + '\n' + 'Total: ' + str(self._total) + '\n')
    def notificarDescuento(self):
	return (("Se dio descuento de " + str (self._subTotal * 0.10) + " (10%) en el subtotal por ser cliente preferencial") if self._cliente._esPreferencial else "No recibe descuento por ser cliente normal.")
