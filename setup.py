from distutils.core import setup


setup(
    name='distributed_poker',
    packages=['distributed_poker', 'distributed_poker.server',
              'distributed_poker.client'],
    version='1.0.0',
    license='MIT',
    description='This is a distributed poker game',
    author='Matheus Almeida Santos Anjos <mat.almeida@live.com>, Gabriel Figueredo Goes',
    url='https://github.com/matalmeida/distributed-poker',
    keywords=['distributed', 'poker', 'game'],
    install_requires=[],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)