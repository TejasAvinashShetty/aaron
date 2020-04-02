from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='aaron',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="evenly split amounts as far as possible",
    license="GNUv3",
    author="Tejas Avinash Shetty",
    author_email='tejasshetty.1808@gmail.com',
    url='https://github.com/TejasAvinashShetty/aaron',
    packages=['aaron'],
    entry_points={
        'console_scripts': [
            'aaron=aaron.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='aaron',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
