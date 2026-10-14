# 📊 Análise de Risco Geopolítico × Mercado

Ferramenta em Python que investiga **como eventos geopolíticos afetam o preço de ativos**, medindo variação de preço e volatilidade em torno de cada evento. Projeto pessoal de análise exploratória de dados aplicada ao mercado financeiro.

## 🎯 O problema

Eventos geopolíticos (guerras, sanções, decisões da OPEP) movem os mercados mas *quanto*, e *quando*? Este projeto responde isso de forma quantitativa: pega o preço histórico de um ativo, marca as datas de eventos relevantes e mede o impacto de cada um em preço e em volatilidade.

## 🔍 O que ele faz

- Baixa preços históricos de ativos (petróleo Brent, dólar, ações) via `yfinance`
- Marca eventos geopolíticos num gráfico de preço
- Calcula, para cada evento:
  - **Variação %** do preço médio antes vs. depois (janela configurável)
  - **Volatilidade** (desvio-padrão dos retornos) antes vs. depois
- Gera um gráfico e uma tabela-resumo do impacto

## 💡 Exemplo de insight

Analisando o Brent em torno da invasão da Ucrânia (24/02/2022): o preço subiu **+17,5%**, mas o mais revelador foi a **volatilidade quase triplicar** (de 2,2% para 6,0% ao dia), mostrando que o choque geopolítico importou tanto pela *incerteza* criada quanto pela direção do preço. Já o embargo da UE, por já estar "precificado" pelo mercado, teve impacto muito menor: o conceito de *"buy the rumor, sell the news"* aparecendo nos dados.

## 🛠️ Tecnologias

`Python` · `pandas` · `yfinance` · `matplotlib`

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python brent_geopolitica.py
```

Edite os parâmetros no topo do script (`TICKER`, `START`, `END`, `EVENTOS`) para analisar outros ativos e eventos.

## 📈 Resultado

O script gera `brent_geopolitica.png` (preço + eventos) e imprime a tabela de impacto de cada evento no terminal.

---

*Projeto desenvolvido por Natalia Alcantara como estudo de análise de dados aplicada a mercado.*
