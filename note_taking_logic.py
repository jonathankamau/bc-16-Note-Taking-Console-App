from sqlalchemy.orm import Session
from database import Notes, create_db, Base

class Note():
	
	def create_note(self, note_content):
		self.note_content = note_content
		note = Notes(note_content = self.note_content)
		engine = create_db()
		Base.metadata.bind = engine
		session = Session()
		session.add(note)
		session.commit()
	
	def view_note(self, note_id):
		self.note_id = note_id
		session = Session()
		result = session.query(Notes).filter_by(note_id = note_id).first()
		print ("Id: " + str(result.note_id) + " Content: " + result.note_content)

	def view_all_notes(self):
		session = Session()
		result = session.query(Notes).all()
		print(result)
		for item in result:
			print ("Id: " + str(item.note_id) + " Content: " + item.note_content)

	def delete_note(self, note_id):
		self.note_id = note_id
		session = Session()
		session.query(Notes).filter_by(note_id = note_id).first()
		deleted = session.delete(note_id)
		print (deleted)


notes = Note()
notes.create_note('lfuhkf;jpi;')

# notes.create_note("today is Tuesday")
first_1 = Note()
first_1.view_note(1)
# Note.view_note(1)
# print(note.note_content)
all_notes = Note()
all_notes.view_all_notes()

delete_1 = Note()
delete_1.delete_note(2)

