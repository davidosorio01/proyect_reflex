import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "NenePy",
            height="40px",
            font_size="1em",
            color = "blue",
        ),
        bg="gray",
        position="sticky",
        padding_x = "16px",
        padding_y = "8px",
        z_index="999",
    )