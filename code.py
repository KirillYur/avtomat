import streamlit as st

from iapws import IAPWS97
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from iapws import IAPWS97 as WSP
import math as M
from PIL import Image
import streamlit.components.v1 as components


st.write("Выполнили: Парнова Екатерина ФПэ-01-19, Юричковский Кирилл ТФэ-01-19, Буйницкий Савелий ТФэ-01-19,Абрамова Анна ФПэ-01-19 ")
st.write("# Колебания лопаток")
st.write("# Определение собственной частоты одиночной лопатки в статических условиях")
dsr = 0.8355
Fx=2.44e-4
l2 = 0.211
Jx=0.43e-8
betau=85.0
ro=8000
E=2e11
z2=132
Bb=40
delta=5
m=12
ksi=0.98
Hb=0.226
m1=0.56
m2=3.51
m3=9.82
dp=1.046
n=50
st.write(" *Изменить исходные данные:* ")
dsr = st.number_input('Введите средний диаметр последней ступени dsr, м', value=dsr)
st.session_state.dsr =dsr
l2 = st.number_input('Введите длину рабочей лопатки l2, м', value=l2)
st.session_state.l2 = l2
Fx = st.number_input('Введите площадь сечения профиля Fx, м2', value=Fx)
st.session_state.Fx = Fx
Jx = st.number_input('Введите момент инерции Jx, м4', value=Jx)
st.session_state.Jx = Jx
#betau = st.number_input('Введите угол установки betau, гр', value=betau)
#st.session_state.betau = betau
betau = st.slider('Введите угол установки betau, гр', min_value=0.0, max_value=90.0, step=0.1, value=betau)
ro = st.number_input('Введите плотность стали ro, гр', value=ro)
st.session_state.ro = ro
E = st.number_input('Введите модуль упругости E, Па ', value=E)
st.session_state.E = E
z2 = st.number_input('Введите число рабочих лопаток z2, шт ', value=z2)
st.session_state.z2 = z2
Bb = st.number_input('Введите размер бандажной ленты Bb, мм ', value=Bb)
st.session_state.Bb = Bb
delta = st.number_input('Введите размер бандажной ленты delta, мм ', value=delta)
st.session_state.delta = delta
Hb = st.number_input('Качество присоединения бандажа Hb ', value=Hb)
st.session_state.Hb = Hb
dp = st.number_input('Введите периферийный диаметр, м', value=dp)
st.session_state.dp = dp
n = st.number_input('Введите частоту вращения, с-1', value=n)
st.session_state.n = n
i=(Jx/Fx)**0.5
lyambda=l2/i
st.write(""" # """)
st.write(" *Дано:* ")
st.write(""" Средний диаметр последней ступени: """)
st.write(""" dsr = """ + str( dsr) + """ м""")
st.write(""" Длина рабочей лопатки: """)
st.write(""" l2 = """ + str(l2) + """ м""")
st.write(""" Площадь сечения профиля: """)
st.write(""" Fx = """ + str(Fx) + """ м2 """)
st.write(""" Момент инерции: """)
st.write(""" Jx = """ + str(Jx) + """ м4 """)
st.write(""" Угол установки: """)
st.write(""" betau = """ + str(betau) + """ гр  """)
st.write(""" Плотность стали: """)
st.write(""" ro = """ + str(ro) + """ кг/м3  """)
st.write(""" Модуль упругости: """)
st.write(""" E = """ + str(E) + """ Па  """)
st.write(""" Число рабочих лопаток: """)
st.write(""" z2 = """ + str(z2) + """ шт  """)
st.write(""" Размеры бандажной ленты: """)
st.write(""" Bb = """ + str(Bb) + """ мм  """)
st.write(""" delta = """ + str(delta) + """ мм  """)
st.write(""" Число лопаток в пакете: """)
st.write(""" m = """ + str(m) + """ шт """)
st.write(""" Качество присоединения бандажа: """)
st.write(""" Hb = """ + str(Hb))
st.write(""" Периферийный диаметр: """)
st.write(""" dp = """ + str(dp))   

st.write("""# """)
st.write("# Определение собственной частоты колебаний одиночной лопатки в статических условиях")

