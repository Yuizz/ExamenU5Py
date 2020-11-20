from bullet import Bullet, SlidePrompt, Check, YesNo, Input, Password, Numbers,  colors
import os
def clear(): return os.system('clear')


def AddAdvice():
    clear()
    Add = SlidePrompt(
        [
            Input("Marca del teléfono: ", default="",
                  word_color=colors.foreground["yellow"]),
            Bullet("Sistema operativo:", choices=[
                   "Android", "IOS"], margin=2, background_on_switch=colors.background["white"], word_on_switch=colors.foreground["black"]),
            Numbers(
                "RAM: ", word_color=colors.foreground["yellow"], type=int),
            Input("CPU: ", default="", word_color=colors.foreground["yellow"]),
            Numbers("Números de ventas en el año: ",
                    word_color=colors.foreground["yellow"], type=int)
        ]
    )
    actualDevice = Add.launch()
    deviceDic = {'brand': actualDevice[0][1], 'os': actualDevice[1][1],
                 'ram': actualDevice[2][1], 'cpu': actualDevice[3][1], 'sales': actualDevice[4][1]}
    devices.append(deviceDic)


def PrintReport():
    clear()
    print("| {0:<10} | {1:<10} | {2:>5} | {3:>9} | {4:>7} |".format(
        "Marca ", "OS", "RAM", "CPU", "Ventas"))
    for element in devices:
        print("\n| {0:<10} | {1:<10} | {2:>5} | {3:>9} | {4:>7} |".format(
            element['brand'], element['os'], element['ram'], element['cpu'], element['sales']))
    FindMajor()
    input("\nPresiona enter para continuar. ")


def FindMajor():
    index = 0
    major = 0
    counter = 0
    for element in devices:
        if element['sales'] > major:
            index = counter
            major = element['sales']
        counter = counter + 1
    print(
        f"\n\tEl dispositivo mas vendido en el año fue: {devices[index]['brand']} con {devices[index]['sales']} ventas.")


selectedOption = ""
devices = list()
while(selectedOption != "Salir del programa"):
    clear()
    principalMenu = Bullet("Menú principal", choices=[
        "Agregar dispositivo", "Imprimir reporte", "Salir del programa"], margin=2, bullet=">")
    selectedOption = principalMenu.launch()

    if selectedOption == "Agregar dispositivo":
        AddAdvice()
    if selectedOption == "Imprimir reporte":
        PrintReport()
    print(selectedOption)
