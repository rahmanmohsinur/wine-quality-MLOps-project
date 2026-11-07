
from pathlib import Path
from setuptools import setup, find_packages


# Project metadata
__version__ = "0.1.0"

SRC_REPO = "mlProject"

AUTHOR_USER_NAME = "rahmanmohsinur"
AUTHOR_EMAIL = "rahmanmohsinur@gmail.com"

REPO_NAME = "wine-quality-MLOps-project"


# Read README
ROOT_DIR = Path(__file__).parent

with open(ROOT_DIR / "README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=SRC_REPO,
    version=__version__,

    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,

    description="End-to-end Wine Quality Prediction ML project",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    project_urls={
        "Bug Tracker": (
            f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        ),
    },

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    # python_requires=">=3.11",
    
    # install_requires=[
    #     "pandas",
    #     "numpy",
    #     "scikit-learn",
    #     "mlflow",
    #     "PyYAML",
    #     "python-box==6.0.2",
    #     "ensure==1.0.2",
    #     "joblib",
    #     "tqdm",
    # ],
)
