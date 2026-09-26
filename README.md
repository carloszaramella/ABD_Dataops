# ABD_Dataops — Data Quality & DataOps

Projeto acadêmico desenvolvido para a disciplina de **DataOps — MBA FIAP**, com foco em **Data Quality, Data Governance, automação e orquestração de pipelines de dados**.

O projeto utiliza **Python, Pandas, Jupyter Notebook, Docker e Apache Airflow** para implementar critérios de qualidade de dados e executar os testes de forma automatizada e orquestrada.

---

## 📋 Sumário

* [Sobre o projeto](#-sobre-o-projeto)
* [Objetivos](#-objetivos)
* [Arquitetura](#-arquitetura)
* [Tecnologias](#-tecnologias)
* [Estrutura do projeto](#-estrutura-do-projeto)
* [Pré-requisitos](#-pré-requisitos)
* [1. Clonar o projeto](#1-clonar-o-projeto)
* [2. Subir o ambiente Jupyter](#2-subir-o-ambiente-jupyter)
* [3. Acessar o Jupyter](#3-acessar-o-jupyter)
* [4. Executar os testes de Data Quality](#4-executar-os-testes-de-data-quality)
* [5. Subir o ambiente Airflow](#5-subir-o-ambiente-airflow)
* [6. Acessar o Airflow](#6-acessar-o-airflow)
* [7. Validar o DAG](#7-validar-o-dag)
* [8. Executar o pipeline pelo Scheduler](#8-executar-o-pipeline-pelo-scheduler)
* [9. Fluxo do pipeline](#9-fluxo-do-pipeline)
* [10. Troubleshooting](#10-troubleshooting)
* [11. Encerrar o ambiente](#11-encerrar-o-ambiente)
* [Próximos passos](#-próximos-passos)

---

# 📌 Sobre o projeto

A qualidade dos dados é um dos principais componentes de uma estratégia de DataOps e Data Governance.

O projeto implementa testes automatizados para identificar inconsistências nos dados antes que eles sejam utilizados em processos analíticos.

Os testes contemplam:

1. **Schema**
2. **Volume**
3. **Valores**
4. **Numéricos e Datas**
5. **Formatos**
6. **Unicidade**
7. **Integridade Referencial**

A lógica de validação é implementada em módulos Python reutilizáveis e pode ser utilizada tanto no notebook quanto na DAG do Airflow.

---

# 🎯 Objetivos

* Implementar testes de qualidade de dados utilizando Python.
* Validar a estrutura dos datasets.
* Identificar valores inválidos.
* Validar o volume de registros.
* Validar valores numéricos e datas.
* Validar formatos e padrões.
* Verificar unicidade.
* Validar integridade referencial.
* Executar os testes em ambiente reproduzível utilizando Docker.
* Utilizar Jupyter Notebook para desenvolvimento e evidências.
* Utilizar Apache Airflow para orquestrar os testes de Data Quality.

---

# 🏗️ Arquitetura

## Desenvolvimento e validação

```text
Dataset
   │
   ▼
Jupyter Notebook
   │
   ▼
Python / Pandas
   │
   ▼
Data Quality
```

## Execução automatizada

```text
                 Dataset
                    │
                    ▼
              Apache Airflow
                    │
                    ▼
             PythonOperator
                    │
                    ▼
              validate_all()
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     Schema      Volume      Values
        │           │           │
        └───────────┼───────────┘
                    │
                    ▼
              Numeric / Date
                    │
                    ▼
                  Format
                    │
                    ▼
                Uniqueness
                    │
                    ▼
          Referential Integrity
                    │
              ┌─────┴─────┐
              ▼           ▼
            PASS         FAIL
```

O **Airflow** é responsável pela orquestração, enquanto a lógica de validação permanece implementada em Python.

---

# 🧰 Tecnologias

| Tecnologia       | Utilização                   |
| ---------------- | ---------------------------- |
| Python           | Implementação das validações |
| Pandas           | Manipulação dos dados        |
| Jupyter Notebook | Desenvolvimento e evidências |
| Docker           | Containerização              |
| Docker Compose   | Gerenciamento dos containers |
| Apache Airflow   | Orquestração                 |
| PostgreSQL       | Metadata Database do Airflow |
| Git              | Versionamento                |
| GitHub           | Repositório                  |

---

# 📁 Estrutura do projeto

```text
ABD_Dataops/
│
├── ml/
│   ├── curso.txt
│   ├── README.md
│   └── trab_testes_data_quality.ipynb
│
├── data_quality/
│   ├── __init__.py
│   ├── schema.py
│   ├── volume.py
│   ├── values.py
│   ├── numeric_dates.py
│   ├── formats.py
│   ├── uniqueness.py
│   └── referential_integrity.py
│
├── airflow/
│   ├── dags/
│   │   └── data_quality_dag.py
│   ├── logs/
│   └── plugins/
│
├── docker-compose-jupyter.yml
├── docker-compose-airflow.yml
├── validate_airflow.sh
├── README.md
├── config_cdc.sh
├── remove.sh
├── trabalho.sh
├── run_datacatalog.sh
├── local_run_openmetadata.sh
├── kowl_config.yaml
└── mysql/
```

---

# 💻 Pré-requisitos

Instale:

* Git
* Docker
* Docker Compose
* VS Code
* Extensão Python
* Extensão Jupyter

Verifique o Docker:

```bash
docker --version
```

Verifique o Docker Compose:

```bash
docker compose version
```

O projeto utiliza a sintaxe atual:

```bash
docker compose
```

e não:

```bash
docker-compose
```

---

# 1. Clonar o projeto

```bash
git clone https://github.com/carloszaramella/ABD_Dataops.git
```

Entre no projeto:

```bash
cd ABD_Dataops
```

Verifique os arquivos:

```bash
ls
```

---

# 2. Subir o ambiente Jupyter

O ambiente Jupyter/AutoML é executado através do Docker Compose.

Execute:

```bash
docker compose -f docker-compose-jupyter.yml up -d
```

Verifique os containers:

```bash
docker ps
```

O container deverá aparecer como `Up`.

Exemplo:

```text
abd_dataops-automl-1
```

O projeto publica:

```text
HOST 8789 → CONTAINER 8888
```

---

# 3. Acessar o Jupyter

Utilize:

```text
http://127.0.0.1:8789
```

> **Importante:** neste ambiente Linux/WSL, utilize `127.0.0.1` em vez de `localhost` quando houver problema de resolução IPv6.

O endereço interno do container é diferente do endereço utilizado pelo navegador da máquina host.

---

## 🔐 Token do Jupyter

Para obter o token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

O resultado será semelhante a:

```text
http://127.0.0.1:8888/?token=SEU_TOKEN
```

Para acessar pela máquina host, utilize a porta publicada:

```text
http://127.0.0.1:8789/?token=SEU_TOKEN
```

O token pode mudar quando o container/Jupyter for reiniciado.

---

# 4. Executar os testes de Data Quality

O notebook principal está localizado em:

```text
ml/trab_testes_data_quality.ipynb
```

Abra o arquivo no VS Code ou no Jupyter.

O notebook contém as implementações e evidências dos testes de qualidade de dados.

> **Importante:** um arquivo `.ipynb` não deve ser executado diretamente pelo Bash.

Não faça:

```bash
ml/trab_testes_data_quality.ipynb
```

Para trabalhar com o notebook, abra-o pelo VS Code ou Jupyter.

---

# 5. Subir o ambiente Airflow

O Airflow é executado separadamente através do:

```text
docker-compose-airflow.yml
```

Suba o ambiente:

```bash
docker compose -f docker-compose-airflow.yml up -d
```

Verifique os serviços:

```bash
docker compose -f docker-compose-airflow.yml ps
```

A configuração atual utiliza:

```text
airflow-postgres
airflow-webserver
airflow-scheduler
```

O PostgreSQL é utilizado como **metadata database do Airflow**.

O ambiente também pode apresentar o serviço:

```text
abd_dataops-automl-1
```

que é responsável pelo Jupyter/AutoML.

---

## Serviços e portas

```text
Airflow Webserver
127.0.0.1:8080 → container:8080

Jupyter / AutoML
127.0.0.1:8789 → container:8888
```

---

# 6. Acessar o Airflow

Abra:

```text
http://127.0.0.1:8080
```

Login:

```text
Usuário: admin
Senha: admin
```

> **Importante:** utilize `127.0.0.1:8080` em vez de `localhost:8080` neste ambiente.

O acesso por `127.0.0.1:8080` foi validado com sucesso.

---

# 7. Validar o DAG

O DAG implementado no projeto é:

```text
data_quality_checks
```

Arquivo:

```text
airflow/dags/data_quality_dag.py
```

Para verificar se o Airflow reconhece o DAG:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags list
```

O resultado deverá conter:

```text
data_quality_checks
```

---

## Verificar erros de importação

Execute:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags list-import-errors
```

Se não houver erros, o DAG foi carregado corretamente.

---

## Testar o DAG diretamente

Para executar o DAG em modo de teste:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags test data_quality_checks 2026-09-26
```

Esse comando executa o DAG diretamente e permite validar a lógica sem depender do agendamento do Scheduler.

O resultado esperado é:

```text
Marking task as SUCCESS
```

e:

```text
Marking run ... state:success
```

### Resultado validado no projeto

A execução foi realizada com sucesso e apresentou:

```text
Data Quality: PASS
```

Foram validados:

* Schema
* Volume
* Values
* Numeric / Date
* Formats
* Uniqueness
* Referential Integrity

A execução validada apresentou:

```text
199 registros
199 matrículas únicas
```

e:

```text
DagRun ... state:success
```

---

# 8. Executar o pipeline pelo Scheduler

Para executar o pipeline através do Airflow Scheduler, utilize:

```bash
docker compose -f docker-compose-airflow.yml exec airflow-webserver \
  airflow dags trigger data_quality_checks
```

O comando retorna o `run_id` da execução.

Depois acompanhe o Scheduler:

```bash
docker compose -f docker-compose-airfl
```
