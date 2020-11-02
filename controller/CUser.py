from model.User import User

def ajouterUtilisateur(request):
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        birthDate = request.form.get('birthDate')

        User.ajouterUtilisateur(email, password, birthDate)

        return True

    except:
        return False