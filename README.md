# La visualisation des données pour tous en Python

Ce repository contient les IPython notebooks utilisés lors de la présentation
sur les alternatives à matplotlib, qui a eu lieu à l'[IRAP][irap] le 5 juin 2015 dans
le cadre des rencontres Python ktafé.

La présentation aborde des librairies de visualisation de données qui
pourraient être utiles aux chercheurs en fonction de leur besoin:

* [seaborn][seaborn]: une librairie s'appuyant sur matplotlib mais orientée analyse statistique
* [ggplot][ggplot]: une librairie permettant de réaliser des plots en utilisant une API simple ("Grammar Of Graphics")
* [bokeh][bokeh]: une librairie moderne utilisant un moteur Javascript pour créer des plots interactifs comparables à d3.js


## Installation du IPython notebook et des librairies de visualisation

* Avec [pip][pip]:

        pip install -r requirements.txt


* Avec [anaconda][anaconda]:

        conda update conda
        conda update ipython ipython-notebook ipython-qtconsole pandas
        conda install seaborn bokeh

**NOTE**: ggplot n'est pas disponible depuis conda. 


## Lancement de l'application avec bokeh-server

`bokeh` permet d'interagir avec des données grâce à une application `Flask`[flask]. La communication entre l'application et les données se fait avec l'exécutable `bokeh-server`:

        cd mtcars_app
        bokeh-server --script app.py

Ouvrez alors votre navigateur à l'adresse URL:

        http://localhost:5006/bokeh/mtcars


## Notes diverses

* La commande:

        %matplotlib inline

permet d'afficher les plots dans le notebook.

* L'extension de IPython, [watermark][watermark] permet d'afficher les versions des modules utilisés.

        # Installation
        %install_ext https://raw.githubusercontent.com/rasbt/watermark/master/watermark.py

        # Chargement
        %load_ext watermark

        # Exécution
        %watermark -v -p bokeh,seaborn,matplotlib,pandas,numpy,scipy,ggplot



[anaconda]: https://store.continuum.io/cshop/anaconda/
[pip]: https://pip.pypa.io/en/stable/
[seaborn]: http://stanford.edu/~mwaskom/software/seaborn/
[ggplot]: http://ggplot.yhathq.com/
[bokeh]: http://bokeh.pydata.org/en/latest/
[irap]: http://www.irap.omp.eu/
[watermark]: https://github.com/rasbt/watermark
[flask]: http://flask.pocoo.org/
