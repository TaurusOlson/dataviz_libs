"""A simple app using bokeh-server to play with mtcars dataset"""

import logging

logging.basicConfig(level=logging.DEBUG)

import numpy as np

from bokeh.plotting import figure
from bokeh.models import Plot, ColumnDataSource, HoverTool
from bokeh.properties import Instance
from bokeh.server.app import bokeh_app
from bokeh.server.utils.plugins import object_page
from bokeh.models.widgets import HBox, Slider, TextInput, VBoxForm
import pandas as pd


mtcars = pd.read_csv("data/mtcars.csv")

class MtcarsApp(HBox):
    """An example of a browser-based, interactive plot with slider controls."""

    extra_generated_classes = [["MtcarsApp", "MtcarsApp", "HBox"]]

    inputs = Instance(VBoxForm)

    text = Instance(TextInput)

    cyl = Instance(Slider)
    hp = Instance(Slider)
    carb = Instance(Slider)

    plot = Instance(Plot)
    source = Instance(ColumnDataSource)

    @classmethod
    def create(cls):
        """One-time creation of app's objects.

        This function is called once, and is responsible for
        creating all objects (plots, datasources, etc)
        """
        obj = cls()

        data = dict(name=mtcars.name, wt=mtcars.wt, mpg=mtcars.mpg)
        obj.source = ColumnDataSource(data=data)

        # TEXT INPUT
        obj.text = TextInput(title="title", name='title',
                value='Distance parcourue par les voitures')

        # SLIDER
        # cyl
        obj.cyl = Slider(
            title="cyl", name='cyl',
            value=mtcars.cyl.min(),
            start=mtcars.cyl.min(),
            end=mtcars.cyl.max(), 
            step=1
        )

        # hp
        obj.hp = Slider(
            title="hp", name='hp',
            value=mtcars.hp.mean(), 
            start=mtcars.hp.min(), 
            end=mtcars.hp.max(), 
        )

        # carb
        obj.carb = Slider(
            title="carb", name='carb',
            value=mtcars.carb.min(),
            start=mtcars.carb.min(),
            end=mtcars.carb.max(),
            step=1
        )

        toolset = "pan,reset,resize,save,wheel_zoom,hover"

        # Generate a figure container
        plot = figure(title_text_font_size="12pt",
                      plot_height=500,
                      plot_width=500,
                      tools=toolset,
                      title=obj.text.value,
                      x_range=[mtcars.wt.min()-1, mtcars.wt.max()+1],
                      y_range=[mtcars.mpg.min()-1, mtcars.mpg.max()+1]
        )

        # Plot the line by the x,y values in the source property
        colors = {3: "steelblue", 4: "indianred", 5: "seagreen"}
        gear_colors = map(lambda x: colors[x], mtcars.gear)
        # plot.scatter('x', 'y', color="indianred", size=12, alpha=0.6,
        #         source=obj.source)
        plot.circle('wt', 'mpg', color="indianred", size=12, fill_alpha=0.6,
                source=obj.source)

        # HoverTool
        hover = plot.select(dict(type=HoverTool))
        hover.tooltips = [
            ("name", "@name"),
            ("(wt, mpg)", "(@wt, @mpg)"),
        ]

        plot.xaxis.axis_label = "Weight (lbs)"
        plot.yaxis.axis_label = "Distance (miles/gallon)"

        obj.plot = plot
        obj.update_data()

        obj.inputs = VBoxForm(
            children=[ obj.text, obj.cyl, obj.hp, obj.carb ]
        )

        obj.children.append(obj.inputs)
        obj.children.append(obj.plot)

        return obj

    def setup_events(self):
        """Attaches the on_change event to the value property of the widget.

        The callback is set to the input_change method of this app.
        """
        super(MtcarsApp, self).setup_events()
        if not self.text:
            return

        # Text box event registration
        self.text.on_change('value', self, 'input_change')

        # Slider event registration
        for w in ["cyl", "hp", "carb"]:
            getattr(self, w).on_change('value', self, 'input_change')

    def input_change(self, obj, attrname, old, new):
        """Executes whenever the input form changes.

        It is responsible for updating the plot, or anything else you want.

        Args:
            obj : the object that changed
            attrname : the attr that changed
            old : old value of attr
            new : new value of attr
        """
        self.update_data()
        self.plot.title = self.text.value

    def update_data(self):
        """Called each time that any watched property changes.

        This updates the sin wave data with the most recent values of the
        sliders. This is stored as two numpy arrays in a dict into the app's
        data source property.
        """
        # Get the current slider values
        cyl_min = self.cyl.value
        hp_min = self.hp.value
        carb_min = self.carb.value

        # Generate the sine wave
        selected = mtcars[(mtcars.cyl >= cyl_min) &\
                   (mtcars.hp >= hp_min) &\
                   (mtcars.carb >= carb_min)]

        self.source.data = dict(name=selected.name, wt=selected.wt, mpg=selected.mpg)


@bokeh_app.route("/bokeh/mtcars/")
@object_page("sin")
def make_mtcars():
    app = MtcarsApp.create()
    return app
