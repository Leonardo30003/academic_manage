import reflex as rx
from datetime import datetime
from ..backend.backend_register import State

class FormState(rx.State):
    name: str = ""
    last_name: str = ""
    cedula: str = ""
    email: str = ""
    password: str = ""
    rol: str = "Estudiante"
    active: bool = True

    def handle_change(self, key: str, value: str):
        setattr(self, key, value)

    def handle_checkbox(self, value: bool):
        self.active = value

    def handle_register(self):
        # Create a dictionary with the user data
        user_data = {
            "name": self.name,
            "last_name": self.last_name,
            "cedula": self.cedula,
            "email": self.email,
            "password": self.password,
            "rol": self.rol,
            "active": self.active,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # Call the method to add the user to the database
        result = State.add_user_to_db(user_data)
        if result:
            print("Usuario creado exitosamente")
            rx.window_alert("Usuario registrado exitosamente.")
            return rx.redirect("/login")  # Redirect after successful registration
        else:
            self.handle_existing_user()

    def handle_existing_user(self):
        """Handle the case where the user already exists and redirect to the login page."""
        print("El usuario ya existe. Redirigiendo a la página de login.")
        rx.window_alert("El usuario ya existe. Serás redirigido a la página de inicio de sesión.")
        return rx.redirect("/login")

# Define the signup form component
def signup_form() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="",
                        width="15em",  # Aumentado para mejor visibilidad
                        height="auto",
                        border_radius="50px",
                        border="5px solid #555"
                    ),
                    rx.heading(
                        "Registro de Usuario",
                        size="3em",  # Aumentado para mejor visibilidad
                        color="#FF011D",  # Red color for the title
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%"
                ),
                rx.vstack(
                    rx.text(
                        "Nombre",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Nombre",
                        size="2em",  # Aumentado para mejor visibilidad
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#FFFFFF",  # White background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.5em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("name", value),
                    ),
                    rx.text(
                        "Apellido",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Apellido",
                        size="2em",  # Aumentado para mejor visibilidad
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#FFFFFF",  # White background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.50em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("last_name", value),
                    ),
                    rx.text(
                        "Cédula",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Cédula",
                        size="2em",  # Aumentado para mejor visibilidad
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#FFFFFF",  # White background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.5em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("cedula", value),
                    ),
                    rx.text(
                        "Correo Electrónico",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="ejemplo@gmail.com",
                        type="email",
                        size="2em",  # Aumentado para mejor visibilidad
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#FFFFFF",  # White background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.5em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("email", value),
                    ),
                    rx.text(
                        "Contraseña",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        size="2em",  # Aumentado para mejor visibilidad
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#FFFFFF",  # White background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.5em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("password", value),
                    ),
                    rx.text(
                        "Rol",
                        size="2em",  # Aumentado para mejor visibilidad
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.select(
                        ["Docente", "Administrador"],
                        placeholder="Seleccione un rol",
                        color_scheme="blue",
                        size="3",
                        on_change=lambda value: FormState.handle_change("rol", value),
                    ),
                    rx.box(
                        rx.checkbox(
                            rx.text("Activo", color="black", size="1.5em"),  # Texto más grande para checkbox
                            default_checked=FormState.active,
                            on_change=lambda value: FormState.handle_checkbox(value),
                            color_scheme="indigo",  # Dark blue for checkbox
                        ),
                    ),
                    rx.button(
                        "Registrarse",
                        size="2em",  # Botón más grande
                        width="100%",
                        background="#001737",  # Dark blue for the button
                        color="white",
                        border_radius="0.75em",
                        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                        on_click=FormState.handle_existing_user,
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("¿Ya tienes una cuenta?", color="#000000", size="1.5em"),  # Texto más grande
                    rx.link(
                        "Iniciar sesión",
                        href="/login",
                        color="#FF011D",  # Vibrant red for the link
                        text_decoration="underline",
                        hover_color="#001737",  # Dark blue on hover
                        size="1.5em",  # Texto más grande para el enlace
                    ),
                    spacing="2",
                ),
                width="100%",
            ),
            size="18",  # Aumentado para ocupar más espacio
            max_width="70rem",  # Aumentado para ocupar más espacio
            width="100%",
            background_color="white",
            padding="3em",  # Aumentado para un padding mayor
            border_radius="1.5em",
            box_shadow="0 8px 10px rgba(0, 0, 0, 0.8)",
        ),
        height="100vh",
        background_color="#F0F0F0",
    )

@rx.page(route="/register", title="Registro")
def register_page() -> rx.Component:
    return signup_form()
