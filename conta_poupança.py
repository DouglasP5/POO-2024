from conta_bancaria import ContaB
from conta_corrente import ContaC

class ContaP(ContaB):
    def __init__(self, titular, cpf, rendimento, saldo=0):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento
    
    def ver_rendimento(self):
        print(f"Taxa de Rendimento: {self.rendimento * 100:.2f}%")
    
    def render(self):
        rendimento_gerado = self.saldo * self.rendimento
        self.saldo += rendimento_gerado
        print(f"Rendimento aplicado. Novo saldo: R$ {self.saldo:.2f}")


def menu():
    global contas
    contas = []
    while True:
        print("Bem Vindo ao nosso banco!, o que você deseja?")
        print("\nMenu:")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Poupança")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Verificar Saldo")
        print("6. Ver Rendimento (Poupança)")
        print("7. Aplicar Rendimento (Poupança)")
        print("8. Mostrar Conta Corrente")
        print("9. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titular = input("Nome do titular: ")
            cpf = input("CPF do titular: ")
            numerocc = input("Número da Conta Corrente: ")
            saldo = float(input("Saldo inicial: "))
            nova_conta = ContaC(titular, cpf, numerocc, saldo)
            contas.append(nova_conta)
            print("Conta Corrente criada com sucesso.")
        
        elif opcao == "2":
            titular = input("Nome do titular: ")
            cpf = input("CPF do titular: ")
            rendimento = float(input("Taxa de Rendimento (em decimal, ex: 0.01 para 1%): "))
            saldo = float(input("Saldo inicial: "))
            nova_conta = ContaP(titular, cpf, rendimento, saldo)
            contas.append(nova_conta)
            print("Conta Poupança criada com sucesso.")
        
        elif opcao == "3":
            cpf = input("CPF da conta para depósito: ")
            valor = float(input("Valor do depósito: "))
            conta = None
            for c in contas:
                if c.cpf == cpf:
                    conta = c
                    break
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        
        elif opcao == "4":
            cpf = input("CPF da conta para saque: ")
            valor = float(input("Valor do saque: "))
            conta = None
            for c in contas:
                if c.cpf == cpf:
                    conta = c
                    break
            if conta:
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")
        
        elif opcao == "5":
            cpf = input("CPF da conta para verificar saldo: ")
            conta = None
            for c in contas:
                if c.cpf == cpf:
                    conta = c
                    break
            if conta:
                conta.verificar_saldo()
            else:
                print("Conta não encontrada.")
        
        elif opcao == "6":
            cpf = input("CPF da conta poupança para ver rendimento: ")
            conta = None
            for c in contas:
                if c.cpf == cpf and isinstance(c, ContaP):
                    conta = c
                    break
            if conta:
                conta.ver_rendimento()
            else:
                print("Conta poupança não encontrada.")
        
        elif opcao == "7":
            cpf = input("CPF da conta poupança para aplicar rendimento: ")
            conta = None
            for c in contas:
                if c.cpf == cpf and isinstance(c, ContaP):
                    conta = c
                    break
            if conta:
                conta.render()
            else:
                print("Conta poupança não encontrada.")
        
        elif opcao == "8":
            cpf = input("CPF da conta corrente para mostrar: ")
            conta = None
            for c in contas:
                if c.cpf == cpf and isinstance(c, ContaC):
                    conta = c
                    break
            if conta:
                conta.mostrarcc()
            else:
                print("Conta corrente não encontrada.")
        
        elif opcao == "9":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()