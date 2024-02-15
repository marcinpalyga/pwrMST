function romberg(f, xmin, xmax; n=8)
    m = n
    # First value:
    r = zeros((n+1, m+1))  
    r[1, 1] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.

    # One side of the triangle:
    for i in 1 : n
        h_i = (xmax - xmin) / (2^i)
        sum_f_x = 0
        for k in 1 : 2^(i - 1)
            sum_f_x += f(xmin + ((2 * k - 1) * h_i))
        end
        r[i + 1, 1] = (r[i, 1] / 2.) + (h_i * sum_f_x)
    end

    # All the other values:
    for j in 1 : m
        for i in j : n
            r[i + 1, j + 1] = (((4. ^j) * r[i + 1, j]) - r[i, j]) / (4. ^j - 1.)
        end
    end

    r[n + 1, m + 1]
end

f(x)=sin(x)
a = 0  
b= π

println(romberg(f, a, b, n=8))