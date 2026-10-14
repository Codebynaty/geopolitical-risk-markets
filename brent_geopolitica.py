"""
============================================================
PROJETO: Risco geopolítico -> Mercado (Brent × eventos)
============================================================
Ideia: pegar o preço do petróleo Brent, marcar datas de eventos
geopolíticos no gráfico e medir QUANTO o mercado se mexeu em torno
de cada evento (variação % e mudança de volatilidade).

É a versão mínima do que um macro/quant researcher faz:
juntar o "porquê" (geopolítica) com o "quanto" (dados).

COMO RODAR (na sua máquina, com internet):
    pip install yfinance pandas matplotlib
    python brent_geopolitica.py

Depois, brinque: troque os eventos, o ativo, as janelas.
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ------------------------------------------------------------
# 1) CONFIGURAÇÃO — mude à vontade
# ------------------------------------------------------------
TICKER = "BZ=F"          # Brent. Experimente também: "CL=F" (WTI), "BRL=X" (dólar/real), "GC=F" (ouro)
START  = "2021-06-01"
END    = "2023-03-01"
JANELA = 10              # nº de pregões antes/depois do evento para medir o impacto

# Eventos: {data: "rótulo"}. Troque pelos que você quiser estudar.
EVENTOS = {
    "2021-11-04": "OPEP+ mantém corte de produção",
    "2022-02-24": "Invasão da Ucrânia pela Rússia",
    "2022-06-03": "Embargo da UE ao petróleo russo",
}

# ------------------------------------------------------------
# 2) BAIXAR OS DADOS
# ------------------------------------------------------------
print(f"Baixando {TICKER}...")
dados = yf.download(TICKER, start=START, end=END, progress=False, auto_adjust=True)

# yfinance às vezes devolve colunas em 2 níveis; aqui achatamos para ficar simples.
if isinstance(dados.columns, pd.MultiIndex):
    dados.columns = dados.columns.get_level_values(0)

preco = dados["Close"].dropna()          # série de preços de fechamento
retorno = preco.pct_change()             # retorno diário (variação % de um dia p/ o outro)

# ------------------------------------------------------------
# 3) ANÁLISE — o que aconteceu em torno de cada evento?
# ------------------------------------------------------------
print(f"\n{'EVENTO':<38} {'PREÇO ANTES':>12} {'PREÇO DEPOIS':>13} {'VARIAÇÃO':>10} {'VOL. ANTES':>11} {'VOL. DEPOIS':>12}")
print("-" * 100)

linhas = []
for data_str, rotulo in EVENTOS.items():
    data = pd.to_datetime(data_str)
    # posição do pregão mais próximo do evento no índice de datas
    pos = preco.index.get_indexer([data], method="nearest")[0]

    # fatias de "antes" e "depois" (JANELA pregões de cada lado)
    antes  = preco.iloc[max(0, pos - JANELA): pos]
    depois = preco.iloc[pos: pos + JANELA]

    preco_antes  = antes.mean()
    preco_depois = depois.mean()
    variacao = (preco_depois / preco_antes - 1) * 100      # variação % média antes->depois

    # volatilidade = desvio-padrão dos retornos diários na janela (quanto o preço "treme")
    vol_antes  = retorno.iloc[max(0, pos - JANELA): pos].std() * 100
    vol_depois = retorno.iloc[pos: pos + JANELA].std() * 100

    print(f"{rotulo:<38} {preco_antes:>12.2f} {preco_depois:>13.2f} {variacao:>9.1f}% {vol_antes:>10.2f}% {vol_depois:>11.2f}%")
    linhas.append((rotulo, variacao))

# ------------------------------------------------------------
# 4) GRÁFICO — preço + linhas verticais nos eventos
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(preco.index, preco.values, color="#1a1a1a", lw=1.4, label=TICKER)

for data_str, rotulo in EVENTOS.items():
    data = pd.to_datetime(data_str)
    ax.axvline(data, color="#c0392b", ls="--", lw=1, alpha=0.8)
    ax.annotate(rotulo, xy=(data, preco.max()), rotation=90,
                va="top", ha="right", fontsize=8.5, color="#c0392b")

ax.set_title(f"{TICKER} × eventos geopolíticos", fontsize=13, weight="bold")
ax.set_ylabel("Preço de fechamento (US$)")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%y"))
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig("brent_geopolitica.png", dpi=120)
print("\nGráfico salvo em: brent_geopolitica.png")
plt.show()
