import tkinter as tk
from tkinter import ttk, messagebox

DIGITOS = {
    "preto": 0,
    "marrom": 1,
    "vermelho": 2,
    "laranja": 3,
    "amarelo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "cinza": 8,
    "branco": 9
}

CORES = {
    "preto": "#000000",
    "marrom": "#8B4513",
    "vermelho": "#F01818",
    "laranja": "#F28C00",
    "amarelo": "#F5D000",
    "verde": "#229447",
    "azul": "#1769C2",
    "violeta": "#8A2BE2",
    "cinza": "#808080",
    "branco": "#FFFFFF",
    "dourado": "#D4AF37",
    "prata": "#C0C0C0"
}

MULTIPLICADORES = {
    "prata": 0.01,
    "dourado": 0.1,
    "preto": 1,
    "marrom": 10,
    "vermelho": 100,
    "laranja": 1000,
    "amarelo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "cinza": 100000000,
    "branco": 1000000000
}

TOLERANCIAS = {
    "marrom": ("±1%", 1),
    "vermelho": ("±2%", 2),
    "verde": ("±0,5%", 0.5),
    "azul": ("±0,25%", 0.25),
    "violeta": ("±0,1%", 0.1),
    "cinza": ("±0,05%", 0.05),
    "dourado": ("±5%", 5),
    "prata": ("±10%", 10)
}


class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora de Resistor")
        self.janela.geometry("800x500")
        self.janela.configure(bg="#eef2f7")

        #modo inicial
        self.modo = tk.StringVar(value="valor")

        #variáveis do modo valor -> cores
        self.valor = tk.StringVar()
        self.tolerancia_valor = tk.StringVar(value="dourado")

        # variáveis do modo cores -> valor
        self.banda1 = tk.StringVar(value="vermelho")
        self.banda2 = tk.StringVar(value="vermelho")
        self.multiplicador = tk.StringVar(value="laranja")
        self.tolerancia_cores = tk.StringVar(value="violeta")

    
        self.criar_interface()

        self.atualizar_modo()


    

    def criar_interface(self):
        
        #título
        ttk.Label(
            self.janela,
            text="Calculadora de Resistor",
            style="Titulo.TLabel"
        ).pack(anchor="w", padx=18, pady=(18, 10))

        # painel principal
        self.painel = ttk.Frame(
            self.janela,
            style="Painel.TFrame",
            padding=15
        )
        self.painel.pack(fill="both", expand=True, padx=14, pady=(0, 15))

        #selecionar do modo
        ttk.Label(
            self.painel,
            text="Como deseja informar o resistor?",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(0, 8))

        frame_radio = ttk.Frame(self.painel, style="Painel.TFrame")
        frame_radio.pack(anchor="w")

        ttk.Radiobutton(
            frame_radio,
            text="Valor da resistência",
            variable=self.modo,
            value="valor",
            command=self.atualizar_modo
        ).pack(side="left", padx=(0, 16))

        ttk.Radiobutton(
            frame_radio,
            text="Cores do resistor",
            variable=self.modo,
            value="cores",
            command=self.atualizar_modo
        ).pack(side="left")

        # área que muda de dependendo do modo escolhid
        self.area_controles = ttk.Frame(
            self.painel,
            style="Painel.TFrame"
        )
        self.area_controles.pack(fill="x", pady=(13, 8))

        #resultado calcular
        self.resultado = ttk.Label(
            self.painel,
            text="Digite o valor da resistência ou selecione as cores.",
            style="Resultado.TLabel"
        )
        self.resultado.pack(anchor="w", pady=(4, 10))

        #canvas
        self.canvas = tk.Canvas(
            self.painel,
            width=575,
            height=205,
            bg="#fbfcfe",
            highlightbackground="#d7dce2",
            highlightthickness=1
        )
        self.canvas.pack(fill="x")

        self.canvas.bind(
            "<Configure>",
            lambda event: self.desenhar_resistor()
        )

    #controles
    def limpar_controles(self):
        for widget in self.area_controles.winfo_children():
            widget.destroy()

    def criar_controles_valor(self):
        self.limpar_controles()

        linha = ttk.Frame(
            self.area_controles,
            style="Painel.TFrame"
        )
        linha.pack(anchor="w")

        ttk.Label(
            linha,
            text="Valor da resistência (Ω):"
        ).grid(row=0, column=0, sticky="w", padx=(0, 22))

        ttk.Label(
            linha,
            text="Tolerância:"
        ).grid(row=0, column=1, sticky="w")

        entrada = ttk.Entry(
            linha,
            textvariable=self.valor,
            width=18
        )
        entrada.grid(row=1, column=0, padx=(0, 22), pady=(5, 0))
        entrada.focus_set()

        combo = ttk.Combobox(
            linha,
            textvariable=self.tolerancia_valor,
            values=list(TOLERANCIAS.keys()),
            state="readonly",
            width=14
        )
        combo.grid(row=1, column=1, pady=(5, 0))

        ttk.Button(
            self.area_controles,text="Calcular cores",command=self.calcular_valor
).pack(anchor="w", pady=(10, 0))

    def criar_controles_cores(self):
        self.limpar_controles()

        linha = ttk.Frame(
            self.area_controles,
            style="Painel.TFrame"
        )
        linha.pack(fill="x")

        dados = [
            ("Banda 1:", self.banda1, list(DIGITOS.keys())),
            ("Banda 2:", self.banda2, list(DIGITOS.keys())),
            ("Multiplicador:", self.multiplicador,
             list(MULTIPLICADORES.keys())),
            ("Tolerância:", self.tolerancia_cores,
             list(TOLERANCIAS.keys()))
        ]

        for coluna, (texto, variavel, valores) in enumerate(dados):
            ttk.Label(
                linha,
                text=texto
            ).grid(
                row=0,
                column=coluna,
                sticky="w",
                padx=(0 if coluna == 0 else 10, 6)
            )

            combo = ttk.Combobox(
                linha,
                textvariable=variavel,
                values=valores,
                state="readonly",
                width=13
            )
            combo.grid(
                row=1,
                column=coluna,
                sticky="w",
                padx=(0 if coluna == 0 else 10, 6),
                pady=(5, 0)
            )

        ttk.Button(
            self.area_controles,
            text="Calcular resistência",
            command=self.calcular_cores
        ).pack(anchor="w", pady=(10, 0))

