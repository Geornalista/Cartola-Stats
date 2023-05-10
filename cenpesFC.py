import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

#================================
rodada_atual = 4
#================================

# FUNÇÕES ====================
def pontos(df,rodada):
  texto = 'RODADA == '+str(rodada)
  pts = df.query(texto)['PONTOS'].sum()
  return pts

def valor(df,rodada):
    texto = 'RODADA == '+str(rodada)
    val = df.query(texto)['VALORIZACAO'].sum()
    return val

def figura_rodadas(scout):
    cor_bg = 'lightgray'
    cor_leg = 'white'
    cor_bar = 'darkblue'
    pts = {
            'GEORGE':gpt,
            'XINGU':xpt,
            'LEO':lpt,
            'LUIZ':lzpt,
            'VITOR':vpt,
            'RAFAEL':rpt,
            }
    val = {
            'GEORGE':cartoletas_g,
            'XINGU':cartoletas_x,
            'LEO':cartoletas_l,
            'LUIZ':cartoletas_lz,
            'VITOR':cartoletas_v,
            'RAFAEL':cartoletas_r,
            }
    if scout == 'TOTAL DE PONTOS':
        prop = pts
    if scout == 'CARTOLETAS':
        prop = val

    fig, axs = plt.subplots(6, 1,figsize=(15,30))
    fs = 20
    ls = 20

    m1 = max(prop['GEORGE'])
    m2 = max(prop['XINGU'])
    m3 = max(prop['LEO'])
    m4 = max(prop['LUIZ'])
    m5 = max(prop['VITOR'])
    m6 = max(prop['RAFAEL'])
    maior = max(m1,m2,m3,m4,m5,m6)

    axs[0].bar(rods,prop['GEORGE'],color=cor_bar)
    axs[0].set_title('GEORGE',fontsize=fs)
    rects = axs[0].patches
    for rect, label in zip(rects, prop['GEORGE']):
        height = rect.get_height()
        if height < 1.5:
            height = 0.5
        axs[0].text(
             rect.get_x() + rect.get_width() / 2, 0.5 * height, label, ha="center", va="bottom",
             color=cor_leg,fontsize=20
        )
    axs[1].bar(rods,prop['XINGU'],color=cor_bar)
    axs[1].set_title('XINGU',fontsize=fs)
    axs[2].bar(rods,prop['LEO'],color=cor_bar)
    axs[2].set_title('LEO',fontsize=fs)
    axs[3].bar(rods,prop['LUIZ'],color=cor_bar)
    axs[3].set_title('LUIZ',fontsize=fs)
    axs[4].bar(rods,prop['VITOR'],color=cor_bar)
    axs[4].set_title('VITOR',fontsize=fs)
    axs[5].bar(rods,prop['RAFAEL'],color=cor_bar)
    axs[5].set_title('RAFAEL',fontsize=fs)

    for ax in axs.flat:
        ax.set_facecolor(cor_bg)
        ax.set(ylim=(0,1.05*maior))
        ax.grid(axis='y',color='k',alpha=0.1)
        ax.tick_params(axis='x', which='major', labelsize=ls)
        ax.tick_params(axis='y', which='major', labelsize=ls)
    
    plt.tight_layout(h_pad=5)
    return fig

