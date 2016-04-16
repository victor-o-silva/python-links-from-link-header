from distutils.core import setup

with open('README.rst', 'r') as readme_file:
    readme_txt = readme_file.read()

setup(
    name='links-from-link-header',
    packages=['links_from_header'],
    version='0.1.0',
    description='Python module that extracts links and their relations '
                'from a Link Header Field and returns them in a dict.',
    long_description=readme_txt,
    author='Victor Oliveira da Silva',
    author_email='victor_o_silva@hotmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/victor-o-silva/python-links-from-link-header',
)
