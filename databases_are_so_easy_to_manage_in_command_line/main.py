from sys import argv
from models import *

def create_tables():
    my_models_db.connect()
    my_models_db.create_tables([School, Batch, User, Student, Exercise])

def print_table():
    if len(argv) == 3:
        if argv[2] == "school":
            rows = School.select()
            for row in rows:
                print row
        elif argv[2] == "batch":
            rows = Batch.select()
            for row in rows:
                print row
        elif argv[2] == "user":
            rows = User.select()
            for row in rows:
                print row
        elif argv[2] == "student":
            rows = Student.select()
            for row in rows:
                print row
        elif argv[2] == "exercise":
            rows = Exercise.select()
            for row in rows:
                print row

def insert_record():
    if argv[2] == "school":
        new = School.create(name=argv[3])
        print "New school: " + str(new)
    elif argv[2] == "batch":
        new = Batch.create(chool=argv[3],name=argv[4])
        print "New batch: " + str(new)
    elif argv[2] == "student":
        if len(argv) == 7:
            new = Student.create(
                batch=int(argv[3]),
                age=int(argv[4]),
                last_name=argv[5],
                first_name=argv[6],
            )
        else:
            new = Student.create(
                batch=int(argv[3]),
                age=int(argv[4]),
                last_name=argv[5],
            )
        print "New student: " + str(new)
    elif argv[2] == "exercise":
        new = Exercise.create(
            student = int(argv[3]),
            subject = argv[4],
            note = int(argv[5]),
        )
        print "New exercise: " + str(new)

def delete_tables():
    '''deletes table or prints nothing to delete'''
    if argv[2] == "school":
        q = School.select().where(Schools.id == argv[3])
        if q.exists():
            targ = q.get()
            School.delete().where(School.id == argv[3]).execute()
            print "Delete: %s" % str(targ)
        else:
            print "Nothing to delete"
    elif argv[2] == "batch":
        q = Batch.select().where(Batch.id == argv[3])
        if q.exists():
            targ = q.get()
            Batch.delete().where(Batch.id == argv[3]).execute()
            print "Delete: %s" % str(targ)
        else:
            print "Nothing to delete"
    elif argv[2] == "student":
        q = Student.select().where(Student.id == argv[3])
        if q.exists():
            targ = q.get()
            Student.delete().where(Student.id == argv[3]).execute()
            print "Delete: %s" % str(targ)
        else:
            print "Nothing to delete"
    elif argv[2] == "exercise":
        query = Exercise.select().where(Exercise.id == argv[3])
        if q.exists():
            targ = q.get()
            Exercise.delete().where(Exercise.id == argv[3]).execute()
            print "Delete: %s" % str(targ)

def print_batch_by_school():
    q = (School.select().where(School.id == argv[2]))
    if q.exists():
        data = (Batch.select().where(Batch.school == argv[2]))
        for b in data:
            print b
    else:
        print "School not found"

def print_student_by_batch():
    q = (Batch.select().where(Batch.id == argv[2]))
    if q.exists():
        data = (Student.select().where(Student.batch == argv[2]))
        for stdnt in data:
            print stdnt
    else:
        print "Batch not found"

def print_student_by_school():
    q = (School.select().where(School.id == argv[2]))
    if q.exists():
        data = (Student.select().join(Batch).where(Batch.school == argv[2]))
        for stdnt in data:
            print stdnt
    else:
        print "School not found"

def print_family():
    q = (Student.select().where(Student.last_name == argv[2]))
    for stdnt in query:
        print stdnt

def age_average():
    if len(argv) == 3:
        q = (Student.select(peewee.fn.Avg(Student.age).alias('age_avg')).where(Student.batch == argv[2])).get()
        print q.age_avg
    else:
        q = (Student.select(peewee.fn.Avg(Student.age).alias('age_avg'))).get()
        print q.age_avg

def change_batch():
    student = (Student.select().where(Student.id == argv[2]))
    batch = (Batch.select().where(Batch.id == argv[3]))
    if student.exists():
        student = student.get()
        if batch.exists():
            batch = batch.get()
            print student.batch.id
            if student.batch != batch:
                student.batch = batch
                student.save()
                print "%s has been moved to %s" % (str(student), str(batch) )
            else:
                print "%s already in %s" % (str(student), str(batch) )
        else:
            print "Batch not found"
    else:
        print "Student not found"

def print_all():
    schools = School.select()
    batches = (Batch.select().join(School))
    students = (Student.select().join(Batch))
    exercises = (Exercise.select().join(Student))
    for school in schools:
        print school
        school_batches = batches.where(School.id == school.id)
        for batch in school_batches:
            print '\t' + str(batch)
            batch_students = students.where(Batch.id == batch.id)
            for student in batch_students:
                print '\t\t' + str(student)
                student_exercises = exercises.where(Student.id == student.id)
                for exercise in student_exercises:
                    print '\t\t\t' + str(exercise)

