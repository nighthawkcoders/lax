import markdown

@app_notes.route('/notes')
@login_required
def notes():
    ### see complete details below

    return render_template('notes.html', user=user, notes=list_notes)


user = uo.read()  # extract user record (Dictionary)
for note in uo.notes:  # loop through each user note
    note = note.read()  # extract note record (Dictionary)
    note['note'] = markdown.markdown(note['note'])  # convert text, markdown, etc to html
    list_notes.append(note)  # prepare note list for render_template

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    # Define the Users schema
    userID = db.Column(db.Integer, primary_key=True)

    #### see below for full definition

    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    notes = db.relationship("Notes", cascade='all, delete', backref='users', lazy=True)

class Notes(db.Model):
    __tablename__ = 'notes'

    #### see below for full definition
    # Defines ForeignKey, in this case userID is the one who created the note
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))

