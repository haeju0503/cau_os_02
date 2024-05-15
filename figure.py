#figure파일
import math

"""
20244744 황해주의 모듈
class Line 1개와
함수 3개로 구성되어있다
"""


class Line:
    """
    class Line은 외부에서 접근 불가능한 필드 __length를 가지며
    getter인 get_length와 setter인 set_length를 가진다.    
    """
    __length = 1

    def __init__(self, initnum=1):
        """
        생성자를 이용해 __length의 값을 변경할 수 있다
        값은 0 초과의 int 또는 float만 가능하며 이에 해당하지 않거나 값을 입력하지 않으면 기본값인 1이 __length가 된다
        Arg:
            initnum : 초기값
        Examples:
            newLine1 = Line("냠냠냠") : newLine1의 __length는 1이 된다
            newLine2 = Line(120) : newLine2의 __length는 120이된다
            newLine3 = Line(0) : newLine3의 __length는 1이 된다
        """
        if((type(initnum) == int or type(initnum) == float) and initnum > 0):
            self.__length = initnum
        else :
            self.__length = 1

    def get_length(self):
        """
        getter이다, 반환값으로 __length를 준다
        """
        return self.__length
    
    def set_length(self, num=1):
        """
        setter이다
        만약 입력값이 0 이하이거나 정수/실수가 아니라면 기존의 __length값을 유지한다
        Examples:
            newLine4 = Line(7)
            newLine4.set_length(-12) : newLine4의 __length는 7을 유지한다
        """
        if((type(num) == int or type(num) == float) and num > 0):
            self.__length = num
    
    def __mul__(self, other):
        """
        곱하기를 위한부분이다.
        Line과 Line을 곱할때와 Line과 Line이 아닌 것을 곱할때로 나누었다.
        Line을 정수나 실수로 곱하면 __length * (정수/실수)를 반환하고
        Line1 * Line2 는 Line1의 __length값과 Line2의 __length값을 곱한다.
        Examples:
        Line5 = Line(4)
        Line6 = Line(8)
        print(Line5 * Line6) :출력값은 32
        print(Line5 * 2.5) : 출력값은 10.0
        print(Line6 * "와구와구") : 출력값은 와구와구와구와구와구와구와구와구와구와구와구와구와구와구와구와구
        """
        if (type(other) == Line):
            new_length = self.__length * other.get_length()
        else:
            new_length = self.__length * other 
        return new_length
    
    

def area_square(a):
    """
    사각형의 넓이를 구하는 함수이다
    Arg:
        a : 클래스 Line
    return:
        a * a : a의 __length의 제곱, 인수가 클래스 Line이 아니면 0을 반환한다.
    Examples:
        line7 = Line(3)
        k = area_square(line7) : k는 9이다
        l = area_square(3) : l은 0이다
    """
    if(type(a) == Line):
        return a * a
    else:
        return 0
    
def area_circle(a):
    """
    원의 넓이를 구하는 함수이다
    Arg:
        a : 클래스 Line
    return:
        a * a * 𝜋 : a의 __length의 제곱에 𝜋를 곱한다, 인수가 클래스 Line이 아니면 0을 반환한다.
    Examples:
        line8 = Line()
        m = area_square(line8) : m는 3.14~이다
        n = area_square(1) : n은 0이다
    """
    if(type(a) == Line):
        return a * a * math.pi
    else:
        return 0
    
def area_regular_triangle(a):
    """
    정삼각형의 넓이를 구하는 함수이다
    Arg:
        a : 클래스 Line
    return:
        a * a * 루트(3) / 4 : a의 __length의 제곱에 루트3을 곱한뒤 4로 나눈다, 인수가 클래스 Line이 아니면 0을 반환한다.
    Examples:
        line9 = Line(2)
        q = area_square(line9) : q는 1.732~이다
        w = area_square(w) : w은 0이다
    """
    if(type(a) == Line):
        return a * a * math.sqrt(3) / 4
    else:
        return 0

