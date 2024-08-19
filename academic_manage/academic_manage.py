import reflex as rx
from .components.stats_cards import stats_cards_group
from .views.navbar import navbar, navbar_docente
from .views.table import main_table, docente_table
from .views.login import login_page
from .views.register import register_page
from .views.dashboard_student import cursos_page
from .views.asignacion_tareas import asignar_tarea_page
from .views.dashboard_docente import cursos_page



def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )

#==========================================PAGINA DEL DOCENTE===================

def docente() -> rx.Component:
    return rx.vstack(
        navbar_docente(),
        rx.box(
            docente_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
)

app.add_page(
    login_page
)



