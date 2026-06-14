import tkinter as tk
from tkinter import ttk, messagebox

# colores
BG_COLOR     = '#0d1117'
PANEL_COLOR  = '#161b22'
ACCENT_COLOR = '#58a6ff'
TEXT_COLOR   = '#e6edf3'
ENTRY_BG     = '#21262d'
BUTTON_COLOR = '#1f6feb'
RESULT_COLOR = '#3fb950'
ERROR_COLOR  = '#f85149'
ERROR_COLOR  = '#e74c3c'

# ---- Helpers ----

def make_entry(parent):
    e = tk.Entry(parent, bg=ENTRY_BG, fg=TEXT_COLOR,
                 insertbackground=TEXT_COLOR, font=("Helvetica", 11),
                 relief='flat')
    e.pack(fill='x', pady=4)
    return e

def make_label(parent, text):
    tk.Label(parent, text=text, bg=PANEL_COLOR,
             fg=TEXT_COLOR, font=("Helvetica", 10)).pack(anchor='w', pady=(8,0))

def make_result_label(parent):
    lbl = tk.Label(parent, text="", bg=PANEL_COLOR,
                   fg=RESULT_COLOR, font=("Helvetica", 12, "bold"),
                   wraplength=440, justify='left')
    lbl.pack(anchor='w', pady=(6,0))
    return lbl

def make_buttons(parent, calc_cmd, clear_cmd, calc_text="Calcular"):
    f = tk.Frame(parent, bg=PANEL_COLOR)
    f.pack(fill='x', pady=8)
    tk.Button(f, text=calc_text, bg=BUTTON_COLOR, fg='white',
          command=calc_cmd, relief='flat', cursor='hand2',
          padx=18, pady=7, font=("Helvetica", 10, "bold")).pack(side='left')
    tk.Button(f, text="Limpiar", bg=ENTRY_BG, fg='#8b949e',
          command=clear_cmd, relief='flat', cursor='hand2',
          padx=18, pady=7, font=("Helvetica", 10)).pack(side='left', padx=8)

def section_title(parent, text):
    tk.Label(parent, text=text, font=("Helvetica", 13, "bold"),
             bg=PANEL_COLOR, fg=ACCENT_COLOR).pack(anchor='w', pady=(0,4))

def panel(notebook, tab_name):
    frame = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame, text=tab_name)
    inner = tk.Frame(frame, bg=PANEL_COLOR, padx=20, pady=15)
    inner.pack(fill='both', expand=True, padx=20, pady=15)
    return inner

def get_float(entry):
    return float(entry.get().strip().replace(',', '.'))

# ================================================================
# Ventana principal
# ================================================================
window = tk.Tk()
window.title("Calculadora de Soluciones Químicas")
window.configure(bg=BG_COLOR)
window.geometry("580x580")
window.resizable(False, False)

tk.Label(window, text=" ◉ Calculadora de Soluciones ◉ ",
         font=("Helvetica", 20, "bold"),
         bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(22,2))
tk.Label(window, text="Química · Code in Place 2026",
         font=("Helvetica", 9),
         bg=BG_COLOR, fg='#8b949e').pack(pady=(0,10))

# ---- Notebook (pestañas) ----
style = ttk.Style()
style.theme_use('clam')
style.configure('TNotebook', background=BG_COLOR, borderwidth=0)
style.configure('TNotebook.Tab', background=ENTRY_BG, foreground=TEXT_COLOR,
                padding=[14, 6], font=("Helvetica", 10))
style.map('TNotebook.Tab', background=[('selected', ACCENT_COLOR)],
          foreground=[('selected', 'white')])

nb = ttk.Notebook(window)
nb.pack(fill='both', expand=True, padx=18, pady=6)

# ================================================================
# PESTAÑA 1 — Molaridad
# ================================================================
p1 = panel(nb, "Molaridad")
section_title(p1, "Molaridad   M = n / V")
tk.Label(p1, text="Moles de soluto (mol):", bg=PANEL_COLOR, fg=TEXT_COLOR).pack(anchor='w', pady=(10,0))
e_mol_M  = make_entry(p1)
make_label(p1, "Volumen de solución (L):")
e_vol_M  = make_entry(p1)
lbl_M    = make_result_label(p1)

def calc_M():
    try:
        result = get_float(e_mol_M) / get_float(e_vol_M)
        lbl_M.config(text=f"Molaridad: {result:.4f} mol/L", fg=RESULT_COLOR)
    except: lbl_M.config(text="Verificá los valores ingresados.", fg=ERROR_COLOR)

