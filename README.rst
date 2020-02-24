===============
kcrw.apple_news
===============

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/kcrw.apple_news.svg
        :target: https://pypi.python.org/pypi/kcrw.apple_news

.. image:: https://img.shields.io/travis/alecpm/kcrw.apple_news.svg.svg
        :target: https://travis-ci.com/alecpm/kcrw.apple_news

.. image:: https://readthedocs.org/projects/kcrw.apple-news/badge/?version=latest
        :target: https://kcrw.apple-news.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/KCRW-org/kcrw.apple-news/shield.svg
     :target: https://pyup.io/repos/github/KCRW-org/kcrw.apple-news/
     :alt: Updates

``kcrw.apple_news`` is a simple library for using the `Apple News API`_ from Python 2 or 3 (>= 2.7 or >= 3.5).


* Free software: MIT license
* Documentation: https://kcrw.apple-news.readthedocs.io.


Features
--------

* Provides support for making signed API requests to the Apple News Publisher API
* Includes suport for "Read Channel", "Create Article", "Update Article",
  "Read Article Information", "Delete Article" API calls as well making generic
  signed requests.
* Provides a command line tool ``apple_news_api`` for making API calls directly.


.. _Apple News API: https://developer.apple.com/documentation/apple_news/apple_news_api
