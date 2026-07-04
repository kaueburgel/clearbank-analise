# ClearBank — Análise de Transações

Projeto do desafio final do módulo de Python para análise de dados. O notebook lê transações bancárias de um CSV, valida e limpa os dados, calcula métricas financeiras mensais, identifica transações suspeitas e exporta um relatório em JSON.

## Como executar

1. Clone o repositório e entre na pasta do projeto.
2. Crie o ambiente virtual (opcional) e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Certifique-se de que o arquivo `transacoes.csv` está na raiz do projeto.
4. Abra o notebook no Jupyter ou Google Colab:

```bash
jupyter notebook desafio-final.ipynb
```

5. Execute todas as células em ordem, da primeira à última.

## Arquivos de entrada e saída

| Arquivo | Descrição |
|---------|-----------|
| `transacoes.csv` | Histórico de transações exportado pela ClearBank |
| `relatorio.json` | Relatório gerado pelo notebook com métricas e suspeitas |
| `grafico.png` | Gráfico de saldo mensal (requisito opcional) |

## O que o notebook faz

- Lê o CSV com o módulo nativo `csv` (sem pandas na solução principal)
- Valida cada linha e descarta registros inválidos silenciosamente
- Agrupa transações por mês e calcula créditos, débitos, saldo, média e extremos
- Identifica transações com valor acima de R$ 10.000,00 como suspeitas
- Exibe um relatório formatado no terminal
- Salva o resultado em `relatorio.json`

## Requisitos opcionais

- `analise_pandas.py` — versão alternativa usando pandas para comparação
- `grafico.png` — gráfico de barras com saldo mensal gerado com matplotlib

## Estrutura do repositório

```
clearbank-analise/
├── desafio-final.ipynb
├── transacoes.csv
├── relatorio.json
├── analise_pandas.py
├── grafico.png
└── README.md
```
