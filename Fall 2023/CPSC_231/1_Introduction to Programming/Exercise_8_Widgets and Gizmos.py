WIDGETS = 75 
GIZMOS = 112

widgets = float(input("Enter the Amount of Widgets: "))
gizmos = float(input("Enter the Amount of Gizmos: "))

tWidgets = widgets * WIDGETS
tGizmos = gizmos * GIZMOS

total = tWidgets + tGizmos

print("The Total Weight Of The Parts is: ", total)