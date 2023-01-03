import os
import subprocess

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

seeds_dir = os.path.join(os.path.dirname(__file__), 'seeds')

paths = ['projects']

for path in paths:
    seed = os.path.join(seeds_dir, path, 'seed.py')
    cmd = 'python {}'.format(seed)
    print('{}Seeding {}{}...'.format(COLOR_GREEN, path, COLOR_END))
    subprocess.call(cmd, shell=True)
