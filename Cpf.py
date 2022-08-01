class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Invalido! Digite Novamente')

    def __str__(self):
        return self.cpf_formatado()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def cpf_formatado(self):
        parte_um = self.cpf[:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]
        return f'{parte_um}.{parte_dois}.{parte_tres}-{parte_quatro}'

