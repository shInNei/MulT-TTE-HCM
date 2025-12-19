import pandas as pd
import math
import ast  # để parse chuỗi dạng "[[lon, lat], [lon, lat], ...]"

# === Cấu hình ===
csv_path = "train.csv"
column_name = "POLYLINE"   # cột chứa danh sách tọa độ

# === Hàm tính khoảng cách haversine (mét) ===
def haversine(lon1, lat1, lon2, lat2):
    R = 6371000  # bán kính Trái đất (m)
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# === Biến tổng ===
total_distance = 0.0
total_segments = 0
chunk_size = 10000  # tăng lên nếu RAM dư (ví dụ 50000)

# === Đọc theo từng phần nhỏ ===
for chunk in pd.read_csv(csv_path, usecols=[column_name], chunksize=chunk_size):
    for poly_str in chunk[column_name].dropna():
        try:
            # Chuyển chuỗi "[[lon, lat], [lon, lat], ...]" thành list thực
            coords = ast.literal_eval(poly_str)
            if not isinstance(coords, list) or len(coords) < 2:
                continue

            # Tính khoảng cách giữa các cặp điểm liên tiếp
            for i in range(len(coords) - 1):
                lon1, lat1 = coords[i]
                lon2, lat2 = coords[i + 1]
                total_distance += haversine(lon1, lat1, lon2, lat2)
                total_segments += 1

        except Exception:
            # bỏ qua dòng lỗi parse (ví dụ chuỗi hỏng)
            continue

# === Kết quả ===
if total_segments > 0:
    avg_dist = total_distance / total_segments
    print(f"📏 Khoảng cách trung bình giữa hai điểm liên tiếp: {avg_dist:.2f} mét")
else:
    print("⚠️ Không có dữ liệu hợp lệ để tính toán.")
