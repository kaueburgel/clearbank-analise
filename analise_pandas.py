"""Versão alternativa da análise usando pandas (requisito opcional RO1)."""

from datetime import datetime
from pathlib import Path

import pandas as pd

ARQUIVO_CSV = Path("transacoes.csv")
LIMITE_SUSPEITO = 10000.00


def carregar_e_validar(caminho: Path) -> pd.DataFrame:
    df = pd.read_csv(caminho, dtype=str)

    df["id_num"] = pd.to_numeric(df["id"], errors="coerce")
    df["valor_num"] = pd.to_numeric(df["valor"], errors="coerce")
    df["data_dt"] = pd.to_datetime(df["data"], format="%Y-%m-%d", errors="coerce")
    df["tipo"] = df["tipo"].str.strip().str.lower()
    df["cliente_id"] = df["cliente_id"].fillna("").str.strip()

    mascara = (
        df["id_num"].notna()
        & df["cliente_id"].ne("")
        & df["data_dt"].notna()
        & df["tipo"].isin(["credito", "debito"])
        & df["valor_num"].notna()
        & (df["valor_num"] > 0)
    )

    validas = df[mascara].copy()
    validas["mes"] = validas["data_dt"].dt.strftime("%Y-%m")
    validas["valor"] = validas["valor_num"]
    return validas


def agrupar_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    creditos = df[df["tipo"] == "credito"].groupby("mes")["valor"].sum()
    debitos = df[df["tipo"] == "debito"].groupby("mes")["valor"].sum()
    quantidade = df.groupby("mes")["valor"].count()

    resumo = pd.DataFrame({
        "quantidade": quantidade,
        "total_credito": creditos,
        "total_debito": debitos,
    }).fillna(0)

    resumo["saldo"] = resumo["total_credito"] - resumo["total_debito"]
    resumo["media"] = (resumo["total_credito"] + resumo["total_debito"]) / resumo["quantidade"]

    maiores = df.groupby("mes")["valor"].max()
    menores = df.groupby("mes")["valor"].min()
    resumo["maior_valor"] = maiores
    resumo["menor_valor"] = menores

    return resumo.round(2)


def main() -> None:
    df = carregar_e_validar(ARQUIVO_CSV)
    resumo = agrupar_por_mes(df)
    suspeitas = df[df["valor"] > LIMITE_SUSPEITO]

    print("===== ANÁLISE COM PANDAS =====")
    print(f"Transações válidas: {len(df)}")
    print(f"Transações inválidas: {len(pd.read_csv(ARQUIVO_CSV)) - len(df)}")
    print("\nResumo mensal:")
    print(resumo.to_string())
    print(f"\nTransações suspeitas: {len(suspeitas)}")


if __name__ == "__main__":
    main()
