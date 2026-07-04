#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "============================================"
echo "  Teste ClearBank — desafio-final"
echo "============================================"
echo ""

echo "[1/3] Executando notebook..."
python3 -m nbconvert --to notebook --execute desafio-final.ipynb \
  --output /tmp/desafio-final-test.ipynb \
  --ExecutePreprocessor.timeout=120 >/dev/null
echo "  OK — notebook executou sem erros"
echo ""

echo "[2/3] Executando analise_pandas.py..."
python3 analise_pandas.py
echo ""

echo "[3/3] Verificando arquivos gerados..."
for arquivo in relatorio.json grafico.png; do
  if [[ -f "$arquivo" ]]; then
    echo "  OK — $arquivo ($(wc -c < "$arquivo" | tr -d ' ') bytes)"
  else
    echo "  ERRO — $arquivo não encontrado"
    exit 1
  fi
done

echo ""
echo "Resumo do relatorio.json:"
python3 -c "
import json
with open('relatorio.json', encoding='utf-8') as f:
    d = json.load(f)
print(f\"  Válidas:   {d['total_transacoes_validas']}\")
print(f\"  Inválidas: {d['total_transacoes_invalidas']}\")
print(f\"  Período:   {d['periodo']['data_mais_antiga']} → {d['periodo']['data_mais_recente']}\")
print(f\"  Suspeitas: {len(d['transacoes_suspeitas'])}\")
print(f\"  Meses:     {', '.join(sorted(d['resumo_mensal']))}\")
"

echo ""
echo "============================================"
echo "  Todos os testes passaram!"
echo "============================================"
