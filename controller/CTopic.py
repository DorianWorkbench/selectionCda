from model.Topic import Topic

def creationTopic(request):
    title = request.form.get('title')
    idCategory = request.form.get('idCategory')
    idUser = request.form.get('idUser')

    return Topic.creationTopic(title, idCategory, idUser)

def supressionTopic(request):
    idTopic = request.form.get('idTopic')

    return Topic.supressionTopic(idTopic)

def miseAjourTopic(request):
    title = request.form.get('title')
    idTopic = request.form.get('idTopic')

    return Topic.miseAjourTopic(idTopic, title)

def listeTitreTopic():
    return Topic.listeTitreTopic()
