from distutils.core import setup

setup(
  name = 'pzgram',
  packages = ['pzgram'],
  version = '0.2',
  description = 'A pz-way to create your telegram bot',
  author = 'Giovani Casari',
  author_email = 'casari.giovanni@gmail.com',
  url = 'https://github.com/infopz/pzgram',
  download_url = 'https://github.com/infopz/pzgram/archive/0.2.tar.gz',
  license = 'LICENSE.txt',
  install_requires = ["requests >= 2.18.4"],
  keywords = ['telegram', 'telegram-bot', 'telegram-api'],
  classifiers = [],
)
