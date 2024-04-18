import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "Abhishek6360"
SRC_REPO = "textSummarization"
AUTHOR_EMAIL = "abhishekr4532@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small Python package that",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/abhishek6360/Text_Summarization",
    project_urls={
        "Bug tracker": f"https://github.com/abhishek6360/Text_Summarization/issues",
        
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    
)