from setuptools import setup, find_namespace_packages

setup (
    name='clean_folder',
    version='0.1',
    description='Script for sorted files',
    url='https://github.com/anton-serafim/GoIT_PythonCore05/new/main/home_work_7',
    author='Anton Padura',
    license= No License,
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts':['clean-folder = clean_folder.clean:clean_f']})
