from tkinter import Canvas, BOTH, Button, Frame

points = []
lines = []
canvas = None
frame = None


def on_dot_click(event):
    x = event.x
    y = event.y
    points.append((x, y))
    canvas.create_rectangle(x, y, x + 3, y + 3, fill="#476042")


def reset_canvas(e):
    canvas.delete("all")
    points.clear()
    lines.clear()
    print("Reset")


def convex_hull(e):
    for line in lines:
        canvas.delete(line)

    # res = []

    for i, point_i in enumerate(points):
        for point_j in points[i:]:
            greater = False
            less = False

            a = point_j[1] - point_i[1]
            b = point_i[0] - point_j[0]
            c = a * (point_i[0]) + b * (point_i[1])

            for point in points:
                check = a * point[0] + b * point[1]

                if check > c:
                    greater = True
                elif check < c:
                    less = True

            if (not greater and less) or (greater and not less):
                lines.append(canvas.create_line(point_i[0], point_i[1], point_j[0], point_j[1]))
                # if point_i not in res:
                #     res.append(point_i)

    if not len(lines):
        return "Impossible"
    # return res


if __name__ == "__main__":
    frame = Frame(None, bg='grey', height=2)
    frame.pack()

    canvas = Canvas(frame, width="600", height="600")
    canvas.pack(fill=BOTH, expand=1)
    button = Button(frame, text="Start")
    button.bind('<Button-1>', convex_hull)
    button.pack(side='left', padx=10)
    reset = Button(frame, text="Reset")
    reset.pack(side='left', padx=10)
    reset.bind('<Button-1>', reset_canvas)

    canvas.bind('<Button-1>', on_dot_click)
    frame.mainloop()
    # print(points)