def note_average_by_student():
    query = (Student.select().where(Student.id == argv[2]))
    if query.exists():
        averages = (Exercise
                   .select(Exercise.subject, peewee.fn.Avg(Exercise.note)
                       .coerce(False)
                       .alias('note_avg'))
                   .join(Student)
                   .group_by(Exercise.subject)
                   .where(Exercise.student == argv[2]))
        for average in averages:
            print average.subject + ": " + str(average.note_avg)
    else:
        print "Student not found"

def note_average_by_batch():
    query = (Batch.select().where(Batch.id == argv[2]))
    if query.exists():
        averages = (Exercise.select(Exercise.subject, peewee.fn.Avg(Exercise.note)
                            .coerce(False)
                            .alias('note_avg'))
                    .join(Student)
                    .group_by(Exercise.subject)
                    .where(Student.batch == argv[2]))
        for average in averages:
            print average.subject + ": " + str(average.note_avg)
    else:
        print "Batch not found"

def note_average_by_school():
    query = (School.select().where(School.id == argv[2]))
    if query.exists():
        averages = (Exercise
                    .select(Exercise.subject.alias('subject'),
                            peewee.fn.Avg(Exercise.note)
                            .coerce(False)
                            .alias('note_total'))
                    .join(Student)
                    .join(Batch)
                    .group_by(Exercise.subject)
                    .where(Batch.school == argv[2]))
        for average in averages:
            print average.subject + ": " + str(average.note_total)
    else:
        print "School not found"

def top_batch():
    query = (Batch.select().where(Batch.id == argv[2]))
    if query.exists():
        if len(argv) == 4:
            averages = (Exercise
                        .select(Exercise.subject, Exercise.student, peewee.fn.Avg(Exercise.note)
                                .coerce(False)
                                .alias('note_avg'))
                        .join(Student)
                        .group_by(Exercise.subject, Exercise.student)
                        .where(Exercise.subject == argv[3],
                               Student.batch == argv[2])
                        .order_by(peewee.fn.Avg(Exercise.note).desc()))
            print str(averages[0].student)
        elif len(argv) == 3:
            averages = (Exercise
                        .select(Exercise.student,
                                peewee.fn.Avg(Exercise.note)
                                .coerce(False)
                                .alias('note_avg'))
                        .join(Student)
                        .group_by(Exercise.student)
                        .order_by(peewee.fn.Avg(Exercise.note).desc()))
            print str(averages[0].student)
    else:
        print "Batch not found"

def top_school():
    query = (School.select().where(School.id == argv[2]))
    if query.exists():
        if len(argv) == 4:
            averages = (Exercise
                        .select(Exercise.subject,
                                Exercise.student,
                                peewee.fn.Avg(Exercise.note)
                                .coerce(False)
                                .alias('note_avg'))
                        .join(Student)
                        .join(Batch)
                        .group_by(Exercise.subject, Exercise.student)
                        .where(Exercise.subject == argv[3],
                               Batch.school == argv[2])
                        .order_by(peewee.fn.Avg(Exercise.note).desc()))
            print str(averages[0].student)
        elif len(argv) == 3:
            averages = (Exercise.select(Exercise.subject,Exercise.student,peewee.fn.Avg(Exercise.note)
                                .coerce(False)
                                .alias('note_avg'))
                        .join(Student)
                        .join(Batch)
                        .where(Batch.school == argv[2])
                        .group_by(Exercise.student)
                        .order_by(peewee.fn.Avg(Exercise.note).desc()))
            if averages.exists():
                print str(averages[0].student)
    else:
        print "Batch not found"


if len(argv) < 2:
    print "Please enter an action"
elif argv[1] == "create":
    create_tables()
elif argv[1] == "print":
    print_table()
elif argv[1] == "insert":
    insert_record()
elif argv[1] == "delete":
    delete_tables()
elif argv[1] == "print_family":
    print_family()
elif argv[1] == "age_average":
    age_average()
elif argv[1] == "change_batch":
    change_batch()
elif argv[1] == "print_all":
    print_all()
elif argv[1] == "note_average_by_student":
    note_average_by_student()
elif argv[1] == "note_average_by_batch":
    note_average_by_batch()
elif argv[1] == "print_batch_by_school":
    print_batch_by_school()
elif argv[1] == "print_student_by_batch":
    print_student_by_batch()
elif argv[1] == "print_student_by_school":
    print_student_by_school()
elif argv[1] == "note_average_by_school":
    note_average_by_school()
elif argv[1] == "top_batch":
    top_batch()
elif argv[1] == "top_school":
    top_school()
else:
    print "Undefined action " + argv[1]