def figura1(dado,scout):
    cor_bg = 'lightgray'
    cor_leg = 'white'
    cor_bar = 'darkblue'
    
    fig, ax = plt.subplots(figsize=(15,10))
    ax.set_facecolor(cor_bg)
    ax.bar(usuarios,dado,color=cor_bar,edgecolor='k')
    ax.set_title(scout,fontsize=20)
    ax.grid(axis='y',color='k',alpha=0.1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.tick_params(axis='both', which='major', labelsize=20)

    rects = ax.patches
    for rect, label in zip(rects, dado):
        height = rect.get_height()
        if height < 1.5:
          height = 0.5
        ax.text(
            rect.get_x() + rect.get_width() / 2, 0.5 * height, label, ha="center", va="bottom",
            color=cor_leg,fontsize=20
        )
    return fig

rods = []
for i in range(rodada_atual):
  rods.append('R'+str(i+1))

files = {
         'GEORGE':'g_rodadas.csv',
         'XINGU':'x_rodadas.csv',
         'LEO':'l_rodadas.csv',
         'LUIZ':'lz_rodadas.csv',
         'VITOR':'v_rodadas.csv',
         'RAFAEL':'r_rodadas.csv',
        }

for user in files:
    tmp = pd.read_csv(files[user])
    tmp.drop('Unnamed: 0',axis=1,inplace=True)

    if user == 'GEORGE':
        george = tmp
    elif user == 'XINGU':
        xingu = tmp
    elif user == 'LEO':
        leo = tmp
    elif user == 'LUIZ':
        luiz = tmp
    elif user == 'VITOR':
        vitor = tmp
    else:
        rafael = tmp

usuarios = ['GEORGE','XINGU','LEO','LUIZ','VITOR','RAFAEL']

data = {
        'GEORGE':george,
        'XINGU':xingu,
        'LEO':leo,
        'LUIZ':luiz,
        'VITOR':vitor,
        'RAFAEL':rafael
        }

scouts = list(george.columns)

st.sidebar.title('CARTOLAFC\nPESQUISADORES DO CENPES\n2023')

teste1 = st.sidebar.radio('Escolha a Totalização:',(
            'RODADA',
            'TOTAL DE PONTOS',
            'CARTOLETAS',
            'RODADAS VENCEDORAS',
            'LANTERNAS',
            'PONTOS DO CAPITÃO'))

gpt=[]
xpt=[]
lpt=[]
lzpt=[]
vpt=[]
rpt=[]

gval = []
xval = []
lval = []
lzval = []
vval = []
rval = []

cartoletas_g = []
cartoletas_x = []
cartoletas_l = []
cartoletas_lz = []
cartoletas_v = []
cartoletas_r = []

c_g = 100
c_x = 100
c_l = 100
c_lz = 100
c_v = 100
c_r = 100

for user in usuarios:
    for irod in range(1,rodada_atual+1):
        cartola = data[user]
        p1 = pontos(cartola,irod)
        v1 = valor(cartola,irod)
        if user == 'GEORGE':
            gpt.append(p1)
            gval.append(v1)
        if user == 'XINGU':
            xpt.append(p1)
            xval.append(v1)
        if user == 'LEO':
            lpt.append(p1)
            lval.append(v1)
        if user == 'LUIZ':
            lzpt.append(p1)
            lzval.append(v1)            
        if user == 'VITOR':
            vpt.append(p1)
            vval.append(v1)
        if user == 'RAFAEL':
            rpt.append(p1)
            rval.append(v1)

for irod in range(rodada_atual):
    c_g = c_g + gval[irod]
    c_x = c_x + xval[irod]
    c_l = c_l + lval[irod]
    c_lz = c_lz + lzval[irod]
    c_v = c_v + vval[irod]
    c_r = c_r + rval[irod]
    cartoletas_g.append(c_g)
    cartoletas_x.append(c_x)
    cartoletas_l.append(c_l)
    cartoletas_lz.append(c_lz)
    cartoletas_v.append(c_v)
    cartoletas_r.append(c_r)

if teste1 == 'RODADA':
    rodada = st.slider('Escolha a Rodada:', 1, rodada_atual, rodada_atual,1)

    tipo = st.radio('Escolha:',('PONTOS','VALORIZAÇÃO'))

    if tipo == 'PONTOS':
        R = [gpt[rodada-1],xpt[rodada-1],lpt[rodada-1],lzpt[rodada-1],vpt[rodada-1],rpt[rodada-1]]
    else:
        R = [gval[rodada-1],xval[rodada-1],lval[rodada-1],lzval[rodada-1],vval[rodada-1],rval[rodada-1]]

    fig, ax = plt.subplots(figsize=(15,10))
    cor_bg = 'lightgray'
    cor_leg = 'white'
    cor_bar = 'darkblue'
    ax.set_facecolor(cor_bg)
    ax.bar(usuarios,R,color=cor_bar,edgecolor='k')
    ax.set_title('RODADA '+str(rodada),fontsize=20)
    ax.grid(axis='y',color='k',alpha=0.3)
    ax.tick_params(axis='both', which='major', labelsize=20)

    rects = ax.patches
    for rect, label in zip(rects, R):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, 0.5 * height, label.round(2), ha="center", va="bottom",
            color=cor_leg,fontsize=20
        )
    st.pyplot(fig)

