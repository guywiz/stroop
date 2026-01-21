# Stroop

Ce dépôt contient un code minimaliste permettant de reproduire une expérience attestant de l'[*effet de Stroop*](https://fr.wikipedia.org/wiki/Effet_Stroop).

L'effet consiste à soumettre à un utilisateur deux stimulis, typiquement un mot et une couleur (d'encre utilisée pour afficher le mot), et à demander à l'utilisateur d'indiquer la couleur utilisée pour afficher le mot.

Les stimulis peuvent être *congruents* (le mot affiché est celui de la couleur utilisée pour l'afficher) ou *incongruents* (le mot indique une couleur différente de celle utilisée pour l'afficher).

([repris de Wikipedia](https://fr.wikipedia.org/wiki/Effet_Stroop))
"""... le temps de réaction — en d'autres termes le temps nécessaire à la dénomination de la couleur avec laquelle le mot est écrit — est beaucoup plus long lorsque le mot est incongruent (le mot « bleu » écrit en rouge) que lorsque le mot est congruent (le mot « rouge » écrit en rouge) ou neutre (le mot « lion » écrit en rouge).

Le pourcentage d'erreurs (dire bleu lorsque le mot « bleu » est écrit en rouge) est également plus élevé en présence des mots incongruents. Il existe donc un effet d'interférence sémantique, ou effet Stroop, provoqué par la lecture automatique du mot.
"""

## Expérience de Stroop

Le code implémente pour l'instant une application web très simple:

- L'utilisateur clique et obtient l'affichage d'un mot,
- Il clique ensuite sur un bouton indiquant la couelur du mot,
- Le temps écoule entre l'affichage et le second clic est mesuré et stocké dans un fichier local.

### Installer et utiliser l'application

L'application utilise le [framework `dash`](https://dash.plotly.com/).

Il est recommandé de créer un environnement dédié sous python 3.10 (par exemmple).

`conda create -n stroop python==3.10`

ou avec `venv`, au choix.

Le fichier `requirements.txt` contient les dépendances (seules dash est inclus au fichier, qui déclenche l'installation d'un tas de librairies annexes nécessaires à `dash`).

Puis reste à lancer l'application depuis un terminal, et depuis le répertoire où se trouve le code source:

`> python stroop.py`

avant de visualiser l'application dans le navigateur à l'URL:

`http://127.0.0.1:8050/`.

Les résultats de l'expérience sont pour l'instant ajouté à un fichier `/src/tmp.txt` (qui est créé au départ et auxquels toutes les mesures subséquentes s'jaoutent ensuite).

## Méthodologie

### Participants

Une première tâche pour réaliser l'expérience est de recruter un échantillon de participants.

- Cette tâche exige de caractériser la population depuis laquelle l'échantillon est extrait, ce qui cadre la généralité des conclusions qu'on pourra tirer de l'expérience.
- Il importe aussi de s'assurer que tous les participants s'exécutent dans les mêmes conditions.

### Analyse des résultats

Pour chacun des sujets, on considère différentes valeurs:

- `mean_RT_congruent`, `mean_RT_incongruent` (sur les essais corrects, c'est-à-dire sans erreur),
- `sd_RT_congruent`, `sd_RT_incongruent` (écart-type sur les valeurs retenues)

On peut aussi considérer:

- `error_rate_congruent`, `error_rate_incongruent`

Et pour chaque sujet on calcule:

- `diff_RT` = `mean_RT_incongruent` − `mean_RT_congruent`

On fait l'hypothèse de la normalité (de la distribution des valeurs),

et on forme les hypothèses à tester:

- HO (pas de différence entre stimulis congruents et stimulis incongruents), c'est-à-dire $\mu({\tt diff}) = 0$
- H1 (différence entre les stimulis), c'est-à-dire $\mu({\tt diff}) > 0$

L'analyse des résultats consiste à établir si la moyenne observée (dont on attend qu'elle soit supérieure à 0) est suffisamment grande pour conclure à une différence significative entre les deux conditions (congruence vs non congruence).

*Remarque*. (Ce type d'analyse rejoint le programme de l'atelier 2, en partie au moins).

- On dispose d'un échantillon $X$ (de $N$ valeurs $x_1, x_2, \ldots, x_N$ des différences de temps de réaction entre les deux conditions expérimentales), qui permet de calculer une moyenne observée $\bar X$.

- La moyenne observée $\bar X$ est en quelque sorte la meillleure estimation que l'on ait de la moyenne $\mu$ sur la population (la "vraie" moyenne).

- Or, la moyenne observée sur différents échantillons risquent fort de varier ... (en effet, si on considère un autre échantillon $X'$, on aura sans doute une autre valeur $\bar X' \not = \bar X$).
  - Si on imagine l'ensemble de tous les échantillons posisbles, on pourrait alors calculer la moyenne entre tous ces échantillons, notons la $\mu_{\bar X}$.
  - Fort heureusement, il se trouve que cette valeur coincide avec la moyenne, c'est-à-dire $\mu = \mu_{\bar X}$
  - Et de plus, l'écart-type $\sigma_{\bar X}$ sur l'ensemble de tous les échantillons est lié à l'écart-type $\sigma$ sur la population
  - Mieux encore, la distribution des moyennes observées suit une loi normale (dès lors que les échantillons sont de taille au moins $N \geq 30$)

Ainsi, si on calcule le $z$-score:

$z = \frac{\bar X - \mu_X}{\sigma_X} = \frac{\bar X - \mu}{\frac{\sigma}{\sqrt{N}}}$

on peut rejeter l'hypothèse nulle $H_0$ dès lors que $z$ est trop grand (on calcule la probabilité que $z$ soit au-delà de la moyenne d'au moins deux écart-type, typiquement).

Le problème est qu'on nbe connait pas la valeur $\sigma_X$. Nous pouvons en revanche l'estimer à partir des valeurs observées, en calculant

$s = \sqrt{\frac{\sum_i (x_i - \bar X)^2 }{N-1}}$

mais il nous alors remplacer le $z$ score par le calcul d'un $t$-score

$t = \frac{\bar X - \mu}{\frac{s}{\sqrt{N}}}$

Or, la distribution de ce $t$-score n'est plus une distribution normale et on doit se référer à une autre distribution (et donc à d'autres tables, [comme celle-ci](./src/t-table.pdf)) pour déterminer si le score est suffisamment grand pour rejeter $H_0$
  - A noter que la distribution à utliser dépend aussi du degré de liberté de l'expérience (qui est égal à $N - 1$ où $N$ est la taille des échantilllons)

## L'expérience de Stroop comme projet semestriel

A venir, un calendrier prévisionnel pour cadrer la mise en place de l'expérience et l'analyse des résultats, leurs présentation.

- L'expérience nécessite de bien s'organiser
  - pour arriver à faire tourner l'application
  - pour recruter l'échantillon de participants
  - pour noter rigoureusement la méthodologie suivie afin de pouvoir en rapporter clairement

- L'analyse nécessite de mettre en oeuvre les quelques connaissances statistiques de l'atelier 2
  - Comprendre ce qu'est une distribution normale
  - Comprendre ce qu'est un z-score et comment on l'utilise (pour le calcul de la $p$-value)
  - Comprendre la formulation des hypothèses $H_0$ et $H_1$ en lien avec le but poursuivi
  - Comprendre les conditions particulières qui amène au test de Student
- Savoir rapporter de la démarche suivie et des réulstats obtenus

### Regard critique sur la méthodologie

On peut penser quand dans cerains cas, les équipes auront suivi des raccourcis par manque de temps, par exemple

- Dans le cas d'un échantillon mal formé, il peut être intéressant de discuter de la validité de l'expérience ou des conclusiosn qui sont tirées. Pensons par exemple à des étudiants qui, à la bourre, décide de de prêter eux-mêmes à l'expérience à plusieurs reprises, ou encore de soumettre un même participant à l'expérience plusieurs fois, introduisant un biais d'apprentissage ...
- Dans le cas de données erronées (mauvais déroulé de l'expérience à cause de mauvaise condition, disons), données bruitées, nécessité de filtrer, etc.
- ...

### Variantes

On peut aller vers des variantes de l'expérience

- Plutôt que l'incongruence sur la couleur, on peut jouer sur les positionnement gauche-droite (gauche affiché à gauche ou ... droite
- A suivre

