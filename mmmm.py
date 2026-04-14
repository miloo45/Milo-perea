total = 0
while True:
        print(">>> TAQUILLA <<<")
        ticket =input("pago por el ticket: ")
        if ticket.lower() == "x":
            break
        try:    
            precio = float(ticket.replace(".", ""))
            total = total + precio
            print(f"total alv ${total}")
        
        except ValueError:
            print("que es eso!?")
print("="*45)
print(f">>> VENTA DE HOY OR WHATEVER <<<: ${total}")
print("="*45)