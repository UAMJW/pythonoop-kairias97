class Item:
    def __init__(self, cantidad, objeto_producto):
        self._cantidad = cantidad
	self._producto = objeto_producto
    def calcularValorTotalItem(self):
	return (self._cantidad * self._producto._precioUnitario)
