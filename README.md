Name: cidrcomm
 * Similiar to Linux 'comm' command. Supports -1, -2, -12
   * -1: Suppress file1 unique entries
   * -2: Suppress file2 unique entries
   * -12: Suppress file1 unique entries and file2 unique entries, i.e. show common entries
 * Each line of input file is an IP, CIDR expression, or IP range (a.b.c.N, a.b.c.M where N and M is the range).
   * Examples
     * IP: 1.2.3.4
     * CIDR: 1.2.3.0/24
     * IP range: 1.2.3.4-1.2.3.8

Examples
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

// Find IPs or IP ranges that are found from file2 only
% python app.py -1 in1.txt in2.txt
1.2.3.8
2.2.3.8

// Find IPs or IP ranges that are found from file1 only
% python app.py -2 in1.txt in2.txt
1.2.3.1-1.2.3.3
2.2.3.1-2.2.3.3
3.2.3.1
3.2.3.255
4.2.3.1-4.2.3.2
4.2.3.254-4.2.3.255

// Find IPs or IP ranges that are found from both files, i.e., show common entries.
% python app.py -12 in1.txt in2.txt
1.2.3.4-1.2.3.7
2.2.3.4-2.2.3.7
3.2.3.2-3.2.3.254
4.2.3.3-4.2.3.253
