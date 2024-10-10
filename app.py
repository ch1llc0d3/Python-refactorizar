""" comentario

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()
    
    if num.isdecimal():
        num = int(num)
        if num == 1:
            while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = input()
                
                if point.isdecimal():
                    point = int(point)
                    
                    if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                        print('Indíquelo en una escala de 1 a 5')
                    else:
                        print('Por favor, introduzca un comentario')
                        comment = input()
                        post = f'punto: {point} comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{ post } \n')
                        file_pc.close()
                        break
                else:
                    print('Por favor, introduzca la puntuación en números')
        
        elif num == 2:
            print('Resultados hasta la fecha.')
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        
        elif num == 3:
            print('Finalizando')
            break  # Sentencia para finalizar el procesamiento
        
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')
"""
# Funcion para poner una puntuacion del usuario
def ingresar_puntuacion_y_comentario():
    while True:
        print("Introduce una puntuacion en una escala de 1 a 5")
        point = input()

        if point.isdecimal():
            point = int(point)
            
            if 1 <= point <= 5:
                print('Introduce un comentario')
                comment = input()
                post = f'punto: {point}, comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print("Puntuacion y comentarios guardados.")
                break 
            else:
                print('Error: Indica la puntuacion del 1 a 5.')
        else:
            print('Error: Introduzca la puntuacion en numeros')

# Funcion para mostrar resultados guardados en el archivo
def mostrar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido: 
                print("Resultados hasta la fecha:")
                print(contenido)
            else: 
                print("No hay resultados guardados aun")
    except FileNotFoundError:
        print("No hay resultados guardados aun")

        
# Funcion para finalizar el programa
def finalizar():
    print("Finalizando el programa")
    exit()
    
def espada():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣶⡎⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢱⣶⣶⣶⣶⣶⣶⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⢣⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠈⠛⠛⠛⠛⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⢣⣤⡄⠀⠀⠀⠀⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡸⠿⢇⣀⣀⠀⠀⠻⠿⢃⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠿⠿⢇⣀⡸⠿⠿⣀⣀⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢰⣶⡎⠉⠱⣶⣶⠉⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⣶⣶⡌⠉⢱⣶⡆⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣴⣶⡎⠉⠁
⠀⠀⠀⣤⣤⠛⠛⢡⣤⡜⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠃⠀⠀
⢀⣤⣤⠛⠛⣤⣤⡘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣀⣀⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    exit()
    
