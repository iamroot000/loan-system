import pkgutil

# Set the path to the directory containing the packages
path = '/Users/nikkoreiaratan/workspace-rei/django-workspace/test-project/backend_loansystem'

# Use pkgutil to iterate over all the packages in the directory
for package in pkgutil.iter_modules([path]):
    print(package.name)
    