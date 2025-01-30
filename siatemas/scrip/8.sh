#!/bin/bash
opcion=0

while [ $opcion -le 2 ]
do
    clear
    echo "Para poder ejecutar este script necesitas tener Instalado el netsatat."
    echo "1. Sí, lo tengo instalado"
    echo "2. No, necesito instalarlo"
    read -p "Selecciona una opción: " opcion

    case $opcion in
        1)
            op=0
            while [ $op -le 4 ]
            do
                clear
                echo "1. Muestra el estado de los puertos, con su protocolo de los host de tu red."
                echo "2. Muestra los hosts activos de tu red."
                echo "3. Identifca los Sistemas operativos de los hosts de tu red."
                echo "4.Manda la información de los puntos 1 y 3 a un fichero ""salida_host.txt""."
                echo "5.Busca toda la información relativa a un host, cuya IP solicitaras por pantalla en el fichero salida_host.txt."
                echo "6. Salir"
                read -p "Selecciona una opción: " op

                case $op in
                    1)
                        echo "Mostrando puertos "
                        sudo netstat -tuln
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                    2)
                        echo "Mostrando host activos"
                        sudo netstat -an | grep ESTABLISHED
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                    3)
                        read -p "introduce la red que quieres escarnear(ponlo con el /24 ...): " red
                        sudo nmap -sn $red
                        ;;
                    4)
                        echo "exprotando informacion..."
                        read -p "introduce la red que quieres escarnear(ponlo con el /24 ...): " red
                        sudo nmap -sn $red
                        sudo netstat -tuln > salida_host.txt
                        ;;
                    5)
                        read -p "introduce la ip que quieres escarnear: " ip
                        sudo nmap -A -v $ip >> salida_host.txt
                        ;;
                    6)
                        echo "¡ADIOOOOS!"
                        exit
                        ;;
                    *)
                        echo "Opción incorrecta. No está dentro del rango..."
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                esac
            done
            ;;
        2)
            echo "Actualizando repositorios..."
            sudo apt update
            echo "Instalando NETSATAT..."
            sudo apt install net-tools
            echo "IPTABLES instalado correctamente."
            read -p "Pulsa una tecla para continuar..."
            ;;
        *)
            echo "Opción no válida. Intente de nuevo."
            read -p "Pulsa una tecla para continuar..."
            ;;
    esac
done
