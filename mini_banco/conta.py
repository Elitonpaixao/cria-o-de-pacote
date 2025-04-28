class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError("Saque não permitido: saldo insuficiente ou valor inválido.")

    def saldo_atual(self):
        return self.saldo
