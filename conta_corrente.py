from conta_bancaria import ContaB

class ContaC(ContaB):
    def __init__(self, titular, cpf, numerocc, saldo):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc
    
    def mostrarcc(self):
        print(f"Conta Corrente {self.numerocc} - Titular: {self.titular}, CPF: {self.cpf}, Saldo: R$ {self.saldo:.2f}")