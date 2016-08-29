class Cliente:
    def __init__(self, id_cliente, nom_comp, pref):
        self._idCliente = id_cliente
	self._nombreCompleto = nom_comp
	self._esPreferencial = pref

    def mostrarInfoCliente(self):
	return ('Codigo del cliente: ' + self._idCliente + '\n' +  
	       'Nombre completo: ' + self._nombreCompleto + '\n' +
	       "Preferencial: " + ("SI" if self._esPreferencial else "No" ))
