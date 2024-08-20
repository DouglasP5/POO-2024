class ContaB:
    def __init__(self, titular, cpf, saldo):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")