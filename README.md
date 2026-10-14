# 📊 Análise de Risco Geopolítico × Mercado

Ferramenta em Python que investiga **como eventos geopolíticos afetam o preço de ativos** — medindo variação de preço e mudança de volatilidade em torno de cada evento, e comparando o impacto de um mesmo choque sobre ativos diferentes.

Projeto pessoal de análise exploratória de dados (EDA) aplicada ao mercado financeiro.

## 🎯 O problema

Eventos geopolíticos (guerras, sanções, crises de oferta) movem os mercados — mas *quanto*, *quando* e *em quais ativos*? Este projeto responde isso de forma quantitativa: pega o preço histórico de um ativo, marca as datas de eventos relevantes e mede o impacto de cada um em preço e em volatilidade.

## 🔍 O que ele faz

- Baixa preços históricos de ativos via `yfinance`
- Marca eventos geopolíticos num gráfico de preço
- Para cada evento, calcula **variação %** do preço e **mudança de volatilidade** (antes vs. depois)
- **Compara vários ativos** (petróleo, dólar/real, ouro, Ibovespa) sob o mesmo choque, revelando quem sente mais e quem funciona como "porto seguro"

## 📌 Caso de estudo: a crise do Estreito de Ormuz (2026)

O petróleo em 2026 girou em torno do Estreito de Ormuz — ponto por onde passa boa parte do petróleo do mundo. O projeto analisa quatro marcos:

| Data | Evento |
|---|---|
| 28/02/2026 | Ataques EUA-Israel ao Irã; fechamento de Ormuz (Brent chegou a ~US$120) |
| 17/06/2026 | MoU de Islamabad (trégua) |
| 17/08/2026 | Expiração do MoU; reescalada e novas sanções |
| 24/09/2026 | EUA-Irã negociam reabertura |

## 💡 Insights que a análise revela

- **Choque ≠ só direção:** no fechamento de Ormuz, não foi só o preço que subiu — a **volatilidade disparou**, mostrando que o choque importou tanto pela *incerteza* criada quanto pela direção.
- **Fadiga geopolítica:** eventos sucessivos e esperados (como a expiração do MoU) tendem a mexer menos no preço do que o choque inicial surpresa — o mercado "aprende" e reage de forma mais gradual.
- **Porto seguro:** a comparação entre ativos mostra o padrão clássico de crise — petróleo e ouro reagindo diferente do real e da bolsa.

## 🛠️ Tecnologias

`Python` · `pandas` · `numpy` · `yfinance` · `matplotlib`

Código organizado em funções reutilizáveis (download, cálculo de impacto, comparação entre ativos, visualização).

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python brent_geopolitica.py
```

Edite os parâmetros no topo do script (`ATIVO_PRINCIPAL`, `ATIVOS_COMPARACAO`, `EVENTOS`, `JANELA`) para analisar outros ativos e eventos.

## 📈 Saída

- `brent_geopolitica.png` — gráfico do preço com os eventos marcados
- Tabela do impacto de cada evento sobre o Brent (variação % e volatilidade)
- Tabela comparando o impacto do choque principal entre vários ativos

---

*Projeto desenvolvido por Natalia Alcantara como estudo de análise de dados aplicada ao mercado financeiro.*

