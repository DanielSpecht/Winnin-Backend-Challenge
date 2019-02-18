#from distutils.core import setup
from setuptools import setup
setup(name='winnin_backend_challenge',
      version='1.0',
      packages=['winnin_backend_challenge'],
      install_requires=['Flask==1.0.2', 'flask-restful-swagger-2==0.35','requests==2.21.0','pytz==2018.9','peewee==3.8.2','apscheduler==3.5.3'],
      #install_requires=['pysqlite3', 'Flask', 'flask-restful-swagger-2','requests','pytz','peewee','apscheduler'],
      
      test_suite='tests',
      tests_require=['unittest'],

      author='Daniel Specht Menezes',
      author_email='danielssmenezes@gmail.com',
      license='MIT')