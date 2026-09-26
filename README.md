# ABD_Dataops — Data Quality & DataOps

Projeto acadêmico do **DataOps — MBA FIAP**, com foco em **Data Quality, automação e orquestração de pipelines**.

A solução utiliza **Python, Pandas, Jupyter Notebook, Docker e Apache Airflow** para executar e orquestrar validações de qualidade de dados.

## 🎯 Objetivos

* Validar schema, volume e valores.
* Validar dados numéricos e datas.
* Validar formatos.
* Verificar unicidade.
* Validar integridade referencial.
* Executar as validações de forma reproduzível com Docker.
* Orquestrar as validações com Airflow.

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

O **Airflow atua como orquestrador**. As regras de Data Quality permanecem implementadas nos módulos Python dentro de `data_quality/`.

A DAG chama a função central `validate_all()`, que executa todas as validações utilizadas no notebook.

## 🧰 Tecnologias

| Tecnologia       | Uso                          |
| ---------------- | ---------------------------- |
| Python           | Regras de Data Quality       |
| Pandas           | Manipulação dos dados        |
| Jupyter          | Desenvolvimento e evidências |
| Docker / Compose | Ambiente de execução         |
| Apache Airflow   | Orquestração                 |
| PostgreSQL       | Metadata do Airflow          |
| Git / GitHub     | Versionamento                |

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

* Git
* Docker
* Docker Compose
* VS Code / Jupyter

Verifique:

```bash
docker --version
docker compose version
```

## 1. Jupyter

Subir o ambiente:

```bash
docker compose -f docker-compose-jupyter.yml up -d
```

Acessar:

```text
http://127.0.0.1:8789
```

Para consultar o token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

Notebook:

```text
ml/trab_testes_data_quality.ipynb
```

> O arquivo `.ipynb` deve ser aberto pelo Jupyter ou VS Code, e não executado diretamente pelo Bash.

## 2. Airflow

Subir o ambiente:

```bash
docker compose -f docker-compose-airflow.yml up -d
```

Ou utilizar o script de validação:

```bash
./validate_airflow.sh
```

Verificar os containers:

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

Verificar se a DAG foi carregada:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags list
```

Verificar erros de importação:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags list-import-errors
```

Executar um teste direto:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags test data_quality_checks 2026-09-26
```

Resultado esperado:

```text
Marking task as SUCCESS
DagRun ... state:success
```

A DAG executa a função `validate_all()`, responsável por aplicar todas as regras de Data Quality utilizadas no projeto.

## 4. Executar pelo Scheduler

Disparar a DAG:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags trigger data_quality_checks
```

Acompanhar a execução:

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
run_quality_checks()
 ↓
validate_all()
 ↓
Data Quality
 ↓
SUCCESS / FAIL
```

A task `validate_data_quality` executa todas as validações por meio do `validate_all()`.

## 🧹 Encerrar

Airflow:

```bash
docker compose -f docker-compose-airflow.yml down
```

Jupyter:

```bash
docker compose -f docker-compose-jupyter.yml down
```


