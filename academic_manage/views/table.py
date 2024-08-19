import reflex as rx
from ..backend.backend import State, Customer
from ..components.form_field import form_field
from ..components.status_badges import status_badge
from ..models.assignmsent_model import Assignmsent


def show_customer(user: Customer):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
        rx.table.cell(f"${user.payments:,}"),
        rx.table.cell(user.date),
        rx.table.cell(
            rx.match(
                user.status,
                ("Delivered", status_badge("Delivered")),
                ("Pending", status_badge("Pending")),
                ("Cancelled", status_badge("Cancelled")),
                status_badge("Pending"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_customer(getattr(user, "id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Customer", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Add New Customer",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Fill the form with the customer's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            "Name",
                            "Customer Name",
                            "text",
                            "name",
                            "user",
                        ),
                        # Email
                        form_field(
                            "Email", "user@reflex.dev", "email", "email", "mail"
                        ),
                        # Phone
                        form_field("Phone", "Customer Phone", "tel", "phone", "phone"),
                        # Address
                        form_field(
                            "Address", "Customer Address", "text", "address", "home"
                        ),
                        # Payments
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Customer"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_customer_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def update_customer_dialog(user):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_user(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Edit Customer",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edit the customer's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            "Name",
                            "Customer Name",
                            "text",
                            "name",
                            "user",
                            user.name,
                        ),
                        # Email
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "email",
                            "email",
                            "mail",
                            user.email,
                        ),
                        # Phone
                        form_field(
                            "Phone",
                            "Customer Phone",
                            "tel",
                            "phone",
                            "phone",
                            user.phone,
                        ),
                        # Address
                        form_field(
                            "Address",
                            "Customer Address",
                            "text",
                            "address",
                            "home",
                            user.address,
                        ),
                        # Payments
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            user.payments.to(str),
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                default_value=user.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update Customer"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.update_customer_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            add_customer_button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                ["name", "email", "phone", "address", "payments", "date", "status"],
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "user"),
                    _header_cell("Email", "mail"),
                    _header_cell("Phone", "phone"),
                    _header_cell("Address", "home"),
                    _header_cell("Payments", "dollar-sign"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Status", "truck"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.users, show_customer)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )

#==========================================TABLA DE LOS DOCENTES===========================
def show_assignment(assignment: Assignmsent):
    """Show an assignment in a table row."""

    return rx.table.row(
        rx.table.cell(assignment.academic_year),
        rx.table.cell(assignment.subject),
        rx.table.cell(assignment.parallel),
        rx.table.cell(assignment.trimester),
        rx.table.cell(assignment.work_type),
        rx.table.cell(assignment.assignment_type),
        rx.table.cell(
            rx.hstack(
                update_assignment_dialog(assignment),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_assignment(getattr(assignment, "id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def add_assignment_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Assignment", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="book", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Add New Assignment",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Fill the form with the assignment's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Año Académico
                        form_field(
                            "Año Académico",
                            "2024",
                            "text",
                            "academic_year",
                            "calendar",
                        ),
                        # Asignatura
                        form_field(
                            "Asignatura", "Matemáticas", "text", "subject", "book"
                        ),
                        # Paralelo
                        form_field("Paralelo", "A", "text", "parallel", "columns"),
                        # Trimestre
                        form_field(
                            "Trimestre", "Primero", "text", "trimester", "layers"
                        ),
                        # Tipo de Trabajo
                        form_field(
                            "Tipo de Trabajo",
                            "Individual",
                            "text",
                            "work_type",
                            "briefcase",
                        ),
                        # Tipo de Asignación
                        form_field(
                            "Tipo de Asignación",
                            "Lección",
                            "text",
                            "assignment_type",
                            "clipboard",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Assignment"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_assignment_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def update_assignment_dialog(assignment):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_assignment(assignment),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Edit Assignment",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edit the assignment's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Año Académico
                        form_field(
                            "Año Académico",
                            "2024",
                            "text",
                            "academic_year",
                            "calendar",
                            assignment.academic_year,
                        ),
                        # Asignatura
                        form_field(
                            "Asignatura",
                            "Matemáticas",
                            "text",
                            "subject",
                            "book",
                            assignment.subject,
                        ),
                        # Paralelo
                        form_field(
                            "Paralelo",
                            "A",
                            "text",
                            "parallel",
                            "columns",
                            assignment.parallel,
                        ),
                        # Trimestre
                        form_field(
                            "Trimestre",
                            "Primero",
                            "text",
                            "trimester",
                            "layers",
                            assignment.trimester,
                        ),
                        # Tipo de Trabajo
                        form_field(
                            "Tipo de Trabajo",
                            "Individual",
                            "text",
                            "work_type",
                            "briefcase",
                            assignment.work_type,
                        ),
                        # Tipo de Asignación
                        form_field(
                            "Tipo de Asignación",
                            "Lección",
                            "text",
                            "assignment_type",
                            "clipboard",
                            assignment.assignment_type,
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update Assignment"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.update_assignment_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def docente_table():
    return rx.fragment(
        rx.flex(
            add_assignment_button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                [
                    "academic_year", 
                    "subject", 
                    "parallel", 
                    "trimester", 
                    "work_type", 
                    "assignment_type"
                ],
                placeholder="Sort By: Academic Year",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Año Académico", "calendar"),
                    _header_cell("Asignatura", "book"),
                    _header_cell("Paralelo", "columns"),
                    _header_cell("Trimestre", "layers"),
                    _header_cell("Tipo de Trabajo", "briefcase"),
                    _header_cell("Tipo de Asignación", "clipboard"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.assignments, show_assignment)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )


