# pygame
CSF101, CAP2
This is a unittest test case for testing the snake game functions:

- imports unittest and snake modules

- TestSnake class inherits from unittest.TestCase 

- test_change_direction()
  - Calls change() function to change aim direction
  - Checks aim.x and aim.y were updated correctly

- test_inside()
  - Creates head vector outside bounds, checks inside() returns False
  - Creates head vector inside bounds, checks inside() returns True

- test_move() 
  - Mocks turtle functions to avoid errors
  - Tests normal move doesn't change length
  - Tests hitting wall doesn't change length
  - Tests eating food increases length

- Runs tests if file executed directly using __main__ check

Key points:

- Test case inherits from unittest.TestCase
- Sets up and cleans test data
- Each test method tests one specific function/case
- Uses asserts to validate results 
- Avoids turtle errors by mocking functions


