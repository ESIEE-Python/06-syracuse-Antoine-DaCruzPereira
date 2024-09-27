"""
Import des fonction Scatter, Figure du module plotly.graphobjects
"""
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """
    Retourne la suite de Syracuse de source n

    Args: n (int): la source de la suite

    Returns: list: la suite de Syracuse de source n
    """
    l = [n]
    am = n
    while am > 1:
        if am%2 == 0:
            am = am//2
            l.append(am)
        else:
            am = (am*3)+1
            l.append(am)
    return l

def temps_de_vol(l):
    """
    Retourne le temps de vol d'une suite de Syracuse

    Args: l (list): la suite de Syracuse

    Returns: int: le temps de vol
    """
    return len(l)-1

def temps_de_vol_en_altitude(l):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse

    Args: l (list): la suite de Syracuse

    Returns: int: le temps de vol en altitude
    """
    n = 0
    for i in range(1, len(l)):
        if l[i] > l[0]:
            n += 1
    return n


def altitude_maximale(l):
    """
    Retourne l'altitude maximale d'une suite de Syracuse

    Args: l (list): la suite de Syracuse

    Returns: int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():
    """
    Permet de tester la suite de syracuse avec les listes

    Arg: None

    Return: None
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
