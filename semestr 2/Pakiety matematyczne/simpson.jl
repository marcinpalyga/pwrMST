function simpson(a, b, n)
    n%2 == 0 || error("n powinno być parzyste")
    h = float((b-a)/n)
    x0 = f(a)
    xn = f(b)
    xi = 0
    xj = 0
    for i in 1:n-1
        x = a + i*h
        if f(x) == -Inf || f(x) == Inf
            continue
        end
        if x0 == -Inf || x0 == Inf
            x0 = f(a + i*h)
        end
        if xn == -Inf || xn == Inf
            xn = f(a + (n-i)*h)
        end
        if i%2 == 0
            xj += f(x)
        else 
            xi += f(x)
        end
    end
    ans = h*(x0 + 2*xi + 4*xj + xn)/3
    return ans
end

f(x) = log(x)
simpson(0, 1, 10000)
