import reflex as rx
from Reflex_py.components.link_button import link_personal

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/favicon.ico",
                size="xl",
            ),
            rx.text(
                "@dosorio_01",
                #ESTILOS
                size="4",
                margin_top="10px",
                weight="bold",
            ),
            link_personal(
                text="Instagram",
                url="https://www.instagram.com/d.osorio01/profilecard/?igsh=MWo3MWNrZTh0bGxlag==", 
                color="#E1306C",
                margin_left="100px",
                icon_text="instagram",
            ),
            link_personal(
                text="GitHub", 
                url="https://github.com/davidosorio01/", 
                color="#181717",
                margin_left="0px",
                icon_text="github",    
            ),
        ), 
        #linea separadora
        rx.divider(
            size="4",
        ),
        rx.text(
            "¡Hola! Soy David Osorio Avendaño.",
            #ESTILOS
            size="5",
            weight="regular",
            margin_left="95px"
        ),
        rx.text(
            """
            Creé esta página con Python, utilizando Reflex como framework. A través de estos botones, tendrás acceso a las aplicaciones interactivas que aprendí a desarrollar con Reflex. ¡Espero que las disfrutes!
            """,
        ),
        rx.icon(
            "arrow-down",
            #ESTILOS
            size=50,
            margin_left="47%"
        )
    )