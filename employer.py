import openml

# Settings
python_path = "/home/jhoof/python/python36/bin/python3"
api_path = "/home/jhoof/GridSearcher/cli.py"
config = "#!/bin/sh\n#SBATCH -t 6:00:00 -N=1 --constraint=avx2"

# Default tasks
default_tasks = [146825, 14969, 6, 3, 9978, 15, 37, 22, 18, 16, 29, 32, 2074, 49, 23, 3917, 3021, 9985, 9964, 10101,
                 3481, 3022, 3918, 9952, 3903, 9957, 146800, 3549, 146822, 3902, 146824, 167119, 3573, 146817, 14954,
                 125922, 167120, 167121, 167124, 167125, 31, 14, 28, 43, 53, 11, 2079, 12, 219, 10093, 9981, 9976, 3560,
                 45, 9946, 7592, 9971, 9977, 3904, 9960, 3913, 146819, 167141, 9910, 14952, 146818, 167140, 146820,
                 125920, 146195, 14965, 14970, 146821]

# We want to exclude tasks that have a dimensionality of more than 9 million
excluded_tasks = [
    # Id     # Dataset name             # Dimensionality #
    # ------ # ------------------------ # -------------- #
    9981,    # cnae-9                   # 925560         #
    9976,    # madelon                  # 1302600        #
    167120,  # Numerai28.6              # 2119040        #
    146195,  # Connect-4                # 2904951        #
    9977,    # nomao                    # 4101335        #
    3481,    # isolet                   # 4818546        #
    167125,  # Internet-Advertisements  # 5111961        #
    14970,   # har                      # 5788038        #
    9910,    # Bioresponse              # 6665527        #
    3573,    # Mnist_784                # 54950000       #
    146825,  # Fashion-MNIST            # 54950000       #
    167121,  # Devnagari-Script         # 94300000       #
    167124,  # CIFAR_10                 # 184380000      #
]

# Gather tasks
tasks = [i for i in default_tasks if i not in excluded_tasks]

# Create jobs for each task
for task_id in tasks:
    with open(f"jobs/{task_id}.sh", "w+") as f:
        description = f"{config}\n{python_path} {api_path} {task_id}"
        f.write(description)
