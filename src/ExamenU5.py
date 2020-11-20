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
            Input("CPU: ", default="", word_color=colors.foreground["yellow"])
        ]
    )
    actualDevice = Add.launch()
    deviceDic = {'brand': actualDevice[0][1], 'os': actualDevice[1][1],
                 'ram': actualDevice[2][1], 'cpu': actualDevice[3][1]}
    devices.append(deviceDic)


selectedOption = ""
devices = list()
while(selectedOption != "Salir del programa"):
    clear()
    principalMenu = Bullet("Menú principal", choices=[
        "Agregar dispositivo", "Imprimir reporte", "Salir del programa"], margin=5)
    selectedOption = principalMenu.launch()
    if selectedOption == "Agregar dispositivo":
        AddAdvice()
    print(selectedOption)
# print(devices)
for element in devices:
    print(f"Marca: {element['brand']}")
    print(f"OS: {element['os']}")
    print(f"RAM: {element['ram']}")
    print(f"CPU: {element['cpu']}")
