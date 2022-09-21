'''type hints -> allow declaring the type of a 
variable'''
from typing import List, Tuple, Dict, Union, Optional
from typing import Callable

def my_age(age: int) -> str:
  return "My age is " + str(age)

type_annotation_int: int = 43
type_annotation_float: float = 2.54
type_annotation_string: str = 'efe'
type_annotation_bool: bool = True



type_annotation_tuple: Tuple[str] = ('1','2','3')
type_annotation_list: List[str] = ['a', 'b', 'c']
type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

#the function gets a int and returns a str 

def my_age(age):
  """ Returns your age as string """
  return "My age is " + str(age)
type_annotation_func: Callable[[int], str] = my_age

#combining datatypes -- if the variable can have one several different types
#use UNION 

type_annotation_list: List[Union[float,int]] = [1.23, 3.32, 1, 3]
type_annotation_dict: Dict[str, Union[float,int]] = {'a': 1, 'b': 2}

#replacing union with | 

type_annotation_list: List[float | int]= [1.23, 3.32, 1, 3]

#optional operator --> means that the variable is required 
#can be like this: List [int | None]
type_annotation_list: List[Optional[int]] = [1, 3]

#the variable z can be float or if is not filled then itll be None
def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
       return 'You called the_func with ' + str(x) + str(y) + str(z)
   


