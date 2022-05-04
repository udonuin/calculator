import setuptools

setuptools.setup (
  include_package_date = True,
  name='calculator',
  version='0.0.1',
  description='oss-dev calculator',
  author='udonuin',
  author_email='jihwang@donga.ac.kr',
  url = "https://github.com/udonuin/calculator",
  download_url = ""
  install_requires=['pytest'], #관련라이브러리
  long_description = 'oss-dev calculator python module',
  long_description_content = 'text/markdown',
  classifiers=[ #패키지가 어느 범주에 들어가는지 자동 할당 (패키지)
    "Programming Language :: python :: 3",
    "Operating System :: OS Independent",
  ],
)
