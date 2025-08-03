import pandas as pd
import numpy as np
import os

# Caminhos
path_atual = os.getcwd()
path_salvar = os.path.join(os.path.dirname(path_atual), 'dados')
path_arq_origem = os.path.join(path_salvar, 'base_headcount.csv')

# Tabela original
df_origem = pd.read_csv(path_arq_origem, sep=',', encoding='utf-8', dtype=str, on_bad_lines='warn')
df_origem.columns = df_origem.columns.str.strip().str.lower()

# Verificando dados
nome_colunas = df_origem.columns.tolist()
check_nulos = df_origem.isnull().sum()

# Padronizando escrita
for col in nome_colunas:
    if df_origem[col].dtype == 'object':
        df_origem[col] = df_origem[col].str.strip().str.lower()
    else:
        pass

# Verificando duplicidades
duplicados = df_origem.duplicated().sum()

ids_duplicados = df_origem['employee_id'].value_counts()
ids_duplicados = ids_duplicados[ids_duplicados > 1].index.tolist()

# Convertendo tipos de dados
df_origem['salary'] = df_origem['salary'].astype('float64')
df_origem['hire_date'] = pd.to_datetime(df_origem['hire_date'], errors='coerce')
df_origem['termination_date'] = pd.to_datetime(df_origem['termination_date'], errors='coerce')
df_origem['is_active'] = df_origem['is_active'].astype('bool')
df_origem['absence_days'] = df_origem['absence_days'].astype('Int64')
df_origem['sick_days'] = df_origem['sick_days'].astype('Int64')
df_origem['vacation_days_taken'] = df_origem['vacation_days_taken'].astype('Int64')
df_origem['bank_hours'] = df_origem['bank_hours'].astype('float64')
df_origem['overtime_hours'] = df_origem['overtime_hours'].astype('float64')
df_origem['tardiness_count'] = df_origem['tardiness_count'].astype('Int64')
df_origem['number_of_dependents'] = df_origem['number_of_dependents'].astype('Int64')
df_origem['performance_rating'] = df_origem['performance_rating'].astype('Int64')
df_origem['bonus_percentage'] = df_origem['bonus_percentage'].astype('float64')
df_origem['tenure_years'] = df_origem['tenure_years'].astype('float64')
df_origem['probation_completed'] = df_origem['probation_completed'].astype('bool')
df_origem['last_promotion_date'] = pd.to_datetime(df_origem['last_promotion_date'], errors='coerce')
df_origem['last_training_date'] = pd.to_datetime(df_origem['last_training_date'], errors='coerce')

# Criar tabela dimensão dos empregados
dim_empregados = df_origem[[
    "employee_id", "job_title", "department", "location", "gender", "marital_status",
    "number_of_dependents", "education_level", "shift", "contract_type", "cost_center",
    "health_plan", "email", "manager_id","hire_date", "termination_date", "is_active", "salary",
]].drop_duplicates()

# Criar tabela fato dos lancamentos
fato_lancamentos = df_origem[[
    "employee_id", "absence_days", "sick_days", "vacation_days_taken", "bank_hours",
    "overtime_hours", "tardiness_count", "performance_rating", "bonus_percentage",
    "tenure_years", "probation_completed", "last_promotion_date", "last_training_date",
    "compliance_status"
]]

# Salvando tabelas
dim_empregados.to_csv(os.path.join(path_salvar, 'dim_empregados.csv'), index=False, encoding='utf-8', sep=';', decimal=',')
fato_lancamentos.to_csv(os.path.join(path_salvar, 'fato_lancamentos.csv'), index=False, encoding='utf-8', sep=';', decimal=',')