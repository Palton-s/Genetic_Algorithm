import matplotlib.pyplot as plt
from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):

    Y = []
    # converte os cromossomos binários para decimais
    X = aux.converte_populacao(X, limites)
    # avalia quão bons os indivíduos são com base em uma gaussiana de variaveis dimensões

    for individuo in X:
        x = individuo[0]
        y = individuo[1]
        r1 = (x+1.5)**2 + (y-1.5)**2
        r2 = (x-1.0)**2 + (y+1.0)**2
        r3 = (x-1.02753)**2 + (y-1.5793)**2
        random_points = [[-0.5730190814373182, 1.1133101800664646], [-1.4861996650438938, -0.9004050816703724], [0.14868370307354528, -1.0277901981840407], [-1.5040675371220051, -0.10140018583878385], [0.2812806120517575, -0.9959156311503494], [-0.6326965728809371, -1.418631009015305], [-1.2008288252188888, -1.018523020048121], [-1.3823626040359085, 0.9457646097217305], [0.06793665643720814, 0.13559733521599027], [0.06231283662861209, -1.5281672275173213], [0.6499383094521569, -0.9527253123032335], [0.197410307436106, -1.9329924913188519], [0.6472051107462717, -0.294726397400479], [1.675630843751076, 0.0035076663160631405], [-0.728139876424577, -0.15903522727604358], [-0.6465846139006248, -0.10370495025819082], [-0.5777388022198418, 1.6879456952576715], [1.624504101046897, 1.8924824126833988], [0.14051163937017241, 0.7971860143882821], [1.0244134762484145, 1.2637928589945093], [1.5171922278754528, 0.7509318175163733], [-0.035051964737847996, -0.20965739172816766], [-0.7441397363890636, -0.3613044402517649], [-1.281445256809286, 0.5649705367154598], [0.9200562966770782, -1.5109509705900406], [0.21949226652130926, 0.9546359751026312], [0.05457392339016298, -0.5446744815551088], [1.4303375998703602, 0.17112424562522666], [0.90841034719858, -1.777192373903834], [1.80758124295485, -1.1997604962699522], [-0.2673414328256176, 1.5733944746188002], [-0.4035346806276414, -0.1879654192335818], [1.9260899693369828, 0.32208297738343594], [-0.9180044980208866, 1.9948416596986545], [-0.7862003920916831, -1.5906197537237876], [0.6441753892468367, 1.9055693838815966], [-0.6903157415114718, 1.3154910802216593], [-1.0032423269755704, -0.6702249853882183], [1.3611935630322218, 0.1465163936983389], [-0.35978621504604824, -1.6628604520689083], [0.7027317085709708, -1.9751168368384873], [-0.30207289896281875, 1.2593835605300079], [-0.17046917046567422, 1.64109750506088], [-0.3942080786630764, -0.6468992901613517], [0.5171317623414105, -0.7959576691418069], [0.6037371534931117, 1.8577542847500275], [1.4256559909746258, -0.30832053345692056], [0.7748582482006134, 0.5131240574314124], [0.47917311875408375, 1.6284594169501658], [1.4936150679848597, -1.0371548810661149], [1.8245316438796517, 0.7339956017101716], [-0.5683086465688163, -0.03789192339008984], [1.7301377359917653, -1.0039682274841222], [-1.6278665617390988, -0.726943533795958], [0.9002833009383266, -0.9193136531206525], [1.431622783747851, 1.06348249979666], [-0.5299773294007166, -0.6488270002622314], [0.537396950971579, -0.601133302574318], [-0.3833435303732511, 0.15908161130923038], [1.4631243123945468, -0.5886376176334851]]
        z = 0
        z += 0.8*np.exp(-(r1 )/(0.3**2))
        z += 0.879008*np.exp(-(r2 )/(0.03**2))
        z += 1.5345*np.exp(-(r3 )/(0.03**2))
        for i in range(len(random_points)):
            #z += 0.6*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
            z += ((i/len(random_points))*0.3+0.3)*np.exp(-((x-random_points[i][0])**2 + (y-random_points[i][1])**2)/(0.06**2))
        Y.append(z)
    return Y

def potential(A, B, C, x):
    result = A + (1/(B*np.sqrt(2*np.pi)))*np.exp(-((x-C)**2)/(2*(B**2)))

    return result


def potential_2(D, a, r, r_eq):
    m = len(a)
    somatorio = 1
    rho = r - r_eq
    for i in range(1,m+1):
        somatorio += a[i-1]*(rho**i)
    #V_ryd = -D*somatorio*np.exp(-a[0]**2)
    V_ryd = -D*somatorio*np.exp(-a[0]*rho)
    return V_ryd


"""table_s2 = [[1.00, -2.861030, -2.904236, -2.90461],
            [1.05, -2.881138, -2.924612, -2.92505],
            [1.10, -2.896661, -2.940398, -2.94060],
            [1.20, -2.917296, -2.961529, -2.96182],
            [1.30, -2.928109, -2.972775, -2.97320],
            [1.40, -2.932502, -2.977519, -2.97798],
            [1.42, -2.932825, -2.977901, -2.97835],
            [1.44, -2.932998, -2.978130, -2.97841],
            [1.4632, -2.933029, -2.978221, -2.97869],
            [1.48, -2.932948, -2.978179, -2.97860],
            [1.50, -2.932747, -2.978022, -2.97844],
            [1.60, -2.930379, -2.975811, -2.97626],
            [1.70, -2.926438, -2.971930, -2.97230],
            [1.80, -2.921631, -2.967091, -2.96761],
            [1.90, -2.916436, -2.961783, -2.96212],
            [2.00, -2.911170, -2.956339, -2.95674],
            [2.20, -2.901175, -2.945856, -2.94606],
            [2.40, -2.892510, -2.936624, -2.93717],
            [2.60, -2.885395, -2.928959, -2.92956],
            [2.80, -2.879755, -2.922839, -2.92341],
            [3.00, -2.875393, -2.918087, -2.91860],
            [3.20, -2.872075, -2.914472, -2.91507],
            [3.40, -2.869580, -2.911757, -2.91220],
            [3.60, -2.867718, -2.909734, -2.91027],
            [3.80, -2.866330, -2.908232, -2.90862],
            [4.00, -2.865296, -2.907115, -2.90767],
            [4.50, -2.863701, -2.905401, -2.90589],
            [5.00, -2.862888, -2.904532, -2.90504],
            [5.50, -2.862444, -2.904061, -2.90431],
            [6.00, -2.862184, -2.903787, -2.90439],
            [7.00, -2.861918, -2.903506, -2.90370],
            [8.00, -2.861795, -2.903376, -2.90396]
            ]
x = [table_s2[i][0] for i in range(len(table_s2))]
y = [table_s2[i][1] for i in range(len(table_s2))]
y_other = [potential_2(1.289183, [0.675107, 1.244958, 1.466933],x[i],  1.453162) for i in range(len(x))]"""


#plt.plot(x, y, 'o', color='black')
#plt.plot(x, y_other, 'o', color='red')
#plt.show()

