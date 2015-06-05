# La visualisation des données pour tous en Python

Ce repository contient les IPython notebooks utilisés lors de la présentation
sur les alternatives à matplotlib, qui a eu lieu à l'[IRAP][irap] le 5 juin 2015 dans
le cadre des rencontres Python kt'afé.

La présentation aborde des librairies de visualisation de données qui
pourraient être utiles aux chercheurs en fonction de leur besoin:

* [seaborn][seaborn]: une librairie s'appuyant sur matplotlib mais orientée analyse statistique
* [ggplot][ggplot]: une librairie permettant de réaliser des plots en utilisant une API simple ("Grammar Of Graphics")
* [bokeh][bokeh]: une librairie moderne utilisant un moteur Javascript pour créer des plots interactifs comparables à d3.js


## Installation du IPython notebook et des librairies de visualisation

* Avec [pip][pip]:

    pip install 'ipython[notebook]'
    pip install seaborn ggplot bokeh


* Avec [anaconda][anaconda]:

    conda update conda
    conda update ipython ipython-notebook ipython-qtconsole
    conda install seaborn bokeh


**NOTE**: ggplot n'est pas disponible depuis conda. 


[anaconda]: https://store.continuum.io/cshop/anaconda/
[pip]: https://pip.pypa.io/en/stable/
[seaborn]: http://stanford.edu/~mwaskom/software/seaborn/
[ggplot]: http://ggplot.yhathq.com/
[bokeh]: http://bokeh.pydata.org/en/latest/
[irap]: http://www.irap.omp.eu/
