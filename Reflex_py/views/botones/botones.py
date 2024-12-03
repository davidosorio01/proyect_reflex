import reflex as rx

def botones_principales(number, on_click):
    return rx.hstack(
        rx.button(
            number,
            on_click=on_click,
            font_size = "2em",
            size="4",
            margin_left="15px"
        ),
    )
    
def botones_secundarios(number, on_click):
    return rx.hstack(
        rx.button(
            number,
            on_click=on_click,
            size="4",
            font_size = "2em",
            margin_left="13px"
        ),
    )

def botones_inferiores(number, on_click):
    return rx.hstack(
        rx.button(
            number,
            on_click=on_click,
            size="4",
            font_size = "2em",
            margin_left="13px"
        ),
    )
    
def botones_icon(number, on_click):
    return rx.hstack(
        rx.button(
            rx.icon(
                number,
            ),
            on_click=on_click,
            size="4",
            margin_left="7px",
            color_scheme="gray"
        ),
    )