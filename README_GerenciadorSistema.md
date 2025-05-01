
# 📊 Gerenciador de Sistema em Python

Um aplicativo gráfico moderno, desenvolvido com Python, que monitora em tempo real o uso de CPU, memória, bateria e processos ativos do sistema. Inspirado no Gerenciador de Tarefas do Windows.

---

## 🚀 Funcionalidades

- Monitoramento em tempo real da **CPU**, **memória RAM** e **bateria**
- **Gráficos dinâmicos** do uso de CPU e memória (últimos 60 segundos)
- Lista dos **20 processos mais ativos**, com botão para finalizar
- Interface moderna e escura usando `customtkinter`
- Layout responsivo e limpo

---

## 🧰 Tecnologias Utilizadas

| Biblioteca       | Finalidade                                           |
|------------------|------------------------------------------------------|
| `psutil`         | Acesso aos dados do sistema                          |
| `customtkinter`  | Interface gráfica moderna                            |
| `matplotlib`     | Criação dos gráficos dinâmicos                       |
| `collections.deque` | Armazena os últimos dados para exibir nos gráficos |

---

## 📦 Instalação

1. Clone este repositório ou copie o código.
2. Instale as dependências:

```bash
pip install psutil customtkinter matplotlib
```

3. Execute o programa:

```bash
python gerenciador_sistema.py
```

---

## 📷 Captura de Tela

Interface moderna com abas e gráficos ao vivo:

```
[🖥️ Uso da CPU: 30.5%]
[📦 Uso da Memória: 55.3% (4520 MB de 8192 MB)]
[🔋 Bateria: 98% - Carregando]
```

---

## ✨ Possíveis Melhorias Futuras

- Monitoramento de **discos e rede**
- Salvamento de logs em arquivo
- Modo compacto / detalhado
- Geração de `.exe` para Windows

---

## 🧑‍💻 Autor

Desenvolvido por Lucas com apoio do ChatGPT como instrutor de projeto 💡

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.
