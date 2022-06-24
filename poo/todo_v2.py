#!/usr/local/bin/python3
from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar louça')
    print(casa)

    casa.procurar('Lavar louça').concluir()
    for tarefa in casa.tarefas:
        print(f' - {tarefa}')
    print(casa)

    mercado = Projeto('Compra no mercado')
    mercado.add('Frios')
    mercado.add('Pães')
    mercado.add('Produtos de limpeza')

    produtos_limpeza = mercado.procurar('Produtos de limpeza')
    produtos_limpeza.concluir()
    for tarefa in mercado.tarefas:
        print(f' - {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
