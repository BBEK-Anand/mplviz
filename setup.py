from setuptools import setup, find_packages

setup(
    name='mlpviz',
    version='0.1.0',
    description='A fluent wrapper around matplotlib for easy, expressive visualizations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BBEK-Anand',
    url='https://github.com/BBEK-Anand/mlpviz',  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'matplotlib>=3.0.0',
        'numpy>=1.18.0',
        'ipython>=7.0.0'  
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Visualization',
        'Framework :: Matplotlib',
    ],
    python_requires='>=3.7',
)
