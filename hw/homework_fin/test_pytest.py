import pytest
from task1 import*

@pytest.mark.parametrize("subject, grade", [("Математика", 1), ("Математика", 6)])
def test_add_grade_2to5(subject, grade):
    with pytest.raises(ValueError):
        student.add_grade(subject, grade)

@pytest.mark.parametrize("subject, grade", [("Математика", 2.5), ("Математика", "5")])
def test_add_grade_is_int(subject, grade):
    with pytest.raises(ValueError):
        student.add_grade(subject, grade)

@pytest.mark.parametrize("subject, test_score", [("Математика", 0), ("Математика", 101)])
def test_add_grade_1to100(subject, test_score):
    with pytest.raises(ValueError):
        student.add_test_score(subject, test_score)

@pytest.mark.parametrize("subject, test_score", [("Математика", 1.0), ("Математика", "1")])
def test_add_grade_is_int(subject, test_score):
    with pytest.raises(ValueError):
        student.add_test_score(subject, test_score)

def test_correct_subject():
    with pytest.raises(ValueError):
        student.add_grade("Русский", 4)


                
if __name__ == "__main__":
    pytest.main(['-v'])