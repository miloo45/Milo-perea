import tkinter as tk
from tkinter import messagebox

def nuevo_cliente():
    global ventas # Le avisamos a Python que vamos a vaciar la lista principal
    ventas = []
    etiqueta_total_vivo.config(text="Total acumulado: $0")
    entrada_pago.delete(0, tk.END)
    messagebox.showinfo("Limpieza", "¡Listo para el siguiente cliente!")

def procesar_venta():
    producto = entrada_producto.get()
    try:
        precio = float(entrada_precio.get())
        ventas.append((producto, precio))
        
        # Actualizamos el total en la pantalla en tiempo real
        total_acumulado = sum(v[1] for v in ventas)
        etiqueta_total_vivo.config(text=f"Total acumulado: ${total_acumulado}")
        
        # Limpiamos para el siguiente
        entrada_producto.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_producto.focus()
    except ValueError:
        messagebox.showerror("Error", "Escribe un precio válido")

def ver_vueltas():
    try:
        total_actual = sum(v[1] for v in ventas)
        pago = float(entrada_pago.get())
        cambio = pago - total_actual
        if cambio < 0:
            messagebox.showwarning("Atención", f"Faltan ${abs(cambio)}")
        else:
            messagebox.showinfo("Cambio", f"Dar de vuelta: ${cambio}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa el pago del cliente")

# --- INTERFAZ ---
ventana = tk.Tk()
ventana.title("Super Inter POS v2.0")
ventana.geometry("800x400")

# Sección Registro
tk.Label(ventana, text="PRODUCTO:").pack(pady=15)
entrada_producto = tk.Entry(ventana)
entrada_producto.pack()

tk.Label(ventana, text="PRECIO:").pack(pady=20)
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

tk.Button(ventana, text="Registrar", bg="red", fg="white", command=procesar_venta).pack(pady=10)

# El total que cambia en vivo
etiqueta_total_vivo = tk.Label(ventana, text="Total acumulado: $0", font=("Sans", 14, "bold"))
etiqueta_total_vivo.pack(pady=20)

# Sección Vueltas
tk.Label(ventana, text="PAGÓ CON:").pack(pady=5)
entrada_pago = tk.Entry(ventana)
entrada_pago.pack()

tk.Button(ventana, text="Calcular Cambio", command=ver_vueltas).pack(pady=10)

ventana.mainloop()

print("___INICIO DE TURNO___")
while True:
    producto = input("producto: ")
    
    if producto.lower() == 'fin':
        break
    
    try:
        precio = float(input(f"precio de '{producto}': "))
        ventas.append((producto, precio))
        total +=precio
        
    except ValueError:
            print("alto ahi, escribe de nuevo un numero valido")
            
print("producto" + "="*25)
print("ticket de venta")
print("="*25)
for item, valor in ventas:
    print(f"{item.capitalize()}: ${valor}")
print("-" * 25)
print(f"total: ${total}")
print("="*25)


with open("historial de ventas.txt", "a") as archivo:
    archivo.write(f"SESION CERRADA. total: ${total} producto")
    
print("archivo actualizado!")


pago = float(input("\n¿Con cuánto pagó el cliente?: "))
cambio = pago - total

if cambio < 0:
    print(f"Falta dinero! El cliente debe: ${abs(cambio)}")
else:
    print(f"El cambio para el cliente es: ${cambio}")