import reflex as rx
from Reflex_py.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Diferentes aplicaciones:",
            size="4",
        ),
        link_button(
            text="CALCULADORA",
            url="/calculadora",
            icon_text="calculator",
        ),
        link_button(
            text="FORMULARIO",
            url="/",
            icon_text="file-text",
        ),
        link_button(
            text="DATA SCIENCE",
            url="/datascience",
            icon_text="database",
        ),
        link_button(
            text="INFORMACIÓN",
            url="/",
            icon_text="info", 
        ),
         #linea separadora
        rx.divider(
            size="4",
        ),
        width="100%",
    )