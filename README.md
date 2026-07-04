# ftr-dados-python

Notebook Python para leitura, validação e análise de transações bancárias a partir de CSV.

## Sobre o desafio

Desenvolver um notebook que:

1. **Lê e valida** um arquivo CSV de transações bancárias
2. **Agrupa** os dados por mês
3. **Calcula métricas** financeiras
4. **Sinaliza** movimentações relevantes
5. **Exporta** o resultado em JSON

## Estrutura do projeto

```
ftr-dados-python/
├── data/
│   └── transacoes.csv      # CSV de entrada (exemplo)
├── notebooks/
│   └── analise_transacoes.ipynb
├── output/                 # JSON gerado pelo notebook
├── requirements.txt
└── README.md
```

## Formato esperado do CSV

| Coluna     | Tipo   | Descrição                          |
|------------|--------|------------------------------------|
| `data`     | date   | Data da transação (`YYYY-MM-DD`)   |
| `descricao`| string | Descrição da movimentação          |
| `valor`    | float  | Valor (positivo = crédito, negativo = débito) |
| `categoria`| string | Categoria da transação (opcional)  |

## Como executar

```bash
# Criar ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate   # macOS/Linux

# Instalar dependências
pip install -r requirements.txt

# Abrir o notebook
jupyter notebook notebooks/analise_transacoes.ipynb
```

## Saída esperada (JSON)

O notebook deve gerar um arquivo em `output/resultado.json` com, no mínimo:

- Resumo por mês (totais de crédito, débito, saldo)
- Métricas financeiras consolidadas
- Lista de movimentações sinalizadas (alertas)
