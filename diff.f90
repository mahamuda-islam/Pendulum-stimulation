program differentiation
    implicit none
    real :: t(7), x(7)
    real :: h, d2, d3

    t = (/0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6/)
    x = (/1.0, 0.90484, 0.81873, 0.74082, 0.67032, 0.60653, 0.54881/)

    h = 0.1

    ! 2-point differentiation
    d2 = (x(5) - x(3)) / (2*h)

    ! 3-point central differentiation
    d3 = (x(5) - x(3)) / (2*h)

    print *, "2-point derivative at t=0.3 =", d2
    print *, "3-point derivative at t=0.3 =", d3

end program differentiation