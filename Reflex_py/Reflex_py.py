import reflex as rx
from Reflex_py.views.header.header import header
from Reflex_py.views.header.header_calculadora import valor_calculadora
from Reflex_py.views.links.links import links
from Reflex_py.components.footer import footer
from Reflex_py.views.botones.botones import *
from Reflex_py.backend.backend_calculadora import Calculadora
        
#PÁGINA PRINCIPAL
@rx.page(route="/", title="Menu")
def index():
    return rx.center(
        rx.card(
            rx.vstack(
                header(),
                links(),
                footer(),
                max_width="600px",
            ),  
            width="40%",
            heigth="100%",
        ),
    )

#PÁGINA CALCULADORA
@rx.page(route="/calculadora", title="Calculadora")
def index():
    return rx.center(
        rx.card(
            valor_calculadora(),
            rx.card(
                rx.hstack(
                    botones_icon("refresh-cw-off", on_click=Calculadora.clear),
                    botones_icon("circle-x", on_click=Calculadora.valoresdel),
                    botones_icon("percent", on_click=Calculadora.valoresporc),
                    botones_icon("divide", on_click=Calculadora.simbol("/")),
                    margin = "10px",
                ),
                rx.hstack(
                    botones_inferiores("7", on_click=Calculadora.valores(7)),
                    botones_inferiores("8", on_click=Calculadora.valores(8)),
                    botones_inferiores("9", on_click=Calculadora.valores(9)),
                    botones_icon("x", on_click=Calculadora.simbol("*")),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_secundarios("4", on_click=Calculadora.valores(4)),
                    botones_secundarios("5", on_click=Calculadora.valores(5)),
                    botones_secundarios("6", on_click=Calculadora.valores(6)),
                    botones_icon("minus", on_click=Calculadora.simbol("-")),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_principales("1", on_click=Calculadora.valores(1)),
                    botones_principales("2", on_click=Calculadora.valores(2)),
                    botones_principales("3", on_click=Calculadora.valores(3)),
                    botones_icon("plus", on_click=Calculadora.simbol("+")),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_principales("0", on_click=Calculadora.valores(0)),
                    botones_icon("dot", on_click=Calculadora.simbol(".")),
                    botones_icon("equal", on_click=Calculadora.valoresiqual),
                    margin = "10px",
                    margin_left = "98px",
                ),
                #ESTILOS CARD HIJA
                padding="20px",
                width="100%",
            ),
        ),
        #ESTILOS DE CENTER
        width="100%",
        height="100%",
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=False,
        radius="large",
        accent_color="red",
    ),
)
app.add_page(index) 
app._compile()
