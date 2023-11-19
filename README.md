```
// in1.txt
1.2.3.1-1.2.3.7
2.2.3.1-2.2.3.7
3.2.3.0/24
4.2.3.0/24

// in2.txt
1.2.3.4-1.2.3.8
2.2.3.4-2.2.3.8
3.2.3.2-3.2.3.254
4.2.3.3-4.2.3.253

// Find IP ranges that are found from file2 only
% python app.py -1 in1.txt in2.txt
1.2.3.8
2.2.3.8

// Find IP ranges that are found from file2 only
% python app.py -2 in1.txt in2.txt
1.2.3.1-1.2.3.3
2.2.3.1-2.2.3.3
3.2.3.1
3.2.3.255
4.2.3.1-4.2.3.2
4.2.3.254-4.2.3.255

// Find common ranges.
% python app.py -12 in1.txt in2.txt
1.2.3.4-1.2.3.7
2.2.3.4-2.2.3.7
3.2.3.2-3.2.3.254
4.2.3.3-4.2.3.253
