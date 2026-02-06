import matplotlib.pyplot as plt
import pandas as pd

# Datos extraídos del análisis de frecuencia de palabras clave en el documento (Secciones 2.C.1, 2.C.2)
# Basado en conteo manual de menciones explícitas en las tablas de "Carencias" y "Habilidades para la empleabilidad"

soft_skills_data = {
    'Habilidad': ['Autonomía/Proactividad', 'Comunicación (Oral/Escrita/Cliente)', 'Actitud/Ganas/Motivación', 
                  'Responsabilidad/Madurez', 'Trabajo en Equipo', 'Puntualidad/Normas', 'Pensamiento Crítico'],
    'Menciones': [14, 12, 10, 9, 7, 5, 5] # Frecuencia aproximada en el texto
}

hard_skills_data = {
    'Tecnología/Área': ['IA / Uso Ético IA', 'Cloud (Azure/AWS)', 'Seguridad/Ciberseguridad', 
                        'Docker/Contenedores', 'Bases de Datos (SQL/NoSQL)', 'Sistemas (Linux/Windows)', 'iOS/Móviles'],
    'Menciones': [9, 6, 6, 4, 4, 3, 3]
}

# Crear DataFrames
df_soft = pd.DataFrame(soft_skills_data).sort_values(by='Menciones', ascending=True)
df_hard = pd.DataFrame(hard_skills_data).sort_values(by='Menciones', ascending=True)

# Configuración de gráficos
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Soft Skills
ax[0].barh(df_soft['Habilidad'], df_soft['Menciones'], color='#4e79a7')
ax[0].set_title('Top "Soft Skills" demandadas por las empresas\n(Frecuencia de mención en el informe)')
ax[0].set_xlabel('Número de menciones')

# Gráfico 2: Hard Skills
ax[1].barh(df_hard['Tecnología/Área'], df_hard['Menciones'], color='#f28e2b')
ax[1].set_title('Tecnologías y Áreas Técnicas solicitadas\n(Frecuencia de mención en el informe)')
ax[1].set_xlabel('Número de menciones')

plt.tight_layout()
plt.savefig('analisis_talent_pyme.png')