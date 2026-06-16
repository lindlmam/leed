import matplotlib.pyplot as plt
import numpy as np

def plot_grid(grid):
    """
    Plots a set of vectors.

    Parameters:
    - vectors (numpy.ndarray): Array of vectors to be plotted.

    Returns:
    - None (displays the plot).
    """

    x_coords, y_coords = grid[:, 0], grid[:, 1]

    fig = plt.figure()
    ax = plt.subplot(111)

    ax.plot(x_coords, y_coords, 'o', label='lattice point', markersize=8)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('lattice')
    ax.legend(loc='upper left', bbox_to_anchor=(0, -0.05), fancybox=True)
    ax.grid(True)

    plt.show()


def plot_both_grids(grid, reciprocal_grid):
    """
    Plots lattice points and reciprocal lattice points in two subplots.

    Parameters:
    - grid (numpy.ndarray): Array representing lattice points. Each row should contain X and Y coordinates.
    - reciprocal_grid (numpy.ndarray): Array representing reciprocal lattice points. Each row should contain X and Y coordinates.

    Returns:
    None

    This function takes two sets of coordinates (lattice points and reciprocal lattice points),
    and plots them in two subplots side by side. The first subplot represents the lattice points,
    and the second subplot represents the reciprocal lattice points. Each point is plotted as a circle ('o')
    with a label, and the subplots are labeled accordingly with axis labels, titles, and legends.
    """
    x_coords_grid, y_coords_grid = grid[:, 0], grid[:, 1]
    x_coords_reciprocal_grid, y_coords_reciprocal_grid = reciprocal_grid[:, 0], reciprocal_grid[:, 1]

    fig = plt.figure()

    ax1 = plt.subplot(121)
    ax1.plot(x_coords_grid, y_coords_grid, 'o', label='lattice point', markersize=8)

    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('Y-axis')
    ax1.set_title('lattice')
    ax1.legend(loc='upper left', bbox_to_anchor=(0, -0.05), fancybox=True)
    ax1.grid(True)

    ax2 = plt.subplot(122)
    ax2.plot(x_coords_reciprocal_grid, y_coords_reciprocal_grid, 'o', label='reciprocal lattice point', markersize=8)

    ax2.set_xlabel('X-axis')
    ax2.set_ylabel('Y-axis')
    ax2.set_title('reciprocal lattice')
    ax2.legend(loc='upper left', bbox_to_anchor=(0, -0.05), fancybox=True)
    ax2.grid(True)

    plt.show()


def plot_image(reciprocal_grid, pixel_size, save_path):

    pixel_range = np.arange(np.floor(np.min(reciprocal_grid)),
                            np.ceil(np.max(reciprocal_grid)) + pixel_size,
                            pixel_size)
    pixel_image = np.zeros((len(pixel_range), len(pixel_range)))
    reciprocal_grid_pixel = np.round(reciprocal_grid / pixel_size) * pixel_size
    reciprocal_grid_pixel_coordinates = ((reciprocal_grid_pixel - np.min(pixel_range)) / pixel_size).astype(int)

    pixel_image[reciprocal_grid_pixel_coordinates[:, 1], reciprocal_grid_pixel_coordinates[:, 0]] = 1

    f = plt.figure()
    plt.imshow(pixel_image, cmap='gray',
               extent=[np.min(pixel_range), np.max(pixel_range), np.min(pixel_range), np.max(pixel_range)])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('LEED Pattern')
    plt.colorbar()
    # plt.show()
    plt.savefig(save_path)
    plt.close(f)

