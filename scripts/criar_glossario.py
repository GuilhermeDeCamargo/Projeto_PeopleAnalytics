import pandas as pd
import os

# caminhos
path_atual = os.getcwd()
path_salvar = os.path.join(os.path.dirname(path_atual),'glossario.md')

# informacoes glossario
dados_glossario = [
    ["employee_id", "string", "Identificador único do colaborador.", "Formato: EMP_XXXXX."],
    ["job_title", "string", "Cargo atual do colaborador.", "-"],
    ["department", "string", "Departamento do colaborador.", "-"],
    ["location", "string", "Cidade onde o colaborador atua.", "-"],
    ["salary", "float", "Salário mensal em reais.", "Formato: Positivo com 2 casas decimais."],
    ["hire_date", "date", "Data de admissão.", "Formato: YYYY-MM-DD."],
    ["termination_date", "date", "Data de desligamento (se aplicável).", "Formato: YYYY-MM-DD."],
    ["is_active", "boolean", "Se o colaborador está ativo.", "Valores: True ou False."],
    ["absence_days", "int", "Dias de ausência registrados.", "Valores: positivos ou zero."],
    ["sick_days", "int", "Dias de atestado médico.", "Valores: positivos ou zero."],
    ["vacation_days_taken", "int", "Dias de férias tirados.", "Valores: entre 0 e 30 dias."],
    ["bank_hours", "int", "Horas acumuladas no banco de horas.", "Valores: positivos ou negativos."],
    ["overtime_hours", "int", "Horas extras trabalhadas.", "Valores: positivos ou zero."],
    ["tardiness_count", "int", "Número de atrasos.", "Valores: positivos ou zero."],
    ["gender", "string", "Gênero do colaborador.", "Valores: Masculino, Feminino ou Outro."],
    ["marital_status", "string", "Estado civil.", "Valores: Viúvo, Casado, Solteiro, Divorciado ou Outro."],
    ["number_of_dependents", "int", "Número de dependentes.", "Valores: positivos ou zero."],
    ["education_level", "string", "Nível de escolaridade.", "Valores: Ensino Médio, Bacharelado, Mestrado ou Doutorado."],
    ["performance_rating", "int", "Avaliação de desempenho.", "Valores: entre 1 a 5."],
    ["bonus_percentage", "float", "Porcentagem de bônus.", r"Valores: entre 0% e 100%."],
    ["shift", "string", "Turno de trabalho.", "Valores: Diurno, Vespertino ou Noturno."],
    ["contract_type", "string", "Tipo de contrato.", "Valores: Efetivo, Temporário ou Terceiro."],
    ["cost_center", "string", "Código do centro de custo.", "Formato: CCXXX."],
    ["compliance_status", "string", "Status de conformidade.", "Valores: Conforme ou Não-Conforme."],
    ["health_plan", "string", "Tipo de plano de saúde.", "Valores: Basic, Standard ou Premium."],
    ["email", "string", "E-mail corporativo.", "-"],
    ["tenure_years", "float", "Tempo de casa em anos.", "Valores: positivos ou zero."],
    ["probation_completed", "boolean", "Completou período de experiência.", "Valores: True ou False."],
    ["manager_id", "string", "ID do gestor imediato.", "Formato: EMP_XXXXX."],
    ["last_promotion_date", "date", "Data da última promoção.", "Formato: YYYY-MM-DD."],
    ["last_training_date", "date", "Data do último treinamento.", "Formato: YYYY-MM-DD."]
]

df_glossario = pd.DataFrame(dados_glossario, columns=["coluna_tabela", "tipo", "descricao", "observacoes"])

# Salvar como arquivo markdown
df_glossario.to_markdown(path_salvar, index=False)
