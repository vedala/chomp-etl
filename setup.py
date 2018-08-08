import setuptools

setuptools.setup(
    name="chomp_etl",
    version="0.0.1",
    author="Kalyan Vedala",
    author_email="svedala23@gmail.com",
    description="Chomp ETL",
    long_description="A command-line ETL program.",
    long_description_content_type="text/markdown",
    url="https://github.com/vedala/chomp-etl",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ),
)
