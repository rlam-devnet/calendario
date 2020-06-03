#!/usr/bin/python

from yaml import safe_load
from netmiko import Netmiko
from jinja2 import Environment, FileSystemLoader
import pdb

# cargamos el inventario de los host que vamos a utilizar
with open("hosts.yml", "r") as handle:
    device = safe_load(handle)
# pdb.set_trace()


# necesitamos realizar un mapa de valores para SO por netmiko
maps_so = {"ios": "cisco_ios", "iosxr": "cisco_ioscr"}

for host in device["lista_host"]:
    plataform = maps_so[host["plataforma"]]

    # Abrimos nuestro archivo con las variables para cargar la configuracion
    with open(f"hosts_vars/{plataform}_conf.yml", "r") as handle:
        ntps = safe_load(handle)

    # Creamos el entorno para jinja2
    jinja_env = Environment(
        loader=FileSystemLoader("."), trim_blocks=True, autoescape=True
    )
    template = jinja_env.get_template(f"templates/{plataform}_ntp.j2")
    nueva_config = template.render(data=ntps)
    pdb.set_trace()

    # realizamos la conexión con Netmiko
    conexion = Netmiko(
        host=host["name"],
        username="richard",
        password="agamib15",
        device_type=plataform,
    )

    print(f"Ingresando en el equipo {conexion.find_prompt()}, corectamente")
    resultado = conexion.send_config_set(nueva_config.split("\n"))

    print(resultado)

    conexion.close()
