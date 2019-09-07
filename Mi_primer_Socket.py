import socket

print("  _____             _          _____                      _ _         ")
print(" |  __ \           | |        / ____|                    (_) |        ")
print(" | |  | | __ _ _ __| |_ _____| (___   ___  ___ _   _ _ __ _| |_ _   _ ")
print(" | |  | |/ _` | '__| __|______\___ \ / _ \/ __| | | | '__| | __| | | |")
print(" | |__| | (_| | |  | |_       ____) |  __/ (__| |_| | |  | | |_| |_| |")
print(" |_____/ \__,_|_|   \__|     |_____/ \___|\___|\__,_|_|  |_|\__|\__, |")
print("                                                                 __/ |")
print("                www.hc-security.com.mx       by:Equinockx       |___/ ")
print("                                                                      ")

print("Ingresa la Url:")
url = input()

try:
   print("---" * 20)
   print(f"La URL ingresada es: {url}")
   print("Nombre del Dominio completo: \n" + socket.getfqdn(url))
   print("Nombre de Host a direccion IP: \n" + socket.gethostbyname(url))
   print("Nombre de host para extender la dirección IP: \n" + str(socket.gethostbyname_ex(url)))
   print("Host de solicitud: \n" + socket.gethostname())
   print("---" * 20)
except Exception as err:
   print("Error" + str(err))
