#!/bin/bash

archivo="contraseña.txt"

while true; do
    echo "===== Generador de contraseñas ====="
    echo "1. Generar una contraseña"
    echo "2. Salir"
    read -p "Elige una opción: " opcion

    case $opcion in
        1)
            # Pedir longitud
            read -p "Introduzca la longitud de la contraseña (8-32): " longitud
            if [[ ! $longitud =~ ^[0-9]+$ ]] || [[ $longitud -lt 8 ]] || [[ $longitud -gt 32 ]]; then
                echo "Error, introduzca un número válido (8-32)"
                continue
            fi

            # Tipos de caracteres
            read -rp "¿Incluir mayúsculas? (s/n): " mayusculas
            read -rp "¿Incluir números? (s/n): " numeros
            read -rp "¿Incluir caracteres especiales? (s/n): " especiales

            if [[ $mayusculas != "s" && $numeros != "s" && $especiales != "s" ]]; then
                echo "Error. Debes seleccionar al menos un tipo de caracter"
                continue
            fi

            # Conjunto de caracteres
            minusculas="abcdefghijklmnñopqrstuvwxyz"
            caracteres="$minusculas"

            [[ $mayusculas == "s" ]] && caracteres+="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            [[ $numeros == "s" ]] && caracteres+="1234567890"
            [[ $especiales == "s" ]] && caracteres+="!@#$%&/()-_.,^{}¿?'¡"

            # Generar contraseña
            password=""
            for (( i=0; i < longitud; i++ )); do
                rand=$((RANDOM % ${#caracteres}))
                password+="${caracteres:$rand:1}"
            done

            echo "Tu contraseña generada es: $password"
            echo "$password" >> $archivo
            sleep3 

            ;;
        2)
            echo "Saliendo del generador de contraseñas"
            exit 0
            ;;
        *)
            echo "Opción no válida, introduzca otra opción"
            ;;
    esac
done
