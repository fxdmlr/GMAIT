'''
General Mathematical Ability Index Test.

Author : -----------
This is a tool to asses one's general 
mathematical aptitude. 

'''

import math
import random
import time
import utils
import multgame
import matrixgames
import os

def static(prechoice=None):
    os.system("clear")
    if prechoice is not None:
        choice = prechoice
    print("\n")
    if prechoice is None:
        choice = int(input("Enter the desired mode :\n0-Quit\n1-regMul\n2-polyMul\n3-RegDet\n4-PolyDet\n5-regMatMul\n6-polyMatMul\n7-polyEval\n8-evalRoot\n9-evalRootPoly\n10-surdGame\n11-divGame\n12-polyDiv\n13-EigenGame\n14-RootGame\n15-DiscGame\n16-PFD\n17-IntegralGame\n18-RegDig\n19-Fourier Series\n20-Equation system\n21-Mean\n22-Stdev\n"))
    if choice == 1:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("clear")
        stats = multgame.regMulGame(number_of_rounds=rounds, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 2:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        os.system("clear")
        stats = multgame.polyMulGame(number_of_rounds=rounds, max_deg=max_deg, nrange=ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 3:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("clear")
        stats = matrixgames.regDetGame(number_of_rounds=rounds, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2])) 
    
    if choice == 4:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dims : "))
        
        max_deg = int(input("Maximum degree : "))
        os.system("clear")
        stats = matrixgames.polyDetGame(number_of_rounds=rounds, dims=dims, nrange=ranges, max_deg=max_deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 5:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("clear")
        stats = matrixgames.regMulGame(number_of_rounds=rounds, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 6:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dims : "))
        
        max_deg = int(input("Maximum degree : "))
        os.system("clear")
        stats = matrixgames.polyMulGame(number_of_rounds=rounds, dims=dims, nrange=ranges, max_deg=max_deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 7:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of abs of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of abs of inputs (seperated by blank space): ").split(" ")
        inp_ranges = [int(c), int(d)]
        
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polyEval(rounds, deg, ranges[:], inp_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 8:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        os.system("clear")
        stats = multgame.evalRoot(number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 9:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        e, f = input("Range of coeffs: ").split(" ")
        coeff_ranges = [int(e), int(f)]
        deg = int(input("Degree : "))
        os.system("clear")
        stats = multgame.evalRootPoly(deg, coeffs_range=coeff_ranges, number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 10:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        os.system("clear")
        stats = multgame.surdGame(number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 11:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.divGame(number_of_rounds=rounds, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 12:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("clear")
        stats = multgame.polyDivGame(number_of_rounds=rounds, max_deg=max_deg, nrange=ranges[:], ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 13:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("clear")
        print("Enter the smallest real part of all eigen values for each matrix.")
        stats = matrixgames.eigenvalueGame(number_of_rounds=rounds, dims=dims, nrange=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 14:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of abs of roots (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polyroots(number_of_rounds=rounds, root_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 15:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polydisc(number_of_rounds=rounds, coeff_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 16:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        os.system("clear")
        stats = multgame.partialFractionGame(number_of_rounds=rounds, max_deg=max_deg, nrange=ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 17:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        c, d = input("Range of bounds of integration (seperated by blank space): ").split(" ")
        branges = [int(c), int(d)]
        
        max_deg = int(input("Maximum degree : "))
        ndigits = int(input("Digits after floating point : "))
        mode = int(input("Enter the mode : \n 1-Rational Expressions\n 2-Algebraic Expression\n 3-Trig Expression\n 4-Shuffle\n"))
        os.system("clear")
        stats = multgame.integralGame(number_of_rounds=rounds, deg=max_deg, mode=mode, nranges=ranges[:], boundranges=branges[:], ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 18:
        rounds = int(input("Number of rounds : "))
        a = int(input("Number of Digits : "))
        
        os.system("clear")
        stats = multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    if choice == 19:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        c, d = input("Range of half period (seperated by blank space): ").split(" ")
        p_ranges = [int(c), int(d)]
        
        max_deg = int(input("Maximum degree : "))
        exp_cond = int(input("Exponential mode? 1 : Yes\t0 : No "))
        os.system("clear")
        stats = multgame.fourierSgame(number_of_rounds=rounds, nranges=ranges[:], deg=max_deg, p_range=p_ranges, exp_cond=exp_cond)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 20:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of answers (seperated by blank space): ").split(" ")
        param_ranges = [int(c), int(d)]
        parameters = int(input("Number of unknowns : "))
        os.system("clear")
        stats = multgame.linearEqSystem(number_of_rounds=rounds, coeff_abs_ranges=ranges[:], parameters=parameters, param_abs_ranges=param_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2])) 
    
    if choice == 21:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("N : "))
        ndigits = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.meanGame(number_of_rounds=rounds, nrange=ranges, n=max_deg, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    if choice == 22:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("N : "))
        ndigits = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.stdevGame(number_of_rounds=rounds, nrange=ranges, n=max_deg, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
def dynamic(prechoice=None):
    os.system("clear")
    if prechoice is not None:
        choice = prechoice
    print("\n")
    if prechoice is None:
        choice = int(input("Enter the desired mode :\n 0-Quit\n 1-regMul\n 2-regMulII\n 3-divGame\n 4-divGameII\n 5-MixedArr\n 6-MixedArrII\n 7-polyEval\n 8-DetGame\n 9-EigenValGame\n 10-DiscGame\n 11-rootGame\n 12-PFD\n 13-IntegralGame\n 14-regMulDig\n 15-Fourier Series\n 16-Equation System\n 17-Mean\n 18-Stdev\n "))
    if choice == 0:
        return
    
    if choice == 1:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("clear")
        stats = multgame.regMulDyn(total_time=duration, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 2:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("clear")
        stats = multgame.regMulDynII(total_time=duration, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    
    if choice == 3:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.divGameDyn(total_time=duration, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 4:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.divGameDynII(total_time=duration, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 5:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers for Mul(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of numbers for Div(seperated by blank space): ").split(" ")
        ranges_div = [int(c), int(d)]
        a_fl = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.mixedArithmeticDyn(total_time=duration, nrange_mul=ranges, nrange_div=ranges_div, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 6:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers for Mul(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of numbers for Div(seperated by blank space): ").split(" ")
        ranges_div = [int(c), int(d)]
        a_fl = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.mixedArithmeticDynII(total_time=duration, nrange_mul=ranges, nrange_div=ranges_div, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 7:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of abs of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of abs of inputs (seperated by blank space): ").split(" ")
        inp_ranges = [int(c), int(d)]
        
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polyEvalDyn(duration, deg, ranges[:], inp_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 8:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("clear")
        stats = matrixgames.regDetGameDyn(tot_time=duration, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 9:
        duration = int(input("duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("clear")
        print("Enter the smallest real part of all eigen values for each matrix.")
        stats = matrixgames.eigenvalueGameDyn(tot_time=duration, dims=dims, nrange=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    if choice == 10:
        duration = int(input("duration: "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polydiscDyn(tot_time=duration, coeff_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 11:
        duration = int(input("duration : "))
        a, b = input("Range of abs of roots (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        deg = int(input("Polynomial degree : "))
        os.system("clear")
        stats = multgame.polyrootsDyn(tot_time=duration, root_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 12:
        duration = int(input("Duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        os.system("clear")
        stats = multgame.partialFractionDyn(tot_time=duration, max_deg=max_deg, nrange=ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 13:
        duration = int(input("Duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        c, d = input("Range of bounds of integration (seperated by blank space): ").split(" ")
        branges = [int(c), int(d)]
        
        max_deg = int(input("Maximum degree : "))
        ndigits = int(input("Digits after floating point : "))
        mode = int(input("Enter the mode : \n 1-Rational Expressions\n 2-Algebraic Expression\n 3-Trig Expression\n 4-Shuffle\n"))
        os.system("clear")
        stats = multgame.integralGameDyn(tot_time=duration, deg=max_deg, mode=mode, nranges=ranges[:], boundranges=branges[:], ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 14:
        duration = int(input("Time in seconds : "))
        a = int(input("Number of digits : "))
        
        os.system("clear")
        stats = multgame.regMulDynDig(total_time=duration, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 15:
        duration = int(input("Duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        c, d = input("Range of half period (seperated by blank space): ").split(" ")
        p_ranges = [int(c), int(d)]
        
        max_deg = int(input("Maximum degree : "))
        exp_cond = int(input("Exponential mode? 1 : Yes\t0 : No "))
        os.system("clear")
        stats = multgame.fourierSgameDyn(tot_time=duration, nranges=ranges[:], deg=max_deg, p_range=p_ranges, exp_cond=exp_cond)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 16:
        duration = int(input("Duration : "))
        a, b = input("Range of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of answers (seperated by blank space): ").split(" ")
        param_ranges = [int(c), int(d)]
        parameters = int(input("Number of unknowns : "))
        os.system("clear")
        stats = multgame.linearEqSystemDyn(tot_time=duration, coeff_abs_ranges=ranges[:], parameters=parameters, param_abs_ranges=param_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 17:
        duration = int(input("Duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("N : "))
        ndigits = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.meanGameDyn(tot_time=duration, nrange=ranges, n=max_deg, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 18:
        duration = int(input("Duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("N : "))
        ndigits = int(input("Digits after floating point : "))
        os.system("clear")
        stats = multgame.stdevGameDyn(tot_time=duration, nrange=ranges, n=max_deg, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
          
while True:
    mode = int(input("Mode :\n 1-Static \n 2-Dynamic\n 3-Quit\n"))
    mode_str = str(mode)
    if len(mode_str) > 1:
        if mode_str[0] == "1":
            static(prechoice=int(mode_str[1:]))
        elif mode_str[0] == "2":
            dynamic(prechoice=int(mode_str[1:]))
        else:
            break
    if mode == 1:
        static()
    elif mode == 2:
        dynamic()
    elif mode == 3:
        break
quit()
