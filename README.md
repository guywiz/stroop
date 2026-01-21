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



## Mise en place de l'expérience

### Participants

Une première tâche pour réaliser l'expérience est de recruter un échantillon de participants.

- Cette tâche exige de caractériser la population depuis laquelle l'échantillon est extrait, ce qui cadre la généralité des conclusions qu'on pourra tirer de l'expérience.
- Il importe aussi de s'assurer que tous les participants s'exécutent dans les mêmes conditions.

### Analyse des résultats



  - Dans le cas d'un échantillon mal formé, il peut être intéressant de discuter de la validité de l'expérience ou des conclusiosn qui sont tirées. Pensons par exemple à des étudiants qui, à la bourre, décide de de prêter eux-mêmes à l'expérience à plusieurs reprises, ou encore de soumettre un même participant à l'expérience plusieurs fois, introduisant un biais d'apprentissage ...