# Composition

from ggplot import *


# Exemple 1:
ggplot(aes(x="carat", y="price", color="cut", size="table"), data=diamonds) +\
    geom_point(alpha=0.5) + ggtitle("Diamonds")


# Exemple 2:
ggplot(diamonds, aes(x='price', fill='cut')) +\
    geom_density(alpha=0.25) +\
    facet_grid("clarity")


# Exemple 3:
ggplot(aes(x="wt", y="hp", label="name"), data=mtcars) +\
    geom_point(color="steelblue", size=50) +\
    ggtitle("Puissance en fonction du poids") +\
    geom_hline(yintercept=mtcars.hp.mean(), color="red") +\
    geom_text(alpha=0.5) +\
    xlab("Poids (lb/1000)") + ylab("Puissance (chevaux)")
