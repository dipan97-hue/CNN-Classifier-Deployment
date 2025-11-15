import setuptools
with open('Readme.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'
REPO_NAME ='CNN-Classifier-Deployment'
Source_Repo = 'cnnClassifier'
Author_username = 'dipan97-hue'
Author_email ='dipanbanerjee97@gmail.com'

setuptools.setup(
    name= Source_Repo,
    version=__version__,
    author=Author_username,
    author_email=Author_email,
    description='A python package for cnn classification',
    long_description=long_description,
    url = f"https:github.com/{Author_username}/{Source_Repo}/issues",
    long_description_content_type='text/markdown',
    project_url = {
        'Bug Tracker': f'https:github.com/{Author_username}/{Source_Repo}/issues'
    },
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where='src')
)