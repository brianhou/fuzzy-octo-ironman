from setuptools import setup

setup(
    name='simple-server',
    version='v0.1.0',
    description='A version-independent HTTP server.',
    url='https://github.com/brianhou/fuzzy-octo-ironman',
    author='Brian Hou',
    packages=['simple_server'],
    entry_points={
        'console_scripts': [
            'pyserve=simple_server.__init__:main',
        ],
    },
)
