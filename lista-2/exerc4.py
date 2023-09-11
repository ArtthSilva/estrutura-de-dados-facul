class ContaBancaria:

    def __init__(self, titular, saldo = 0):
        self.titulo = titular
        self.saldo = saldo


    def depositar(self, deposito):
        self.saldo = self.saldo + deposito 

        print(f'saldo depois do deposito {self.saldo}') 

    def sacar(self, sacar):
        self.saldo = self.saldo - sacar 
        print(f'saldo depois de sacar {self.saldo}')       

conta = ContaBancaria('arthur', 15)
print(f'saldo antes do deposito: {conta.saldo}')
conta.depositar(50)
conta.sacar(10)

 