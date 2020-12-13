# Docker file for the breast cancer predictor using clinical and anthropometric data project
# Aditya Bhatraju, Anene Ifeanyi, Rahul Kuriyedath, Saule Atymtayeva, 12 Dec 2020.

# Use jupyter/scipy-notebook as the base image
FROM jupyter/scipy-notebook

# Install Python packages
RUN conda install --quiet --yes \
    'ipykernel' \
    'matplotlib>=3.2.2' \
    'scikit-learn>=0.23.2' \
    'pandas>=1.1.3' \
    'requests>=2.24.0' \
    'graphviz' \
    'python-graphviz' \
    'altair>=4.1.0' \
    'jinja2' \
    'pip>=20' \
    'pandas-profiling>=1.4.3' \
    'docopt=0.6.2' \
    'seaborn=0.11' \
    'dataframe_image' \
    'psutil>=5.7.2' \
     'xgboost>=1.*' \
     'lxml'
