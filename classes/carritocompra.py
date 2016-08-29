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
	    st += item.calcularValorTotalItem()
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
    def notificarDescuento(self):
	return (("Se dio descuento de " + str (self._subTotal * 0.10) + " (10%) en el subtotal por ser cliente preferencial") if self._cliente._esPreferencial else "No recibe descuento por ser cliente normal.")

