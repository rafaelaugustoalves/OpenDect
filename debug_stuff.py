import copy


class Test:
    class_immutable_list = [8, 9]
    class_mutable_list = ['y', 'z']
    def __init__(self):
        self.instance_immutable_list = [0, 1]  # list of immutable objects
        self.instance_mutable_list = ['a', 'b']  # list of immutable objects
        self.list_1 = [2, 3]
        self.value_1 = 1
        self.list_2 = [4, 5]
        self.value_2 = 2


# test_1 = Test()
# test_2 = Test()
# print('--- Initial Condition ---')
# print(f'test_1.class_immutable_list -> {test_1.class_immutable_list}')
# print(f'test_1.class_immutable_list -> {test_2.class_immutable_list}')
# # print(f'test_1.class_mutable_list -> {test_1.class_mutable_list}')
# # print(f'test_1.class_mutable_list -> {test_2.class_mutable_list}')
# print(f'test_1.instance_immutable_list -> {test_1.instance_immutable_list}')
# print(f'test_1.instance_immutable_list -> {test_2.instance_immutable_list}')
# # print(f'test_1.instance_mutable_list -> {test_1.instance_mutable_list}')
# # print(f'test_1.instance_mutable_list -> {test_2.instance_mutable_list}')
#
# print('--- modify test1.class_immutable_list ---')
# test_1.class_immutable_list.append(5)
# print(f'test_1.class_immutable_list -> {test_1.class_immutable_list}')
# print(f'test_2.class_immutable_list -> {test_2.class_immutable_list}')
#
# print('--- modify test1.instance_immutable_list ---')
# test_1.instance_immutable_list.append(5)
#
# print(f'test_1.instance_immutable_list -> {test_1.instance_immutable_list}')
# print(f'test_2.instance_immutable_list -> {test_2.instance_immutable_list}')

# print('--- Initial test3 condition ---')
# test_3 = Test()
# print(f'test_3.list_1 -> {test_3.list_1}')
# print(f'test_3.list_2 -> {test_3.list_2}')
#
# print('--- assign test_3.list_1 to test_3.list_2 ---')
# test_3.list_2 = test_3.list_1
# print(f'test_3.list_1 -> {test_3.list_1}')
# print(f'test_3.list_2 -> {test_3.list_2}')
#
# print('--- modify test_3.list_1 ---')
# test_3.list_1.append(10)
# print(f'test_3.list_1 -> {test_3.list_1}')
# print(f'test_3.list_2 -> {test_3.list_2}')
#
# print('--- recreate test3, assign and modify test_3.list_2 ---')
# test_3 = Test()
# test_3.list_2 = test_3.list_1
# test_3.list_2.append(10)
# print(f'test_3.list_1 -> {test_3.list_1}')
# print(f'test_3.list_2 -> {test_3.list_2}')
#
# print('Conclusion: assigning a mutable object (e.g. test_3.list_1 = test_3.list_2) '
#       'works like passing a reference. Changing either one will change both')
# print('=' * 90)

# print('--- Initial test3 condition ---')
# test_3 = Test()
# print(f'test_3.value_1 -> {test_3.value_1}')
# print(f'test_3.value_2 -> {test_3.value_2}')
#
# print('--- assign test_3.value_1 to test_3.value_2 ---')
# test_3.value_2 = test_3.value_1
# print(f'test_3.value_1 -> {test_3.value_1}')
# print(f'test_3.value_2 -> {test_3.value_2}')
#
# print('--- modify test_3.value_1 ---')
# test_3.value_1 += 10
# print(f'test_3.value_1 -> {test_3.value_1}')
# print(f'test_3.value_2 -> {test_3.value_2}')
#
# print('--- recreate test3, assign and modify test_3.value_2 ---')
# test_3 = Test()
# test_3.value_2 = test_3.value_1
# test_3.value_2 += 10
# print(f'test_3.value_1 -> {test_3.value_1}')
# print(f'test_3.value_2 -> {test_3.value_2}')
#
# print('Conclusion: assigning an immutable object (e.g. test_3.value_1 = test_3.value_2) '
#       'works like a copy. Changing one will not affect the other')
# print('=' * 90)

print('--- Initial test3 condition ---')
test_3 = Test()
simple_list = [5, 6]
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- assign simple_list to test_3.list_1 and test_3.list_1 to test_3.list_2---')
test_3.list_1 = simple_list
test_3.list_2 = test_3.list_1
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- modify simple_list ---')
simple_list[0] = 10
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- reset to initial condition ---')
test_3 = Test()
simple_list = [5, 6]
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- assign simple_list to test_3.list_1 and test_3.list_1 to test_3.list_2---')
test_3.list_1 = simple_list
test_3.list_2 = test_3.list_1
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- assign new list to simple_list ---')
simple_list = [9]
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- modify test_3.list_2 ---')
test_3.list_2[0] = 20
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('--- modify simple_list ---')
simple_list[0] = 70
print(f'simple_list -> {simple_list}')
print(f'test_3.list_1 -> {test_3.list_1}')
print(f'test_3.list_2 -> {test_3.list_2}')

print('Conclusion: assigning a mutable object (e.g. test_3.list_1 = simple_list) '
      'works like passing a reference, test_3.list_1 "is" simple_list. Modifying '
      'the mutable object (as in "modify in place") will change both. '
      'But, if we assign a new object to either, it works as replacing the older '
      'reference. New changes to one will not affect the other.')
print('=' * 90)