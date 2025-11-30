# Documento do Experimento - Sprint 1



## 1. Hipóteses



* **H0 (Hipótese nula):** Não há diferença significativa no tempo de resposta entre a API REST e a API GraphQL.

* **H1 (Hipótese alternativa):** Há diferença significativa no tempo de resposta entre a API REST e a API GraphQL.



## 2. Variáveis



### Variável Independente



* Tipo de API (REST ou GraphQL)



### Variáveis Dependentes



* Tempo de resposta (ms)

* Latência média

* Número de requisições por segundo

* Taxa de erro



## 3. Tratamentos



* T1: API REST

* T2: API GraphQL



## 4. Objetos Experimentais



* Conjunto de operações CRUD aplicadas sobre a mesma base de dados:



&nbsp; * Criar Cliente

&nbsp; * Atualizar Cliente

&nbsp; * Listar Clientes

&nbsp; * Buscar Cliente por ID

&nbsp; * Remover Cliente



## 5. Tipo de Projeto Experimental



* Projeto **intragruppo**, com execução de ambos os tratamentos sobre a mesma infraestrutura.



## 6. Quantidade de Medições



* 100 execuções por operação para cada API.

* Total esperado: 500 medições REST e 500 medições GraphQL.



## 7. Ameaças à Validade



### Validade Interna



* Processos concorrentes na máquina podem influenciar o tempo de resposta.

* Falhas temporárias na rede podem alterar resultados.



### Validade Externa



* Resultados podem não representar ambientes de produção reais.



### Validade de Construção



* Scripts de medição podem conter vieses.



## 8. Preparação do Experimento



* Utilização de **Docker** para padronizar ambiente.

* Banco MariaDB previamente populado com 1.000 clientes.

* Scripts Python serão utilizados para medição automatizada.

* A API REST e GraphQL serão executadas na mesma máquina.



## 9. Ferramentas



* Docker / Docker Compose

* Python 3

* MariaDB 10+

* Apache Bench / Python Requests

* Ambiente Unix/MacOS
