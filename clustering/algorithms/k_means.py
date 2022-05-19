import math
import random
import time
from clustering.utilities.canvas import Canvas
from clustering.utilities.colors import random_color
from clustering.utilities.metric import euclidean_distance

def k_means(points: list[list[float]], number_of_centroids: int, canvas: Canvas = None) -> tuple[list[int], list[list]]:
    min_v = [min(points, key=lambda p: p[i])[i] for i in range(len(points[0]))]
    max_v = [max(points, key=lambda p: p[i])[i] for i in range(len(points[0]))]

    labels: list[int] = []
    colors: list[str] = []
    centroids: list[list[float]] = []
    for _ in range(number_of_centroids):
        colors.append(random_color())
        centroids.append([random.uniform(min_v[i], max_v[i]) for i in range(len(points[0]))])

    position_updated = True

    while position_updated:
        position_updated = False
        labels = []

        points_count: list[int] = []
        new_centroids: list[list[float]] = []
        for _ in range(number_of_centroids):
            points_count.append(0)
            new_centroids.append([0 for _ in range(len(points[0]))])

        for point in points:
            min_distance = math.inf
            centroid_idx = 0

            for idx, centroid in enumerate(centroids):
                distance = euclidean_distance(point, centroid)

                if distance < min_distance:
                    min_distance = distance
                    centroid_idx = idx

            for i in range(len(points[0])):
                new_centroids[centroid_idx][i] += point[i]
            labels.append(centroid_idx)
            points_count[centroid_idx] += 1

        if canvas:
            draw(canvas, min_v, max_v, centroids, points, labels, colors)

        for i in range(number_of_centroids):
            if points_count[i] == 0:
                continue

            for j in range(len(points[0])):
                new_centroids[i][j] /= points_count[i]

            if new_centroids[i] != centroids[i]:
                centroids[i] = new_centroids[i]
                position_updated = True

    return labels, centroids

def draw(canvas: Canvas, min_v: list[float], max_v: list[float], centroids: list[list[float]], points: list[list[float]], labels: list[int], colors: list[str]) -> None:
    centroids = normalize(centroids, min_v, max_v, 0, 400)
    points = normalize(points, min_v, max_v, 0, 400)

    canvas.remove_objects()

    for idx, centroid in enumerate(centroids):
        canvas.add_point(centroid[:2], 4, colors[idx])

    for idx, point in enumerate(points):
        canvas.add_point(point[:2], 1, colors[labels[idx]])

    time.sleep(0.2)

def normalize(points: list[list[float]], min_v: list[float],  max_v: list[float], new_min: float, new_max: float) -> list[list[float]]:
    new_points: list[list[float]] = []
    for point in points:
        new_points.append([new_min + (point[i] - min_v[i])*(new_max - new_min)/(max_v[i] - min_v[i]) for i in range(len(points[0]))])

    return new_points
