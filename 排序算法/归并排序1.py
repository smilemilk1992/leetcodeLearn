def merge(list_left, list_right):
    """
    https://segmentfault.com/a/1190000021872846
    入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
    合并(将两个有序的列表合并成一个有序的列表)
    """
    # 两个数组的起始下标
    l, r = 0, 0

    new_list = []
    while l < len(list_left) and r < len(list_right):
        if list_left[l] < list_right[r]:
            new_list.append(list_left[l])
            l += 1
        else:
            new_list.append(list_right[r])
            r += 1
    #填补剩余元素
    new_list += list_left[l:]
    new_list += list_right[r:]
    return new_list


def merge_sort(mylist):
    """归并排序
    mylist: 待排序数组
    return: 新数组list
    归并排序(分治法)
    """
    if len(mylist) <= 1:
        return mylist

    mid = len(mylist) // 2
    list_left = merge_sort(mylist[:mid])
    list_right = merge_sort(mylist[mid:])
    return merge(list_left, list_right)


if __name__ == "__main__":
    mylist = [1,4,2,3,6,5,9,7,8]
    result = merge_sort(mylist)
    print(f'归并排序后：{result}')