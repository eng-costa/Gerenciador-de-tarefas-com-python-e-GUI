# 📊 Gerenciador de Sistema em Python

Um Sistema gráfico moderno, desenvolvido com Python, para a Disciplina de **Sistemas Operacionais** que monitora em tempo real o uso de CPU, memória, bateria e processos ativos do sistema — inspirado no Gerenciador de Tarefas do Windows.

---

## 🚀 Funcionalidades

- Monitoramento em tempo real da **CPU**, **memória RAM** e **bateria**
- **Gráficos dinâmicos** do uso de CPU e memória (últimos 60 segundos)
- Lista dos **20 processos mais ativos**, com botão para finalizar
- Interface moderna com abas, escura e responsiva (via `customtkinter`)

---

## 🧰 Tecnologias Utilizadas

| Biblioteca        | Finalidade                                           |
|-------------------|------------------------------------------------------|
| `psutil`          | Acesso aos dados do sistema (CPU, RAM, processos)    |
| `customtkinter`   | Interface gráfica moderna                            |
| `matplotlib`      | Criação dos gráficos dinâmicos                       |
| `collections.deque` | Armazena os últimos dados para exibir nos gráficos |

---

## 💻 Execução

### ▶️ Modo 1: Usar o Executável (.exe)

Se você estiver no Windows, pode rodar diretamente o executável gerado:

```
dist/sistema.exe
```

> ✔️ **Não é necessário ter Python instalado.** Basta dar dois cliques ou executar pelo terminal.

---

### 🐍 Modo 2: Rodar via Python (para desenvolvedores)

1. Clone o repositório:

```bash
git clone https://github.com/eng-costa/Gerenciador-de-tarefas-com-python-e-GUI.git
cd sistema
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script:

```bash
python sistema.py
```

---

## 📦 Gerar Executável (.exe) — Para Desenvolvedores

Se quiser criar o `.exe` você mesmo:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole sistema.py
```

O executável será gerado na pasta `dist/`.

---

## 📷 Captura de Tela

Exemplo da exibição das informações:

```
🖥️ Uso da CPU: 32.7%
📦 Uso da Memória: 56.4% (4590 MB de 8192 MB)
🔋 Bateria: 98% - Carregando
```

---

## ✨ Melhorias Futuras

- Monitoramento de **disco e rede**
- Modo compacto
- Salvamento de logs em arquivo
- Filtro de processos por nome
- Exportação de relatório

---

## 📁 Estrutura do Projeto

```
├── .venv/                # Ambiente virtual (ignorado pelo Git)
├── build/                # Arquivos intermediários do PyInstaller
├── dist/                 # Contém o sistema.exe gerado
│   └── sistema.exe
├── sistema.py            # Código principal da aplicação
├── sistema.spec          # Arquivo de configuração gerado pelo PyInstaller
├── requirements.txt      # Dependências
├── README.md             # Este arquivo
└── .gitignore            # Arquivos/pastas ignorados pelo Git
```

---

## 🧑‍💻 Autor

Desenvolvido por **Lucas** 💡

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.
