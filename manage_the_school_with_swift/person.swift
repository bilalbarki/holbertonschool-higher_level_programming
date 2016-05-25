class Person:CustomStringConvertible{
    var first_name:String
    var last_name:String
    var age:Int
    
    //initialization for Person class
    init(first_name: String, last_name: String, age: Int){
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    
    //returns full name
    func fullName() -> String{
        return "\(first_name) \(last_name)"
    }
    
    //returns a string for printing if print call is made for a Person object
    var description:String{
        return self.fullName()
    }
}

//protocol for Student and Mentor
protocol Classify{
    func isStudent() -> Bool
}

//defines subjects
enum Subject{
    case Math
    case English
    case French
    case History
}

class Mentor:Person, Classify{
    let subject: Subject
    
    //initialization for mentor class
    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math){
        self.subject = subject
        super.init(first_name:first_name, last_name:last_name, age:age)
    }
    
    //returns subject name
    func stringSubject() -> String{
        switch subject{
            case .Math: return "Math"
            case .English: return "English"
            case .French: return "French"
            case .History: return "History"
        }
        
    }
    
    //returns true if a person is a student
    func isStudent() -> Bool{
        return false
    }
    
}

class Student:Person, Classify{
    //returns true of a person is a student
    func isStudent() -> Bool{
        return true
    }
    
    var list_exercises: ([Exercise]!) = []
    
    //adds new note
    func addNewNote(subject: Subject, note: Int = 0){
        let new_exercise=Exercise(subject: subject)
        new_exercise.setNote(note)
        self.list_exercises.append(new_exercise)
    }
    
    //returns subject average of a student
    func average(subject: Subject) -> Float{
        var total = 0
        var count = 0
        for exercise in list_exercises{
            if (exercise.subject == subject){
                total += exercise.note
                count += 1
            }
        }
        if (count != 0){
            return (Float)(total) / (Float)(count)
        }
        return 0
    }
    
    //returns average of all notes of a student
    func averageAll() -> Float{
        var total = 0
        var count = 0
        for exercise in list_exercises{
            total += exercise.note
            count += 1
        }
        if (count != 0){
            return (Float)(total) / (Float)(count)
        }
        return 0
    }
}

class School{
    var name:String
    var list_persons:[Person] = []
    
    //initialization function for School
    init(name: String){
        self.name = name
    }
    
    //adds a student to list_persons
    func addStudent(p: Person) -> Bool{
        if (p is Student){
            list_persons.append(p)
            return true
        }
        return false
    }
    
    //adds a mentor to list_persons
    func addMentor(p: Person) -> Bool{
        if (p is Mentor){
            list_persons.append(p)
            return true
        }
        return false
    }
    
    //returns a list of Students
    func listStudents() -> [Person]{
        var student_list:[Person] = []
        for person in list_persons{
            if person is Student{
                student_list.append(person)
            }
        }
        return student_list.sort({$0.age > $1.age})
    }
    
    //returns a list of Mentors
    func listMentors() -> [Person]{
        var mentor_list:[Person] = []
        for person in list_persons{
            if person is Mentor{
                mentor_list.append(person)
            }
        }
        return mentor_list.sort({$0.age > $1.age})
    }
    
    //returns an array of Persons with mentor list having Subject passed as argument
    func listMentorsBySubject(subject:Subject) -> [Person]{
        var mentor_list_by_subject:[Person] = []
        for person in list_persons{
            let mentor = person as? Mentor
            if (mentor != nil && mentor!.subject == subject){
                mentor_list_by_subject.append(person)
            }
        }
        return mentor_list_by_subject
    }
    
    //returns average age of mentors
    func mentorsAgeAverge() -> Int{
        let mentors = self.listMentors()
        var total = 0
        var count = 0
        for mentor in mentors{
            total+=mentor.age
            count+=1
        }
        if (count != 0){
            return total / count
        }
        return 0
    }
    
    //returns average age of students
    func studentsAgeAverge() -> Int{
        let students = self.listStudents()
        var total = 0
        var count = 0
        for student in students{
            total+=student.age
            count+=1
        }
        if (count != 0){
            return total / count
        }
        return 0
    }
    
    //returns average of a particular subject
    func average(subject: Subject) -> Float{
        let students = self.listStudents()
        var total:Float = 0
        var count:Float = 0
        for student in students{
            if let st = student as? Student{
                total += st.average(subject)
                count+=1
            }
        }
        if (count != 0){
            return total / count        }
        return 0
    }
    
    //returns average of all students
    func averageAll() -> Float{
        let students = self.listStudents()
        var total:Float = 0
        var count: Float = 0
        for student in students{
            if let st = student as? Student{
                total += st.averageAll()
                count+=1
            }
        }
        if (count != 0){
            return total / count
        }
        return 0
    }
}

//Exercise class
class Exercise{
    var subject:Subject
    var note:Int
    
    //initialization of subject
    init(subject: Subject){
        self.subject = subject
        note = 0
    }
    
    //Note setter
    func setNote(note: Int){
        if (note<0 || note>10){
            self.note=0
        }
        else{
            self.note=note
        }
    }
}