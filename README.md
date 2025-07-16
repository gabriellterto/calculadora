# 💧 Calculadora de Conta de Água por Pessoa-Dia

Projeto em Python para calcular e dividir o valor da conta de água entre casas de aluguel com base no consumo proporcional de **pessoa-dia** (quantidade de pessoas e dias consumidos em cada casa).

## 🚀 Funcionalidade

- Divide o valor da conta de água proporcionalmente entre as casas com base na quantidade de pessoas e no tempo que elas permaneceram no local.
- Ideal para imóveis com **medidor único de água compartilhado**.

## 📘 Exemplo de cálculo

Suponha uma conta de água de R$300 para 3 casas:
- Casa 1: 2 pessoas por 30 dias
- Casa 2: 1 pessoa por 15 dias
- Casa 3: 3 pessoas por 30 dias

O valor por pessoa-dia será:

Cada casa pagará:
- Casa 1: R$109,09
- Casa 2: R$27,27
- Casa 3: R$163,64

## 🧩 Estrutura do Projeto

```plaintext
calculadora-agua/
├── main.py
├── lib/
│   ├── interface.py
│   └── calculadora.py
└── tests/
    ├── __init__.py
    └── test_calculadora.py
```


## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/gabriellterto/calculadora.git
cd calculadora-agua
```

## 🔧 Requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária (apenas bibliotecas padrão do Python)

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.  
Você é livre para usar, modificar e distribuir este software, desde que mantenha o aviso de direitos autorais original.

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.



