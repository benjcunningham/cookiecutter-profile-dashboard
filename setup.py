from setuptools import setup


with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()


extras = {
    "quality": ["black", "flake8", "isort"],
    "testing": ["pytest", "pytest-cookies"],
}

extras["dev"] = extras["quality"] + extras["testing"]

setup(
    name="cookiecutter-profile-dashboard",
    version="0.1.0.dev0",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Cookiecutter template for GitHub profile project dashboards",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/benjcunningham/cookiecutter-profile-dashboard",
    install_requires=["cookiecutter"],
    extras_require=extras,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
)
