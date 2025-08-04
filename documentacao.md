# Documentação Técnica do Projeto

## 1. Objetivo
O objetivo deste projeto é analisar dados fictícios de Recursos Humanos e transformá-los em informações úteis através de limpeza, estruturação e visualização.

## 2. Arquivos Criados

### `dados/base_headcount.csv`
Base original com dados brutos dos colaboradores.

### `glossario.md`
Glossário criado via script python `criar_glossario.py`, com descrição, tipo, e observações de cada coluna da base.

### `scripts/gerar_tabelas.py`
Script responsável por quebrar a base original em:
- `dados/fato_lancamentos.csv`: contém atributos principais como salário, faltas, horas extras e etc.
- `dados/dim_empregados.csv`: informações gerais sobre os colaboradores.

### `power_bi/dashboard_rh.pbix`
Dashboard com filtros por cargo, departamento, localização, além de KPIs como:
- Headcount
- Admitidos
- Desligados
- Turnover
- Absenteísmo
- Horas Extras
- Banco de Horas

### `apresentacao/apresentacao.pdf`
Apresentação visual com insights e recomendações baseadas nos dados.

## 3. Tecnologias Utilizadas
- Python 3.12.10
- Pandas
- Power BI Desktop
- Git & GitHub
- Power Point