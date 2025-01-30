#!/bin/bash
opcion=0

while [ $opcion -le 2 ]
do
    clear
    echo "Para poder ejecutar este script necesitas tener IPTABLES instalado."
    echo "1. Sí, lo tengo instalado"
    echo "2. No, necesito instalarlo"
    read -p "Selecciona una opción: " opcion

    case $opcion in
        1)
            op=0
            while [ $op -le 4 ]
            do
                clear
                echo "1. Hacer filtrado de paquetes de forma que ningún equipo del exterior pueda acceder."
                echo "2. Realizar un filtrado de paquetes de forma que las PCs de la clase no puedan acceder."
                echo "3. Realizar un filtrado de paquetes salientes para que ningún equipo pueda acceder a Facebook."
                echo "4. Salir"
                read -p "Selecciona una opción: " op

                case $op in
                    1)
                        read -p "Introduce la IP a bloquear: " ip
                        sudo iptables -A INPUT -s $ip -j DROP
                        echo "Se ha bloqueado el acceso desde la IP $ip."
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                    2)
                        read -p "Introduce la primera IP del rango: " ip1
                        read -p "Introduce la última IP del rango: " ip2
                        sudo iptables -A OUTPUT -m iprange --src-range $ip1-$ip2 -j DROP
                        echo "Se ha bloqueado el rango de IPs $ip1 a $ip2."
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                    3)
                        read -p "Introduce la IP de la red con máscara (por ejemplo: 192.168.1.0/24): " ip
                        sudo iptables -A OUTPUT -s $ip -d www.facebook.com -j DROP
                        echo "Se ha bloqueado el acceso a Facebook desde la red $ip."
                        read -p "Pulsa una tecla para continuar..."
                        ;;
                    4)
                        echo "¡ADIOOOOOS!"
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
            echo "Instalando IPTABLES..."
            sudo apt install -y iptables
            echo "IPTABLES instalado correctamente."
            read -p "Pulsa una tecla para continuar..."
            ;;
        *)
            echo "Opción no válida. Intente de nuevo."
            read -p "Pulsa una tecla para continuar..."
            ;;
    esac
done
