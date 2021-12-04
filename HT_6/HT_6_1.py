"""
   Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
"""

from time import sleep

traffic_light_cars = ('Red', 'Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green', 'Green', 'Yellow', 'Yellow')
traffic_light_pedestrian = ('Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red' )

def traffic_light():
    print("---","     ","------")
    print("Car","     ","People")
    print("---","     ","------")

    while True:
        for i in range(len(traffic_light_cars)):
            sleep(1)
            if traffic_light_cars[i] == 'Yellow' and traffic_light_pedestrian[i] == 'Green':
                print(traffic_light_cars[i],'   ',traffic_light_pedestrian[i])
            elif traffic_light_cars[i] == 'Yellow' and traffic_light_pedestrian[i] == 'Red':
                print(traffic_light_cars[i],'     ',traffic_light_pedestrian[i])
            elif traffic_light_cars[i] == 'Green' and traffic_light_pedestrian[i] == 'Red':
                print(traffic_light_cars[i],'      ',traffic_light_pedestrian[i])
            elif traffic_light_cars[i] == 'Red' and traffic_light_pedestrian[i] == 'Green':
                print(traffic_light_cars[i],'      ',traffic_light_pedestrian[i])

traffic_light()