#atualizar modo

    def atualizar_modo(self):
        if self.modo.get() == "valor":
            self.criar_controles_valor()
            self.resultado.config(
                text="Digite o valor da resistência ou selecione as cores."
            )
        else:
            self.criar_controles_cores()
            self.resultado.config(
                text="Selecione as quatro faixas do resistor."
            )

        self.desenhar_resistor()


    # modo valor
    def calcular_valor(self):
        texto = self.valor.get().strip().replace(",", ".")

        try:
            valor = float(texto)
        except ValueError:
            messagebox.showwarning(
                "Valor inválido",
                "Digite um valor numérico, por exemplo: 3300"
            )
            return

        if valor <= 0:
            messagebox.showwarning(
                "Valor inválido",
                "O valor da resistência deve ser maior que zero."
            )
            return

        resultado = self.encontrar_faixas(valor)

        if resultado is None:
            messagebox.showwarning(
                "Valor não representável",
                "Esse valor não pode ser representado exatamente "
                "com um resistor de 4 faixas."
            )
            return

        d1, d2, multiplicador = resultado

        self.banda1.set(d1)
        self.banda2.set(d2)
        self.multiplicador.set(multiplicador)

        tolerancia = self.tolerancia_valor.get()
        texto_tol = TOLERANCIAS[tolerancia][0]

        self.resultado.config(
            text=f"Resistência: {self.formatar(valor)} {texto_tol}"
        )

        self.desenhar_resistor()

    def encontrar_faixas(self, valor):
        for nome, fator in MULTIPLICADORES.items():
            base = valor / fator

            if 10 <= base <= 99:
                inteiro = round(base)

                if abs(base - inteiro) < 0.000001:
                    primeiro = inteiro // 10
                    segundo = inteiro % 10

                    if (
                        primeiro in range(10)
                        and segundo in range(10)
                    ):
                        nome1 = list(DIGITOS.keys())[primeiro]
                        nome2 = list(DIGITOS.keys())[segundo]
                        return nome1, nome2, nome

        return None


    # modo cores
    def calcular_cores(self):
        d1 = DIGITOS[self.banda1.get()]
        d2 = DIGITOS[self.banda2.get()]
        fator = MULTIPLICADORES[self.multiplicador.get()]

        valor = (d1 * 10 + d2) * fator
        tolerancia = TOLERANCIAS[self.tolerancia_cores.get()][0]

        self.resultado.config(
            text=f"Resistência: {self.formatar(valor)} {tolerancia}"
        )

        self.desenhar_resistor()


    # formatação
    def formatar(self, valor):
        if valor >= 1_000_000:
            return f"{valor / 1_000_000:.2f} MΩ"
        elif valor >= 1_000:
            return f"{valor / 1_000:.2f} kΩ"
        else:
            return f"{valor:.2f} Ω"

    #DESENHO
    def desenhar_resistor(self):
        if not hasattr(self, "canvas"):
            return

        self.canvas.delete("all")

        largura = max(self.canvas.winfo_width(), 500)
        altura = max(self.canvas.winfo_height(), 180)

        centro_y = altura // 2

        esquerda = 35
        direita = largura - 35

        corpo_esq = esquerda + 55
        corpo_dir = direita - 55
        topo = centro_y - 32
        baixo = centro_y + 32

        # fios
        self.canvas.create_line(
            esquerda, centro_y,
            corpo_esq, centro_y,
            fill="#777777",
            width=5
        )

        self.canvas.create_line(
            corpo_dir, centro_y,
            direita, centro_y,
            fill="#777777",
            width=5
        )

        #corpo do resistor
        self.canvas.create_rectangle(
            corpo_esq,
            topo,
            corpo_dir,
            baixo,
            fill="#f4e5b8",
            outline="#725a31",
            width=2
        )

        #descobrir as cores atuais
        if self.modo.get() == "valor":
            nomes = [
                self.banda1.get(),
                self.banda2.get(),
                self.multiplicador.get(),
                self.tolerancia_valor.get()
            ]
        else:
            nomes = [
                self.banda1.get(),
                self.banda2.get(),
                self.multiplicador.get(),
                self.tolerancia_cores.get()
            ]

        cores = [CORES[nome] for nome in nomes]

        # faixas
        largura_corpo = corpo_dir - corpo_esq
        posicoes = [
            corpo_esq + largura_corpo * 0.25,
            corpo_esq + largura_corpo * 0.39,
            corpo_esq + largura_corpo * 0.53,
            corpo_esq + largura_corpo * 0.67
        ]

        for i, (x, cor) in enumerate(zip(posicoes, cores)):
            largura_faixa = 17 if i < 3 else 13

            self.canvas.create_rectangle(
                x - largura_faixa / 2,
                topo,
                x + largura_faixa / 2,
                baixo,
                fill=cor,
                outline="#555555",
                width=1
            )

        #titulo do desenho
        self.canvas.create_text(
            largura / 2,
            20,
            text="Resistor de 4 faixas",
            font=("Arial", 12, "bold"),
            fill="#222222"
        )

        #nomes das cores  abaixo
        nomes_texto = "    ".join(
            nome.capitalize() for nome in nomes
        )

        self.canvas.create_text(
            largura / 2,
            baixo + 30,
            text=nomes_texto,
            font=("Arial", 9),
            fill="#444444"
        )


if __name__ == "__main__":
    janela = tk.Tk()
    app = Calculadora(janela)
    janela.mainloop()