def clear_M():
    e_mol_M.delete(0, tk.END); e_vol_M.delete(0, tk.END); lbl_M.config(text="")

make_buttons(p1, calc_M, clear_M)

# ================================================================
# PESTAÑA 2 — Molalidad
# ================================================================
p2 = panel(nb, "Molalidad")
section_title(p2, "Molalidad   m = n / kg solvente")
make_label(p2, "Moles de soluto (mol):")
e_mol_m  = make_entry(p2)
make_label(p2, "Masa del solvente (kg):")
e_kg_m   = make_entry(p2)
lbl_m    = make_result_label(p2)

def calc_m():
    try:
        result = get_float(e_mol_m) / get_float(e_kg_m)
        lbl_m.config(text=f"Molalidad: {result:.4f} mol/kg", fg=RESULT_COLOR)
    except: lbl_m.config(text="Verificá los valores ingresados.", fg=ERROR_COLOR)

def clear_m():
    e_mol_m.delete(0, tk.END); e_kg_m.delete(0, tk.END); lbl_m.config(text="")

make_buttons(p2, calc_m, clear_m)

# ================================================================
# PESTAÑA 3 — Fracción molar
# ================================================================
p3 = panel(nb, "Fracción molar")
section_title(p3, "Fracción molar   X = n_soluto / n_total")
make_label(p3, "Moles de soluto (mol):")
e_n_sol  = make_entry(p3)
make_label(p3, "Moles de solvente (mol):")
e_n_solv = make_entry(p3)
lbl_X    = make_result_label(p3)

def calc_X():
    try:
        n1 = get_float(e_n_sol)
        n2 = get_float(e_n_solv)
        X  = n1 / (n1 + n2)
        lbl_X.config(text=f"Fracción molar del soluto: {X:.4f}", fg=RESULT_COLOR)
    except: lbl_X.config(text="Verificá los valores ingresados.", fg=ERROR_COLOR)

def clear_X():
    e_n_sol.delete(0, tk.END); e_n_solv.delete(0, tk.END); lbl_X.config(text="")

make_buttons(p3, calc_X, clear_X)

# ================================================================
# PESTAÑA 4 — Porcentajes
# ================================================================
p4 = panel(nb, "Porcentajes")
section_title(p4, "Concentraciones porcentuales")

# % m/m
tk.Label(p4, text="% masa/masa  →  (masa soluto / masa solución) × 100",
         bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "italic")).pack(anchor='w', pady=(8,0))
f_mm = tk.Frame(p4, bg=PANEL_COLOR); f_mm.pack(fill='x')
tk.Label(f_mm, text="Masa soluto (g):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=22, anchor='w').pack(side='left')
e_mm1 = tk.Entry(f_mm, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_mm1.pack(side='left', padx=4)
tk.Label(f_mm, text="Masa solución (g):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=20, anchor='w').pack(side='left')
e_mm2 = tk.Entry(f_mm, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_mm2.pack(side='left', padx=4)

# % m/v
tk.Label(p4, text="% masa/volumen  →  (masa soluto (g) / volumen solución (mL)) × 100",
         bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "italic")).pack(anchor='w', pady=(10,0))
f_mv = tk.Frame(p4, bg=PANEL_COLOR); f_mv.pack(fill='x')
tk.Label(f_mv, text="Masa soluto (g):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=22, anchor='w').pack(side='left')
e_mv1 = tk.Entry(f_mv, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_mv1.pack(side='left', padx=4)
tk.Label(f_mv, text="Volumen sol. (mL):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=20, anchor='w').pack(side='left')
e_mv2 = tk.Entry(f_mv, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_mv2.pack(side='left', padx=4)

# % v/v
tk.Label(p4, text="% volumen/volumen  →  (vol. soluto / vol. solución) × 100",
         bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "italic")).pack(anchor='w', pady=(10,0))
f_vv = tk.Frame(p4, bg=PANEL_COLOR); f_vv.pack(fill='x')
tk.Label(f_vv, text="Vol. soluto (mL):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=22, anchor='w').pack(side='left')
e_vv1 = tk.Entry(f_vv, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_vv1.pack(side='left', padx=4)
tk.Label(f_vv, text="Vol. solución (mL):", bg=PANEL_COLOR, fg=TEXT_COLOR, width=20, anchor='w').pack(side='left')
e_vv2 = tk.Entry(f_vv, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                  font=("Helvetica", 11), relief='flat', width=10); e_vv2.pack(side='left', padx=4)

lbl_pct = make_result_label(p4)

def calc_pct():
    results = []
    try:
        results.append(f"% m/m = {get_float(e_mm1) / get_float(e_mm2) * 100:.4f} %")
    except: results.append("% m/m: datos incompletos")
    try:
        results.append(f"% m/v = {get_float(e_mv1) / get_float(e_mv2) * 100:.4f} %")
    except: results.append("% m/v: datos incompletos")
    try:
        results.append(f"% v/v = {get_float(e_vv1) / get_float(e_vv2) * 100:.4f} %")
    except: results.append("% v/v: datos incompletos")
    lbl_pct.config(text="  |  ".join(results), fg=RESULT_COLOR)

def clear_pct():
    for e in [e_mm1, e_mm2, e_mv1, e_mv2, e_vv1, e_vv2]:
        e.delete(0, tk.END)
    lbl_pct.config(text="")

make_buttons(p4, calc_pct, clear_pct, "Calcular los tres")

# ================================================================
# PESTAÑA 5 — PPM
# ================================================================
p5 = panel(nb, "PPM")
section_title(p5, "Partes por millón   ppm = mg soluto / L solución")
make_label(p5, "Masa del soluto (mg):")
e_mg_ppm = make_entry(p5)
make_label(p5, "Volumen de solución (L):")
e_L_ppm  = make_entry(p5)
lbl_ppm  = make_result_label(p5)

def calc_ppm():
    try:
        result = get_float(e_mg_ppm) / get_float(e_L_ppm)
        lbl_ppm.config(text=f"Concentración: {result:.4f} ppm  (mg/L)", fg=RESULT_COLOR)
    except: lbl_ppm.config(text="Verificá los valores ingresados.", fg=ERROR_COLOR)

def clear_ppm():
    e_mg_ppm.delete(0, tk.END); e_L_ppm.delete(0, tk.END); lbl_ppm.config(text="")

make_buttons(p5, calc_ppm, clear_ppm)

# ================================================================
# PESTAÑA 6 — Diluciones
# ================================================================
p6 = panel(nb, "Diluciones")
section_title(p6, "Dilución   C₁V₁ = C₂V₂")

tk.Label(p6, text="Ingresá tres valores y dejá vacío el que querés calcular:",
         bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "italic")).pack(anchor='w', pady=(0,6))

campos_dil = [
    ("C1 — Concentración inicial (mol/L):", 'c1'),
    ("V1 — Volumen inicial (L):",            'v1'),
    ("C2 — Concentración final (mol/L):",    'c2'),
    ("V2 — Volumen final (L):",              'v2'),
]
dil_entries = {}
for lbl_txt, key in campos_dil:
    make_label(p6, lbl_txt)
    dil_entries[key] = make_entry(p6)

lbl_dil = make_result_label(p6)

def calc_dil():
    vals = {}
    empty = []
    for key, entry in dil_entries.items():
        txt = entry.get().strip().replace(',', '.')
        if txt == '':
            empty.append(key)
        else:
            try: vals[key] = float(txt)
            except:
                lbl_dil.config(text=f"Valor inválido en {key}.", fg=ERROR_COLOR)
                return
    if len(empty) != 1:
        lbl_dil.config(text="Dejá exactamente UN campo vacío para calcular.", fg=ERROR_COLOR)
        return
    target = empty[0]
    try:
        if target == 'v2': result = vals['c1'] * vals['v1'] / vals['c2']
        elif target == 'c2': result = vals['c1'] * vals['v1'] / vals['v2']
        elif target == 'v1': result = vals['c2'] * vals['v2'] / vals['c1']
        elif target == 'c1': result = vals['c2'] * vals['v2'] / vals['v1']
        label_names = {'c1':'C1','v1':'V1','c2':'C2','v2':'V2'}
        units = {'c1':'mol/L','v1':'L','c2':'mol/L','v2':'L'}
        lbl_dil.config(
            text=f"{label_names[target]} = {result:.4f} {units[target]}",
            fg=RESULT_COLOR)
    except: lbl_dil.config(text="No se pudo calcular. Revisá los valores.", fg=ERROR_COLOR)

def clear_dil():
    for e in dil_entries.values(): e.delete(0, tk.END)
    lbl_dil.config(text="")

make_buttons(p6, calc_dil, clear_dil)

# ---- Pie ----
tk.Label(window,
         text="Code in Place 2026 · Stanford University",
         font=("Helvetica", 8), bg=BG_COLOR, fg='#7f8c8d').pack(pady=8)
window.lift()
window.focus_force()
tk.Frame(window, bg='#21262d', height=1).pack(fill='x', padx=20)
tk.Label(window, text="Stanford University · Code in Place 2026",
         font=("Helvetica", 8), bg=BG_COLOR, fg='#484f58').pack(pady=10)
window.mainloop()