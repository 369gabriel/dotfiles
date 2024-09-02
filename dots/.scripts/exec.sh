#!/bin/bash

# Exibe o prompt do dmenu e captura o comando digitado
cmd=$(echo "" | dmenu -p "Command:")

# Verifica se o usuário digitou algo e executa o comando
if [ -n "$cmd" ]; then
    eval "$cmd"
fi

