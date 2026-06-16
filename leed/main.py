from create import *
from plot import *

import os
from tqdm import tqdm

amount_per_type = 1
percentage_of_training = 0.8

# Test
lattice_types = ['mp', 'hp', 'tp', 'op']    # 'oc'
length_range = (1, 2)   # encountered problems with (1,5)
theta_range = (50, 80)  # encountered problems with (0,90)
num_repetitions = 3
pixel_size = 0.1
# lattice_vectors = np.array([[1, 0], [0.5, 1]])


base_folder = 'data'
for set_type in ['train_data', 'test_data']:
    for lattice_type in lattice_types:
        folder_path = os.path.join(base_folder, set_type, lattice_type)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

for ii in tqdm(range(1, 101), ncols = 100, desc ="Creating Data"):
    if ii < 100 * percentage_of_training:
        set_type = 'train_data'
    else:
        set_type = 'test_data'

    for lattice_type in lattice_types:
        save_folder_path = os.path.join(base_folder, set_type, lattice_type)

        for identification_number in range(amount_per_type):
            save_name = lattice_type + '_' + str(ii) + '_' + str(identification_number)
            save_path = save_folder_path + '/' + save_name

            lattice_vectors = generate_lattice_vectors(lattice_type, length_range, theta_range)
            reciprocal_lattice_vectors = convert_to_reciprocal(lattice_vectors)

            grid = generate_grid(lattice_vectors, num_repetitions)
            reciprocal_grid = generate_grid(reciprocal_lattice_vectors, num_repetitions)

            # plot_both_grids(grid, reciprocal_grid)
            # print(save_path)
            plot_image(reciprocal_grid, pixel_size, save_path)








