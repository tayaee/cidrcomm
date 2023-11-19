import argparse
import ipaddress


def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    ips = set()
    for line in lines:
        line = line.strip()
        if line and not line.startswith('//'):
            if '-' in line:
                start_ip, end_ip = line.split('-')
                start = int(ipaddress.IPv4Address(start_ip))
                end = int(ipaddress.IPv4Address(end_ip))
                for ip_int in range(start, end + 1):
                    ips.add(ipaddress.IPv4Address(ip_int))
            else:
                net = ipaddress.ip_network(line, strict=False)
                for ip in net:
                    if ip.packed[-1] != 0:
                        ips.add(ip)
    return ips


def cidrcomm(file1, file2, option):
    ips1 = parse_file(file1)
    ips2 = parse_file(file2)
    if '1' in option and option['1'] and '2' in option and option['2']:
        common = ips1 & ips2
        return common
    elif '1' in option and option['1']:
        unique1 = ips2 - ips1
        return unique1
    elif '2' in option and option['2']:
        unique2 = ips1 - ips2
        return unique2


def print_ips(ips):
    if len(ips) == 0:
        return
    sorted_ips = sorted(ips)
    start_ip = sorted_ips[0]
    end_ip = sorted_ips[0]
    for ip in sorted_ips[1:]:
        if int(ip) == int(end_ip) + 1:
            end_ip = ip
        else:
            if start_ip == end_ip:
                print(start_ip)
            else:
                print(f'{start_ip}-{end_ip}')
            start_ip = ip
            end_ip = ip
    if start_ip == end_ip:
        print(start_ip)
    else:
        print(f'{start_ip}-{end_ip}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two files of IP addresses.')
    parser.add_argument('file1', type=str, help='First file to compare')
    parser.add_argument('file2', type=str, help='Second file to compare')
    parser.add_argument('-1', action='store_true', help='Suppress the output column of lines unique to file1')
    parser.add_argument('-2', action='store_true', help='Suppress the output column of lines unique to file2')
    args = parser.parse_args()
    result = cidrcomm(args.file1, args.file2, vars(args))
    print_ips(result)
