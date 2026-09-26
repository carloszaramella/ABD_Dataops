# ABD_Dataops — Data Quality & DataOps

Projeto acadêmico do **DataOps — MBA FIAP**, com foco em **Data Quality, automação e orquestração de pipelines**.

A solução utiliza **Python, Pandas, Jupyter Notebook, Docker e Apache Airflow** para executar validações de qualidade de dados. fileciteturn4file0L1-L5

## 🎯 Objetivos

- Validar schema, volume e valores.
- Validar dados numéricos e datas.
- Validar formatos.
- Verificar unicidade.
- Validar integridade referencial.
- Executar as validações de forma reproduzível com Docker.
- Orquestrar os testes com Airflow. fileciteturn4file0L49-L71

## 🏗️ Arquitetura

```text
Dataset
   │
   ▼
Jupyter / Python / Pandas
   │
   ▼
Data Quality
   │
   ▼
Apache Airflow
   │
   ▼
validate_all()
   │
   ├── Schema
   ├── Volume
   ├── Valores
   ├── Numeric / Date
   ├── Formats
   ├── Uniqueness
   └── Referential Integrity
   │
   ▼
PASS / FAIL
```

O **Airflow** realiza a orquestração e as regras permanecem implementadas em Python. fileciteturn4file0L101-L127 fileciteturn4file0L129-L199

## 🧰 Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Validações |
| Pandas | Dados |
| Jupyter | Desenvolvimento e evidências |
| Docker / Compose | Ambiente |
| Airflow | Orquestração |
| PostgreSQL | Metadata do Airflow |
| Git / GitHub | Versionamento |

## 📁 Estrutura

```text
ABD_Dataops/
├── ml/
│   ├── curso.txt
│   └── trab_testes_data_quality.ipynb
├── data_quality/
│   ├── schema.py
│   ├── volume.py
│   ├── values.py
│   ├── numeric_dates.py
│   ├── formats.py
│   ├── uniqueness.py
│   └── referential_integrity.py
├── airflow/
│   └── dags/
│       └── data_quality_dag.py
├── docker-compose-jupyter.yml
├── docker-compose-airflow.yml
├── validate_airflow.sh
└── README.md
```

## 💻 Pré-requisitos

- Git
- Docker
- Docker Compose
- VS Code / Jupyter

Verifique:

```bash
docker --version
docker compose version
```

## 1. Jupyter

Subir:

```bash
docker compose -f docker-compose-jupyter.yml up -d
```

Acessar:

```text
http://127.0.0.1:8789
```

Token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

Notebook:

```text
ml/trab_testes_data_quality.ipynb
```

> O `.ipynb` não deve ser executado diretamente pelo Bash. Abra pelo Jupyter ou VS Code. fileciteturn4file0L381-L491

## 2. Airflow

Subir:

```bash
docker compose -f docker-compose-airflow.yml up -d
```

Ou:

```bash
./validate_airflow.sh
```

Verificar:

```bash
docker compose -f docker-compose-airflow.yml ps
```

Acessar:

```text
http://127.0.0.1:8080
```

Login:

```text
admin
admin
```

## 3. Validar a DAG

DAG:

```text
data_quality_checks
```

Verificar:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver   airflow dags list
```

Verificar erros:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver   airflow dags list-import-errors
```

Teste direto:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver   airflow dags test data_quality_checks 2026-09-26
```

Resultado esperado:

```text
Marking task as SUCCESS
DagRun ... state:success
```

A execução validada processou **199 registros e 199 matrículas únicas**, com os critérios de Data Quality aprovados. fileciteturn4file0L643-L715

## 4. Executar pelo Scheduler

Disparar:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver   airflow dags trigger data_quality_checks
```

Acompanhar:

```bash
docker compose -f docker-compose-airflow.yml logs -f airflow-scheduler
```

Fluxo:

```text
DAG
 ↓
Scheduler
 ↓
validate_data_quality
 ↓
validate_all()
 ↓
Data Quality
 ↓
SUCCESS / FAIL
```

## 🧹 Encerrar

Airflow:

```bash
docker compose -f docker-compose-airflow.yml down
```

Jupyter:

```bash
docker compose -f docker-compose-jupyter.yml down
```

## 🚀 Próximas evoluções

- [x] Módulos de Data Quality
- [x] DAG do Airflow
- [x] Execução pelo Scheduler
- [x] Validação do pipeline
- [ ] Logs estruturados
- [ ] Alertas de qualidade
- [ ] CI/CD
- [ ] Data Catalog e lineage

## 👨‍💻 Autor

**Carlos Zaramella**

Projeto acadêmico — MBA FIAP — DataOps.

**Repositório:**  
https://github.com/carloszaramella/ABD_Dataops