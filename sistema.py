import psutil
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

# ==========================
# CONFIGURAÇÃO INICIAL
# ==========================
ctk.set_appearance_mode("dark")  # Tema escuro
ctk.set_default_color_theme("blue")  # Tema azul

app = ctk.CTk()
app.title("Gerenciador de Sistema")
app.geometry("700x600")
app.resizable(False, False)

# ==========================
# ABAS
# ==========================
abas = ctk.CTkTabview(app, width=680, height=560)
abas.pack(padx=10, pady=10)

aba_sistema = abas.add("Sistema")
aba_processos = abas.add("Processos")

# ==========================
# ABA SISTEMA - Info de CPU, RAM e Bateria
# ==========================
frame_info = ctk.CTkFrame(aba_sistema, corner_radius=10)
frame_info.pack(pady=15, padx=15, fill="x")

# Função para criar cada linha de informação (CPU, RAM, Bateria)
def criar_linha_info(emoji, titulo, valor):
    linha = ctk.CTkFrame(frame_info, fg_color="transparent")
    linha.pack(fill="x", pady=5)

    label_emoji = ctk.CTkLabel(linha, text=emoji, font=ctk.CTkFont(size=18))
    label_emoji.pack(side="left", padx=5)

    label_titulo = ctk.CTkLabel(linha, text=titulo, font=ctk.CTkFont(size=14, weight="bold"))
    label_titulo.pack(side="left", padx=5)

    label_valor = ctk.CTkLabel(linha, text=valor, font=ctk.CTkFont(size=14))
    label_valor.pack(side="left", padx=5)

    return label_valor

# Criação das três linhas principais com ícones
label_cpu_valor = criar_linha_info("🖥️", "Uso da CPU:", "Carregando...")
label_mem_valor = criar_linha_info("📦", "Uso da Memória:", "Carregando...")
label_bat_valor = criar_linha_info("🔋", "Bateria:", "Carregando...")

# ==========================
# GRÁFICO DE USO AO VIVO
# ==========================
frame_grafico = ctk.CTkFrame(aba_sistema)
frame_grafico.pack(padx=10, pady=10, fill="both", expand=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4), dpi=100)
fig.subplots_adjust(hspace=0.6)
grafico = FigureCanvasTkAgg(fig, master=frame_grafico)
grafico.get_tk_widget().pack(fill="both", expand=True)

# Dados ao vivo para os gráficos
dados_cpu = deque([0]*60, maxlen=60)
dados_memoria = deque([0]*60, maxlen=60)

# ==========================
# FUNÇÃO DE ATUALIZAÇÃO SISTEMA
# ==========================
def atualizar_sistema():
    # CPU e RAM
    cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory()
    mem_percent = memoria.percent
    used_mb = memoria.used // (1024 ** 2)
    total_mb = memoria.total // (1024 ** 2)

    label_cpu_valor.configure(text=f"{cpu:.1f}%")
    label_mem_valor.configure(text=f"{mem_percent:.1f}% ({used_mb} MB de {total_mb} MB)")

    # Bateria
    bateria = psutil.sensors_battery()
    if bateria:
        status = "🔌 Carregando" if bateria.power_plugged else "🔋 Usando bateria"
        label_bat_valor.configure(text=f"{bateria.percent}% - {status}")
    else:
        label_bat_valor.configure(text="Dispositivo sem bateria")

    # Atualizar gráfico
    dados_cpu.append(cpu)
    dados_memoria.append(mem_percent)

    ax1.clear()
    ax1.plot(dados_cpu, color="cyan")
    ax1.set_ylim(0, 100)
    ax1.set_title("Uso da CPU (%)")
    ax1.grid(True)

    ax2.clear()
    ax2.plot(dados_memoria, color="magenta")
    ax2.set_ylim(0, 100)
    ax2.set_title("Uso da Memória (%)")
    ax2.grid(True)

    grafico.draw()
    app.after(1000, atualizar_sistema)  # Atualiza a cada 1 segundo

# ==========================
# ABA PROCESSOS
# ==========================
frame_top = ctk.CTkFrame(aba_processos)
frame_top.pack(pady=10, padx=10, fill="both", expand=True)

lista = ctk.CTkScrollableFrame(frame_top)
lista.pack(fill="both", expand=True)

label_instrucao = ctk.CTkLabel(aba_processos, text="Clique em um processo para finalizar", font=ctk.CTkFont(size=12))
label_instrucao.pack(pady=5)

# Função para encerrar um processo
def finalizar_processo(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
    except Exception as e:
        print(f"Erro ao encerrar processo: {e}")
    atualizar_processos()

# Lista e atualiza os processos ativos
def atualizar_processos():
    for widget in lista.winfo_children():
        widget.destroy()

    processos = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)

    for proc in processos[:20]:  # Exibe os 20 principais
        pid = proc.info['pid']
        nome = proc.info['name']
        cpu = proc.info['cpu_percent']
        mem = proc.info['memory_percent']

        texto = f"{nome} | CPU: {cpu:.1f}% | Memória: {mem:.1f}%"
        linha = ctk.CTkFrame(lista)
        linha.pack(fill="x", pady=2, padx=2)

        label = ctk.CTkLabel(linha, text=texto)
        label.pack(side="left", padx=4)

        btn = ctk.CTkButton(linha, text="Finalizar", width=80, fg_color="red", hover_color="darkred",
                            command=lambda pid=pid: finalizar_processo(pid))
        btn.pack(side="right", padx=4)

    app.after(4000, atualizar_processos)  # Atualiza a lista a cada 4 segundos

# ==========================
# INICIAR ATUALIZAÇÕES
# ==========================
atualizar_sistema()
atualizar_processos()
app.mainloop()
