import math
import random
import cmath


def minor(array, pos):
    new_arr = []
    for i in range(len(array)):
        col = []
        if i == pos[0]:
            continue

        for j in range(len(array[i])):
            if j != pos[1]:
                col.append(array[i][j])

        new_arr.append(col)

    return new_arr

def sgn(x):
    return x >= 0 if not callable(x) else x() >= 0

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i
    return 1

def strpprint(pp):
    new_q = ["".join(i) for i in pp]
    return "\n".join(new_q)

def matrixpprint(pp):
    arr = [strpprint(i) for i in pp]
    return "\n\n".join(arr) 

def connect(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    
    return arr3[:]


def det(array):
    if len(array) == 1:
        return array[0][0]

    else:
        a = []
        for i in range(len(array)):
            a.append(array[0][i] * det(minor(array, [0, i])) * (-1)**(i))
        
        z = a[0]
        for i in range(1, len(a)):
            z+=a[i]
        return z

def numericIntegration(function, c, d, dx=0.0001):
    s = 0
    a = min(c, d)
    b = max(c, d)
    i = a
    while i <= b:
        s += (function(i) + function(i+dx))*dx/2
        i += dx
    return s * sgn(d - c)

def numericDiff(function, x, dx=0.0001):
    return (function(x+dx) - function(x-dx))/(2*dx)

        
class poly:
    def __init__(self, coeffs):
        self.coeffs = coeffs[:]
        for i in range(len(self.coeffs)):
            if isinstance(self.coeffs[i], float):
                if int(self.coeffs[i]) == self.coeffs[i]:
                    self.coeffs[i] = int(self.coeffs[i])
        self.deg = len(coeffs) - 1
    
    def __call__(self, x):
        s = 0
        for i in range(self.deg + 1):
            s += self.coeffs[i] * x ** i
        
        return s
    
    def __str__(self):
        '''
        string = []
        for i in range(self.deg + 1):
            if i < self.deg:
                if i > 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] == 1 or self.coeffs[i] == -1:
                        string += ["%s%s^%d"%("+" if self.coeffs[i] == 1 else "-", "x", i)]
                    else:
                        string += ["%s%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "" , str(self.coeffs[i]), "x", i)]
                elif i == 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x")]
                    else:
                        string += ["%s%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" ,str(self.coeffs[i]), "x")]
                elif i == 0:
                    if self.coeffs[i] == 0:
                        continue;
                    string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" , str(self.coeffs[i]))]
            
            else:
                if i > 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x", i)]
                    else:
                        string += ["%s%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "", str(self.coeffs[i]), "x", i)]
                elif i == 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x")]
                    else:
                        string += ["%s%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" ,str(self.coeffs[i]), "x")]
                elif i == 0:
                    if self.coeffs[i] == 0:
                        continue;
                    string += ["%s"%(str(self.coeffs[i]))]

        string.reverse()
        return "".join(string)
        '''
        return strpprint(self.pprint())
    
    def pprint(self):
        new_array = self.coeffs[:]
        new_array.reverse()
        lines = [[], [], []]
        for i in range(len(new_array)):
            temp_lines1 = [[" "], ["+" if sgn(new_array[i]) else "-"], [" "]]
            if i == self.deg:
                temp_lines2 = connect(temp_lines1, [[" " for i in range(len(str(new_array[i])))], [str(abs(new_array[i]))], [" " for i in range(len(str(new_array[i])))]])
            elif i == self.deg - 1:
                temp_lines2 = connect(temp_lines1, [[" " for i in range(len(str(new_array[i])) + 1)], [str(abs(new_array[i])) + "x"], [" " for i in range(len(str(new_array[i])) + 1)]])
                
            else:
                if abs(new_array[i]) != 1:
                    temp_lines2 = connect(temp_lines1, [["".join([" " for i in range(len(str(abs(new_array[i]))) + 1)]) + str(self.deg - i)], [str(abs(new_array[i])) + "x" + "".join([" " for i in range(len(str(self.deg - i)))])], [" " for i in range(len(str(abs(new_array[i]))) + len(str(self.deg - i)))]])
                else:
                    temp_lines2 = connect(temp_lines1, [["".join([" "]) + str(self.deg - i)], ["x" + "".join([" " for i in range(len(str(self.deg - i)))])], [" " for i in range(1 + len(str(self.deg - i)))]])
            lines = connect(lines, temp_lines2)
        return lines[:]
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            x = self.coeffs[:]
            x[0] += other
            return poly(x[:])
        
        elif isinstance(other, poly):
            large_poly = self if self.deg >= other.deg else other
            small_poly = self if self.deg < other.deg else other
            
            res_arr = small_poly.coeffs[:] + [0 for i in range(large_poly.deg - small_poly.deg)]
            for i in range(len(large_poly.coeffs)):
                res_arr[i] += large_poly.coeffs[i]
            
            return poly(res_arr[:])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = [other * i for i in self.coeffs[:]]
            return poly(x)
        
        elif isinstance(other, poly):
            arr = [0 for i in range(self.deg + other.deg + 1)]
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    arr[i + j] += self.coeffs[i] * other.coeffs[j]
            
            return poly(arr[:])
    
    def __pow__(self, other):
        if isinstance(other, int):
            p = poly([1])
            for i in range(other):
                p *= self
            return p
    def __eq__(self, other):
        return self.coeffs[:] == other.coeffs[:]
    
    def __truediv__(self, other):
        
        def normalize(poly):
            while poly and poly[-1] == 0:
                poly.pop()
            if poly == []:
                poly.append(0)


        def poly_divmod(num, den):
            #Create normalized copies of the args
            num = num[:]
            normalize(num)
            den = den[:]
            normalize(den)

            if len(num) >= len(den):
                #Shift den towards right so it's the same degree as num
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return [0], num

            quot = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                #Get the next coefficient of the quotient.
                mult = num[-1] / divisor
                quot = [mult] + quot

                #Subtract mult * den from num, but don't bother if mult == 0
                #Note that when i==0, mult!=0; so quot is automatically normalized.
                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            normalize(num)
            return quot, num
        return poly(poly_divmod(self.coeffs[:], other.coeffs)[0])
    
    def __mod__(self, other):
        def normalize(poly):
            while poly and poly[-1] == 0:
                poly.pop()
            if poly == []:
                poly.append(0)


        def poly_divmod(num, den):
            #Create normalized copies of the args
            num = num[:]
            normalize(num)
            den = den[:]
            normalize(den)

            if len(num) >= len(den):
                #Shift den towards right so it's the same degree as num
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return [0], num

            quot = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                #Get the next coefficient of the quotient.
                mult = num[-1] / divisor
                quot = [mult] + quot

                #Subtract mult * den from num, but don't bother if mult == 0
                #Note that when i==0, mult!=0; so quot is automatically normalized.
                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            normalize(num)
            return quot, num
        return poly(poly_divmod(self.coeffs[:], other.coeffs)[1])

    def __round__(self, ndigits = 3):
        return poly([round(i, ndigits=ndigits) for i in self.coeffs])
    
    def diff(self):
        array = []
        for i in range(1, len(self.coeffs)):
            array.append(i * self.coeffs[i])
        
        return poly(array)
    
    def integral(self, c):
        array = [c]
        for i in range(len(self.coeffs)):
            array.append(self.coeffs[i] / (i + 1))
        
        return poly(array)
    
    def resultant(self, other):
        array = []
        for i in range(self.deg + other.deg):
            l = []
            for j in range(self.deg + other.deg):
                l.append(0)
            array.append(l)
        for i in range(other.deg):
            for j in range(self.deg + 1):
                array[j + i][i] = self.coeffs[j]
        
        for i in range(self.deg):
            for j in range(other.deg + 1):
                array[j + i][i + other.deg] = other.coeffs[j]

        return det(array)
    
    def disc(self):
        n = self.deg
        return (1/self.coeffs[-1])*((-1)**(n*(n-1)/2)) * self.resultant(self.diff())
    
    def roots(self):
        if self.deg == 1:
            return -self.coeffs[0] / self.coeffs[1]
        
        if self.deg == 2:
            a = self.coeffs[2]
            b = self.coeffs[1]
            c = self.coeffs[0]
            d = b**2 - 4*a*c
            return [(-b + cmath.sqrt(d))/(2*a), (-b - cmath.sqrt(d))/(2*a)]
        
        if self.deg == 3:
            a = self.coeffs[3]
            b = self.coeffs[2]
            c = self.coeffs[1]
            d = self.coeffs[0]
            
            d0 = b**2 - 3*a*c
            d1 = 2*b**3-9*a*b*c+27*d*a**2
            C = ((d1 + cmath.sqrt(d1**2-4*d0**3)) / 2)**(1/3)
            r1 = (-1/(3*a)) * (b + C + d0/C)
            r2, r3 = (self / poly([-r1, 1])).roots()
            
            return [r1, r2, r3]
            
    
    __rmul__ = __mul__
    __radd__ = __add__
    @staticmethod
    def rand(deg, coeff_range = [0, 10]):
        coeffs = [(-1)**random.randint(1, 10) * random.randint(coeff_range[0], coeff_range[1]) for i in range(deg + 1)]
        return poly(coeffs)
    
    
    @staticmethod
    def newtonsmethod(pl, start, max_iter):
        x_i = start
        x_ig = start
        for i in range(max_iter):
            x_ig = x_i
            x_i -= pl(x_i) / pl.diff()(x_i)
            x_i = round(x_i, ndigits=10)
            if x_i == x_ig:
                break
        
        return x_i


    