class Persona(object):
    def __init__(self, nom_comp, edad, sexo, est_civ):
	self._nombreCompleto = nom_comp
	self._edad = edad
	self._sexo = sexo
	self._estadoCivil = est_civ
    def __str__(self):
	return ('Nombre Completo: '+ self._nombreCompleto + '\n' + 
		'Edad: ' + str(self._edad) + '\n' + 
	 	'Sexo: ' + self._sexo + '\n' +
		'Estado Civil:' + self._estadoCivil + '\n')
    """"""
    def presentarse(self):
	pass	
