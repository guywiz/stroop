<!-- lang: fr -->

# Stroop "fraction"

Ce dépôt contient un code minimaliste permettant de reproduire l'expérience classique attestant de l'[*effet de Stroop*](https://fr.wikipedia.org/wiki/Effet_Stroop) dans une variante qui mérite d'être examinée.

L'expérience soumet de manière répétée un utilisateur à un stimulus : deux nombres sont affichés à l'écran, sous forme de fractions de deux entiers (entre 1 et 9). L'un d'eux est plus grand en magnitude, même s'il utilise des entiers (au numérateur et/ou dénominateur qui sont plus petits). La tâche de l'utilisateur consiste à indiquer, rapidement "sans réfléchir", quel nombre est le plus grand (en magnitude) en tapant un touche au clavier: "F" si le nombre le plus grand est à gauche, "J" sinon.

Les stimuli peuvent être *congruents* (le nombre affichant globalement de plus grands entiers est effectivement le plus grand des deux) ou *incongruents* (le mot affichant globalement de plus grands entiers est plus petit).

L'image ici montre un cas de stimuli *incongruents*.

---

<img src="./screenshot_stroop_fractions.png" width="60%">

---

Cette expérience doit montrer que :([adapté de Wikipédia](https://fr.wikipedia.org/wiki/Effet_Stroop))
"... *le temps de réaction — en d'autres termes le temps nécessaire à indiquer lequel des nombres est le plus grand (en magnitude) — est beaucoup plus long lorsque les stimuli sont incongruents que lorsqu'ils sont congruents.*

*Le pourcentage d'erreurs est également plus élevé en présence des stimuli incongruents. Il existe donc un effet d'interférence sémantique, ou effet Stroop, provoqué par la taille d'affichage des nombres.*
"

P.S. Cette variante pourrait toutefois exiger de nuancer la conclusion, on pourrait penser que le conflit entre système 1 et système 2 (de Kahneman) que soulève l'expérience de Stroop est ici moins prononcé (comment en faire le constat ?). C'est l'un des intérêts de cette variante.
