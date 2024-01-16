from setuptools import setup, find_packages

setup(
    name='code_transformer',
    version='0.1',
    description='Code Transformer',
    author='Daniel Zügner, Tobias Kirschstein, Michele Catasta, Jure Leskovec, Stephan Günnemann',
    author_email='zuegnerd@in.tum.de,kirschto@in.tum.de',
    packages=find_packages(),
    install_requires=[
        "jsonlines==4.0.0", "rouge==1.0.1", "tensorflow>=2.0.0",
        "joblib==1.3.2", "scipy==1.10.1", "networkx<3.0.0", "Pygments==2.15.1",
        "torch==2.1.2", "numpy>=1.17", "jsonpickle==3.0.2", "pandas==2.0.3",
        "tqdm==4.66.1", "transformers==4.36.2", "six==1.16.0",
        "pytest==7.4.4", "PyYAML==6.0.1", "Requests==2.31.0",
        "scikit_learn==1.3.2", "environs==10.3.0", "sacred==0.8.5"
    ],
    zip_safe=False
)
