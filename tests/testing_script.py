import messy_project.src.utils.basic_maths_operations as basic_maths_operations

def test_add():
    assert basic_maths_operations.Add(2, 3) == 5

def test_sub():
    assert basic_maths_operations.subTract(5, 3) == 2
