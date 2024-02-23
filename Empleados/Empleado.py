class Empleado:
    #aqui va el dodigo
    '''-----------------------------------------------------------------
     #Atributos
    -----------------------------------------------------------------'''

    nombres=''
    apellidos=''

    '''--------------------------------------------------------------
    # 1 = Masculino y 2 = Femenino 
    ---------------------------------------------------------------'''

    sexo=0
    salario=0
    '''--------------------------------------------------------
    # Metodos
    --------------------------------------------------------'''

    def cambiarSalario(self, nSalario):
        #Aqui va el codigo
        self.salario = nSalario 
        return "Su nuevo salario es:" + self.salario

    def ConsultarSalario(self):
        #Aqui va el codigo 
        return self.salario
    
    def AumentoSalario(self)
        # Aqui va el codigo 
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "su nuevo salario es: " + self.salario
    

