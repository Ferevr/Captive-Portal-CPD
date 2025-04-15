import subprocess
import logging

def authenticate_with_radius(username, password):
    try:
        print(f"Intentando autenticar con usuario: {username}, password: {password}")

        # Construye el comando para radclient
        command = f'echo "User-Name={username},User-Password={password}" | radclient -x 127.0.0.1 auth test1234'

        # Ejecuta el comando
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Imprime la salida para debug
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)

        # Verifica si la respuesta contiene "Access-Accept"
        if "Access-Accept" in result.stdout:
            print("Autenticación exitosa")
            return True
        else:
            print("Autenticación fallida")
            return False

    except Exception as e:
        logging.error(f"Error al autenticar con RADIUS: {e}")
        return False