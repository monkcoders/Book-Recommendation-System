from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "book-recommendation-system"
AUTHOR_USER_NAME = "monkcoders"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Project to recommend books to users using collaborative filtering",
    long_description=long_description,
    long_description_content_type="text/markddown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email= "abhisheksharma46002@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)