#GRÁFICOS =========================================

if (teste1 == 'TOTAL DE PONTOS') or (teste1 == 'CARTOLETAS'):
    st.title(teste1)
    st.pyplot(figura_rodadas(teste1))

if (teste1 == 'RODADAS VENCEDORAS') or (teste1 == 'LANTERNAS'):
    vitorias = [0,0,0,0,0,0]
    lanternas = [0,0,0,0,0,0]
    for rod in range(rodada_atual):
        tmp = [gpt[rod],xpt[rod],lpt[rod],lzpt[rod],vpt[rod],rpt[rod]]
        idx1 = tmp.index(max(tmp))
        idx2 = tmp.index(min(tmp))
        vitorias[idx1] = vitorias[idx1]+1
        lanternas[idx2] = lanternas[idx2]+1

    st.title(teste1)

    if teste1 == 'RODADAS VENCEDORAS':
        st.pyplot(figura1(vitorias,teste1))
    else:
        st.pyplot(figura1(lanternas,teste1))

if teste1 == 'PONTOS DO CAPITÃO':
    capitao = [round(george['CAP'].sum(),2),round(xingu['CAP'].sum(),2),round(leo['CAP'].sum(),2),
               round(luiz['CAP'].sum(),2),round(vitor['CAP'].sum(),2),round(rafael['CAP'].sum(),2)]
    st.pyplot(figura1(capitao,teste1))

#props = st.sidebar.checkbox('Mostrar SCOUTS')

#if props:
#    teste2 = st.sidebar.selectbox('Escolha o SCOUT:',(
#        'GOL',
#        'ASSISTÊNCIA',
#       'FINALIZAÇÃO DEFENDIDA',
#        'FINALIZAÇÃO PRA FORA',
#        'FINALIZAÇÃO NA TRAVE',
#        'SG',
#        'GOL SOFRIDO',
#        'DEFESA DE PÊNALTI',
#        'DEFESA',
#        'DESARME',
#        'GOL CONTRA',
#        'CARTÃO VERMELHO',
#        'CARTÃO AMARELO',
#        'FALTA SOFRIDA',
#        'FALTA COMETIDA',
#        'PÊNALTI SOFRIDO',
#        'PÊNALTI COMETIDO',
#        'PÊNALTI PERDIDO',
#        'IMPEDIMENTO'))
    
#    st.title(teste2)

