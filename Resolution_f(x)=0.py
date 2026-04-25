import matplotlib.pyplot as plt
import math

# Fonction f et sa dérivée
def f(x):
    return x**3 - math.exp(-x) - 20

def df(x):
    return 3*x**2 + math.exp(-x)

# Calcul de l'ordre de convergence
def ordre_convergence(valeurs):
    if len(valeurs) < 4:
        return None

    alpha = valeurs[-1]
    p_vals = []

    for i in range(2, len(valeurs)-1):
        e1 = abs(valeurs[i+1] - alpha)
        e2 = abs(valeurs[i] - alpha)
        e3 = abs(valeurs[i-1] - alpha)

        if e1 > 0 and e2 > 0 and e3 > 0:
            try:
                p = math.log(e1/e2) / math.log(e2/e3)
                if not math.isnan(p) and not math.isinf(p):
                    p_vals.append(p)
            except:
                pass

    if len(p_vals) == 0:
        return None

    return sum(p_vals) / len(p_vals)

# Méthode de dichotomie
def dichotomie(a, b, eps):
    if f(a)*f(b) >= 0:
        raise ValueError("Intervalle invalide")

    valeurs = []
    n = 0

    while (b - a)/2 > eps:
        c = (a + b)/2
        valeurs.append(c)
        n += 1

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    racine = (a + b)/2
    valeurs.append(racine)

    return racine, n, valeurs

# Fonction de point fixe correcte stable et contractante
def g(x):
    return (math.exp(-x) + 20)**(1/3)

# Méthode du point fixe
def point_fixe(x0, eps, max_iter=1000):
    valeurs = [x0]
    n = 0

    while n < max_iter:
        x1 = g(x0)
        valeurs.append(x1)
        n += 1

        if abs(x1 - x0) < eps:
            return x1, n, valeurs

        x0 = x1

    raise ValueError("Pas de convergence")

# Méthode de Newton-Raphson
def newton_raphson(x0, eps, max_iter=1000):
    valeurs = [x0]
    n = 0

    while n < max_iter:
        x1 = x0 - f(x0)/df(x0)
        valeurs.append(x1)
        n += 1

        if abs(x1 - x0) < eps:
            return x1, n, valeurs

        x0 = x1

    raise ValueError("Pas de convergence")

# Exécution principale
eps = 1e-6

rd, nd, vd = dichotomie(2, 3, eps)
rf, nf, vf = point_fixe(2, eps)
rn, nn, vn = newton_raphson(2, eps)

print("Comparaison des méthodes terminée.")

# Tracé des erreurs
def tracer_erreurs(valeurs, titre):
    alpha = valeurs[-1]
    erreurs = [abs(x - alpha) for x in valeurs]

    plt.plot(erreurs, marker='o')
    plt.yscale('log')
    plt.xlabel("Itérations")
    plt.ylabel("Erreur")
    plt.title(titre)
    plt.grid(True)
    plt.show()

tracer_erreurs(vd, "Convergence par dichotomie")
tracer_erreurs(vf, "Convergence par point fixe")
tracer_erreurs(vn, "Convergence par Newton-Raphson")

# Comparaison globale
plt.figure(figsize=(8,5))

alpha_d = vd[-1]
alpha_f = vf[-1]
alpha_n = vn[-1]

plt.plot([abs(x - alpha_d) for x in vd], marker='o', label='Dichotomie')
plt.plot([abs(x - alpha_f) for x in vf], marker='s', label='Point fixe')
plt.plot([abs(x - alpha_n) for x in vn], marker='^', label='Newton-Raphson')

plt.yscale('log')
plt.xlabel("Itérations")
plt.ylabel("Erreur |xₙ − α|")
plt.title("Comparaison des méthodes numériques")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()



