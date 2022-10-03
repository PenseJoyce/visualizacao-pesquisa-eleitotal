#!/usr/bin/env python
# coding: utf-8

# In[5]:


import basedosdados as bd
import pandas as pd


# In[6]:


# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_poder360_pesquisas',
table_id='microdados',
billing_project_id="keen-vehicle-364417")


# In[24]:


# realizando a filtragem dos dados que me interessam 

pesquisa_2022 = df[(df.instituto == 'Datafolha') 
   & (df.ano == 2022)
   & (df.cargo == 'presidente')
   & (df.sigla_uf.isnull() == True)
   & (df.tipo == 'estimulada')
   & (df.turno == 1)
   & ((df.nome_candidato == 'Lula') | (df.nome_candidato == 'Bolsonaro') |
     (df.nome_candidato == 'Ciro') | (df.nome_candidato == 'Simone Tebet'))
   & (df.descricao_cenario.str.contains('cenário 1') == True)]


# In[25]:


pesquisa_2022 = pesquisa_2022.sort_values(by=['data'], ascending=True)


# In[30]:


# alterando 
pd.options.plotting.backend = 'plotly'


# In[31]:


pesquisa_2022.plot(x='data', y = 'percentual', color='nome_candidato')


# In[32]:


# realizando a filtragem dos dados que me interessam 

pesquisa_2022_02 = df[(df.instituto == 'Datafolha') 
   & (df.ano == 2022)
   & (df.cargo == 'presidente')
   & (df.sigla_uf.isnull() == True)
   & (df.tipo == 'estimulada')
   & ((df.nome_candidato == 'Lula') | (df.nome_candidato == 'Bolsonaro') |
     (df.nome_candidato == 'Ciro') | (df.nome_candidato == 'Simone Tebet'))
   & (df.descricao_cenario.str.contains('cenário 1') == True)]


# In[33]:


pesquisa_2022_02.plot(x='data', y = 'percentual', color='nome_candidato', facet_row='turno')


# In[ ]:




