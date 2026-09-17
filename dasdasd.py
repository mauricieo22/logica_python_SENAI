import tkinter as tk
from tkinter import ttk

#cores
COLOR_HEX = {
    'Preto': '#000000',
    'Marrom': '#8B4513',
    'Vermelho': '#e80a0a',
    'Laranja': '#f79204',
    'Amarelo': '#FEFE09',
    'Verde': '#08d415',
    'Azul': '#006de1',
    'Violeta': '#ab04ed',
    'Cinza': '#676767',
    'Branco': '#ffffff',
    'Ouro': '#d4af37',
    'Prata': '#c0c0c0',
}

DIGIT_MAP = {
    'Preto': 0, 'Marrom': 1, 'Vermelho': 2, 'Laranja': 3, 'Amarelo': 4,
    'Verde': 5, 'Azul': 6, 'Violeta': 7, 'Cinza': 8, 'Branco': 9
}

MULT_MAP = {
    'Prata': 0.01, 'Ouro': 0.1, 'Preto': 1, 'Marrom': 10, 'Vermelho': 100,
    'Laranja': 1_000, 'Amarelo': 10_000, 'Verde': 100_000, 'Azul': 1_000_000, 'Violeta': 10_000_000
}

TOL_MAP = {
    'Prata': 10, 'Ouro': 5, 'Preto': 20, 'Marrom': 1, 'Vermelho': 2,
    'Verde': 0.5, 'Azul': 0.25, 'Violeta': 0.1, 'Cinza': 0.05
}

COLOR_NAMES = ['Preto','Marrom','Vermelho','Laranja','Amarelo','Verde','Azul','Violeta','Cinza','Branco','Ouro','Prata']

#janela proncipal
root = tk.Tk()
root.title('Calculadora de Resistor')
root.geometry('820x520')
root.config(bg='white')

#titulo
titulo = tk.Label(root, text='Calculadora de Resistor', font=('Arial', 20, 'bold'), bg='white')
titulo.place(x=20, y=12)

info_ask = tk.Label(root, text='Como deseja informar o resistor?', font=('Arial', 10, 'bold'), bg='white')
info_ask.place(x=20, y=60)

# Canvas para desenho
canvas = tk.Canvas(root, width=760, height=260, bg='white', highlightthickness=1, highlightbackground='#d0d0d0')
canvas.place(x=30, y=220)

#resultado
label_result = tk.Label(root, text='', font=('Arial', 12, 'bold'), bg='white')
label_result.place(x=30, y=180)

#funções

def format_resistance(value):
    """Formata o valor de resistência em Ω/kΩ/MΩ"""
    if value >= 1_000_000:
        return f"{value/1_000_000:.2f} MΩ"
    if value >= 1_000:
        return f"{value/1_000:.2f} kΩ"
    if value >= 1:
        return f"{value:.2f} Ω"
    # abaixo de 1 ohm
    return f"{value:.2f} Ω"


def draw_resistor_on_canvas(cnv, band_colors, tol_color, title='Resistor de 4 faixas'):
    cnv.delete('all')
    w = 760
    h = 260
    mid_y = h // 2
    x0 = 80
    x1 = w - 80

    # título
    cnv.create_text(w//2, 20, text=title, font=('Arial', 14, 'bold'))

    # linhas de ligação
    cnv.create_line(10, mid_y, x0, mid_y, width=8, fill='#707070')
    cnv.create_line(x1, mid_y, w-10, mid_y, width=8, fill='#707070')

    # corpo
    body_top = mid_y - 40
    body_bottom = mid_y + 40
    cnv.create_rectangle(x0, body_top, x1, body_bottom, fill='#f4e6c2', outline='#b58f4a', width=2)

    # bandas
    band_w = 18
    gap = 18
    center = (x0 + x1) / 2
    positions = [center - band_w - gap, center, center + band_w + gap]
    for pos, color in zip(positions, band_colors):
        hexc = COLOR_HEX.get(color, '#000000')
        cnv.create_rectangle(pos-band_w/2, body_top, pos+band_w/2, body_bottom, fill=hexc, outline='')

    # tolerância (mais à direita)
    tol_x = x1 - band_w - 14
    cnv.create_rectangle(tol_x-band_w/2, mid_y-30, tol_x+band_w/2, mid_y+30, fill=COLOR_HEX.get(tol_color,'#d4af37'), outline='')

    # legendas embaixo das faixas
    legend_y = body_bottom + 18
    labels = [c for c in band_colors] + [tol_color]
    label_xs = [positions[0], positions[1], positions[2], tol_x]
    for lx, lab in zip(label_xs, labels):
        cnv.create_text(lx, legend_y, text=lab, font=('Arial', 10))


#modo por cores

faixa1_label = tk.Label(root, text='Banda 1:', bg='white')
faixa1_label.place(x=30, y=95)
cb_f1 = ttk.Combobox(root, values=COLOR_NAMES, state='readonly', width=14)
cb_f1.current(2)  # vermelho
cb_f1.place(x=30, y=115)

faixa2_label = tk.Label(root, text='Banda 2:', bg='white')
faixa2_label.place(x=200, y=95)
cb_f2 = ttk.Combobox(root, values=COLOR_NAMES, state='readonly', width=14)
cb_f2.current(2)
cb_f2.place(x=200, y=115)

mult_label = tk.Label(root, text='Multiplicador:', bg='white')
mult_label.place(x=370, y=95)
cb_mult = ttk.Combobox(root, values=['Prata','Ouro'] + list(DIGIT_MAP.keys()), state='readonly', width=14)
cb_mult.current(2)  # Preto
cb_mult.place(x=370, y=115)

tol_label = tk.Label(root, text='Tolerância:', bg='white')
tol_label.place(x=540, y=95)
cb_tol = ttk.Combobox(root, values=list(TOL_MAP.keys()), state='readonly', width=14)
cb_tol.current(7)  # Violeta
cb_tol.place(x=540, y=115)


def calculate_from_colors():
    c1 = cb_f1.get()
    c2 = cb_f2.get()
    cm = cb_mult.get()
    ct = cb_tol.get()
    if c1 not in DIGIT_MAP or c2 not in DIGIT_MAP or cm not in MULT_MAP or ct not in TOL_MAP:
        label_result.config(text='Selecione todas as cores corretamente')
        return

    digits = DIGIT_MAP[c1] * 10 + DIGIT_MAP[c2]
    multiplier = MULT_MAP[cm]
    value = digits * multiplier
    tol = TOL_MAP[ct]

    label_result.config(text=f'Resistência: {format_resistance(value)} ±{tol}%')
    draw_resistor_on_canvas(canvas, [c1,c2,cm if cm in COLOR_HEX else cm], ct)


# Botão calcular
btn_calc = tk.Button(root, text='Calcular resistência', command=calculate_from_colors, bg='#2e8b57', fg='white', font=('Arial', 11, 'bold'))
btn_calc.place(x=30, y=140)

# Modo por valor (simples): converter valor para faixas (apenas aproximação)

mode_var = tk.IntVar(value=2)  # default: cores

rb_valor = tk.Radiobutton(root, text='Valor da resistência', variable=mode_var, value=1, bg='white', command=lambda: switch_mode())
rb_valor.place(x=30, y=80)
rb_cores = tk.Radiobutton(root, text='Cores do resistor', variable=mode_var, value=2, bg='white', command=lambda: switch_mode())
rb_cores.place(x=200, y=80)

# widgets do modo valor
valor_entry = tk.Entry(root, width=14)
valor_entry.place(x=30, y=115)
valor_entry.insert(0,'1000')
valor_entry.place_forget()

cb_tol_val = ttk.Combobox(root, values=list(TOL_MAP.keys()), state='readonly', width=14)
cb_tol_val.current(1)
cb_tol_val.place(x=200, y=115)
cb_tol_val.place_forget()


def value_to_bands(value):
    """Converte valor em Ω para 3 bandas (2 dígitos + multiplicador) - aproximação"""
    # evitar zero
    if value <= 0:
        return None
    # normalize to get two first significant digits and multiplier
    exp = 0
    v = value
    while v >= 100:
        v /= 10
        exp += 1
    while v < 10:
        v *= 10
        exp -= 1
    # now v in [10,100)
    d = int(round(v))
    if d >= 100:
        d = 99
    d1 = d // 10
    d2 = d % 10
    # multiplier power is 10**exp
    mult_value = 10 ** exp
    # find closest multiplier name
    mult_name = 'Preto'
    mult_candidates = {k: v for k,v in MULT_MAP.items()}
    # choose the key with value closest to mult_value
    best = min(mult_candidates.items(), key=lambda kv: abs(kv[1]-mult_value))
    mult_name = best[0]
    # map digits to color
    inv_digit = {v:k for k,v in DIGIT_MAP.items()}
    return inv_digit.get(d1,'Preto'), inv_digit.get(d2,'Preto'), mult_name


def calculate_from_value():
    try:
        raw = float(valor_entry.get())
    except Exception:
        label_result.config(text='Valor inválido')
        return
    tol = cb_tol_val.get() if cb_tol_val.get() in TOL_MAP else 'Ouro'
    bands = value_to_bands(raw)
    if not bands:
        label_result.config(text='Não foi possível converter')
        return
    c1,c2,cm = bands
    label_result.config(text=f'Resistência: {format_resistance(raw)} ±{TOL_MAP.get(tol,5)}%')
    # atualizar comboboxes visuais também
    cb_f1.set(c1)
    cb_f2.set(c2)
    cb_mult.set(cm)
    cb_tol.set(tol)
    draw_resistor_on_canvas(canvas, [c1,c2,cm], tol)

btn_calc_val = tk.Button(root, text='Calcular cores', command=calculate_from_value, bg='#2e8b57', fg='white', font=('Arial', 11, 'bold'))
btn_calc_val.place(x=200, y=140)
btn_calc_val.place_forget()


def switch_mode():
    m = mode_var.get()
    if m == 1:
        # mostrar widgets de valor
        valor_entry.place(x=30, y=115)
        cb_tol_val.place(x=200, y=115)
        btn_calc_val.place(x=200, y=140)
        # esconder modo cores
        cb_f1.place_forget(); cb_f2.place_forget(); cb_mult.place_forget(); cb_tol.place_forget(); btn_calc.place_forget();
        faixa1_lbl.place_forget(); faixa2_lbl.place_forget(); mult_lbl.place_forget(); tol_lbl.place_forget()
    else:
        # mostrar widgets de cores
        valor_entry.place_forget(); cb_tol_val.place_forget(); btn_calc_val.place_forget()
        cb_f1.place(x=30, y=115); cb_f2.place(x=200, y=115); cb_mult.place(x=370, y=115); cb_tol.place(x=540, y=115);
        btn_calc.place(x=30, y=140)
        faixa1_lbl.place(x=30, y=95); faixa2_lbl.place(x=200, y=95); mult_lbl.place(x=370, y=95); tol_lbl.place(x=540, y=95)

# criar rótulos usados no switch_mode (referências)
faixa1_lbl = faixa1_label
faixa2_lbl = faixa2_label
mult_lbl = mult_label
tol_lbl = tol_label

# inicializar desenho padrão
draw_resistor_on_canvas(canvas, [cb_f1.get(), cb_f2.get(), cb_mult.get()], cb_tol.get())

# atalho: atualizar desenho quando muda combobox
cb_f1.bind('<<ComboboxSelected>>', lambda e: draw_resistor_on_canvas(canvas, [cb_f1.get(), cb_f2.get(), cb_mult.get()], cb_tol.get()))
cb_f2.bind('<<ComboboxSelected>>', lambda e: draw_resistor_on_canvas(canvas, [cb_f1.get(), cb_f2.get(), cb_mult.get()], cb_tol.get()))
cb_mult.bind('<<ComboboxSelected>>', lambda e: draw_resistor_on_canvas(canvas, [cb_f1.get(), cb_f2.get(), cb_mult.get()], cb_tol.get()))
cb_tol.bind('<<ComboboxSelected>>', lambda e: draw_resistor_on_canvas(canvas, [cb_f1.get(), cb_f2.get(), cb_mult.get()], cb_tol.get()))

switch_mode()

root.mainloop()
