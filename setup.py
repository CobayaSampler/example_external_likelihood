# example Cobaya external likelihood package, here just a simple H0 prior

from setuptools import setup

setup(name="test_package",
      version='1.0',
      description='Example external Cobaya likelihood package',
      zip_safe=True,  # set to false if you want to easily access bundled package data files
      packages=['test_package', 'test_package.sub_module'],
      package_data={'test_package': ['test_like.yaml'],
                    'test_package.sub_module': ['test_like2.yaml']},
      install_requires=['cobaya (>=2.0.3)']
      )