x_list= [3.565,3.739,4.174,4.696,5.478,6.696,7.826,9.739,12.087, 13.913,16.435,20.083,22.407,25.228,27.884,30.539,33.776,36.515,40.513,43.59,46.154,48.462,51.282,53.761,56.923,59.658]
y_list= [0.463,0.482,0.514,0.552,0.595,0.639,0.675,0.716,0.764,0.795,0.828,0.862,0.881,0.904,0.924,0.938,0.952,0.961,0.975,0.981,0.986,0.988,0.989,0.989,0.991, 0.991]

st.write(""" Так как значения частот колебаний оказываетсются ниже рассчитанных, используют поправочный коэффициент ksi=fдейств/fрасч для первого тона колебаний  """)
st.write(""" lyambda = """ + str('{:.4}'.format(lyambda)))
x_list_y_list = plt.figure()
fig = figure(
title='Зависимость ksi для первого тона колебаний от гибкости лопатки',
x_axis_label='Гибкость лопатки',
y_axis_label='Поправочный коэффициент')

fig.line(x_list, y_list , line_width=3)
st.bokeh_chart(fig, use_container_width=True)
ksi=0.00000002*(lyambda/10)**6+0.0000003*(lyambda/10)**5-0.00003*(lyambda/10)**4-(0.0007*(lyambda/10)**3)+0.0062*(lyambda/10)**2+0.0451*(lyambda/10)+0.7891
#st.write(""" ksi = """ + str(ksi))
#st.write(""" ksi = """ + str(ksi))
st.write(""" # """)
st.write("# Определение собственной частоты колебаний пакета лопаток в статических условиях")
st.write(""" # """)
st.write(""" Действительная частота колебаний fst1: """)
f1=ksi*(m1/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f1 = """ + str('{:.6}'.format(f1)) + """ Гц """)
st.write(""" Действительная частота колебаний fst2: """)
f2=1*(m2/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f2 = """ + str('{:.6}'.format(f2)) + """ Гц """)
st.write(""" Действительная частота колебаний fst3: """)
f3=1*(m3/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f3 = """ + str('{:.6}'.format(f3)) + """ Гц """)

st.write(""" # """)
st.write("# Определение собственной частоты колебаний пакета лопаток в статических условиях")

Eb=E
dp= 1.046 

Jb=Bb/12*delta**3
tb=(M.pi*dp)/z2
betta=90-betau
bettarad=betta*M.pi/180
kb=((12*(m-1)*Hb*Eb*Jb*M.cos(bettarad)*M.cos(bettarad)*l2)/(m*tb*E*Jx))/10**12
st.write(""" Коэффициент жесткости бандажа: """)
st.write(""" kb = """ + str('{:.4}'.format(kb)))
nub=(Bb*10**-3*delta*10**-3*tb*ro)/(Fx*l2*ro)
st.write(""" Относительная масса бандажа nu_b =""" + str('{:.5}'.format(nub)))

#phi1
if 0<nub<=0.04:
 delta_a1 = nub/0.04
 A1_0 = 2e-9*kb**6-3e-7*kb**5+2e-5*kb**4-0.0005*kb**3+0.0081*kb**2-0.0078*kb+6.2302
 A1_004 = -4e-8*kb**6+3e-5*kb**5-0.0001*kb**4+0.0018*kb**3-0.0105*kb**2+0.0754*kb+5.6671
 phi_1 = A1_004 + delta_a1*(A1_0-A1_004)
elif 0.04<nub<0.1:
 delta_a2 = (nub-0.04)/0.06
 A1_004 = -4e-8*kb**6+3e-5*kb**5-0.0001*kb**4+0.0018*kb**3-0.0105*kb**2+0.0754*kb+5.6671
 A1_01 = 1e-7*kb**6 - 8e-6*kb**5 + 0.0002*kb**4 - 0.0036*kb**3 + 0.0269*kb**2 - 0.0349*kb + 5.3714
 phi_1 = A1_01 + delta_a2*(A1_004-A1_01)
elif 0.1<nub<0.2:
 delta_a3 = (nub-0.1)/0.1
 A1_02 = -3e-07*kb**6 + 1e-05*kb**5 - 0.0003*kb**4 + 0.0018*kb**3 - 0.001*kb**2 + 0.0579*kb + 4.9632
 A1_01 = 1e-7*kb**6 - 8e-6*kb**5 + 0.0002*kb**4 - 0.0036*kb**3 + 0.0269*kb**2 - 0.0349*kb + 5.3714
 phi_1 = A1_02 + delta_a3*(A1_01-A1_02)
elif 0.2<nub<0.3:
 delta_a4 = (nub-0.2)/0.1
 A1_02 = -3e-07*kb**6 + 1e-05*kb**5 - 0.0003*kb**4 + 0.0018*kb**3 - 0.001*kb**2 + 0.0579*kb + 4.9632
 A1_03 = 1e-6*kb**6 - 6e-5*kb**5 + 0.0014*kb**4 - 0.0167*kb**3 + 0.0953*kb**2 - 0.1395*kb+4.8747
 phi_1 = A1_03 + delta_a4*(A1_02-A1_03)
 
#phi2
if 0<nub<=0.3:
 delta_b1 = nub/0.3
 B0_0= 1e-7*kb**6 - 8e-6*kb**5 + 0.0002*kb**4 - 0.0036*kb**3 + 0.0242*kb**2 - 0.0086*kb + 4.217
 B0_03= -2e-7*kb**6 + 1e-5*kb**5 - 0.0004*kb**4 + 0.0049*kb**3 - 0.0293*kb**2 + 0.115*kb + 4.1009
 phi_2 = B0_03 + delta_b1*(B0_0-B0_03)
 
#phi3
if 0<nub<=0.1:
 delta_c1 = nub/0.1
 C_0 = 0.0009*kb**6 - 0.0213*kb**5 + 0.1907*kb**4 - 0.8598*kb**3 + 2.0303*kb**2 - 2.0079*kb + 1.629
 C_01 = -7e-7*kb**6 + 5e-5*kb**5 - 0.0012*kb**4 + 0.0141*kb**3 - 0.0756*kb**2 + 0.2026*kb + 0.6154
 phi_3 = C_01 + delta_c1*(C_0-C_01)
elif 0.1<nub<0.2:
 delta_c2 = (nub-0.1)/0.1
 C_01 = -7e-7*kb**6 + 5e-5*kb**5 - 0.0012*kb**4 + 0.0141*kb**3 - 0.0756*kb**2 + 0.2026*kb + 0.6154
 C_02 = 3e-7*kb**6 - 2e-5*kb**5 + 0.0004*kb**4 - 0.0055*kb**3 + 0.0334*kb**2 - 0.0386*kb + 0.5956
 phi_3 = C_02 + delta_c2*(C_01-C_02)
elif 0.2<nub<0.3:
 delta_c3 = (nub-0.2)/0.1
 C_02 = 3e-7*kb**6 - 2e-5*kb**5 + 0.0004*kb**4 - 0.0055*kb**3 + 0.0334*kb**2 - 0.0386*kb + 0.5956
 C_03 = 4e-8*kb**6 - 3e-6*kb**5 + 0.0001*kb**4 - 0.0017*kb**3 + 0.0138*kb**2 - 0.0191*kb + 0.4507
 phi_3 = C_02 + delta_c3*(C_02-C_03)
#st.write(str(A1_0))
#st.write(str(A1_004))
#st.write("""phi1 =""" + str('{:.5}'.format(phi_1)))
#st.write("""phi2 =""" + str('{:.5}'.format(phi_2)))
#st.write("""phi3 =""" + str('{:.5}'.format(phi_3)))
#elif 0.04 < nub <= 0.1
#ksi1 = -1.3855 * T_ ** 2 + 2.00774 * T_ + 0.0321
#elif 0.1 < nub<= 0.2:
#ksi1 = -2.6536 * T_ ** 2 + 4.2556 * T_ - 0.8569
#elif 0.2 < nub<= 0.3:
#ksi1 = -2.6536 * T_ ** 2 + 4.2556 * T_ - 0.8569

coord_x1= [0.0,	0.057,	0.148,	0.268,	0.388,	0.526,	0.67,	0.837,	1.041,	1.209,	1.383,	1.531,	1.694,	1.837,	1.99,	2.139,	2.304,	2.5]
coord_y1=[0.956,	0.989,	1.096,	1.223,	1.383,	1.511,	1.67,	1.766,	1.894,	1.989,	2.053,	2.053,	2.117,	2.149,	2.181,	2.181,	2.245,	2.245]
coord_x2= [0.0,	0.105,	0.22,	0.335,	0.469,	0.589,	0.694,	0.818,	0.933,	1.041,	1.143,	1.27,	1.403,	1.52,	1.638,	1.77,	1.918,	2,	2.093,	2.186,	2.309,	2.412,	2.5]
coord_y2= [4.229,	4.277,	4.325,	4.386,	4.47,	4.53,	4.59,	4.639,	4.675,	4.723,	4.759,	4.795,	4.843,	4.867,	4.904,	4.928,	4.952,	4.952,	4.976,	4.988,	5,	5.021,	5.021]
coord_x3=[0.0,	0.062,	0.201,	0.359,	0.522,	0.641,	0.818,	0.967,	1.133,	1.321,	1.49,	1.628,	1.776,	1.908,	2.041,	2.186,	2.356,	2.5]
coord_y3=[0.767,	0.789,	0.833,	0.889,	0.922,	0.967,	1,	1.128,	1.223,	1.351,	1.447,	1.511,	1.543,	1.638,	1.67,	1.734,	1.798,	1.83]
coord_x4= [0.0,	0.038,	0.096,	0.187,0.287,	0.368,	0.469,	0.555,	0.646,	0.77,	0.866,	0.981, 1.102, 1.23,	1.383, 1.515, 1.663, 1.811, 1.934, 2.062,	2.227,	2.33,	2.418,	2.5]

coord_y4=[5.362,	5.383,	5.426,	5.489,	5.553,	5.617,	5.691,	5.745,	5.798,	5.862,	5.926,	5.979, 6.052, 6.113, 6.175, 6.216,	6.278,	6.32,	6.361, 6.392, 6.433, 6.443, 6.464, 	6.485]
coord_x5= [0.0,	0.077,	0.167,	0.335,	0.517,	0.66,	0.823,	0.971,	1.173,	1.296,	1.464,	1.587,	1.719,	1.862,	2,	2.103,	2.17,	2.247,	2.325,	2.407,	2.5]
coord_y5=[0.589,	0.611,	0.656,	0.722,	0.789,	0.833,	0.878,	0.922,	0.967,	0.989,	1.064,	1.096,	1.16,	1.191,	1.223,	1.255,	1.287,	1.319,	1.319,	1.351,	1.351]
coord_x6=[0.0	,0.105	,0.201,	0.311	,0.426,	0.569,	0.718,	0.866,	1,	1.143,	1.281,	1.408,	1.566,	1.709	,1.878,	2.052	,2.211,	2.356,	2.5]
coord_y6=[5.021	,5.085,	5.16,	5.245	,5.319,	5.415,	5.5,	5.606,	5.67,	5.745,	5.798,	5.862,	5.904	,5.957	,6.01,	6.062,	6.103	,6.134,	6.175]
coord_x7=[0.0,	0.048	,0.105,	0.182,	0.268,	0.378	,0.478	,0.569,	0.656,	0.746,	0.856,	0.962,	1.056,	1.179	,1.296,	1.423,	1.551,	1.663	,1.77,	1.878,	2.01,	2.129,	2.211	,2.325,	2.418,	2.5]
coord_y7=[0.444,	0.456,	0.478,	0.511,	0.544,	0.578,	0.611,	0.644,	0.678,	0.7,	0.733,	0.756,	0.778	,0.811,	0.833,	0.856,	0.878,	0.9	,0.922	,0.933,	0.944,	0.967,	0.967,	0.978,	0.989,	1]
coord_x8=[0.0,	0.077,	0.201,	0.383,	0.522	,0.684,	0.833,	0.995	,1.133,	1.276,	1.434	,1.607,	1.781,	1.929,	2.072,	2.222,	2.34,	2.5]
coord_y8=[4.819,	4.855,	4.964,	5.096,	5.191,	5.287	,5.372,	5.457,	5.521,	5.585	,5.649,	5.713,	5.777,	5.819,	5.862,	5.894,	5.926	,5.947]
coord_x9=[0.0,	0.249	,0.407,	0.603	,0.78,	0.952,	1.184,	1.398,	1.597,	1.857,	2.046,	2.165,	2.289,	2.397,	2.5	]
coord_y9=[4.193,	4.241,	4.289,	4.325,	4.349,	4.386,	4.434,	4.47,	4.518,	4.566,	4.59,	4.614	,4.651,	4.663,	4.675]
coord_x10=[0.0,	0.072,	0.134,	0.196,	0.244,	0.321,	0.431,	0.536,	0.646,	0.77	,0.88,	1.015,	1.148,	1.301,	1.439,	1.587	,1.699,	1.811	,1.939,	2.036	,2.108	,2.186,	2.289,	2.381	,2.443,	
2.5]
coord_y10=[5.734,	5.787,	5.84,	5.894,	5.936,	5.989,	6.072,	6.134,	6.206,	6.278	,6.34,	6.423,	6.495	,6.557	,6.619,	6.68,	6.722,	6.763,	6.804,	6.825,	6.845,	6.866,	6.887,	6.907,	6.918,	6.928,
 ]
coord_x11=[0.0,	0.038	,0.072	,0.11,	0.172,	0.215,	0.282,	0.34,	0.431	,0.536	,0.608	,0.699,	0.77,	0.866,	0.957,	1.071,	1.168,	1.27,	1.388,	1.485,	1.587,	1.689,	1.781,	1.888,	2.01,	2.093	,2.18,	2.273	,2.381	,
 2.5]
coord_y11=[6.227,	6.247,	6.268	,6.299,	6.34	,6.371	,6.423	,6.474	,6.515,	6.588	,6.629	,6.67,	6.722,	6.773,	6.814,	6.866,	6.907,	6.959,	6.99,	7.041	,7.082,	7.112,	7.143,	7.184,	7.214,	7.255,	7.265,	7.286,	7.296,
           7.316]
coord_x12=[0.0,	0.169,	0.394,	0.711,	1.037,	1.381,	1.836,	2.146,	2.5]
coord_y12=[0.581,	0.645,	0.726,	0.839,	0.919,	0.984,	1.143,	1.238	,1.333]
coord_x13=[0.0,	0.254,	0.634,	1.045,	1.552,	1.978,	2.271,	2.5
]
coord_y13=[0.758,	0.839,	0.952,	1.143,	1.429,	1.619,	1.762,	1.857
]
coord_x14=[0.0,	0.486,	0.993	,1.448	,1.836	,2.257,	2.5
]
coord_y14=[0.952,	1.429,	1.857,	2.048,	2.143,	2.238,	2.238
]
coord_x15=[0.0,	0.331, 0.676,	1.096,	1.765,	2.171,	2.5]
coord_y15=[0.952	,1.286,	1.619,	1.905,	2.143,	2.19,	2.238]
coord_x15_coord_y15=plt.figure()
coord_x14_coord_y14=plt.figure()
coord_x13_coord_y13=plt.figure()
coord_x12_coord_y12=plt.figure()
coord_x11_coord_y11=plt.figure()
coord_x10_coord_y10=plt.figure()
coord_x9_coord_y9=plt.figure()
coord_x8_coord_y8=plt.figure()
coord_x7_coord_y7=plt.figure()
coord_x6_coord_y6=plt.figure()
#coord_x5_coord_y5=plt.figure()
coord_x4_coord_y4= plt.figure()
coord_x1_coord_y1 = plt.figure()
coord_x2_coord_y2= plt.figure()
coord_x3_coord_y3 = plt.figure()
fig = figure(
title='Зависимость множителя fi от коэффициента жесткости бандажа и его относительной массы',
x_axis_label='Коэффициент жесткости бандажа ',
y_axis_label='Множитель fi')

fig.line(coord_x15, coord_y15, line_width=3)
#fig.line(coord_x14, coord_y14, line_width=3,line_color="red")
fig.line(coord_x13, coord_y13, line_width=3,line_color="blue")
fig.line(coord_x12, coord_y12, line_width=3,line_color="orange")
fig.line(coord_x11, coord_y11, line_width=3,line_color="purple")
fig.line(coord_x10, coord_y10, line_width=3,line_color="red")
fig.line(coord_x9, coord_y9, line_width=3,line_color="green")
fig.line(coord_x8, coord_y8, line_width=3, line_color="pink")
fig.line(coord_x7, coord_y7, line_width=3, line_color="yellow")
fig.line(coord_x6, coord_y6, line_width=3, line_color="blue")
#fig.line(coord_x5, coord_y5, line_width=3, line_color="orange"))
fig.line(coord_x4, coord_y4, line_width=3,line_color="orange")
fig.line(coord_x2, coord_y2, line_width=3, line_color="purple")
#fig.line(coord_x1, coord_y1, line_width=3, line_color="green")
#fig.line(coord_x3, coord_y3, line_width=3, line_color="pink")
st.bokeh_chart(fig, use_container_width=True)
st.write("""phiA0 =""" + str('{:.5}'.format(phi_3)))
st.write("""phiB0 =""" + str('{:.5}'.format(phi_2)))
st.write("""phiA1 =""" + str('{:.5}'.format(phi_1)))
# Сделать график!!!!!!!!!!!!! 

fstA0=phi_3*f1
fstB0=phi_2*f1
fstA1=phi_1*f1
st.write(""" fstA0 = """ + str('{:.5}'.format(fstA0)))
st.write(""" fstB0 = """ + str('{:.5}'.format(fstB0)))
st.write(""" fstA1 = """ + str('{:.5}'.format(fstA1)))
st.write("""# Влияние вращения ротора на собственные частоты колебаний лопаток""")
B=0.5*(dsr/l2-1)*(0.5*nub)/((1/3)*nub)+M.sin(betta*M.pi/180)*M.sin(betta*M.pi/180)
st.write(""" B = """ + str('{:.4}'.format(B)))
fdin1=(fstA0**2+B*n**2)**0.5
fdin2=(fstB0**2+B*n**2)**0.5
fdin3=(fstA1**2+B*n**2)**0.5
st.write(""" fdin1 = """ + str('{:.6}'.format(fdin1)))
st.write(""" fdin2 = """ + str('{:.6}'.format(fdin2)))
st.write(""" fdin3 = """ + str('{:.6}'.format(fdin3)))
st.write("""# Вибрационная диаграмма лопаточного аппарата""")

k1 = 1
k2 = 2
k3 = 3
k4 = 4
k5 = 5
k6 = 6
k7 = 7
x1 = np.linspace(0, 65, 65)
y1 = k1*x1
y2 = k2*x1
y3 = k3*x1
y4 = k4*x1
y5 = k5*x1
y6 = k6*x1
y7 = k7*x1
f_max = (1+0.04)*(fstA0**2+B*x1**2)**0.5
f_min = (1-0.04)*(fstA0**2+B*x1**2)**0.5

p2 = figure(
     title='simple line example',
     x_axis_label='n, с^-1',
     y_axis_label='fд, Гц')

p2.line(x1, y1, legend_label='Trend', line_width=2, line_color = "pink")
p2.line(x1, y2, legend_label='Trend', line_width=2, line_color = "green")
p2.line(x1, y3, legend_label='Trend', line_width=2, line_color = "blue")
p2.line(x1, y4, legend_label='Trend', line_width=2, line_color = "red")
p2.line(x1, y5, legend_label='Trend', line_width=2, line_color = "orange")
p2.line(x1, y6, legend_label='Trend', line_width=2, line_color = "yellow")
p2.line(x1, y7, legend_label='Trend', line_width=2, line_color = "violet")
p2.line(x1, f_min, legend_label='Trend', line_width=2)
p2.line(x1, f_max, legend_label='Trend', line_width=2)
st.bokeh_chart(p2, use_container_width=True)
k = 1
k = st.slider('Введите кратность', min_value=0, max_value=7, step=1, value=k)
n_res_max = (1.04*fstA0)/(k**2-(1.04**2)*B)**0.5
n_res_min = (0.96*fstA0)/(k**2-(0.96**2)*B)**0.5
st.write(""" Максимальная резонансная частота = """ + str('{:.6}'.format(n_res_max)))
st.write(""" Минимальная резонансная частота = """ + str('{:.6}'.format(n_res_min)))
