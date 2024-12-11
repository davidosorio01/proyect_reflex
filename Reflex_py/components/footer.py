import reflex as rx
import datetime
fecha_actual = datetime.datetime.now()  

# Extraer el año  
ano_actual = fecha_actual.year

def footer() -> rx.Component:
    return rx.hstack(
        rx.icon(
            "copyright"
        ),
        rx.text(
            f"{ano_actual} - Todos los derechos reservados",
        ), 
        #ESTILOS
        margin_left = "90px",     
    )