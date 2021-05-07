from setuptools import setup

setup(
    name='{{cookiecutter.project_name}}',
    version='0.1.0',    
    # scripts=['{{cookiecutter.project_name}}'],
    description='{{cookiecutter.project_description}}',
    url='{{cookiecutter.project_github}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    license='{{cookiecutter.license}}',
    packages=['{{cookiecutter.project_name}}'],
    install_requires=['',
                      '',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Starting',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: {{cookiecutter.license}}',  
        'Operating System :: POSIX :: {{cookiecutter.operating_system}}',        
        'Programming Language :: Python :: {{cookiecutter.python_version}}',
    ],
)