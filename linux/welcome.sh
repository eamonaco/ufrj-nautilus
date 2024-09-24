#!/usr/bin/bash

# Mensagem de boas vindas
echo "Bem vindo $USER ao terminal do $(hostname)"

# dotfile para arquivar as execuções
logfile="$HOME/.welcome.data"

# Pega a data e hora atual
data_atual=$(date "+%Y-%m-%d %H:%M:%S")

# Escreve a data e hora no arquivo ~/.welcome.data
echo "Script executado em: $data_atual" >> "$logfile"

# Mostra o clima formatado para o padrão CLI
curl wttr.in/?0
