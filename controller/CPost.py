from model.Post import Post

def creationPost(request):
    content = request.form.get('content')
    idTopic = request.form.get('idTopic')
    idUser = request.form.get('idUser')

    return Post.creationPost(content, idTopic, idUser)

def listePost(request):
    idTopic = request.form.get('idTopic')

    return Post.listePost(idTopic)

def suppressionPost(request):
    idPost = request.form.get('idPost')

    return Post.suppressionPost(idPost)

def miseAjourPost(request):
    idPost = request.form.get('idPost')
    content = request.form.get('content')
    return Post.miseAjourPost(idPost, content)