import seaborn as sns
from ipyleaflet import Map  
from shinywidgets import output_widget, render_widget  

# Import data from shared.py
from shared import df
from shiny import App, render, ui

# Import data from plot_utils.py
from utils.plot_utils import fullRRP

# The contents of the first 'page' is a navset with two 'panels'.
page1 = ui.page_fluid(
    ui.card(
        ui.card_header("Median Hourse Price by County"),
        ui.p(output_widget("map"))
    )
)

# page2 = ui.navset_card_underline(
#     ui.nav_panel("Plot", ui.output_plot("hist")),
#     ui.nav_panel("Table", ui.output_data_frame("data")),
#     footer=ui.input_select(
#         "var", "Select variable", choices=["bill_length_mm", "body_mass_g"]
#     ),
#     title="Penguins data",
# )

page2 = ui.page_fluid(
    ui.card(
        ui.card_header("Residential Property Price Register"),
        ui.output_data_frame("data"),
        ui.p("This is still the body."),
        ui.card_footer(
            ui.input_select(
                "var", "Select variable", choices=["bill_length_mm", "body_mass_g"]
            )
        ),
        full_screen=True
    ),
    ui.card(
        ui.card_header("This is the header"),
        ui.output_data_frame("read_fullRRP"),
        ui.p("This is still the body."),
        ui.card_footer("This is the footer"),
        full_screen=True
    )
)

app_ui = ui.page_navbar(
    ui.nav_spacer(),  # Push the navbar items to the right
    ui.nav_panel("Map", page1),
    ui.nav_panel("Stats", page2),
    title="House Prices Ireland",
)


def server(input, output, session):
    @render_widget  
    def map():
        return Map(center=(53.4494762, -7.5029786), zoom=6)
    
    @render.plot
    def hist():
        p = sns.histplot(df, x=input.var(), facecolor="#007bc2", edgecolor="white")
        return p.set(xlabel=None)

    @render.data_frame
    def data():
        return df[["species", "island", input.var()]]
    
    @render.data_frame
    def read_fullRRP():
        return fullRRP

app = App(app_ui, server)