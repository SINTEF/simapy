set -e

# Clean old distribution files
rm -rf dist build

uv build --all-packages -o dist

if $PUBLISH_LIB; then
    # Requires that the sima repository is added to the .pypirc file in home folder
    uv run twine upload dist/* --repository sima
    echo "Library published"
else
    echo "Library not published"
fi
