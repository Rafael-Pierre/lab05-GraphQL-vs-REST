# Documento do Experimento: REST vs GraphQL

## 1. Hipóteses

Para responder à RQ1 (Desempenho Temporal):
* **H0 (Hipótese nula):** Não há diferença significativa no tempo de resposta entre a API REST e a API GraphQL.
* **H1 (Hipótese alternativa):** Há diferença significativa no tempo de resposta entre a API REST e a API GraphQL.

Para responder à RQ2 (Eficiência de Dados/Tamanho):
* **H0 (Hipótese nula):** Não há diferença significativa no tamanho do payload (resposta) entre a API REST e a API GraphQL.
* **H1 (Hipótese alternativa):** O tamanho da resposta da API GraphQL é significativamente menor que o da API REST (devido à eliminação de *overfetching*).

## 2. Variáveis

**Variável Independente**
* Tipo de API (Níveis: REST e GraphQL).

**Variáveis Dependentes**
1.  **Tempo de resposta (ms):** Tempo decorrido entre o envio da requisição e o recebimento completo da resposta.
2.  **Tamanho da resposta (bytes):** Quantidade total de dados trafegados no corpo da resposta (*payload*).

## 3. Tratamentos

* **T1 (REST):** Requisição `GET` ao endpoint `/api/character` retornando a lista padrão de personagens com todos os campos.
* **T2 (GraphQL):** Requisição `POST` ao endpoint `/graphql` com uma *query* específica selecionando apenas os campos `id`, `name` e `status`.

## 4. Objetos Experimentais

* Consulta de leitura (Read) da primeira página de dados da API pública **"The Rick and Morty API"**.
* Ambos os tratamentos recuperam a mesma entidade lógica (lista de 20 personagens).

## 5. Tipo de Projeto Experimental

Experimento controlado de fator único (Tipo de API) com dois níveis. O experimento utiliza amostras independentes executadas sequencialmente.

## 6. Quantidade de Medições

* 30 execuções para o tratamento REST.
* 30 execuções para o tratamento GraphQL.
* **Total:** 60 medições coletadas.

## 7. Ameaças à Validade

**Validade Interna**
* **Latência de Rede:** Como utilizamos uma API pública, variações na conexão de internet da universidade/local podem introduzir ruído nas medições de tempo.
* **Overhead do Cliente:** O tempo de processamento do script Python (biblioteca `requests`) está incluído no tempo total.

**Validade Externa**
* **Generalização:** Os resultados são específicos para a estrutura da API "Rick and Morty". Outras implementações de GraphQL podem ter performances diferentes dependendo da complexidade dos *resolvers* no servidor.

**Validade de Construção**
* A comparação é feita entre uma chamada REST "padrão" (que traz tudo) e uma chamada GraphQL "otimizada". Isso reflete o uso real da tecnologia, mas favorece o GraphQL na métrica de tamanho.

## 8. Preparação do Experimento

* Utilização de *scripts* em **Python** para automação das chamadas.
* Utilização da biblioteca **Pandas** para armazenamento e manipulação dos dados.
* Configuração de *bypass* de verificação SSL (`verify=False`) para garantir execução em ambiente de rede corporativo/acadêmico.
* Garantia de que ambas as requisições buscam o mesmo número de registros (20 itens) para comparação justa.

## 9. Ferramentas

* **Linguagem:** Python 3.x
* **Coleta de Dados:** Biblioteca `requests`
* **Análise Estatística:** Bibliotecas `scipy.stats` (Teste T) e `pandas`
* **Visualização:** Bibliotecas `matplotlib` e `seaborn`
* **Objeto de Estudo:** The Rick and Morty API (Public API)


## 10. Análise de Resultados

O experimento foi executado com sucesso utilizando a API pública "The Rick and Morty API". Foram coletadas 30 amostras para cada abordagem (REST e GraphQL), totalizando 60 medições.

Os dados brutos obtidos foram:

Tempo Médio: REST (119.33 ms) vs GraphQL (160.15 ms).

Tamanho Médio (Payload): REST (19.496 bytes) vs GraphQL (1.074 bytes).

## 11. Discussão e Respostas às Perguntas de Pesquisa

RQ1. Respostas às consultas GraphQL são mais rápidas que respostas às consultas REST? Resposta: Não necessariamente. No experimento, o REST foi ligeiramente mais rápido em média (119ms contra 160ms).

Análise Estatística: O Teste T retornou um p-valor de 0.1368. Como este valor é maior que 0.05 (nível de significância), concluímos que não há diferença estatisticamente significativa entre os tempos.

Discussão: O atraso leve no GraphQL pode ser atribuído ao overhead de processamento da query no servidor (parsing e validação) antes da busca dos dados. O REST entrega o dado estático mais rápido, mas a variação da rede torna os dois tecnicamente equivalentes em performance de tempo neste cenário.

RQ2. Respostas às consultas GraphQL tem tamanho menor que respostas às consultas REST? Resposta: Sim, drasticamente menores.

Análise Estatística: O Teste T retornou um p-valor de 0.000, indicando uma diferença estatística extremamente relevante.

Discussão: O payload do REST foi de aprox. 19.5 KB, enquanto o do GraphQL foi de apenas 1.0 KB. Isso representa uma redução de cerca de 94% no tráfego de dados.

Causa: Isso comprova a capacidade do GraphQL de eliminar o Overfetching (trazer dados inúteis). No REST, recebemos URLs de episódios, datas de criação e imagens que não precisávamos. No GraphQL, trouxemos apenas os campos solicitados (id, name, status).

## 12. Conclusão Final

O experimento demonstrou que, para o cenário avaliado, o principal benefício da adoção do GraphQL não é a latência (tempo), mas sim a eficiência de banda. A redução de 94% no tamanho da resposta torna o GraphQL a escolha superior para ambientes com internet limitada (dispositivos móveis, 4G/3G), enquanto o REST se mantém competitivo em cenários onde a simplicidade e o cache de requisições inteiras são prioritários.
