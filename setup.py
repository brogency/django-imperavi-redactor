import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-materials-extension",
    version="0.0.1",
    author="Anton Petrov",
    author_email="anton.petrov@bro.agency",
    description="A materials extension application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brogency/django-materials-extension",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)