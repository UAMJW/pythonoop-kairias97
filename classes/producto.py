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

