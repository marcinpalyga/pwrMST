function trapezoidRule(a ,b ,n)
    h = float((b-a)/n)
    ans = (f(a)/2)+(f(b)/2)
    for i = 1:n
        ans += f(a+(i*h))
    end
    ans=ans*h
    return ans
end

f(x) = log(x)
trapezoidRule(0.1 , 1, 10^4)