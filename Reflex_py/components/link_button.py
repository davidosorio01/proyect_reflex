import reflex as rx

def link_button(text, url, icon_text) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon_text,
                ),
            ),
            text,
            #ESTILOS
            size="4",
            width="100%",
            _hover={
                "opacity": 0.5,
            }
        ),
        href=url,
        width="100%",
    )
    
    
def link_personal(text, url, color, margin_left, icon_text) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(
              icon_text,  
            ),
            text,
            #ESTILOS
            margin_top="5px",
            background_color=color,
            margin_left=margin_left,
            _hover={
                "opacity": 0.5,
            },
        ),
        href=url,
        is_external=True,
        #ESTILOS
    )