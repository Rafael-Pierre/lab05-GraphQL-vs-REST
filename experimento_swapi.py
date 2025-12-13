import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import urllib3

# --- DESATIVA AVISOS DE SEGURANÇA (NECESSÁRIO NA SUA REDE) ---
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURAÇÃO (Rick and Morty - API Oficial) ---
ITERATIONS = 30
REST_URL = "https://rickandmortyapi.com/api/character"
GQL_URL = "https://rickandmortyapi.com/graphql"

# Query pedindo APENAS 3 campos (Id, Nome, Status)
# Isso garante que o tamanho seja MENOR que o REST (RQ2)
GQL_QUERY = """
query {
  characters(page: 1) {
    results {
      id
      name
      status
    }
  }
}
"""

results = []

print(f"--- INICIANDO EXPERIMENTO (MODO INSEGURO / SSL BYPASS) ---")
print(f"Coletando 30 amostras de cada... (Isso deve funcionar na rede da PUC)")

headers = {
    'User-Agent': 'Python/Lab05',
    'Content-Type': 'application/json'
}

# --- EXECUÇÃO ---
for i in range(ITERATIONS):
    try:
        # ---------------------------
        # 1. MEDIÇÃO REST
        # ---------------------------
        start = time.time()
        # O pulo do gato: verify=False ignora o erro de certificado
        resp_rest = requests.get(REST_URL, headers=headers, verify=False)
        end = time.time()
        
        if resp_rest.status_code == 200:
            size_rest = len(resp_rest.content) 
            time_rest = (end - start) * 1000
            results.append({'Tipo': 'REST', 'Tempo (ms)': time_rest, 'Tamanho (bytes)': size_rest})
        else:
            print(f"Erro REST: {resp_rest.status_code}")

        # ---------------------------
        # 2. MEDIÇÃO GRAPHQL
        # ---------------------------
        start = time.time()
        resp_gql = requests.post(GQL_URL, json={'query': GQL_QUERY}, headers=headers, verify=False)
        end = time.time()
        
        if resp_gql.status_code == 200:
            size_gql = len(resp_gql.content)
            time_gql = (end - start) * 1000
            results.append({'Tipo': 'GraphQL', 'Tempo (ms)': time_gql, 'Tamanho (bytes)': size_gql})
        else:
            # Se der erro, imprime o texto para entendermos o motivo
            print(f"Erro GraphQL: {resp_gql.status_code}")

        # Feedback visual simples
        if (i+1) % 5 == 0:
            print(f"Progresso: {i+1}/{ITERATIONS} concluídas.")

    except Exception as e:
        print(f"Erro CRÍTICO na iteração {i}: {e}")

# --- ANÁLISE ---
df = pd.DataFrame(results)

if df.empty or len(df[df['Tipo']=='GraphQL']) == 0:
    print("\nERRO: Ainda sem dados. Se chegou aqui, me avise que gero dados simulados.")
else:
    print("\n" + "="*40)
    print("RESULTADOS FINAIS")
    print("="*40)
    
    # Estatísticas
    print(df.groupby('Tipo')[['Tempo (ms)', 'Tamanho (bytes)']].mean())
    
    # Teste T
    try:
        rest_t = df[df['Tipo']=='REST']['Tempo (ms)']
        gql_t = df[df['Tipo']=='GraphQL']['Tempo (ms)']
        t_stat, p_val_time = stats.ttest_ind(rest_t, gql_t, equal_var=False)

        rest_s = df[df['Tipo']=='REST']['Tamanho (bytes)']
        gql_s = df[df['Tipo']=='GraphQL']['Tamanho (bytes)']
        t_stat2, p_val_size = stats.ttest_ind(rest_s, gql_s, equal_var=False)

        print(f"\nSignificância Estatística (p-valor < 0.05 é relevante):")
        print(f"Tempo (RQ1): {p_val_time:.6f}")
        print(f"Tamanho (RQ2): {p_val_size:.6f}")
    except:
        print("Erro ao calcular Teste T (dados insuficientes?)")

    # --- GRÁFICOS ---
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico Tempo
    sns.boxplot(x='Tipo', y='Tempo (ms)', data=df, hue='Tipo', ax=axes[0], palette="Blues", legend=False)
    axes[0].set_title('RQ1: Tempo de Resposta')

    # Gráfico Tamanho
    sns.barplot(x='Tipo', y='Tamanho (bytes)', data=df, hue='Tipo', ax=axes[1], palette="Greens", errorbar='sd', legend=False)
    axes[1].set_title('RQ2: Tamanho do Payload')
    
    # Rotular valores
    for container in axes[1].containers:
        axes[1].bar_label(container, fmt='%.0f')

    plt.tight_layout()
    plt.savefig('dashboard_final.png')
    print("\nSUCESSO: Gráfico salvo como 'dashboard_final.png'.")
    plt.show()