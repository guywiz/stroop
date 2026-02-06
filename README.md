<!-- lang: fr -->

# Stroop "classique"

Ce dépôt contient un code minimaliste permettant de reproduire une expérience attestant de l'[*effet de Stroop*](https://fr.wikipedia.org/wiki/Effet_Stroop).

L'expérience classique soumet de manière répétée un utilisateur à un stimulus : un mot et une couleur (d'encre utilisée pour afficher le mot). La tâche de l'utilisateur consiste à indiquer la couleur utilisée pour afficher le mot.

Les stimuli peuvent être *congruents* (le mot affiché est celui de la couleur utilisée pour l'afficher) ou *incongruents* (le mot indique une couleur différente de celle utilisée pour l'afficher).

Cette expérience montre que :([repris de Wikipédia](https://fr.wikipedia.org/wiki/Effet_Stroop))
"... *le temps de réaction — en d'autres termes le temps nécessaire à la dénomination de la couleur avec laquelle le mot est écrit — est beaucoup plus long lorsque le mot est incongruent (le mot « bleu » écrit en rouge) que lorsque le mot est congruent (le mot « rouge » écrit en rouge) ou neutre (le mot « lion » écrit en rouge).*

*Le pourcentage d'erreurs (dire bleu lorsque le mot « bleu » est écrit en rouge) est également plus élevé en présence des mots incongruents. Il existe donc un effet d'interférence sémantique, ou effet Stroop, provoqué par la lecture automatique du mot.*
"

On peut imaginer des variantes de cette expérience. Ce dépôt propose certaines variantes.

## Expérience de Stroop

Le code implémente des variantes de l'expérience de Stroop. Chaque variante a un code qui lui est propre, dans un dossier dédié. L'expérience se déroule à l'aide d'une application web très simple :

- L'utilisateur clique et obtient l'affichage d'un stimulus (un mot, par exemple),
- Il clique ensuite sur un bouton (indiquant la couleur du mot), ou tape sur une touche du clavier.
- Le temps écoulé entre l'affichage et l'action de l'utilisateur est mesuré et stocké dans un fichier local.

En amont de l'expérience, l'utilisateur renseigne son profil (âge, filière de formation, etc.), ce qui permet éventuellement d'analyser les résultats en fonction des profils.

### Installer et utiliser l'application

L'application utilise le [framework `dash`](https://dash.plotly.com/).

Il est recommandé, voire *indispensable*, de créer un environnement dédié sous python 3.10 (par exemple).

#### Création d'un environnement à l'aide de `venv`

([Repris de la documentation officielle de W3Schools](https://www.w3schools.com/python/python_virtualenv.asp))

Typiquement à l'aide d'un terminal (console de commande), un dossier `my_env` (c'est un exemple, vous pouvez appelé votre environnnement comme vous voulez, `stroop`, ou `pydash`, ...) sera créé pour stocker les informations propres à l'environnement (il faut se souvenir où se trouve ce dossier *`<path_to>`*`/myenv`, par exemple `C:\Program Files\...\my_env` sous Windows, ou `/Users/username/Documents/.../my_env` sous OS X (Mac), etc.).

1) L'environnement créé s'appuie sur une version de `python` déjà installée sur ma machine hôte. Nous allons supposer que `python 3.x` est disponible et qu'il est accessible via la commande `python3`.

Ainsi, on peut créer un environnement à l'aide de la commande :

`python3 -m venv` *`<path_to>`*`/myenv`

(par exemple `python3 -m venv C:\Program Files\...\my_env`, `python3 -m venv /Users/username/Documents/.../my_env`)

2) On active l'environnement en faisant, depuis l'endroit où se trouve l'environnement :

`source <path_to>/myenv/bin/activate`

ou

`./<path_to>/myenv/bin/activate`


Le prompt du terminal affiche alors le nom de l'environnement en préfixe, indiquant que l'environnement est bien activé.

`(my_env) >`

3) On peut ensuite se déplacer dans le dossier du projet et installer les librairies requises en faisant, par exemple :

`(my_env) > pip install -r requirements.txt`

En ce qui nous concerne, le fichier `requirements.txt` contient les dépendances de l'application (à d'autres librairies qu'il est nécessaire d'installer).

#### Création d'un environnement à l'aide de `conda`

La création d'un environnement avec `conda` est très similaire, et nécessite de l'avoir installé au préalable, souvent en installant l'[application Anaconda](https://www.anaconda.com/download) (avec une interface graphique, et un accès à un ensemble d'autres applications).

