## Build


The project uses the [Sphinx](https://www.sphinx-doc.org/en/master/) project to build the package documentation.  The documentation is built automatically as part of the development pipeline and published to the branch private repository.  However, to build the documentation locally, one could perform something of the form:

1. Change into the local project folder

    ```shell
    user@host$ cd /some/path/package/
    user@host$
    ```

1. Install the necessary Python dependencies

    ```shell
    user@host$ ./env/Scripts/python -m pip install helloworld[docs]
    user@host$
    ```

1. *If necessary*, automatically build any new [api documentation](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)

    ```shell
    user@host$ ./env/Scripts/sphinx-apidoc -o ./docs/src ./helloworld --force
    user@host$
    ```

1. [Build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) the documentation

    ```shell
    user@host$ ./env/Scripts/sphinx-build -b html ./docs/src ./docs/sphinx-html/
    user@host$
    ```

1. Review the docs

   Open the `./docs/sphinx-html/index.html` in your preferred web browser
