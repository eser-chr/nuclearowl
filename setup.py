from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


def parse_requirements(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

requirements = parse_requirements('requirements.txt')


setup(
    name="nuclearowl",  # Replace with your package name
    version="0.1.0",  # Initial release version
    description="A lib handling nuclear imaging data and Ai applications on top of it",  # Brief description of your package
    long_description=long_description,  # Use the README.md file as the long description
    long_description_content_type="text/markdown",  # Make sure this matches the format of your README file
    url="https://github.com/MarkusStefan/NUKMED-AI",  # URL to the project's homepage or repository
    author="NUMED TEAM",  # Replace with your name
    author_email="clemens.spielvogel@meduniwien.ac.at",  # Replace with your email
    license="MIT",  # License type (e.g., MIT, GPLv3, etc.)
    classifiers=[  # Classifiers help users find your project by categorizing it
        "Development Status :: 3 - Alpha",  # Example: Alpha, Beta, Stable
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="nuclear imaging, medical imaging, python, AI(wow), segmentation",  # Add relevant keywords
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),  # Automatically find your packages
    python_requires=">=3.7",  # Minimum Python version required
    install_requires=requirements,
    package_data={  # Include additional files into the package
        "": ["data/*.dat"],  # Example of including data files
    }
)