À la différence de `venv`, conda installe les informations des environnements dans un dossier qui lui est propre (nul besoin de se remémorer là où l'environnement est installé).

`conda create -n my_env python==3.10`

qui précise aussi la version de python à utiliser (si on omet ce paramètre, la dernière version est installée).

On active l'environnement à l'aide de la commande (exécutée dans un terminal) :

`conda activate my_env`

On procède à l'installation de librairies externes soit à l'aide de la commande :

`pip install -r requirements.txt`

(on peut aussi utiliser `conda install <library_name>` pou rinstalle rune librairie en particulier ou `conda install --file requirements.txt` pour installer les librairies toutes à la fois).

### Lancer l'application

Puis reste à lancer l'application depuis un terminal, et depuis le répertoire où se trouve le code source.

Le code source des applications se trouve dans le dossier `src`. Celui-ci contient un dossier pour chaque variante de l'expérience de Stroop.

Nous allons supposer que vous avez téléchargé l'un de ces dossiers (la variante que vous allez étudier).

Il suffit alors de se placer au niveau du fichier `app.py` et de le lancer :

`> python app.py`

avant de visualiser l'application dans le navigateur à l'URL:

`http://127.0.0.1:8050/`.

Les résultats de l'expérience sont ajoutés à un fichier `results.txt` (qui est créé au départ et auxquels toutes les mesures subséquentes s’ajoutent ensuite).

## Méthodologie

### Participants

Une première tâche pour réaliser l'expérience est de recruter un échantillon de participants.

- Cette tâche exige de caractériser la population depuis laquelle l'échantillon est extrait, ce qui cadre la généralité des conclusions qu'on pourra tirer de l'expérience.
- Il importe aussi de s'assurer que tous les participants s'exécutent dans les mêmes conditions.

### Analyse des résultats

Pour chacun des sujets, on considère différentes valeurs :

- `mean_RT_congruent`, `mean_RT_incongruent` (qui calcule le "mean reaction time" dans le cas de stimuli congruents ou incongruents sur les essais corrects, c'est-à-dire sans erreur),
- `sd_RT_congruent`, `sd_RT_incongruent` (écart-type sur les valeurs retenues)

On peut aussi considérer :

- `error_rate_congruent`, `error_rate_incongruent`

Et pour chaque sujet on calcule :

- `diff_RT` = `mean_RT_incongruent` − `mean_RT_congruent`

On fait l'hypothèse de la normalité (de la distribution des valeurs),

et on formule les hypothèses à tester :

- $H_0$ (pas de différence entre stimuli congruents et stimuli incongruents), c'est-à-dire $\mu({\text diff}) = 0$
- $H_1$ (différence entre les stimuli), c'est-à-dire $\mu({\tt diff}) > 0$

L'analyse des résultats consiste à établir si la moyenne observée (dont on attend qu'elle soit supérieure à 0) est suffisamment grande pour conclure à une différence significative entre les deux conditions (congruence vs non congruence).

*Remarque*. (Ce type d'analyse rejoint le programme de l'atelier 2, en partie au moins).

- On dispose d'un échantillon $X$ (de $N$ valeurs $x_1, x_2, \ldots, x_N$ des différences de temps de réaction entre les deux conditions expérimentales), qui permet de calculer une moyenne observée $\overline X$.

- La moyenne observée ${\overline X}$ est en quelque sorte la meilleure estimation que l'on ait de la moyenne $\mu$ sur la population (la "vraie" moyenne).

- Or, la moyenne observée sur différents échantillons risquent fort de varier ... (en effet, si on considère un autre échantillon $X'$, on aura sans doute une autre valeur ${\overline X'} \not = {\overline X}$).
  - Si on imagine l'ensemble de tous les échantillons possibles, on pourrait alors calculer la moyenne de toutes les moyennes ${\overline X}, {\overline X'}, \ldots$ de tous ces échantillons ; notons la $\mu_{{\overline X}}$.
  - Fort heureusement, il se trouve que cette valeur coïncide avec la moyenne, c'est-à-dire $\mu = \mu_{{\overline X}}$
  - Et de plus, l'écart-type $\sigma_{{\overline X}}$ sur l'ensemble de tous les échantillons est lié à l'écart-type $\sigma$ sur la population, plus précisément $\sigma_X = \frac{\sigma}{\sqrt{N}}$
  - Mieux encore, la distribution des moyennes observées suit une loi normale (dès lors que les échantillons sont de taille au moins $N \geq 30$)

