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

df1 = cartola.query('POSICAO == "Goleiro"')
df2 = cartola.query('POSICAO == "Lateral"')
df3 = cartola.query('POSICAO == "Zagueiro"')
df4 = cartola.query('POSICAO == "Meia"')
df5 = cartola.query('POSICAO == "Atacante"')
df6 = cartola.query('POSICAO == "Técnico"')

tmp11 = df1.query('CASA == 1')
tmp12 = df1.query('FORA == 1')
maxval1 = round(max(tmp11['PONTUACAO'].max(),tmp12['PONTUACAO'].max())+1)

tmp21 = df2.query('CASA == 1')
tmp22 = df2.query('FORA == 1')
maxval2 = round(max(tmp21['PONTUACAO'].max(),tmp22['PONTUACAO'].max())+1)

tmp31 = df3.query('CASA == 1')
tmp32 = df3.query('FORA == 1')
maxval3 = round(max(tmp31['PONTUACAO'].max(),tmp32['PONTUACAO'].max())+1)

tmp41 = df4.query('CASA == 1')
tmp42 = df4.query('FORA == 1')
maxval4 = round(max(tmp41['PONTUACAO'].max(),tmp42['PONTUACAO'].max())+1)

tmp51 = df5.query('CASA == 1')
tmp52 = df5.query('FORA == 1')
maxval5 = round(max(tmp51['PONTUACAO'].max(),tmp52['PONTUACAO'].max())+1)

tmp61 = df6.query('CASA == 1')
tmp62 = df6.query('FORA == 1')
maxval6 = round(max(tmp61['PONTUACAO'].max(),tmp62['PONTUACAO'].max())+1)

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
  tmp1 = tmp11
  tmp2 = tmp12
  tmp3 = df1
  maxval = maxval1
if tipo == 'LATERAL':
  palavra = 'Lateral'
  tmp1 = tmp21
  tmp2 = tmp22
  tmp3 = df2
  maxval = maxval2
if tipo == 'ZAGUEIRO':
  palavra = 'Zagueiro'
  tmp1 = tmp31
  tmp2 = tmp32
  tmp3 = df3
  maxval = maxval3
if tipo == 'MEIA':
  palavra = 'Meia'
  tmp1 = tmp41
  tmp2 = tmp42
  tmp3 = df4
  maxval = maxval4
if tipo == 'ATACANTE':
  palavra = 'Atacante'
  tmp1 = tmp51
  tmp2 = tmp52
  tmp3 = df5
  maxval = maxval5
if tipo == 'TÉCNICO':
  palavra = 'Técnico'
  tmp1 = tmp61
  tmp2 = tmp62
  tmp3 = df6
  maxval = maxval6

texto = 'POSICAO == "'+palavra+'"'

#df_posicao = cartola.query(texto)

#tmp1 = df_posicao.query('CASA == 1')
#tmp2 = df_posicao.query('FORA == 1')
#maxval = round(max(tmp1['PONTUACAO'].max(),tmp2['PONTUACAO'].max())+1)

fig, ax = plt.subplots(1, 3,figsize=(14,fig_size))

boxsort(tmp1,by=['NOME'],column='PONTUACAO',idx=0)
boxsort(tmp2,by=['NOME'],column='PONTUACAO',idx=1)
boxsort(tmp3,by=['NOME'],column='PONTUACAO',idx=2)

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
