from distutils.core import setup

try:
  with open("README.md","r") as fh:
    long_description = fh.read()
except:
  long_description = 'Python101'

setup(
  name = 'python101',         # How you named your package folder (MyLib)
  packages = ['python101'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Basic Python in Lao',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type = "text/markdown",
  author = 'LanuxOS',                   # Type in your name
  author_email = 'lanuxos@gmail.com',      # Type in your E-Mail
  # Provide either the link to your github or to your website
  url='https://github.com/lanuxos/python101',
  # I explain this later on
  download_url='https://github.com/lanuxos/python101/archive/refs/heads/main.zip',
  keywords = ['python', '101', 'basic python', 'lao', 'la', 'lanuxos'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
