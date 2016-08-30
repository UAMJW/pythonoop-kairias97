from persona import Persona
class Empleado(Persona):
    def __init__(self, nom_comp, edad, sexo, est_civ, cod_empl, cargo, salario):
	Persona.__init__(self, nom_comp, edad, sexo, est_civ)
	self._codigoEmpleado = cod_empl
	self._cargo = cargo
	self._salario = salario
    def presentarse(self):
	print 'Hola, soy una instancia de la clase Empleado y heredo atributos de una persona.'
    def __str__(self):
	return ('Nombre Completo: '+ self._nombreCompleto + '\n' + 
		'Edad: ' + str(self._edad) + '\n' +
		'Sexo: ' + self._sexo + '\n' + 
		'Estado Civil: ' + self._estadoCivil + '\n' + 
		'Cargo: ' + self._cargo + '\n' + 
		'Salario: ' + str(self._salario) + '\n')