Ainsi, on calcule le $z$-score:

$z = \frac{{\overline X} - \mu_X}{\sigma_X} = \frac{{\overline X} - \mu}{\frac{\sigma}{\sqrt{N}}}$

Sachant que les valeurs $z$ suivent elles aussi une distribution normale (de moyenne 0 et de variance 1), on peut rejeter l'hypothèse nulle $H_0$ dès lors que $z$ est trop grand (on calcule la probabilité que $z$ soit au-delà de la moyenne d'au moins deux écart-types, typiquement).

Le problème est qu'on ne connaît pas la valeur $\sigma_X$. Nous pouvons en revanche l'estimer à partir des valeurs observées, en calculant

$s = \sqrt{\frac{\sum_i (x_i - {\overline X})^2 }{N-1}}$

mais il nous faut alors remplacer le $z$ score par le calcul d'un $t$-score

$t = \frac{{\overline X} - \mu}{\frac{s}{\sqrt{N}}}$

Or, la distribution de ce $t$-score n'est plus une distribution normale et on doit se référer à une autre distribution (la distribution de Student, et donc à d'autres tables, [comme celle-ci](./src/t-table.pdf)) pour déterminer si le score est suffisamment grand pour rejeter $H_0$
  - À noter que la distribution à utiliser dépend aussi du degré de liberté de l'expérience (qui est égal à $N - 1$ où $N$ est la taille des échantilllons)

## L'expérience de Stroop comme projet semestriel

À venir, un calendrier prévisionnel pour cadrer la mise en place de l'expérience et l'analyse des résultats, leur présentation.

- L'expérience nécessite de bien s'organiser
  - pour arriver à faire tourner l'application
  - pour recruter l'échantillon de participants
  - pour noter rigoureusement la méthodologie suivie afin de pouvoir en rapporter clairement

- L'analyse nécessite de mettre en oeuvre les quelques connaissances statistiques de l'atelier 2
  - Comprendre ce qu'est une distribution normale
  - Comprendre ce qu'est un $z$-score et comment on l'utilise (pour le calcul de la $p$-value)
  - Comprendre la formulation des hypothèses $H_0$ et $H_1$ en lien avec le but poursuivi
  - Comprendre les conditions particulières qui amène au test de Student

- Savoir rapporter de la démarche suivie et des résultats obtenus sous forme de tableau ou de graphique (voir atelier 3)

### Regard critique sur la méthodologie

On peut penser quand dans certains cas, les équipes auront suivi des raccourcis par manque de temps, par exemple :

- Dans le cas d'un échantillon mal formé, il peut être intéressant de discuter de la validité de l'expérience ou des conclusions qui sont tirées. Pensons par exemple à des étudiants qui, à la bourre, décide de se prêter eux-mêmes à l'expérience à plusieurs reprises, ou encore de soumettre un même participant à l'expérience plusieurs fois, introduisant un biais d'apprentissage ...
- Dans le cas de données erronées (mauvais déroulé de l'expérience à cause de mauvaises conditions, disons), données bruitées, nécessité de filtrer, etc.
- ...

Dans tous les cas, il sera important de restituer honnêtement les conditions de réalisation de l'expérience (il en va de sa valeur scientifique !)