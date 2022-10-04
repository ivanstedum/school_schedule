from school_schedule.student import Student
def test_adding_one_class_increases_class_len():
    name= "Ellis"
    grade = "Freshman"
    classes = ["Painting"]
    ellis = Student(name,grade,classes)
    
    ellis.add_class("Pottery")

    assert ellis.classes == ["Painting", "Pottery"]

def test_number_of_classes_returns_correct_amount():
    name= "Alia"
    grade = "Sophomore"
    classes = ["Painting", "Drawing", "Computer Science"]
    alia = Student(name,grade,classes)

    result = alia.get_num_classes()

    assert result == 3

def test_empty_list_returns_0():
    name= "Mariah"
    grade = "Senior"
    classes = []
    mariah = Student(name,grade,classes)

    result = mariah.get_num_classes()

    assert result == 0




