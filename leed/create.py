import numpy as np

def generate_lattice_vectors(lattice_type, length_range, theta_range):
    """
    Generates lattice vectors based on the specified lattice type and parameter ranges.

    Parameters:
    - lattice_type (str): Type of lattice ('mp', 'hp', 'tp', 'op', 'oc').
    - length_range (tuple): Range for generating lengths 'a' and 'b'.
    - theta_range (tuple): Range for generating the angle 'theta' in degrees.

    Returns:
    - lattice_vectors (numpy.ndarray): 2D array representing the lattice vectors.
    """
    while True:
        a = np.random.uniform(*length_range)
        b = np.random.uniform(*length_range)
        theta = np.random.uniform(*theta_range)

        # Check if the generated parameters satisfy the lattice type conditions
        if lattice_type == 'mp':
            if a != b and theta != 90:
                theta_rad = np.radians(theta)
                lattice_vectors = np.array([[a, 0], [b * np.cos(theta_rad), b * np.sin(theta_rad)]])
                break

        elif lattice_type == 'hp':
            b = a
            theta = 120
            theta_rad = np.radians(theta)
            lattice_vectors = np.array([[a, 0], [b * np.cos(theta_rad), b * np.sin(theta_rad)]])
            break

        elif lattice_type == 'tp':
            b = a
            lattice_vectors = np.array([[a, 0], [0, b]])
            break

        elif lattice_type == 'op':
            if a != b:
                lattice_vectors = np.array([[a, 0], [0, b]])
                break

        elif lattice_type == 'oc':
            print('not defined')

        else:
            raise ValueError("Invalid lattice type. Available lattice_type: 'mp', 'hp', 'tp', 'op', 'oc'.")

    return lattice_vectors


def convert_to_reciprocal(lattice_vectors):
    """
    Converts lattice vectors to reciprocal lattice vectors.

    Parameters:
    - lattice_vectors (numpy.ndarray): 2x2 matrix representing the lattice vectors.

    Returns:
    - reciprocal_vectors (numpy.ndarray): 2x2 matrix representing the reciprocal lattice vectors.
    """
    a_1 = lattice_vectors[0, :]
    a_2 = lattice_vectors[1, :]

    R = np.array([[0, -1], [1, 0]])

    b_1 = 2 * np.pi * (R @ a_2) / (a_1 @ R @ a_2)
    b_2 = 2 * np.pi * (R @ a_1) / (a_1 @ R @ a_2)

    reciprocal_vectors = np.array([b_1, b_2])
    return reciprocal_vectors



def generate_grid(lattice_vectors, num_repetitions):
    """
    Generates a grid (set of vectors) based on the given lattice vectors and repetition count.

    Parameters:
    - lattice_vectors (numpy.ndarray): 2x2 matrix representing the lattice vectors.
    - num_repetitions (int): Number of repetitions for the pattern.

    Returns:
    - grid (numpy.ndarray): Array of vectors based on the specified pattern.
    """
    # Initialize the vectors list
    grid = []

    # Generate vectors based on the specified pattern
    for i in np.arange(-num_repetitions, num_repetitions + 1):
        for j in np.arange(-num_repetitions, num_repetitions + 1):
            grid.append(j * lattice_vectors[0, :] + i * lattice_vectors[1, :])

    return np.array(grid)
