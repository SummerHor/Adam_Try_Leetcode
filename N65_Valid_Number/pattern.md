## Solving Such problem that require regex, if you are NOT quite expert in regex yet

- Go to this website : <https://regex101.com/>
- Test the available input to write the regex pattern before plug it in the python or any program you write.

regex: ^[\-\+]?(\.[0-9]+|[0-9]+\.|[0-9]+|[0-9]+\.[0-9]+)([eE][\+\-]?[0-9]+)?$

##### Valid Number Pattern

2
0089
-0.1
+3.14 4.
-.9
2e10
-90E3
3e+7
+6e-1
53.5e93
-123.456e789

##### Invalid Number Pattern

.1.
0e
abc
1a
1e
e3
99e2.5
--6
-+3
95a54e53
