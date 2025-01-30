#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    sudo useradd -m $1
    echo "$1:$2" | sudo chpasswd
    echo "$usuario a sido creado correctamente."
}

opcion2() {
    sudo usermod -p $2 $1
    echo "contraseña de $user modificada correctamente"
}

opcion3() {
    sudo userdel -r $1
    echo "$1 elminado correctamente."
}

opcion4() {
    installfinger
    finger $1
}

opcion5() {
    sudo usermod -aG $2 $1
}
installfinger(){
    op=0
    while [ $op -le 2]
    do
        echo "¿Quieres intalar Fingers o lo tienes ya instalado?"
        echo "1.Si, lo quiero instalar."
        echo "2.No, ya lo tengo instalado"
        case $op in
            1)
               echo "Instalando fingers"
               sudo apt install finger
               echo "Instalado correctamente"
            2)
               echo "saliendo.."
    done
}

salir() {
    echo "Saliendo del menú..."
    exit 0
}

# Menú
while true; do
    clear
    echo "-------------------------"
    echo "     Menú Principal"
    echo "-------------------------"
    echo "1) Crear usuario, pidiendo el usuario y contraseña por pantalla."
    echo " "
    echo "2) Modificar la contraseña del usuario."
    echo " "
    echo "3) Borrar un usuario."
    echo " "
    echo "4) Muestra información de un usuario dado por pantalla."
    echo " "
    echo "5) Añade un usuario a un grupo dado."
    echo " "
    echo "6) Salir"
    echo "-------------------------"
    echo -n "Selecciona una opción: "
    
    read opcion
    
    case $opcion in
        1)
         read -p "Introduce el nombre del usuario" usuario
         read -p "Introduce la contraseña del usuario" contraseña
         opcion1 $usuario $contraseña;;
        2)
         read -p "Introduce el usuario a modificar: " user
         read -p "Introduce ña la nueva contraseña: " contraseña
         opcion2 $user $contraseña;;
        3)
         read -p "Introduce el nombre del usuario a eliminar" user
         opcion3 $user ;;
        4)
        read -p "Introduce el usuario del que quieres saber la informacio" user
        opcion4 $user ;;
        5)
        read -p "Introdice el usuario" user
        read -p "Introduce el grupo" grupo
        opcion5 $user $grupo;;
       6) salir ;;
       *) echo "Opción no válida, por favor selecciona una opción entre 1 y 6." ;; esac

    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
