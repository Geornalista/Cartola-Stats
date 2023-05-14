import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def boxsort(df, by, column,idx):
    df2 = pd.DataFrame({col:vals[column] for col, vals in df.groupby(by)})
    meds = df2.median().sort_values()
    
    meanpointprops = dict(marker='D',markeredgecolor='black',markerfacecolor='red',markersize=6)
    
    return df2[meds.index].boxplot(ax=ax[idx],
                                   vert=False,
                                   color='green',meanprops=meanpointprops,
                                   showmeans=True,showfliers=False,grid=True,
                                   patch_artist=True,
                                   whiskerprops = dict(linewidth=3,color='black'),
                                   capprops = dict(linewidth=3, color='Black'))

cartola = pd.read_csv('cartola.csv')

st.sidebar.title('ESTATÍSTICAS\nCARTOLAF 2023')

tipo = st.sidebar.radio('Escolha a Posição:',(
            'GOLEIRO',
            'LATERAL',
            'ZAGUEIRO',
            'MEIA',
            'ATACANTE',
            'TÉCNICO'))
fig_size = int(st.sidebar.number_input("Comprimento do Gráfico", min_value=5, max_value=40, value=10, step=1, help="Quanto maior o número,maior será o gráfico"))
font_size = int(st.sidebar.number_input("Tamanho da Fonte", min_value=5, max_value=40, value=10, step=1))

#GRÁFICOS =========================================
if tipo == 'GOLEIRO':
  palavra = 'Goleiro'
if tipo == 'LATERAL':
  palavra = 'Lateral'
if tipo == 'ZAGUEIRO':
  palavra = 'Zagueiro'
if tipo == 'MEIA':
  palavra = 'Meia'
if tipo == 'ATACANTE':
  palavra = 'Atacante'
if tipo == 'TÉCNICO':
  palavra = 'Técnico'

texto = 'POSICAO == "'+palavra+'"'

df_posicao = cartola.query(texto)

tmp1 = df_posicao.query('CASA == 1')
tmp2 = df_posicao.query('FORA == 1')

maxval = round(max(tmp1['PONTUACAO'].max(),tmp2['PONTUACAO'].max())+1)

fig, ax = plt.subplots(1, 3,figsize=(14,fig_size))

boxsort(tmp1,by=['NOME'],column='PONTUACAO',idx=0)
boxsort(tmp1,by=['NOME'],column='PONTUACAO',idx=1)
boxsort(df_posicao,by=['NOME'],column='PONTUACAO',idx=2)

ax[0].set_title(f'{palavra} - CASA',fontsize=20)
ax[1].set_title(f'{palavra} - FORA',fontsize=20)
ax[2].set_title(f'{palavra} - TOTAL',fontsize=20)

for axs in ax.flatten():
    axs.set_xlabel('PONTOS',fontsize=14)
    axs.set_xlim(-5,maxval)
    axs.tick_params(axis='x', which='both', labelsize=font_size)
    axs.set_yticklabels(labels=axs.get_yticklabels(), fontsize=font_size)

fig.suptitle('')
fig.tight_layout()

st.pyplot(fig)