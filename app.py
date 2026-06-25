"""
app.py — Aplicación de lista de tareas (TODO) en línea de comandos.
"""

# ---------------------------------------------------------------------------
# Parte 1 — feature/add-tasks
# ---------------------------------------------------------------------------

tareas = []


def agregar_tarea(texto):
    """Añade una nueva tarea a la lista en memoria."""
    tareas.append(texto)
    print(f"✅ Tarea añadida: '{texto}'")


# ---------------------------------------------------------------------------
# Bucle principal — gestión de comandos
# ---------------------------------------------------------------------------

def main():
    print("=== TODO App ===")
    print("Comandos disponibles: add <texto> | quit")
    print()

    while True:
        try:
            entrada = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHasta luego 👋")
            break

        if not entrada:
            continue

        partes = entrada.split(maxsplit=1)
        comando = partes[0].lower()

        # --- Parte 1: add y quit ---
        if comando == "add":
            if len(partes) < 2 or not partes[1].strip():
                print("⚠️  Uso correcto: add <texto de la tarea>")
            else:
                agregar_tarea(partes[1].strip())

        elif comando == "quit":
            print("Hasta luego 👋")
            break

        else:
            print("⚠️  Comando no reconocido.")


if __name__ == "__main__":
    main()
