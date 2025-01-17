from setuptools import setup, find_packages

setup(
    name='django-likes',
    version='0.2.1',
    description='Django app providing view interface to django-secretballot.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-likes',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django-secretballot',
    ],
    tests_require=[
        'django-setuptest>=0.1.4',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
