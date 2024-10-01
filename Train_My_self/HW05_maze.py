def maze_solver_with_teleport(maze: list, portals: dict) -> (int, list):
    """
    แก้ปัญหาเขาวงกตด้วยการใช้พอร์ทัล

    Args:
    maze: ตาราง 2 มิติที่แสดงเขาวงกต
    portals: พจนานุกรมของพอร์ทัลและจุดปลายทางของพอร์ทัลนั้น

    Returns:
    ระยะทางที่สั้นที่สุดจากจุดเริ่มต้น 'S' ไปยังจุดสิ้นสุด 'E' และเส้นทางที่ใช้
    หากไม่พบเส้นทาง คืนค่า (-1, []).
    """

    # ค้นหาตำแหน่งเริ่มต้นและจุดสิ้นสุด
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    # ตรวจสอบว่ามีจุดเริ่มต้นและจุดสิ้นสุดหรือไม่
    if not start or not end:
        return -1, []

    # คิวสำหรับ BFS พร้อมข้อมูล: (ตำแหน่ง, เส้นทาง, ระยะทาง)
    queue = [(start, [start], 0)]
    # เซตเก็บตำแหน่งที่เยี่ยมชมแล้ว
    visited = set([start])

    # BFS เพื่อหาเส้นทางที่สั้นที่สุด
    while queue:
        (x, y), path, distance = queue.pop(0)

        # หากถึงจุดสิ้นสุด 'E' คืนค่าระยะทางและเส้นทางที่ใช้
        if (x, y) == end:
            return distance, path

        # ตรวจสอบเพื่อนบ้าน 4 ทิศทาง (บน, ล่าง, ซ้าย, ขวา)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # ตรวจสอบว่าตำแหน่งเพื่อนบ้านอยู่ในเขตเขาวงกตและไม่ใช่กำแพง
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
                new_position = (nx, ny)

                 # ถ้าตำแหน่งใหม่เป็นพอร์ทัลที่สามารถเทเลพอร์ตได้
                if new_position in portals:
                    # เทเลพอร์ตไปยังจุดปลายทางของพอร์ทัล
                    teleport_position = portals[new_position]

                    # ถ้าตำแหน่งปลายทางของพอร์ทัลยังไม่ถูกเยี่ยมชม
                    if teleport_position not in visited:
                        visited.add(teleport_position)
                        queue.append((teleport_position, path + [new_position, teleport_position], distance + 1))

                # ถ้าไม่ใช่พอร์ทัล ให้เดินตามปกติ
                elif new_position not in visited:
                    visited.add(new_position)
                    queue.append((new_position, path + [new_position], distance + 1))

    # หากไม่พบเส้นทาง คืนค่า -1 และเส้นทางว่าง
    return -1, []

# ตัวอย่างที่ 1
maze = [
    ['S', '.', '.', 'P'],
    ['#', '#', '.', '#'],
    ['P', '.', '.', 'E'],
    ['#', '#', '#', '#']
]

portals = {
    (0, 3): (2, 0),  # พอร์ทัลจาก (0, 3) ไปยัง (2, 0)
    (2, 0): (0, 3)   # พอร์ทัลจาก (2, 0) ไปยัง (0, 3)
}

distance, path = maze_solver_with_teleport(maze, portals)
print(f"Distance: {distance}, Path: {path}")
# Output: Distance: 5, Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]


# ตัวอย่างที่ 2
maze = [
    ['S', '.', '#', 'P', '#', 'P'],
    ['#', '.', '#', '.', '#', '.'],
    ['#', '.', 'P', '.', '.', 'E'],
    ['P', '#', '#', '#', '#', '#'],
    ['#', '.', '.', 'P', '.', '.']
]

portals = {
    (0, 3): (3, 0),  # พอร์ทัลจาก (0, 3) ไปยัง (3, 0)
    (3, 0): (0, 3),  # พอร์ทัลจาก (3, 0) ไปยัง (0, 3)
    (0, 5): (2, 2),  # พอร์ทัลจาก (0, 5) ไปยัง (2, 2)
    (2, 2): (0, 5)   # พอร์ทัลจาก (2, 2) ไปยัง (0, 5)
}

distance, path = maze_solver_with_teleport(maze, portals)
print(f"Distance: {distance}, Path: {path}")
# Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]
