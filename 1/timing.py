import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registrar el tiempo antes de ejecutar la función
        result = func(*args, **kwargs)  # Ejecutar la función decorada
        end_time = time.time()  # Registrar el tiempo después de ejecutar la función
        elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido
        print(f"Tiempo de ejecución de {func.__name__}: {elapsed_time:.6f} segundos")
        return result, elapsed_time
    return wrapper