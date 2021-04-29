# 안정 정렬 / 시간 O(n**2) / 공간 O(n)
def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
bubble_sort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
bubble_sort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
bubble_sort(list3)
print(list3)

# void bubbleSort(int[] arr) {
#     int temp = 0;
# 	for(int i = 0; i < arr.length; i++) {       // 1.
# 		for(int j= 1 ; j < arr.length-i; j++) { // 2.
# 			if(arr[j-1] > arr[j]) {             // 3.
#                 // swap(arr[j-1], arr[j])
# 				temp = arr[j-1];
# 				arr[j-1] = arr[j];
# 				arr[j] = temp;
# 			}
# 		}
# 	}
# 	System.out.println(Arrays.toString(arr));
# }