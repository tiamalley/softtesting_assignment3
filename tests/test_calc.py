from app.py import calc_bmi, categoryBMI
from contextlib import redirect_stdout
from io import StringIO


# tests to make sure BMI is calculated correctly
def test_calculate_bmi():
    assert calc_bmi(67, 110) == 17.6    # underweight
    assert calc_bmi(63, 125) == 22.7    # normal
    assert calc_bmi(61, 150) == 29.0    # overweight
    assert calc_bmi(61, 250) == 48.4    # obese
    

### tests for underweight boundary (<18.5)
# test for underweight interior point (15.0)
def test_category_underweight_interior():
    assert categoryBMI(15.0) == 'Underweight'

# test for underweight OFF POINT (18.4)
def test_category_underweight_OFF():
    assert categoryBMI(18.4) == 'Underweight'

# test for underweight ON POINT (18.5)
def test_category_underweight_ON():
    assert categoryBMI(18.5) == 'Normal Weight'


### tests for normal weight boundaries (>=18.5 and <25.0)
# test for normal weight lower boundary OFF POINT (18.4)
def test_category_normal_lower_OFF():
    assert categoryBMI(18.4) == 'Underweight'

# test for normal weight lower boundary ON POINT (18.5)
def test_category_normal_lower_ON():
    assert categoryBMI(18.5) == 'Normal Weight'

# test for normal weight interior point (20.0)
def test_category_normal_interior():
    assert categoryBMI(20.0) == 'Normal Weight'

# test for normal weight upper boundary OFF POINT (24.9)
def test_category_normal_upper_OFF():
    assert categoryBMI(24.9) == "Normal Weight"

# test for normal weight upper boundary ON POINT (25.0)
def test_category_normal_upper_ON():
    assert categoryBMI(25.0) == "Overweight"


### tests for overweight boundaries (>=25.0 and <30.0)
# test for overweight lower boundary OFF POINT (24.9)
def test_category_over_lower_OFF():
    assert categoryBMI(24.9) == "Normal Weight"

# test for overweight lower boundary ON POINT (25.0)
def test_category_over_lower_ON():
    assert categoryBMI(25.0) == "Overweight"

# test for overweight interior point (27.2)
def test_category_over_interior():
    assert categoryBMI(27.2) == "Overweight"

# test for overweight upper boundary OFF POINT (29.9)
def test_category_over_upper_OFF():
    assert categoryBMI(29.9) == "Overweight"

# test for overweight upper boundary ON POINT (30.0)
def test_category_over_upper_ON():
    assert categoryBMI(30.0) == "Obese"


### tests for obese boundary (>= 30)
# test for obese OFF POINT (29.9)
def test_category_obese_OFF():
    assert categoryBMI(29.9) == 'Overweight'

# test for obese ON POINT (30.0)
def test_category_obese_ON():
    assert categoryBMI(30.0) == 'Obese'

# test for obese interior point (35.7)
def test_category_obses_interior():
    assert categoryBMI(35.7) == 'Obese'
