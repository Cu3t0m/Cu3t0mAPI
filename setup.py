import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="ichs", # Put your username here!
    version="1.7.1", # The version of your package!
    author="Diwan Mohamed Faheer", # Your name here!
    author_email="diwanmohamedfaheer@gmail.com", # Your e-mail here!
    description="A Python module Based on Ilford County High School", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Custom/ichs", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)
