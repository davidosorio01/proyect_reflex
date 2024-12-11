import reflex as rx
from Reflex_py.backend.backend_calculadora import Calculadora

def valor_calculadora():
    return rx.heading(
                Calculadora.valor,
                width="100%",
                margin_top="50%",
                margin_bottom="20px",
                text_align="right",
                font_size="3em"
            ),