| coluna_tabela        | tipo    | descricao                            | observacoes                                                |
|:---------------------|:--------|:-------------------------------------|:-----------------------------------------------------------|
| absence_days         | int     | Dias de ausência registrados.        | Valores: positivos ou zero.                                |
| bank_hours           | int     | Horas acumuladas no banco de horas.  | Valores: positivos ou negativos.                           |
| bonus_percentage     | float   | Porcentagem de bônus.                | Valores: entre 0% e 100%.                                  |
| compliance_status    | string  | Status de conformidade.              | Valores: Conforme ou Não-Conforme.                         |
| contract_type        | string  | Tipo de contrato.                    | Valores: Efetivo, Temporário ou Terceiro.                  |
| cost_center          | string  | Código do centro de custo.           | Formato: CCXXX.                                            |
| department           | string  | Departamento do colaborador.         | -                                                          |
| education_level      | string  | Nível de escolaridade.               | Valores: Ensino Médio, Bacharelado, Mestrado ou Doutorado. |
| email                | string  | E-mail corporativo.                  | -                                                          |
| employee_id          | string  | Identificador único do colaborador.  | Formato: EMP_XXXXX.                                        |
| gender               | string  | Gênero do colaborador.               | Valores: Masculino, Feminino ou Outro.                     |
| health_plan          | string  | Tipo de plano de saúde.              | Valores: Basic, Standard ou Premium.                       |
| hire_date            | date    | Data de admissão.                    | Formato: YYYY-MM-DD.                                       |
| is_active            | boolean | Se o colaborador está ativo.         | Valores: True ou False.                                    |
| job_title            | string  | Cargo atual do colaborador.          | -                                                          |
| last_promotion_date  | date    | Data da última promoção.             | Formato: YYYY-MM-DD.                                       |
| last_training_date   | date    | Data do último treinamento.          | Formato: YYYY-MM-DD.                                       |
| location             | string  | Cidade onde o colaborador atua.      | -                                                          |
| manager_id           | string  | ID do gestor imediato.               | Formato: EMP_XXXXX.                                        |
| marital_status       | string  | Estado civil.                        | Valores: Viúvo, Casado, Solteiro, Divorciado ou Outro.     |
| number_of_dependents | int     | Número de dependentes.               | Valores: positivos ou zero.                                |
| overtime_hours       | int     | Horas extras trabalhadas.            | Valores: positivos ou zero.                                |
| performance_rating   | int     | Avaliação de desempenho.             | Valores: entre 1 a 5.                                      |
| probation_completed  | boolean | Completou período de experiência.    | Valores: True ou False.                                    |
| salary               | float   | Salário mensal em reais.             | Formato: Positivo com 2 casas decimais.                    |
| shift                | string  | Turno de trabalho.                   | Valores: Diurno, Vespertino ou Noturno.                    |
| sick_days            | int     | Dias de atestado médico.             | Valores: positivos ou zero.                                |
| tardiness_count      | int     | Número de atrasos.                   | Valores: positivos ou zero.                                |
| tenure_years         | float   | Tempo de casa em anos.               | Valores: positivos ou zero.                                |
| termination_date     | date    | Data de desligamento (se aplicável). | Formato: YYYY-MM-DD.                                       |
| vacation_days_taken  | int     | Dias de férias tirados.              | Valores: entre 0 e 30 dias.                                |