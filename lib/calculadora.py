class Calculadora:
    def __init__(self, valor_total):
        self.valor_total = valor_total
        self.casas = []

    def adicionar_casa(self, pessoas, dias):
        self.casas.append({
            'pessoas': pessoas,
            'dias': dias,
            'pessoa_dia': pessoas / dias
        })
    
    def calcular(self):
        total_pessoa_dia = sum(casa['pessoa_dia'] for casa in self.casas)
        valor_unitario = self.valor_total / total_pessoa_dia

        resutados = []
        for i, casa in enumerate(self.casas, start=1):
            valor = casa['pessoa_dia'] * valor_unitario
            resutados.append((i, valor))

        return resutados
    