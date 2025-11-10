#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

obstacle_sensor = UltrasonicSensor(Port.S3)
color_sensor = ColorSensor(Port.S4)

# Estado para alternância de curvas: começa virando à direita.
last_turn = 'l' 

def turn_to(side: str):
    """Faz a manobra de desvio para o lado indicado ('r' ou 'l')."""
    if side == 'r':
        robot.turn(90)
        robot.straight(300)
        robot.turn(-90)
    else:
        robot.turn(-90)
        robot.straight(300)
        robot.turn(90)

def drive_ahead():
    global last_turn

    while True:
        cor = color_sensor.color()
        refl = color_sensor.reflection()

        # Condição de parada caso identifique a cor branca.
        if cor == Color.WHITE and refl >= 60:
            robot.stop()
            break

        # Segue em frente.
        robot.drive(125, 0)

        # Verifica se há obstáculo próximo.
        if obstacle_sensor.distance() < 200:
            robot.stop()
            # Se a última foi 'r', agora será 'l', e vice-versa.
            next_turn = 'l' if last_turn == 'r' else 'r'
            # Chama a função que faz o carro virar
            turn_to(next_turn)
            last_turn = next_turn  
            # Pausa para estabilizar sensores/mecânica.
            wait(100)

drive_ahead()
