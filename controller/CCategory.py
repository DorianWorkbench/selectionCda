from model.Category import Category

def creationCategory(request):
    label = request.form.get('label')

    return Category.creationCategorie(label)
