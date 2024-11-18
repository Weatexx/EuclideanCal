def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def getPoints():
    points = []
    n = int(input("Kaç adet nokta girileceğini yazınız"))
    for i in range(n):
        print(f"Nokta {i + 1}:")
        x = float(input("x koordinatını giriniz:"))
        y = float(input("y koordinatını giriniz:"))
        points.append((x, y))
    return points

def main():
    points = getPoints()
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):  
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)

    if distances:  
        min_distance = min(distances)
        print("\n Hesaplanan Mesafe:", distances)
        print("Minimum Mesafe:", min_distance)
    else:
        print("Mesafe Hesabı için yeterince nokta girmediniz!")
if __name__ == "__main__":
    main()
