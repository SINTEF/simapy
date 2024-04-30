set -e

python setup.py clean --all sdist bdist_wheel

if $PUBLISH_LIB; then
    # Requires that the sima repository is added to the .pypirc file in home folder
    python -m twine upload dist/* --repository sima
    echo "Library published"
else
    echo "Library not published"
fi
