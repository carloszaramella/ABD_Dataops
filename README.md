# ABD_Dataops — Data Quality & DataOps

Projeto acadêmico desenvolvido para a disciplina de **DataOps — MBA FIAP**, com foco em **Data Quality, Data Governance, automação e orquestração de pipelines de dados**.

O projeto utiliza **Python, Pandas, Jupyter Notebook e Docker** para implementar critérios de qualidade de dados e, como evolução da solução, utiliza **Apache Airflow** para orquestrar a execução dos testes.

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
* [4. Entender porta e token](#4-entender-porta-e-token)
* [5. Executar os testes](#5-executar-os-testes)
* [6. Data Quality](#6-data-quality)
* [7. Orquestração com Airflow](#7-orquestração-com-airflow)
* [8. Fluxo do pipeline](#8-fluxo-do-pipeline)
* [9. Validação da execução](#9-validação-da-execução)
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

Esses critérios correspondem aos cenários definidos no trabalho acadêmico.

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
* Evoluir os testes para uma execução orquestrada pelo Apache Airflow.

---

# 🏗️ Arquitetura

A solução é dividida em duas partes.

### Desenvolvimento e validação

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
Testes de Data Quality
```

### Execução automatizada

```text
Dataset
   │
   ▼
Airflow
   │
   ├── Schema
   ├── Volume
   ├── Valores
   ├── Numéricos e Datas
   ├── Formatos
   ├── Unicidade
   └── Integridade Referencial
           │
           ▼
       Resultado
        ┌──┴──┐
        ▼     ▼
       PASS  FAIL
```

O Airflow será responsável pela **orquestração**, enquanto a lógica de validação permanecerá implementada em Python.

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
| Git              | Versionamento                |
| GitHub           | Repositório                  |

---

# 📁 Estrutura do projeto

```text
ABD_Dataops/
│
├── ml/
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

> A estrutura `airflow/` será utilizada na evolução da solução para orquestração dos testes.

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

O ambiente Jupyter é executado através do Docker Compose.

Execute:

```bash
docker compose -f docker-compose-jupyter.yml up -d
```

Verifique o container:

```bash
docker ps
```

O container deverá aparecer como `Up`.

Exemplo:

```text
abd_dataops-automl-1
```

O Compose publica a porta `8888` do container na porta `8789` da máquina local.

---

# 3. Acessar o Jupyter

O Jupyter pode ser acessado pelo navegador:

```text
http://localhost:8789
```

ou:

```text
http://127.0.0.1:8789
```

---

# 4. Entender porta e token

## 🔌 Porta

O Docker realiza o seguinte mapeamento:

```text
HOST                  CONTAINER

localhost:8789  ───►  8888
                         │
                         ▼
                       Jupyter
```

Portanto:

```text
http://127.0.0.1:8888
```

é a porta interna do container e não é a URL utilizada normalmente pelo navegador da máquina host.

O acesso deve ser feito pela porta publicada:

```text
http://127.0.0.1:8789
```

---

## 🔐 Token do Jupyter

O Jupyter utiliza um token de autenticação para permitir o acesso ao servidor.

Para obter o token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

O resultado será semelhante a:

```text
http://127.0.0.1:8888/?token=SEU_TOKEN
```

O token é a sequência existente depois de:

```text
?token=
```

Por exemplo:

```text
?token=44ea7656364e7875130beb913cd3ceeb6a9777de5a297bf6
```

Para acessar pela máquina host, utilize a porta publicada:

```text
http://127.0.0.1:8789/?token=SEU_TOKEN
```

### Importante

O token pode mudar quando o container/Jupyter for reiniciado.

Por isso, se o acesso pelo navegador solicitar autenticação novamente, consulte os logs do container:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

---

# 5. Executar os testes

O notebook principal está localizado em:

```text
ml/trab_testes_data_quality.ipynb
```

Abra o arquivo no VS Code ou no Jupyter.

O notebook contém as implementações dos testes de qualidade.

A execução deve ser realizada na sequência apresentada no notebook.

---

# 6. Data Quality

## 6.1 Schema

Verifica:

* existência das colunas;
* quantidade de colunas;
* tipos;
* estrutura esperada.

Exemplo:

```text
ID → INTEGER
NOTA_MAT_1 ... NOTA_MAT_4 → NUMERIC
```

---

## 6.2 Volume

Verifica se a quantidade de registros está dentro do volume esperado.

Exemplo:

```text
19.000 ≤ registros ≤ 21.100
```

---

## 6.3 Valores

Verifica se os valores estão dentro dos conjuntos esperados.

Exemplo:

```text
PERFIL ∈ {
    "DIFICULDADE",
    "MUITO BOM",
    "EXCELENTE"
}
```

---

## 6.4 Numéricos e Datas

Valida intervalos e regras numéricas.

Exemplo:

```text
0 ≤ NOTA_MAT_1 ≤ 10
```

Podem também ser avaliados:

* média;
* mediana;
* desvio padrão;
* somatórios;
* intervalos de datas.

---

## 6.5 Formatos

Valida padrões dos dados.

Exemplo:

```text
NOME → máximo de 157 caracteres

MATRICULA → 6 dígitos numéricos
```

---

## 6.6 Unicidade

Verifica duplicidades em campos que devem ser únicos.

Exemplo:

```text
ID → único

MATRICULA → única
```

---

## 6.7 Integridade Referencial

Verifica a consistência entre dados.

Exemplo:

```text
REPROVACOES_MAT_1 > 0
        ↓
NOTA_MAT_1 < 4
```

Também pode validar a existência de uma `MATRICULA` em uma tabela de referência.

---

# 7. Orquestração com Airflow

Como evolução da solução, os testes serão executados através do **Apache Airflow**.

A abordagem é inspirada na estrutura do projeto de referência `tonanuvem/datagov`, que utiliza scripts de inicialização, DAGs e scripts de validação da execução do pipeline.

No projeto de referência, o Airflow é utilizado como camada de orquestração e as DAGs são posteriormente validadas por um script que dispara a DAG, acompanha seu estado e verifica os resultados.

No `ABD_Dataops`, essa abordagem será adaptada para os testes de Data Quality.

## Estrutura implementada

```text
ABD_Dataops/
│
├── ml/
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
└── .venv/
```

A lógica de qualidade foi separada em módulos reutilizáveis e agora é utilizada tanto no notebook para demonstração acadêmica quanto na DAG do Airflow para execução orquestrada.


---

# 8. Fluxo do pipeline

A DAG deverá executar:

```text
START
  │
  ▼
LOAD DATA
  │
  ▼
SCHEMA TEST
  │
  ▼
VOLUME TEST
  │
  ▼
VALUES TEST
  │
  ▼
NUMERIC / DATE TEST
  │
  ▼
FORMAT TEST
  │
  ▼
UNIQUENESS TEST
  │
  ▼
REFERENTIAL INTEGRITY
  │
  ▼
END
```

Cada tarefa deverá produzir um resultado de sucesso ou falha.

---

# 9. Validação da execução

Assim como no projeto de referência, será criado um script de validação para:

1. verificar se a DAG está registrada;
2. executar a DAG;
3. acompanhar sua execução;
4. identificar `success` ou `failed`;
5. consultar os logs;
6. apresentar um resumo da execução.

Exemplo:

```bash
./airflow/validate_pipeline.sh
```

Resultado esperado:

```text
=== Validação do Pipeline ===

DAG registrada: OK

Executando Data Quality Pipeline...

Schema: PASS
Volume: PASS
Values: PASS
Numeric/Date: PASS
Format: PASS
Uniqueness: PASS
Referential Integrity: PASS

Pipeline concluído com sucesso.
```

---

# 🔄 Fluxo completo DataOps

A solução final será organizada da seguinte maneira:

```text
                  ┌──────────────┐
                  │    Dataset   │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Airflow   │
                  │ Orquestração │
                  └──────┬───────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Data Quality    │
                │ Python / Pandas │
                └────────┬────────┘
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
                    ┌────┴────┐
                    ▼         ▼
                  PASS       FAIL
                    │         │
                    ▼         ▼
                 Success     Logs
```

---

# 🛠️ Troubleshooting

## `docker-compose: command not found`

Utilize:

```bash
docker compose
```

em vez de:

```bash
docker-compose
```

---

## Jupyter não abre

Verifique:

```bash
docker ps
```

Depois consulte:

```bash
docker logs abd_dataops-automl-1
```

Para localizar o token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

---

## Token inválido

O token pode ter sido renovado após o restart do container.

Obtenha o novo token:

```bash
docker logs abd_dataops-automl-1 2>&1 | grep -i token
```

---

## Container parado

Suba novamente:

```bash
docker compose -f docker-compose-jupyter.yml up -d
```

Verifique:

```bash
docker ps
```

---

# 🧹 Encerrar o ambiente

Para parar os serviços:

```bash
docker compose -f docker-compose-jupyter.yml down
```

Para verificar os containers:

```bash
docker ps
```

---

# 🚀 Próximas evoluções

* [ ] Implementar DAG do Airflow
* [ ] Separar regras de Data Quality em módulos Python
* [ ] Criar script de validação do pipeline
* [ ] Implementar logs estruturados
* [ ] Implementar tratamento de falhas
* [ ] Criar alertas para falhas de qualidade
* [ ] Integrar com CI/CD
* [ ] Avaliar Great Expectations
* [ ] Avaliar dbt
* [ ] Adicionar Data Catalog
* [ ] Implementar lineage

---

# 👨‍💻 Autor

**Carlos Zaramella**

Projeto acadêmico — MBA FIAP — DataOps.

## 🔗 Repositório

https://github.com/carloszaramella/ABD_Dataops
