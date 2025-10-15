import tkinter as tk
from tkinter import messagebox

def join_bytes(text):
    return text.replace(" ", "")

def check_text(text):
    return len(join_bytes(text)) % 8 == 0

def split_by_lines(text):
    text = join_bytes(text)
    return [text[i:i+8] for i in range(0, len(text), 8)]

def reverse_bytes(text):
    lines = split_by_lines(text)
    new_list = []
    
    for line in lines:
        reversed_bytes = line[::-1]
        text, text2, text3 = "", "", ""
        
        for i, byte in enumerate(reversed_bytes):
            if i % 2 == 0:
                text2 += byte
            else:
                text += byte
        
        for i in range(len(text)):
            text3 += text[i] + text2[i]
        
        new_list.append(text3.upper())
    
    return new_list

def hex_calculator(initial_address, total_addresses):
    list_addresses = []
    step = 0x4  # Incremento de 4 en cada dirección
    
    current_address = int(initial_address, 16)
    for _ in range(total_addresses):
        hex_str = hex(current_address)[2:].upper().zfill(8)  # Asegura 8 caracteres
        list_addresses.append(hex_str)
        current_address += step
    
    return list_addresses


def process_bytes():
    your_input = input_text.get("1.0", tk.END).strip()
    start_address = address_entry.get().strip()
    
    if not check_text(your_input):
        messagebox.showerror("Error", "Error, write a suitable number of bytes")
        return
    
    try:
        int(start_address, 16)  # Verifica si la dirección ingresada es válida
    except ValueError:
        messagebox.showerror("Error", "Invalid address format")
        return
    
    bytes_list = reverse_bytes(your_input)
    addresses = hex_calculator(start_address, len(bytes_list))
    
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", f"{'D3000000'} {start_address[:2] + '000000'}\n")  # Cabecera directa

    #output_text.insert("1.0", "D3000000 14000000\n")  # Cabecera
    for i in range(len(bytes_list)):
        output_text.insert(tk.END, f"00{addresses[i][2:]} {bytes_list[i]}\n")

    output_text.insert(tk.END, "D2000000 00000000\n")  # Fin

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    root.update()
    messagebox.showinfo("Copied", "Text copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Byte Changer & Hex Calculator")
root.geometry("600x500")

tk.Label(root, text="Input bytes:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

tk.Label(root, text="Enter starting memory address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Process Bytes", command=process_bytes).pack()

tk.Label(root, text="\nOutput:").pack()
output_text = tk.Text(root, height=10)
output_text.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()