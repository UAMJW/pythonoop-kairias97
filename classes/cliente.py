from persona import Persona
class Cliente(Persona):
    def __init__(self, nom_comp, edad, sexo, est_civ,id_cliente, pref):
        Persona.__init__(self, nom_comp, edad, sexo, est_civ)
	self._idCliente = id_cliente
	self._esPreferencial = pref

    def __str__(self):
	return ('Nombre Completo: ' + self._nombreCompleto + '\n' + 
		'Edad: ' + str(self._edad) + '\n' + 
		'Sexo: ' + self._sexo + '\n' + 
		'Estado Civil: ' + self._estadoCivil + '\n' + 
		'Codigo del cliente: ' + self._idCliente + '\n' +  
	        'Preferencial: ' + ('SI' if self._esPreferencial else 'No' ) + '\n')
    def presentarse(self):
	print "Hola. Soy una instancia de la clase Cliente, y heredo propiedades de una persona."
