import math

class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class EnemyAI:
    def __init__(self, x: float, y: float, detection_radius: float, speed: float):
        self.position = Vector2(x, y)
        self.detection_radius = detection_radius
        self.speed = speed
        self.state = "IDLE"

    # 1. Algoritma Perhitungan Jarak (Euclidean Distance)
    def calculate_distance(self, target_pos: Vector2) -> float:
        return math.sqrt((target_pos.x - self.position.x)**2 + (target_pos.y - self.position.y)**2)

    # 2. Algoritma Pathfinding (Representasi Sederhana Algoritma A*)
    def find_path_a_star(self, start: Vector2, target: Vector2, dungeon_grid) -> list:
        # Pada implementasi produksi, A* menggunakan Priority Queue (f = g + h)
        # Mengembalikan urutan titik/waypoint dari start ke target
        return [start, target] 

    # 3. Algoritma Steering Behaviour (Seek)
    def move_towards(self, target_node: Vector2, delta_time: float):
        # Hitung Vektor Arah
        dir_x = target_node.x - self.position.x
        dir_y = target_node.y - self.position.y
        distance = math.sqrt(dir_x**2 + dir_y**2)

        if distance > 0:
            # Normalisasi Vektor dan Perbarui Posisi
            self.position.x += (dir_x / distance) * self.speed * delta_time
            self.position.y += (dir_y / distance) * self.speed * delta_time

    # Dijalankan setiap frame di dalam Game Loop
    def update(self, player_pos: Vector2, dungeon_grid, delta_time: float):
        # Langkah A: Deteksi Jangkauan
        distance_to_player = self.calculate_distance(player_pos)

        # Langkah B: Finite State Machine (Decision)
        if distance_to_player <= self.detection_radius:
            self.state = "CHASE"
            
            # Langkah C: Pathfinding (A*)
            path = self.find_path_a_star(self.position, player_pos, dungeon_grid)
            
            # Langkah D: Movement (Steering Behaviour)
            if len(path) > 1:
                next_waypoint = path[1]
                self.move_towards(next_waypoint, delta_time)
                print(f"[{self.state}] Mengejar Player | Posisi Enemy: ({self.position.x:.2f}, {self.position.y:.2f})")
        else:
            self.state = "IDLE"
            print(f"[{self.state}] Player berada di luar jangkauan (Jarak: {distance_to_player:.2f})")

# --- Contoh Penggunaan Dalam Simulasi Game Loop ---
enemy = EnemyAI(x=2.0, y=2.0, detection_radius=5.0, speed=3.0)
player_pos = Vector2(5.0, 6.0) # Jarak = 5.0 (Masuk Radius)
dungeon_map = [] # Representasi Map Grid
delta_time = 0.016 # Simulasi ~60 FPS (16.67 ms per frame)

# Jalankan 1 frame update
enemy.update(player_pos, dungeon_map, delta_time)