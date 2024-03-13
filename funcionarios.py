class Funcionario:
    def __init__ (self, nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario
    def aumentar_salario (self,percentual):
        self.salario *= (1 = percentual/100)

class Gerente(funcionario):
    def __init__ (self, nome, id, salario, departamento):
        self.nome = nome
        self.id = id
        self.salario = salario
        self.departamento = departamento

    def promover_funcionario (self, funcionario):
        

class funcionarioregular:
    def __init__ (self, nome, id, salario, departamento):
        self.nome = nome
        self.id = id
        self.salario = salario
        self.departamento = departamento 
    def calcular_folha (lista_funcionarios)