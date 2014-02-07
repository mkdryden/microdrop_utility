from distutils.core import setup


setup(name='microdrop_utility',
      version='0.0.1',
      description='Utility functions and classes for MicroDrop, which might '
      'be potentially useful in other projects.',
      keywords='microdrop dropbot utility',
      author='Christian Fobel and Ryan Fobel',
      url='http://github.com/cfobel/microdrop_utility.git',
      license='GPL',
      packages=['microdrop_utility', 'microdrop_utility.gui',
                'microdrop_utility.tests'])
