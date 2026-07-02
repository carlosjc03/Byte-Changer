# 🧠 Byte-Changer

**Byte-Changer** is a lightweight Python GUI tool that helps you exchange, reverse, and calculate program position bytes — just like a cheat engine — and automatically generate valid **Action Replay codes** for Nintendo **NDS / 3DS** games.

> 🐍 Requires **Python 3.9 or higher** (no external dependencies — Tkinter is included by default).
> ⚡ Created by **Scontra**, admin of [Inazuma Life](https://inazumalife.com), to speed up the workflow of finding offsets and creating custom game cheats.

---

## 🚀 Features

✅ Reverse Cheat Engine byte order automatically  
✅ Generate **Action Replay cheats** instantly from raw bytes  
✅ Works as a **Python-based cheat converter** for NDS & 3DS games  
✅ Built-in byte validation (must be multiple of 8)  
✅ Customizable base address and prefix (e.g. D3000000 XX000000)  
✅ Simple and responsive GUI  

---

## 🧩 How It Works

In **Cheat Engine**, byte order is reversed compared to how it should appear in a real Action Replay cheat (that's called **Little Endian Notation**).

For example, if you see the values `CD CC 70 43` in Cheat Engine, you might think you should write: `CDCC7043`  

…but that’s incorrect!  
The actual data that will be written in memory is **`4370CCCD`**, since Cheat Engine displays the bytes in **reverse order** compared to how they appear in the real memory layout.

![Example 1](https://github.com/user-attachments/assets/4a9b1823-380a-4991-94ec-4ea4f9d2e761)
![Example 2](https://github.com/user-attachments/assets/f8c3b2ed-b3ee-40b7-960f-9d4e2bad69a3)

**Byte-Changer** fixes this automatically — simply:
1. Paste the bytes you want to use.
2. Enter the base memory address.
3. Click “Process Bytes”.  

The program will output a fully formatted **Action Replay cheat** with correctly ordered bytes.

---

## ⚙️ Address Rules & Validation

- ✳️ You must enter the **full 8-digit base address** (e.g., `084C0B30`).  
- 🧱 The tool automatically handles the upper bytes (`D3000000 XX000000`) used in **Citra/Desmume** or **NDS/3DS** cheats.  
- 🔢 The total number of bytes must be **divisible by 8**, as each Action Replay line represents 8 characters.  
- 💡 You can use this program as a **byte calculator** for other platforms by changing the line length settings.

---

## 🪟 GUI Preview

The GUI lets you:
- Input raw bytes directly  
- Define your base address  
- Copy generated cheats instantly

<br>

<p align="center">
  <img width="548" height="451" alt="Byte-Changer GUI" src="https://github.com/user-attachments/assets/8a78f992-5868-46e6-9113-c1b5e53c1106" />
  <br>
  <em>Byte-Changer GUI Interface Preview</em>
</p>

---

## 💻 Installation & Usage

1. Make sure you have **Python 3.9 or higher** installed.  
2. Clone this repository:
   ```bash
   git clone https://github.com/carlosjc03/Byte-Changer.git
   cd Byte-Changer
3. Run the GUI:
   ```bash
   python ByteChanger-GUI.py
