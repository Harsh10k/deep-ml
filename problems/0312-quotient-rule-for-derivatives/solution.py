import numpy as np

def rev(a: list) -> list:
    b = a.copy()
    b.reverse()
    return b

def poly_eval(coeff: list, x: float) -> float:
    coeff = rev(coeff)
    s = 0
    for i in range(len(coeff)):
        s += coeff[i] * (x ** i)
    return s

def poly_deriv_eval(coeff: list, x: float) -> float:
    coeff = rev(coeff)
    s = 0
    for i in range(len(coeff)):
        if i == 0:
            s += 0
        else:
            s += coeff[i] * i * (x ** (i - 1))
    return s

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    
    g = g_coeffs
    h = h_coeffs
    result = poly_deriv_eval(g, x) * poly_eval(h, x) - poly_eval(g, x) * poly_deriv_eval(h, x)
    result /= poly_eval(h, x) ** 2
    return result


