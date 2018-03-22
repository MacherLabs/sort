from setuptools import setup

setup( 
    name='sort',
    
    version='0.13',
    description='A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences.',
    url='http://demo.vedalabs.in/',

    # Author details    
    author='Atinderpal Singh',
    author_email='atinderpalap@gmail.com',
    
    license='Commercial',

    packages=['sort'],

    install_requires=['numpy', 'numba', 'sklearn', 'scikit-image', 'matplotlib', 'filterpy'],
    zip_safe=False
    )