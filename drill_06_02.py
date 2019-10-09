from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def move_points(pointX,pointY):
    frame = 0

    # draw p1-p2
    for i in range(0, 50, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * int(pointX[0]) + (-4 * t ** 2 + 4 * t) * int(pointX[1]) + (2 * t ** 2 - t) * int(pointX[2])
        y = (2 * t ** 2 - 3 * t + 1) * int(pointY[0]) + (-4 * t ** 2 + 4 * t) * int(pointY[1]) + (2 * t ** 2 - t) * int(pointY[2])
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, pointX[1], pointY[1])

    for i in range(1,9):
        for j in range(0, 100, 2):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            t = j / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * int(pointX[(i-1)%9]) + (3 * t ** 3 - 5 * t ** 2 + 2) * int(pointX[i]) + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * int(pointX[(i + 1) % 9]) + (t ** 3 - t ** 2) * int(pointX[(i + 2) % 9])) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * int(pointY[(i-1)%9]) + (3 * t ** 3 - 5 * t ** 2 + 2) * int(pointY[i]) + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * int(pointY[(i + 1) % 9]) + (t ** 3 - t ** 2) * int(pointY[(i + 2) % 9])) / 2
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            frame = (frame + 1) % 8
            delay(0.05)
            update_canvas()
        character.clip_draw(frame * 100, 100 * 1, 100, 100, pointX[i], pointY[i])

    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * int(pointX[7]) + (-4 * t ** 2 + 4 * t) * int(pointX[8]) + (
                    2 * t ** 2 - t) * int(pointX[9])
        y = (2 * t ** 2 - 3 * t + 1) * int(pointY[7]) + (-4 * t ** 2 + 4 * t) * int(pointY[8]) + (
                    2 * t ** 2 - t) * int(pointY[9])
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, pointX[9], pointY[9])

    for j in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = j / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * int(pointX[8]) + (3 * t ** 3 - 5 * t ** 2 + 2) * int(pointX[9]) + (
                -3 * t ** 3 + 4 * t ** 2 + t) * int(pointX[0]) + (t ** 3 - t ** 2) * int(
            pointX[1])) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * int(pointY[8]) + (3 * t ** 3 - 5 * t ** 2 + 2) * int(pointY[9]) + (
                -3 * t ** 3 + 4 * t ** 2 + t) * int(pointY[0]) + (t ** 3 - t ** 2) * int(
            pointY[1])) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, pointX[1], pointY[1])



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
pointX = [random.randint(1,1000) for n in range(10)]
pointY = [random.randint(1,1000) for n in range(10)]

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
P1 = [640,512]
P2 = [640,512]

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    move_points(pointX,pointY)
    update_canvas()


    handle_events()

close_canvas()