#    if teste2 == 'GOL':
#        prop = [george['G'].sum(),xingu['G'].sum(),leo['G'].sum(),vitor['G'].sum(),rafael['G'].sum()]
#    if teste2 == 'ASSISTÊNCIA':
#        prop = [george['A'].sum(),xingu['A'].sum(),leo['A'].sum(),vitor['A'].sum(),rafael['A'].sum()]
#    if teste2 == 'CARTÃO AMARELO':
#        prop = [george['CA'].sum(),xingu['CA'].sum(),leo['CA'].sum(),vitor['CA'].sum(),rafael['CA'].sum()]
#    if teste2 == 'CARTÃO VERMELHO':
#        prop = [george['CV'].sum(),xingu['CV'].sum(),leo['CV'].sum(),luiz['CV'].sum(),vitor['CV'].sum(),rafael['CV'].sum()]
#    if teste2 == 'SG':
#        prop = [george['SG'].sum(),xingu['SG'].sum(),leo['SG'].sum(),luiz['SG'].sum(),vitor['SG'].sum(),rafael['SG'].sum()]
#    if teste2 == 'DEFESA':
#        prop = [george['DE'].sum(),xingu['DE'].sum(),leo['DE'].sum(),luiz['DE'].sum(),vitor['DE'].sum(),rafael['DE'].sum()]
#    if teste2 == 'DESARME':
#        prop = [george['DS'].sum(),xingu['DS'].sum(),leo['DS'].sum(),luiz['DS'].sum(),vitor['DS'].sum(),rafael['DS'].sum()]
#    if teste2 == 'PÊNALTI SOFRIDO':
#        prop = [george['PS'].sum(),xingu['PS'].sum(),leo['PS'].sum(),luiz['PS'].sum(),vitor['PS'].sum(),rafael['PS'].sum()]
#    if teste2 == 'IMPEDIMENTO':
#        prop = [george['I'].sum(),xingu['I'].sum(),leo['I'].sum(),luiz['I'].sum(),vitor['I'].sum(),rafael['I'].sum()]
#    if teste2 == 'FINALIZAÇÃO NA TRAVE':
#        prop = [george['FT'].sum(),xingu['FT'].sum(),leo['FT'].sum(),luiz['FT'].sum(),vitor['FT'].sum(),rafael['FT'].sum()]
#    if teste2 == 'FINALIZAÇÃO DEFENDIDA':
#        prop = [george['FD'].sum(),xingu['FD'].sum(),leo['FD'].sum(),luiz['FD'].sum(),vitor['FD'].sum(),rafael['FD'].sum()]
#    if teste2 == 'FINALIZAÇÃO PRA FORA':
#        prop = [george['FF'].sum(),xingu['FF'].sum(),leo['FF'].sum(),luiz['FF'].sum(),vitor['FF'].sum(),rafael['FF'].sum()]
#    if teste2 == 'FALTA SOFRIDA':
#        prop = [george['FS'].sum(),xingu['FS'].sum(),leo['FS'].sum(),luiz['FS'].sum(),vitor['FS'].sum(),rafael['FS'].sum()]
#    if teste2 == 'FALTA COMETIDA':
#        prop = [george['FC'].sum(),xingu['FC'].sum(),leo['FC'].sum(),luiz['FC'].sum(),vitor['FC'].sum(),rafael['FC'].sum()]
#    if teste2 == 'GOL SOFRIDO':
#        prop = [george['GS'].sum(),xingu['GS'].sum(),leo['GS'].sum(),luiz['GS'].sum(),vitor['GS'].sum(),rafael['GS'].sum()]
#    if teste2 == 'DEFESA DE PÊNALTI':
#        prop = [george['DP'].sum(),xingu['DP'].sum(),leo['DP'].sum(),luiz['DP'].sum(),vitor['DP'].sum(),rafael['DP'].sum()]
#    if teste2 == 'PÊNALTI COMETIDO':
#        prop = [george['PC'].sum(),xingu['PC'].sum(),leo['PC'].sum(),luiz['PC'].sum(),vitor['PC'].sum(),rafael['PC'].sum()]
#    if teste2 == 'PÊNALTI PERDIDO':
#        prop = [george['PP'].sum(),xingu['PP'].sum(),leo['PP'].sum(),luiz['PP'].sum(),vitor['PP'].sum(),rafael['PP'].sum()]
#    if teste2 == 'GOL CONTRA':
#        prop = [george['GC'].sum(),xingu['GC'].sum(),leo['GC'].sum(),luiz['GC'].sum(),vitor['GC'].sum(),rafael['GC'].sum()]

#    prop = list(map(int, prop))

#    st.pyplot(figura1(prop,teste2))
