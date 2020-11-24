from setuptools import setup


with open('requirements.txt', 'r') as r:
    requirements = list(map(lambda x: x.strip(), r.readlines()))


setup(
    name="fs-watcher",
    version="0.1.1",
    packages=[
        'fs_watcher'
    ],

    # metadata to display on PyPI
    author="Nico Hanisch",
    author_email="donsprallo@gmail.com",
    description="Simple filesystem watcher",
    license="MIT",
    keywords="file system watcher watchdog",
    install_requires=requirements,

    # cli entry points
    entry_points={
        'console_scripts': [
            'fswatcher=fs_watcher.cli:main'
        ]
    }
)
