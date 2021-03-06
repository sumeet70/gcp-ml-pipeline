import setuptools

setuptools.setup(
  name="aweml",
  version="0.0.1",
  install_requires=[
    'apache-beam==2.0.0',
    'numpy==1.13.1',
    'pydicom==0.9.9',
    'scikit-image==0.13.0',
    'scipy==0.19.1',
  ],
  packages=setuptools.find_packages()
)