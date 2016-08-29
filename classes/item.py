class Item(object):
    def __init__(self, cantidad, objeto_producto):
        self._cantidad = cantidad
	self._producto = objeto_producto
    def calcularValorTotalItem(self):
	return (self._cantidad * self._producto._precioUnitario)
    def __str__(self):
	return (str(self._producto) + 
		'Cantidad solicitada: ' + str(self._cantidad) + '\n' + 
		'Valor total del item: ' + str(self.calcularValorTotalItem()) +'\n')
