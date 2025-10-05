"""
Setup script for Learner Engagement Clustering Analysis
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('-'):
            requirements.append(line)

setup(
    name="learner-engagement-clustering",
    version="1.0.0",
    author="Loyanganba Ngathem",
    author_email="loyanganba.ngathem@gmail.com",
    description="A comprehensive machine learning pipeline for analyzing learner engagement patterns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoyaNg-rgb/learner-engagement-clustering",
    project_urls={
        "Bug Tracker": "https://github.com/LoyaNg-rgb/learner-engagement-clustering/issues",
        "Documentation": "https://github.com/LoyaNg-rgb/learner-engagement-clustering#readme",
        "Source Code": "https://github.com/LoyaNg-rgb/learner-engagement-clustering",
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "pylint>=2.17.0",
            "mypy>=1.3.0",
        ],
        "notebook": [
            "jupyter>=1.0.0",
            "ipython>=8.12.0",
            "notebook>=6.5.4",
        ],
        "all": [
            "pytest>=7.3.0",
            "black>=23.0.0",
            "jupyter>=1.0.0",
            "tqdm>=4.65.0",
            "statsmodels>=0.14.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "learner-clustering=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "machine-learning",
        "clustering",
        "education",
        "learning-analytics",
        "data-science",
        "kmeans",
        "learner-engagement",
        "educational-data-mining",
    ],
    zip_safe=False,
)
