def towerOfHanoi(n, source, to, temp):
    if n < 1:
        print('Minimum 1 disk is required!')
    
    if n == 1:
        print('Move Disk 1 from tower {} to tower {}'.format(source, to))
        return
    
    towerOfHanoi(n - 1, source, temp, to)
    print('Move Disk {} from tower {} to tower {}'.format(n, source, to))
    towerOfHanoi(n - 1, temp, to, source)

if __name__ == "__main__":
    n = int(input('Enter the number of disks : '))
    towerOfHanoi(n, 'A', 'B', 'T')