A  = magic(3)

[r, c] = find(A >= 7)
A(2,3)
help find

a = [1 2 3 4]
sum(a)
prod(a)
floor(a)
ceil(a)

rand(3)
max(rand(3), rand(3))
max(A, [], 1)
max(a)
max(A)
max(max(a))

max(max(A))
A(:)
max(A(:))

A = magic(9)
sum(A,1)
sum(A,2)

eye(9)
A .* eye(9)
sum(sum(A.*eye(9)))
flipud(eye(9))


A = magic(3)
pinv(A)
A * pinv(A)