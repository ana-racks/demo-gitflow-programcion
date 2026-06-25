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
# Parte 2 — feature/list-tasks
# ---------------------------------------------------------------------------

def listar_tareas():
    """Muestra todas las tareas numeradas. Avisa si no hay ninguna."""
    if not tareas:
        print("📭 No hay tareas pendientes.")
        return
    print("📋 Tareas pendientes:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"  {i}. {tarea}")


# ---------------------------------------------------------------------------
# Bucle principal — gestión de comandos
# ---------------------------------------------------------------------------

def main():
    print("=== TODO App ===")
    print("Comandos disponibles: add <texto> | list | quit")
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

        # --- Parte 2: list ---
        elif comando == "list":
            listar_tareas()

        else:
            print("⚠️  Comando no reconocido.")


if __name__ == "__main__":
    main()
