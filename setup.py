from setuptools import setup, find_packages

setup(
    name="django-schema-history",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["django>=3.0"],
    include_package_data=True,
    license="MIT",
    description="A Django package to track model schema changes (added/removed/modified fields).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/moundher122/django-schema-history",
    author="moundher bouroumana",
    author_email="bouorumanamoundher@gmail.com",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
