from k_means import KMeans
import matplotlib.image as img
import numpy as np


def main():
    image = img.imread("sample_img1.png")
    colors = np.zeros((image.shape[0] * image.shape[1], image.shape[2]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            colors[i * image.shape[1] + j] = image[i][j]
    termination_condition_threshold = 0.01
    k_array = [2, 4, 16, 32, 64]
    for k in k_array:
        k_means = KMeans(colors, k)
        k_means.start(termination_condition_threshold)
        output = np.zeros((image.shape[0], image.shape[1], image.shape[2]))
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                output[i][j] = k_means.clusters.get_center(k_means.data.memberships[i * image.shape[1] + j])
        img.imsave(f"output{k}.png", output)


if __name__ == '__main__':
    main()
