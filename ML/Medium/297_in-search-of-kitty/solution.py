def read_input_and_rotate(file_path='input.txt'):
    with open("input.txt", "r") as f:
        image = f.read().splitlines()

    n,_ = map(int,image[0].split())
    arr1 = image[1:n+1]
    n2,_ = map(int,image[n+1].split())
    arr2 = image[n+2:n+n2+2]
    rot_90 = []
    for i in range(len(arr1[0])):
        li = list(map(lambda x: x[i], arr1))
        li.reverse()
        rot_90.append(''.join(li))

    rot_180 = []
    for i in range(len(arr1)):
        li = list(map(lambda x: x[i], rot_90))
        li.reverse()
        rot_180.append(''.join(li))

    rot_270 = [''.join(c) for c in list(zip(*arr1))[::-1]]
    
    return arr1, arr2, rot_90, rot_180, rot_270

def is_subarray(sub, arr):
    rows_sub, cols_sub = len(sub), len(sub[0])
    rows_arr, cols_arr = len(arr), len(arr[0])
    sub_hashes = [hash(i) for i in sub]
    for i in range(rows_arr - rows_sub + 1):
        isMatch= False
        cntr = 0
        for j in range(cols_arr - cols_sub + 1):
            if hash(arr[i][j:j+cols_sub]) == sub_hashes[0]:
                isMatch = True
                last_j =  j
                cntr += 1
                break
        if isMatch:
            for k in range(i+1,i+rows_sub):
                if hash(arr[k][last_j:last_j+cols_sub])==sub_hashes[cntr]:
                    cntr += 1
                else:
                    break
            else:
                return True
    return False

def main():
    arr1, arr2, rot_90, rot_180, rot_270 = read_input_and_rotate('input.txt')

    if is_subarray(arr1,arr2):
        print('Yes')
    elif is_subarray(rot_90,arr2):
        print('Yes')
    elif is_subarray(rot_180,arr2):
        print('Yes')
    elif is_subarray(rot_270,arr2):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()