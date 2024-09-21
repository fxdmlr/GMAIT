import math
import random
import time
import utils
import evaluator as evl

def regMulGame(number_of_rounds=5, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        entry = int(input("%d * %d = "%(n1, n2))) if not float_mode else float(input("%f * %f = "%(n1, n2)))
        if entry == n1 * n2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyMulGame(number_of_rounds=5, max_deg=5, nrange=[10, 100]):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p1 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        p2 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        wentry = input("(%s) * (%s) = "%(str(p1), str(p2))).split(" ") 
        entry = [int(i) for i in wentry]
        entry.reverse()
        entry_poly = utils.poly(entry[:]) 
        if entry_poly == p1 * p2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %s \n" % str(p1 * p2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyEval(number_of_rounds, deg, coeffs_range, input_range):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        x = (-1) ** random.randint(1, 10) * random.randint(input_range[0], input_range[1])
        entry = int(input("%s\t at x = %d : \n"%(str(p), x)))
        if entry == p(x):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %d"%p(x))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def evalRoot(number_of_rounds=5,root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p = utils.AlgebraicReal.randpurer(1, nrange_surd=ranges[:], nrange_root=root_range[:])
        entry = float(input(str(p) + " = "))
        if entry == round(p(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]  

def evalRootPoly(deg, coeffs_range = [10, 100], number_of_rounds=5,root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        r = utils.AlgebraicReal.randpurer(1, nrange_surd=ranges[:], nrange_root=root_range[:])
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        entry = float(input(str(p) + "\n at x = \n" + str(r)))
        if entry == round(p(r()), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p(r()), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]   

def surdGame(number_of_rounds=5, root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n = random.randint(root_range[0], root_range[1])
        p = utils.AlgebraicReal([0, [random.randint(ranges[0], ranges[1]), random.randint(ranges[0], ranges[1]), 2], [random.randint(ranges[0], ranges[1]), random.randint(ranges[0], ranges[1]), 2]])
        entry = float(input("%d root of \n%s : "%(n, str(p))))
        if entry == round(p() ** (1/n), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p() ** (1/n), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]  

def divGame(number_of_rounds=5, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
        entry = float(input("%s \n\t"%string))
        if entry == round(n(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyDivGame(number_of_rounds=5, max_deg=5, nrange=[10, 100], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p1 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        p2 = utils.poly.rand(random.randint(1, p1.deg), coeff_range=nrange[:]) 
        wentry = input("%s \n%s \n > "%(str(p1), str(p2))).split(" ") 
        entry = [float(i) for i in wentry]
        entry.reverse()
        entry_poly = utils.poly(entry[:]) 
        if entry_poly == round(p1 / p2, ndigits=ndigits):
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %s \n" % str(round(p1 / p2, ndigits=ndigits)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def regMulDyn(total_time=600, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        number_of_rounds += 1
        entry = int(input("%d * %d = "%(n1, n2))) if not float_mode else float(input("%f * %f = "%(n1, n2)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == n1 * n2:
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
def regMulDynII(total_time=600, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n3 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n4 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        number_of_rounds += 1
        entry = int(input("%d * %d + %d * %d = "%(n1, n2, n3, n4))) if not float_mode else float(input("%f * %f + %f * %f = "%(n1, n2, n3, n4)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == n1 * n2 + n3 * n4:
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2 + n3 * n4))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
def polyEvalDyn(total_time, deg, coeffs_range, input_range):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        x = (-1) ** random.randint(1, 10) * random.randint(input_range[0], input_range[1])
        number_of_rounds += 1
        entry = int(input("%s\t at x = %d : \n"%(str(p), x)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == p(x):
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        else:
            print("Incorrect. The answer was : %d"%p(x))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def divGameDyn(total_time=600, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
        number_of_rounds += 1
        entry = float(input("%s \n\t"%string))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == round(n(), ndigits=ndigits):
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def divGameDynII(total_time=600, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n = utils.rational.rand(nrange=ranges[:])
        m = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(utils.connect(utils.connect(n.pprint(), [["   "], [" + "], ["   "]]), m.pprint()), [["   "], [" = "], ["   "]]))
        number_of_rounds += 1
        entry = float(input("%s \n\t"%string))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == round(n() + m(), ndigits=ndigits):
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n() + m(), ndigits=ndigits))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def mixedArithmeticDyn(total_time, nrange_mul=[100, 1000], nrange_div=[10, 100],  ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        x = random.randint(1, 10)
        if x%2 == 0:
            n1 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n2 = random.randint(nrange_mul[0], nrange_mul[1]) 
            number_of_rounds += 1
            entry = int(input("%d * %d = "%(n1, n2)))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == n1 * n2:
                print("Correct.")
                print("Remaining time : ", round(total_time - (time.time() - start)))
                pts += 1
            
            else:
                print("Incorrect. The answer was : %f \n" % (n1 * n2))
                print("Remaining time : ", round(total_time - (time.time() - start)))
        else:
            n = utils.rational.rand(nrange=nrange_div[:])
            string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
            number_of_rounds += 1
            entry = float(input("%s \n\t"%string))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == round(n(), ndigits=ndigits):
                print("Correct.")
                print("Remaining time : ", round(total_time - (time.time() - start)))
                pts += 1
            else:
                print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
                print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def mixedArithmeticDynII(total_time, nrange_mul=[100, 1000], nrange_div=[10, 100],  ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        x = random.randint(1, 10)
        if x%2 == 0:
            n1 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n2 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n3 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n4 = random.randint(nrange_mul[0], nrange_mul[1])
            number_of_rounds += 1
            entry = int(input("%d * %d + %d * %d = "%(n1, n2, n3, n4)))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == n1 * n2 + n3 * n4:
                print("Correct.")
                print("Remaining time : ", round(total_time - (time.time() - start)))
                pts += 1
            
            else:
                print("Incorrect. The answer was : %f \n" % (n1 * n2 + n3 * n4))
                print("Remaining time : ", round(total_time - (time.time() - start)))
        else:
            start = time.time()
            pts = 0
            number_of_rounds = 0
            n = utils.rational.rand(nrange=nrange_div[:])
            m = utils.rational.rand(nrange=nrange_div[:])
            string = utils.strpprint(utils.connect(utils.connect(utils.connect(n.pprint(), [["   "], [" + "], ["   "]]), m.pprint()), [["   "], [" = "], ["   "]]))
            number_of_rounds += 1
            entry = float(input("%s \n\t"%string))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == round(n() + m(), ndigits=ndigits):
                print("Correct.")
                print("Remaining time : ", round(total_time - (time.time() - start)))
                pts += 1
            else:
                print("Incorrect. The answer was : %f"%round(n() + m(), ndigits=ndigits))
                print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def polyroots(number_of_rounds=5, root_range=[1, 10], deg=3):
    print("Enter the result of a^n + b^(n-1) + c^(n-2) + ... \nwhere a < b < c < ... \nand a,b,c etc. are the roots of the polynomial and n is the degree.")
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        z = utils.poly([1])
        rarray = []
        for j in range(deg):
            q = (-1)**(random.randint(1, 10)) * random.randint(root_range[0], root_range[1])
            rarray.append(-q)
            z *= utils.poly([q, 1])
        print(z)
        m = int(input("Answer : "))
        narr = list(sorted(rarray))
        res = sum([narr[i] ** (deg - i) for i in range(deg)])
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
            print("The roots were : ", " , ".join([str(i) for i in narr]))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyrootsDyn(tot_time=600, root_range=[1, 10], deg=3):
    print("Enter the result of a^n + b^(n-1) + c^(n-2) + ... \nwhere a < b < c < ... \nand a,b,c etc. are the roots of the polynomial and n is the degree.")
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time()-start <= tot_time:
        z = utils.poly([1])
        rarray = []
        for j in range(deg):
            q = (-1)**(random.randint(1, 10)) * random.randint(root_range[0], root_range[1])
            rarray.append(-q)
            z *= utils.poly([q, 1])
        print(z)
        m = int(input("Answer : "))
        number_of_rounds += 1
        narr = list(sorted(rarray))
        res = sum([narr[i] ** (deg - i) for i in range(deg)])
        if time.time() - start > tot_time:
            print("Time elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
        
        if m == res:
            print("Correct.")
            print("Remaining time : ", round(tot_time - (time.time() - start)))
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
            print("The roots were : ", " , ".join([str(i) for i in narr]))
            print("Remaining time : ", round(tot_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polydisc(number_of_rounds=5, coeff_range=[1, 10], deg=3):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        z = utils.poly.rand(deg, coeff_range=coeff_range[:])
        print(z)
        m = int(input("Discriminant : "))
        res = z.disc()
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polydiscDyn(tot_time=600, coeff_range=[1, 10], deg=3):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time()-start <= tot_time:
        z = utils.poly.rand(deg, coeff_range=coeff_range[:])
        number_of_rounds += 1
        print(z)
        m = int(input("Discriminant : "))
        res = z.disc()
        end = time.time()
        if time.time() - start > tot_time:
            print("Time elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
        
        if m == res:
            print("Correct.")
            print("Remaining time : ", round(tot_time - (time.time() - start)))
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
            print("Remaining time : ", round(tot_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def partialFractionGame(number_of_rounds=5, max_deg=4, nrange=[1, 10]):
    print("For each question, sort the resulting fractions\nby the root of the denominator and write the c-\noefficients in succession without one space be-\ntween them.\n")
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        z = []
        for j in range(max_deg):
            x = (-1)**random.randint(1, 2) * random.randint(nrange[0], nrange[1])
            while x in z:
                x = (-1)**random.randint(1, 2) * random.randint(nrange[0], nrange[1])
            z.append(x)
        z.sort()
        z.reverse()
        q = [utils.poly([j, 1]) for j in z]
        a = 1
        for j in q:
            a *= j
        v = [random.randint(nrange[0], nrange[1]) * ((-1)**random.randint(1,2)) for j in range(len(q))]
        p = utils.poly([0])
        for j in range(len(q)):
            pol_arr = q[:j] + q[j+1:] if j < len(q) - 1 else q[:j]
            r = utils.poly([1])
            for k in pol_arr:
                r *= k
            p += r*v[j]
        str1 = str(p)
        str2 = str(a)
        str1cpy = str1[:]
        str2cpy = str2[:]
        len_measure1 = len(str1cpy.split("\n")[0])
        len_measure2 = len(str2cpy.split("\n")[0])
        str3 = "".join(["-" for j in range(max(len_measure1, len_measure2))])
        print(str1 + "\n" + str3 + "\n" + str2 + "\n")
        x = input("res : ")
        if x == " ".join([str(j) for j in v]):
            pts += 1
            print("Correct.")
        else:
            print("Incorrect. The answer was : ", v)
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]        
def partialFractionDyn(tot_time=600, max_deg=4, nrange=[1, 10]):
    print("For each question, sort the resulting fractions\nby the root of the denominator and write the c-\noefficients in succession without one space be-\ntween them.\n")
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start <= tot_time:
        z = []
        for j in range(max_deg):
            x = (-1)**random.randint(1, 2) * random.randint(nrange[0], nrange[1])
            while x in z:
                x = (-1)**random.randint(1, 2) * random.randint(nrange[0], nrange[1])
            z.append(x)
        z.sort()
        z.reverse()
        q = [utils.poly([j, 1]) for j in z]
        a = 1
        for j in q:
            a *= j
        v = [random.randint(nrange[0], nrange[1]) * ((-1)**random.randint(1,2)) for j in range(len(q))]
        p = utils.poly([0])
        for j in range(len(q)):
            pol_arr = q[:j] + q[j+1:] if j < len(q) - 1 else q[:j]
            r = utils.poly([1])
            for k in pol_arr:
                r *= k
            p += r*v[j]
        str1 = str(p)
        str2 = str(a)
        str1cpy = str1[:]
        str2cpy = str2[:]
        len_measure1 = len(str1cpy.split("\n")[0])
        len_measure2 = len(str2cpy.split("\n")[0])
        str3 = "".join(["-" for j in range(max(len_measure1, len_measure2))])
        print(str1 + "\n" + str3 + "\n" + str2 + "\n")
        x = input("res : ")
        number_of_rounds += 1
        end = time.time()
        if x == " ".join([str(j) for j in v]) and end - start <= tot_time:
            pts += 1
            print("Correct.")
            print("Remaining time : ", round(tot_time - (time.time() - start)))
        elif end - start > tot_time:
            print("Time elapsed before entry.")
            break
        else:
            print("Incorrect. The answer was : ", v)
            print("Remaining time : ", round(tot_time - (time.time() - start)))
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
       
def subIntGame(tot_time, mode, deg, nranges, boundranges, ndigits, dyn=False, start=time.time(), duration=600):
    pts = 0
    if mode == 1:
            p, q, string = utils.generate_integrable_ratExpr(deg, nranges=nranges[:])
            a, b = random.randint(boundranges[0], boundranges[1]), random.randint(boundranges[0], boundranges[1])
            res = round(utils.numericIntegration(lambda x : p(x) / q(x), min(a, b), max(a, b)), ndigits=ndigits)
            print("Evaluate the integral of the function below from %d to %d"%(min(a, b), max(a, b)))
            print(string)
            x = round(evl.evl(input("Answer : ")), ndigits=ndigits)
            if x == res:
                if time.time() - start > duration and dyn:
                    print("Time Elapsed before entry.")
                    return None
                print("Correct.")
                if dyn:
                    print("Remaining time : ", round(tot_time - (time.time() - start)))
                pts += 1
            else:
                print("Incorrect. The answer was %f"%res)
                if dyn:
                    print("Remaining time : ", round(tot_time - (time.time() - start)))
    elif mode == 2:
        f, string = utils.generate_eulersub(deg, nranges=nranges[:])
        a, b = random.randint(boundranges[0], boundranges[1]), random.randint(boundranges[0], boundranges[1])
        res = round(utils.numericIntegration(f, min(a, b), max(a, b)), ndigits=ndigits)
        print("Evaluate the integral of the function below from %d to %d"%(min(a, b), max(a, b)))
        print(string)
        x = round(evl.evl(input("Answer : ")), ndigits=ndigits)
        if x == res:
            if time.time() - start > duration and dyn:
                print("Time Elapsed before entry.")
                return None
            print("Correct.")
            if dyn:
                print("Remaining time : ", round(tot_time - (time.time() - start)))
            pts += 1
        else:
            print("Incorrect. The answer was %f"%res)
            if dyn:
                print("Remaining time : ", round(tot_time - (time.time() - start)))
    
    elif mode == 3:
        f, string = utils.generate_trig(nranges=nranges[:])
        a, b = random.randint(boundranges[0], boundranges[1]), random.randint(boundranges[0], boundranges[1])
        res = round(utils.numericIntegration(f, min(a, b), max(a, b)), ndigits=ndigits)
        print("Evaluate the integral of the function below from %d to %d"%(min(a, b), max(a, b)))
        print(string)
        x = round(evl.evl(input("Answer : ")), ndigits=ndigits)
        if x == res:
            if time.time() - start > duration and dyn:
                print("Time Elapsed before entry.")
                return None
            print("Correct.")
            if dyn:
                print("Remaining time : ", round(tot_time - (time.time() - start)))
            pts += 1
        else:
            print("Incorrect. The answer was %f"%res)
            if dyn:
                print("Remaining time : ", round(tot_time - (time.time() - start)))
    return pts

def integralGame(number_of_rounds=5, deg=2, mode=1, nranges=[1, 10], boundranges=[0, 2], ndigits=2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        if mode in [1, 2, 3]:
            pts += subIntGame(4000, mode, deg, nranges, boundranges, ndigits)
        elif mode == 4:
            new_mode = random.randint(1, 3)
            pts += subIntGame(4000, new_mode, deg, nranges, boundranges, ndigits)
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def integralGameDyn(tot_time=600, deg=2, mode=1, nranges=[1, 10], boundranges=[0, 2], ndigits=2):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start <= tot_time:
        if mode in [1, 2, 3]:
            z = subIntGame(tot_time, mode, deg, nranges, boundranges, ndigits, dyn=True, start=start, duration=tot_time)
            end = time.time()
            number_of_rounds += 1
            if z is not None:
                pts += z
            else:
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
        elif mode == 4:
            new_mode = random.randint(1, 3)
            z = subIntGame(tot_time, new_mode, deg, nranges, boundranges, ndigits, dyn=True, start=start, duration=tot_time)
            end = time.time()
            number_of_rounds += 1
            if z is not None:
                pts += z
            else:
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def regMulGameDig(number_of_rounds=5, digits=5):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n1 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
        n2 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
        entry = int(input("%d * %d = "%(n1, n2))) 
        if entry == n1 * n2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def regMulDynDig(total_time=600, digits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n1 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1)
        n2 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1)
        number_of_rounds += 1
        entry = int(input("%d * %d = "%(n1, n2))) 
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == n1 * n2:
            print("Correct.")
            print("Remaining time : ", round(total_time - (time.time() - start)))
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
            print("Remaining time : ", round(total_time - (time.time() - start)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def fourierSgame(number_of_rounds=5, nranges=[1, 10], deg=2, p_range=[0, 2], exp_cond=False):
    print("Enter the result accurate to 2 digits after floating point.")
    start = time.time()
    pts = 0
    
    for i in range(number_of_rounds):
        f, period, a_n, b_n, a_0, string, p1, c1 = utils.generate_fourier_s(nranges=nranges[:], deg=deg, p_range=p_range, exp_cond=exp_cond)
        print(string)
        print("P =", period)
        x = round(evl.evl(input("a0 + a1 + b1 = ")), ndigits=2)
        res = round(a_0 + a_n(1) + b_n(1), ndigits=2)
        if x == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was ", res)
        
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def fourierSgameDyn(tot_time=600, nranges=[1, 10], deg=2, p_range=[0, 2], exp_cond=False):
    print("Enter the result accurate to 2 digits after floating point.")
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start <= tot_time:
        f, period, a_n, b_n, a_0, string, p1, c1 = utils.generate_fourier_s(nranges=nranges[:], deg=deg, p_range=p_range, exp_cond=exp_cond)
        print(string)
        print("P =", period)
        x = round(evl.evl(input("a0 + a1 + b1 = ")), ndigits=2)
        number_of_rounds += 1
        res = round(a_0 + a_n(1) + b_n(1), ndigits=2)
        end = time.time()
        if time.time() - start > tot_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, tot_time]
        if x == res and time.time() - start <= tot_time:
            print("Correct.")
            pts += 1     
        else:
            print("Incorrect. The answer was ", res)
        
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
            