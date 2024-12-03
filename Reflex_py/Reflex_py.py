import reflex as rx
from Reflex_py.views.header.header import header
from Reflex_py.views.links.links import links
from Reflex_py.components.footer import footer
from Reflex_py.views.botones.botones import *

class State(rx.State):
    valor = [""]
    union_str: str
    i = 0
    
    def valores1(self):
        self.valor.append(1)
    
    def valores2(self):
        self.valor.append(2)
        
    def valores3(self):
        self.valor.append(3)
        
    def valores4(self):
        self.valor.append(4)
    
    def valores5(self):
        self.valor.append(5)
        
    def valores6(self):
        self.valor.append(6)
        
    def valores7(self):
        self.valor.append(7)
        
    def valores8(self):
        self.valor.append(8)
        
    def valores9(self):
        self.valor.append(9)
        
    def valores0(self):
        self.valor.append(0)
    
    def valoresdot(self):
        self.valor.append(".")
    
    def valoresplus(self):
        self.valor.append("+")
        
    def valoresminus(self):
        self.valor.append("-")
    
    def valoresdivide(self):
        self.valor.append("/")
    
    def valoresmult(self):
        self.valor.append("*")
        
    def valoresporc(self):
        self.valor.append("%")
        
        self.valor = [str(i) for i in self.valor]
        self.union_str = ""
        
        for self.i in self.valor:
            if self.i == "%":
                pass
            else:
                self.union_str += str(self.i)

        self.valor = f"= {eval(self.union_str)/100}"
    
    def valoresdel(self):
        self.valor.remove(self.valor[-1])
        
    def valoresiqual(self):
        self.valor = [str(i) for i in self.valor]
        self.union_str = ""
        
        for self.i in self.valor:
            self.union_str += str(self.i)

        self.valor = f"= {eval(self.union_str)}"
        
    def clear(self):
        self.valor = [""]
        self.valor.clear()
        self.valor.append("")
            

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

@rx.page(route="/calculadora", title="Calculadora")
def index():
    return rx.center(
        rx.card(
            rx.heading(
                State.valor,
                width="100%",
                margin_top="50%",
                margin_bottom="20px",
                text_align="right",
                font_size="3em"
            ),
            rx.card(
                rx.hstack(
                    botones_icon("refresh-cw-off", on_click=State.clear),
                    botones_icon("circle-x", on_click=State.valoresdel),
                    botones_icon("percent", on_click=State.valoresporc),
                    botones_icon("divide", on_click=State.valoresdivide),
                    margin = "10px",
                ),
                rx.hstack(
                    botones_inferiores("7", on_click=State.valores7),
                    botones_inferiores("8", on_click=State.valores8),
                    botones_inferiores("9", on_click=State.valores9),
                    botones_icon("x", on_click=State.valoresmult),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_secundarios("4", on_click=State.valores4),
                    botones_secundarios("5", on_click=State.valores5),
                    botones_secundarios("6", on_click=State.valores6),
                    botones_icon("minus", on_click=State.valoresminus),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_principales("1", on_click=State.valores1),
                    botones_principales("2", on_click=State.valores2),
                    botones_principales("3", on_click=State.valores3),
                    botones_icon("plus", on_click=State.valoresplus),
                    margin = "10px"
                ),
                rx.hstack(
                    botones_principales("0", on_click=State.valores0),
                    botones_icon("dot", on_click=State.valoresdot),
                    botones_icon("equal", on_click=State.valoresiqual),
                    margin = "10px",
                    margin_left = "98px",
                ),
                #ESTILOS CARD
                padding="20px",
                width="100%",
            ),
        ),
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
