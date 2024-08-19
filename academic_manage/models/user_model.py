import reflex as rx

class User(rx.Model, table=True):
    "Modelo del Usuario"
    name: str
    last_name: str
    cedula: str
    email: str
    password: str
    rol: str
    active: bool
