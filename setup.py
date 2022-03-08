import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='xgen-klaviyo-sdk',
    version='0.0.1',
    author='Daman Dhillon',
    author_email='damandeep.dhillon@xgen.ai',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/daman-xgen/klaviyo-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'klaviyo-sdk'
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)