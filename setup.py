# example Cobaya external likelihood package, here just a simple H0 prior

from setuptools import setup

setup(name="test_package",
      version='1.0',
      description='Example external Cobaya likelihood package',
      zip_safe=True,  # set to false if you want to easily access bundled package data files
      packages=['test_package', 'test_package.sub_module', 'test_package.tests'],
      package_data={'test_package': ['*.yaml'],
                    'test_package.sub_module': ['*.yaml']},
      install_requires=['cobaya (>=2.0.5)'],
      test_suite='test_package.tests',
      )