def llama():
    print(""" 
          ⠀⠀⠀⠀⠀⢀⠠⠐⠉⠁⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡍⠒⠤⣀⠀⣀⣤⣿⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡄⢹⣦⠀⣿⣿⣿⣟⠒⠉⠀⠁⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠼⠧⣘⠻⠂⣿⣿⣾⣇⢁⠒⠤⣀⣀⣴⣞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⠯⣀⠀⠀⠀⠉⠒⠿⠛⠁⢸⠸⣷⡆⢸⣿⣿⡏⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠸⣆⠉⠶⣀⠀⠀⠀⠀⠀⠸⣀⡉⠇⢸⣿⣏⡷⢀⣰⣾⠀⠀⠀⠀⠀⠀⠀⣀⠶⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠐⢼⡷⣶⡄⠉⠒⠤⢀⠀⠀⠀⠉⠓⢼⣿⣟⣿⡿⣿⣿⠀⠀⠀⣀⠤⠒⠉⠀⠀⠀⠈⠐⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⠤⠚⠋⠉⠓⠤⣀⣷⣤⣉⠒⢤⣴⣾⣿⣟⣿⢾⣟⣿⣽⠤⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠠⢄⠀⠀⠀⠀⠀⠀⠀⠀
⢖⠈⠀⠀⠀⠀⠀⠀⠀⠀⠉⣺⣯⡇⠸⣿⣟⣾⣟⣾⣟⣿⣾⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠠⢀⡀⠀⠀⠀
⣆⡉⠒⠤⣀⠀⠀⣀⣤⣶⣿⣿⠿⡇⢘⣿⣯⣷⣿⣻⣾⡷⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀
⠻⣏⠀⠀⣠⣉⣿⣿⣟⣿⡷⣿⠀⠀⢸⣯⣿⢷⣿⣻⣾⢿⣟⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶
⣧⣼⣻⢳⡼⢿⣿⣷⣻⣯⣿⣿⠀⠂⢸⣿⣯⣿⣿⣻⣽⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣿⣿
⠻⠟⣿⣿⣧⣤⣿⣿⣯⡿⠗⠋⠀⠄⢸⣿⣯⣷⡿⣟⣯⣷⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣾⣿⣿⡿⣟⣿⣾⣿
⠀⠀⢸⢈⠙⠻⠟⠋⠁⡀⠄⡈⠐⡈⢸⣿⡿⣽⣿⡿⣟⣿⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣿⣿⣻⣿⣽⣿⡿⣿⣻⣽
⠀⠀⢸⢈⠐⠠⢂⢈⠡⠐⠠⠌⠁⠄⢸⣿⣿⢿⣯⣿⣿⢿⣻⣟⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⢿⣻⣽⣾⣟⣿⣽⣿⣾⣿⣿⣿⣿
⠀⠀⢸⠀⡌⢑⠠⢠⠘⡀⠡⢀⢃⠂⢸⣿⡿⣿⣿⣷⣿⡿⠟⠋⠀⠀⠀⢀⣤⣴⣿⣿⡿⣟⣯⣿⣻⣿⢿⣻⣽⣿⣻⣯⣷⣿⣷⣿⣯⣿
⠀⠀⢸⠀⡜⠠⢂⠄⢣⠀⢡⠂⠆⠌⢸⣿⣿⢿⣷⣿⣯⠐⠤⣀⣠⣶⣿⣿⡿⣿⣻⣷⣿⢿⣿⣻⣿⣽⣿⡿⣿⣽⣿⣟⣿⣽⣾⣿⣿⣿
⠀⠀⢸⠠⡔⠡⢈⠢⢄⠘⣀⠊⡐⢈⢸⣿⡿⣿⣟⣿⡷⠀⠠⢸⣿⣿⣯⣷⣿⡿⣿⣽⣾⡿⣟⣿⣽⣿⣾⢿⣟⣿⣽⣿⡿⣿⣻⣿⣿⣿
⠀⠀⢸⠰⢆⠁⡆⠶⡈⠰⠀⡆⢱⠀⢸⣿⣿⣿⢿⣿⡿⢀⠰⢸⣿⣷⣿⣏⣷⣿⣿⢿⣹⣿⣿⡿⣿⣾⣿⣿⣿⢿⣏⣿⣿⣿⣿⣿⣿⣿
⠀⠀⢸⢐⠃⡌⡐⠦⣡⠑⡌⡐⣂⠡⢸⣿⣿⡿⣿⣿⣟⠠⢀⢸⣿⡿⣷⣿⢿⣯⣿⡿⣿⣻⣷⣿⣿⣻⣾⣿⣽⣿⡿⣿⣻⣿⣿⣿⢿⠻
⠀⠀⢸⢌⢊⠔⡡⢒⠤⢃⠤⡑⠤⠃⢼⣿⣿⣿⣿⢿⣯⠀⠤⢸⣿⣿⣟⣿⡿⣟⣷⣿⣿⢿⣯⣷⣿⣟⣿⣾⣿⣟⣿⣿⣿⣿⡟⠂⠁⠀
⠀⠀⠈⠛⠢⢎⡐⢣⢘⠢⡑⠬⣁⠏⣸⣿⣿⣿⣾⣿⣿⠀⡐⢸⣿⣷⣿⣻⣿⡿⣿⣻⣾⣿⣿⣻⣽⣿⣿⣽⣾⣿⣿⣻⣽⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⢱⠎⠰⣉⠲⣁⠚⣸⣿⣿⣿⣿⣿⠟⠠⠐⢸⣿⣯⣿⢿⣷⣿⡿⣿⣻⣷⣿⣿⡿⠗⠋⡁⢸⣿⣽⡿⣟⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢨⢳⠀⡈⠙⠒⠭⣸⣿⠿⠛⢁⠰⡀⢆⠉⢼⣿⣟⣿⣿⣻⣷⣿⣿⢿⣿⣿⠁⠀⡐⠠⠐⢸⣿⣿⢿⣿⡿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⣏⠐⠠⠁⠌⡐⣿⣿⣶⣮⡄⣣⠑⢤⣉⢺⣿⣿⣿⣿⡿⣿⣽⣾⣿⡿⣿⠠⢁⠠⢡⠈⢸⣿⣿⣿⣯⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⡒⠠⠄⡉⠐⡀⣿⣿⡿⣿⡇⠀⠙⠓⢤⣺⣿⣿⣾⢿⣽⡿⣿⣿⣿⣿⣿⠐⠠⢁⠂⢌⢸⣿⣿⣾⣿⣽⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢇⡁⢂⠡⠡⠐⣿⣿⣿⢿⡇⠈⡐⠈⠄⠠⢸⣿⡿⣿⣻⣿⣿⣿⣿⣻⣿⠀⡑⠂⠌⡐⢸⣿⣿⣷⡿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣆⠐⠢⢀⠱⢈⣿⣿⡿⣿⡇⡐⠠⠡⠈⠄⢻⣿⣿⢿⣿⣷⣿⣿⣿⣿⣿⠠⢌⡑⠠⡐⢸⣿⣿⣯⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣶⠈⢡⠂⡐⠠⣿⣿⣿⣿⡇⠤⢁⠢⢁⠌⣸⣿⣿⣿⣻⣾⣿⣿⣿⣿⣿⠐⠢⢌⠑⠤⢹⣿⣿⣿⣟⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⡦⢘⢢⠐⣈⠡⣿⣿⣿⣾⡇⠒⠠⢈⠂⡐⢼⣿⣿⣾⢿⣟⡿⠟⠚⠁⢸⢊⠡⢌⠚⡠⢺⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⡵⢈⢂⡱⣀⠒⣿⣿⣿⣿⡇⠈⡅⢂⠂⠡⢺⣿⣿⣽⣿⣿⡇⠀⠀⠀⢸⠇⣘⠢⣡⠑⣼⣿⣿⣿⣿⣿⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣹⠀⢇⠰⣀⠎⣿⣿⣿⣿⡇⢰⠈⠆⡈⠁⣾⣿⣿⣿⣹⣿⡇⠀⠀⠀⠀⠈⠷⢶⡀⢇⢸⣿⣿⢿⠷⠏⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢮⡘⡄⠓⣄⢊⣿⣿⣿⣿⡇⢂⢍⡒⢠⠑⣸⣿⣿⣿⢿⣻⡇⠀⠀⠀⠀⠀⠀⠀⠈⠓⠸⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠤⣊⣿⡿⠟⠉⡇⡌⢄⠒⢢⠁⢾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⡗⠣⢌⡸⠡⠜⣸⣿⣿⣿⣿⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠦⣐⠣⠌⣽⣿⣿⣿⠯⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠚⠼⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)
    
# Mostrar menu principal y gestiona las opciones
def mostrar_menu():
        while True:
            print('Seleccione el proceso que desea aplicar')
            print('1: Ingresar puntuacion y comentario')
            print('2: Comprueba los resultados obtenidos hasta ahora')
            print('3. Finalizar')
            print('4. Espada')
            print('5. Llama')
            
            num = input()
            
            if num.isdecimal():
                num = int(num)
                if num == 1:
                    ingresar_puntuacion_y_comentario()
                elif num == 2:
                    mostrar_resultados()
                elif num == 3:
                    finalizar()
                    break
                elif num == 4:
                    espada()
                elif num == 5:
                    llama()
                else:
                    print('Introduzca un numero del 1 al 5')
            else:
                print('Introduzca un numero del 1 al 5')
# Ejecutar el programa 
mostrar_menu()