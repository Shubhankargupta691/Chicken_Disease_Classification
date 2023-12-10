import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.1"

REPO_NAME = "Chicken_Disease_Classification"
AUTHOR_USER_NAME= "Shubhankargupta691"
SRC_REPO = "Chicken_Disease_Classification"
AUTHOR_Email = "shubhankrgupta691@gmail.com"
CREDIT_USER_NAME= "entbappy"

setuptools.setup(
    name=SRC_REPO ,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_Email,
    description= "Python Package for CNN app",
    long_description=long_description, 
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    credit_url=f"https://github.com/{CREDIT_USER_NAME}",
    project_urls={
            
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)