perfil = {"nombre": "milo", "idioma": "python", "skills": ["python", "github", "write"]}
print(f">>> PERFIL DE {perfil['nombre'].upper()} <<<")
nueva_skill = input("¿que aprendiste hoy?: ")
if len(nueva_skill.strip()) > 3:
    perfil["skills"].append(nueva_skill.strip())
    print(f"buena esa, {nueva_skill.strip()} agregada con exito")
else:
    print("esa no se reconocio compa, aprende algo nuevo por mas pequeño que sea")
print("listado actualizado")
for i, skills in enumerate(perfil["skills"], 1):
    print(f"{i}, {skills}")